---
author: 111qqz
date: 2017-08-07 12:54:23+00:00
draft: false
title: 分布式 tensorflow 学习笔记(非最终版)
type: post
url: /2017/08/tensorflow-notes/
categories:
- deep-learning
tags:
- tensorflow
---

感觉资料不是很多，先收集资料好了。

[tf-distributed官网文档](https://www.tensorflow.org/deploy/distributed)

[SO-between-graph和in-graph的区别](https://stackoverflow.com/questions/41600321/distributed-tensorflow-the-difference-between-in-graph-replication-and-between)

[inception.README.md](https://github.com/tensorflow/models/blob/master/inception/README.md)

[SyncReplicasOptimizer](https://www.tensorflow.org/versions/r0.12/api_docs/python/train/other_functions_and_classes)

[SO_How does ps work in distribute Tensorflow?](https://stackoverflow.com/questions/41480149/how-does-ps-work-in-distribute-tensorflow)



update:在多个nodes（机）上跑。。。tf默认是异步更新的。。。同步的话。。大概需要syncreplicasoptimizer?

来直观感受下，不同task的之间并不同步

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/08/深度截图_选择区域_20170815095908.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/08/深度截图_选择区域_20170815095908.png)



## 创建一个cluster



每一个task唯一对应一个server,server中有一个master，还有若干个worker

cluster是task的集合

cluster是在处理分布式问题时抽象出的概念，类似缩点。

cluster也可以划分成一个或者多个job，每个job包含一个或者多个task.

所以task,job,cluster的关系，从集合的角度考虑：

task的集合中的元素，job是task的（不相交？）子集，cluster是task的全集。

（**似乎要求所有job的交为空，所有job的补为全集，也就是似乎不能越过job直接到taks(?)**）

如下图：

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/08/深度截图_选择区域_20170808105038.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/08/深度截图_选择区域_20170808105038.png)



<blockquote>_A TensorFlow "cluster" is a set of "tasks" that participate in the distributed execution of a TensorFlow graph. Each task is associated with a TensorFlow "server", which contains a "master" that can be used to create sessions, and a "worker" that executes operations in the graph. A cluster can also be divided into one or more "jobs", where each job contains one or more tasks._</blockquote>





通常不同的task运行在不同的machine上，不过也可以运行在同一个machine的不同device上（比如一个机器的多个gpu)



为了创建一个cluster，要做如下步骤：



### **创建 一个 `tf.train.ClusterSpec` 来描述cluster中的全部tasks**



cluster通过一个dictionary将job(task) map到网络地址，我们将这个地址传递给 tf.train.ClusterSpec 构造器，看如下例子：

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/08/深度截图_选择区域_20170808112735.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/08/深度截图_选择区域_20170808112735.png)

我们观察到，**task的id是0-base，按照dictionary中的key的顺序自动递增编号的。**



### 在每一个task中创建一个`tf.train.Server的实例`



tf.train.server包含一些local devices,以及他们和tf.train.clusterspec中描述的其他tasks的connections，还有一个tf.session来实现分布式计算（的交互）

cluster的每个server可以和该cluster中的任意其他server通信


    
    # In task 0:
    cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
    server = tf.train.Server(cluster, job_name="local", task_index=0)
    # In task 1:
    cluster = tf.train.ClusterSpec({"local": ["localhost:2222", "localhost:2223"]})
    server = tf.train.Server(cluster, job_name="local", task_index=1)





## 在你的模型中指定分布式设备



还是用tf.device()，直接看代码：


    
    with tf.device("/job:ps/task:0"):
      weights_1 = tf.Variable(...)
      biases_1 = tf.Variable(...)
    
    with tf.device("/job:ps/task:1"):
      weights_2 = tf.Variable(...)
      biases_2 = tf.Variable(...)
    
    with tf.device("/job:worker/task:7"):
      input, labels = ...
      layer_1 = tf.nn.relu(tf.matmul(input, weights_1) + biases_1)
      logits = tf.nn.relu(tf.matmul(layer_1, weights_2) + biases_2)
      # ...
      train_op = ...
    
    with tf.Session("grpc://worker7.example.com:2222") as sess:
      for _ in range(10000):
        sess.run(train_op)





In the above example, the variables are created on two tasks in the `ps` job, and the compute-intensive part of the model is created in the `worker` job. TensorFlow will insert the appropriate data transfers between the jobs (from `ps` to `worker` for the forward pass, and from `worker` to `ps` for applying gradients).



 在上面的代码中，变量被创建在了ps 上的两个task,模型的计算密集不问被创建在了worker上 。



**tensorflow会插入合适的传输（组件）来（自动地）保证ps和worker的通信（fordward pass时从ps到worker，apply gradients时从worker到ps)**

大概就是下面这个图的过程：

![Partitioned Graph](https://www.tensorflow.org/images/graph_split2.svg)








上面SO的链接中提到了：



<blockquote>Anyway, both "worker" and "ps" are _tasks_ (or _jobs_ rather, which are just groups of _tasks_), so they're really no different. The difference is what they're supposed to be used for. The idea is that state (e.g. `tf.Variable`) should be on the parameter servers, while operations for calculating state should be on the workers. Instead of achieving this by calling `tf.device` manually everywhere, a helper function named [`tf.train.replica_device_setter`](https://www.tensorflow.org/api_docs/python/train/distributed_execution#replica_device_setter) is used that sets a `tf.Variable`'s device to a parameter server, and the other operations to a worker.

`server.join()` just means that parameter servers will wait on the workers, instead of terminating their client processes immediately.

>     
>     with tf.device(tf.replica_device_setter(
>       worker_device="/job:worker/task:%d" % FLAGS.task_index, 
>       cluster=cluster_spec)):
>     
>       v1 = tf.Variable(...)  # Automatically assigned to a parameter server.
>       train_op = ... # Automatically assigned to the worker.
> 
> 
</blockquote>



和我之前的理解基本一致，不过重点是里面提到了名字叫 [tf.train.replica_device_setter](https://www.tensorflow.org/api_docs/python/tf/train/replica_device_setter) 的函数，推荐使用这个函数去指定分布式设备，而不是手动指定。







## Replicated training





一种常见的训练方式叫做“数据并行”，涉及到在一个worker中的多个tasks在不同的mini-batch数据上训练同一个模型，然后更新存放在ps中的共享参数。在tensorflow中完成这样的结构有很多方法，我们构建了一些库去简化replicated trainning的操作，可能的方法如下：






      * **In-graph replication.** In this approach, the client builds a single `tf.Graph` that contains one set of parameters (in `tf.Variable` nodes pinned to `/job:ps`); and multiple copies of the compute-intensive part of the model, each pinned to a different task in `/job:worker`.
      * **Between-graph replication.** In this approach, there is a separate client for each `/job:worker` task, typically in the same process as the worker task. Each client builds a similar graph containing the parameters (pinned to `/job:ps` as before using [`tf.train.replica_device_setter`](https://www.tensorflow.org/api_docs/python/tf/train/replica_device_setter) to map them deterministically to the same tasks); and a single copy of the compute-intensive part of the model, pinned to the local task in `/job:worker`.
      * **Asynchronous training.** In this approach, each replica of the graph has an independent training loop that executes without coordination. It is compatible with both forms of replication above.
      * **Synchronous training.** In this approach, all of the replicas read the same values for the current parameters, compute gradients in parallel, and then apply them together. It is compatible with in-graph replication (e.g. using gradient averaging as in the [CIFAR-10 multi-GPU trainer](https://github.com/tensorflow/models/tree/master/tutorials/image/cifar10/cifar10_multi_gpu_train.py)), and between-graph replication (e.g. using the [`tf.train.SyncReplicasOptimizer`](https://www.tensorflow.org/api_docs/python/tf/train/SyncReplicasOptimizer)).







