---
author: 111qqz
date: 2017-08-20 09:36:00+00:00
draft: false
title: tensorflow variable 学习笔记
type: post
url: /2017/08/tensorflow-variable-notes/
categories:
- deep-learning
tags:
- checkpoint
- tensorflow
---

参考资料：

[programmers_guide/variables](https://www.tensorflow.org/programmers_guide/variables)

[tf/Variable](https://www.tensorflow.org/api_docs/python/tf/Variable)

之前感觉对tensorflow 的variable的理解不是很深刻...跑个模型啥的倒不会有什么问题，但是涉及分布式，模型并行之类的，感觉有些地方还是要理解得仔细一点比较好。



# OVERVIEW



variable的目的是将状态可持久化。

Unlike `tf.Tensor` objects, a `tf.Variable` exists outside the context of a single`session.run` call.

通俗地说就是，variable可以用来存储一个可持久化的tensor

一些op允许读取或者修改tensor的值，这些修改是**跨session可见的**，也就是说，**对于用variable可持久化过的tensor,多个worker（多卡之间）之间可以看到相同的值**。



# Creating a Variable



创建变量可以通过调用tf.get_variable function的方法实现。这个函数要求指明变量名称，这个名称会被作为标识该变量的key。

tf.get_variable也允许变量复用，意思是用之前创建过的有相同名字的变量，创建当前的变量。


    
    my_int_variable = tf.get_variable("my_int_variable", [1, 2, 3], dtype=tf.int32, 
      initializer=tf.zeros_initializer)
    
    #分别是变量名，shape，变量类型，初始化方法。
    #默认类型为tf.float32，默认初始化方法是随机数。
    #tf提供很多其他的初始化方法，以及也可以用一个tensor作为初始化。
    #注意用tensor作为初始化时，shape就不用提供了，因为会用tensor的shape作为variable的shape





# Variable collections



由于在不同的部分创建了的变量可能有是够想一起访问，所以我们需要一个简单的能访问一个集合的变量的方法。tensorflow提供了collecetions,可以理解成python list,

是一个存储tensor，variable或者其他实例的容器。

默认情况下，tf.variable被收集到如下两个collcetions:




      * tf.GraphKeys.GLOBAL_VARIABLES：放置可以被多个设备共享的variable(从名字中的GLOBAL也可以看出来...)
      * tf.GraphKeys.TRAINABLE_VARIABLES:用来放置用来计算梯度的variable


如果不想训练某个variable,那么将它加入名字叫tf.GraphKeys.LOCAL_VARIABLES 的默认collection...

下面是一个将名字叫my_local的variable加入tf.GraphKeys.LOCAL_VARIABLES的例子


    
    my_local = tf.get_variable("my_local", shape=(), 
    collections=[tf.GraphKeys.LOCAL_VARIABLES])



一个等价写法是，将trainable属性设置为False


    
    my_non_trainable = tf.get_variable("my_non_trainable", 
                                       shape=(), 
                                       trainable=False)



当然自定义collcetion也是可以的，名字可以是任何字符串。


    
    #将名字为my_local的variable放置进名字为my_collcetion_name的collection
    #如果当前这个collcetion不存在，则会自动创建
    #也就是说collcetion不用显式定义，在引用的时候如果不存在会自动定义。
    tf.add_to_collection("my_collection_name", my_local)
    
    
    




    
    #得到名字为my_collcetion_name 的collcetion中  的所有varibale,
    #返回一个元素为variable的list，顺序按照这些variable被collect的顺序
    tf.get_collection("my_collection_name")
    





# Device placement



variable和op一样，也可以放在指定的设备上。

在分布式tensorflow中，**variable放在合适的设备上非常重要**，如果不慎将variable 放在了 worker(GPU device)而不是PS(CPU device)上，将会严重减慢训练速度

基于这样的原因，我们提供[replica_device_setter](https://www.tensorflow.org/api_docs/python/tf/train/replica_device_setter),来自动将variable放置在ps上...默认是轮盘转的放置策略


    
    cluster_spec = {
        "ps": ["ps0:2222", "ps1:2222"],
        "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]}
    with tf.device(tf.train.replica_device_setter(cluster=cluster_spec)):
      v = tf.get_variable("v", shape=[20, 20])  # this variable is placed 
                                                # in the parameter server
                                                # by the replica_device_setter





# Initializing variables



在使用一个变量之前，必须先进行初始化。如果你用原生tensorflow，那初始化一般要手动显示完成。如果是使用slim,keras之类，variable的初始化一般是自动完成的。

Explicit initialization is otherwise useful because it allows you not to rerun potentially expensive initializers when reloading a model from a checkpoint as well as allowing determinism when randomly-initialized variables are shared in a distributed setting.

另一方面，明确地初始化可以保证你不会多次运行计算代价可能很昂贵的初始化操作，当你reload一个模型时。

一次性初始化所有变量可以使用tf.global_variables_initializer()，运行
session.run(tf.global_variables_initializer())
这个操作会把tf.GraphKeys.GLOBAL_VARIABLES 中的所有变量初始化。

也可以手动初始化特定变量，


    
    session.run(my_variable.initializer)



还可以得到当前没有被初始化的变量有那些（这样就可以只初始化仍然没有初始化的变量，避免重复初始化，减小计算代价。


    
    print(session.run(tf.report_uninitialized_variables()))



**需要注意的是,tf.global_variables_initializer()初始化所有变量时并没有固定的顺序，所以如果你的某个variable的值依赖于另一个variable的值，那么就很可能出错。**

Any time you use the value of a variable in a context in which not all variables are initialized (say, if you use a variable's value while initializing another variable), it is best to use `variable.initialized_value()` instead of `variable`:

任何时候如果你处于一个不是所有变量都被初始化 的环境，最后使用myvar.initialized_value()来替代myvar


    
    v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
    w = tf.get_variable("w", initializer=v.initialized_value() + 1)





# Using variables



variable可以直接看做tensor


    
    v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
    w = v + 1  # w is a tf.Tensor which is computed based on the value of v.
               # Any time a variable is used in an expression it gets automatically
               # converted to a tf.Tensor representing its value.



对变量赋值可以使用assign,assign_add或者tf.variable class中的方法



# Saving and Restoring





保存和恢复一个模型的最容易的方法就是使用tf.train.Saver object. **该object包含save和restore两个op,**

使用save 或者 restore  op来保存或者恢复**图中**全部，或者指定的varibales

如果想在图外面恢复一个模型的checkpoint,必须先用tf.train.import_meta_graph将checkpoint中的metafile(以meta为后缀）的文件导入

这样会返回一个Saver object，然后才能执行resotre op



## Checkpoint Files





tensorflow将variable存储为二进制文件的形式，通俗地说，就是map variable names to tensor values

当你创建了Saver object 之后，你可以选择为你保存进checkpoint files 文件的变量起一个名字。默认情况下，变量被使用tf.Variabel.name的名字。

如果想检查checkpoint 中的variable,可以使用inspect_checkpoint库，尤其是其中的print_tensors_in_checkpoint_file 函数。



## Saving Variables



下面是一个如何使用Saver object 中的save操作来保存变量的例子


    
    # Create some variables.
    v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
    v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)
    
    inc_v1 = v1.assign(v1+1)
    dec_v2 = v2.assign(v2-1)
    
    # Add an op to initialize the variables.
    init_op = tf.global_variables_initializer()
    
    # Add ops to save and restore all the variables.
    saver = tf.train.Saver()
    
    # Later, launch the model, initialize the variables, do some work, and save the
    # variables to disk.
    with tf.Session() as sess:
      sess.run(init_op)
      # Do some work with the model.
      inc_v1.op.run()
      dec_v2.op.run()
      # Save the variables to disk.
      save_path = saver.save(sess, "/tmp/model.ckpt")
      print("Model saved in file: %s" % save_path)





## Restoring Variables



注意从checkpoint文件中恢复variables的时候没有必要初始化

下面是一个使用saver object 的restore op的例子：


    
    tf.reset_default_graph()
    
    # Create some variables.
    v1 = tf.get_variable("v1", shape=[3])
    v2 = tf.get_variable("v2", shape=[5])
    
    # Add ops to save and restore all the variables.
    saver = tf.train.Saver()
    
    # Later, launch the model, use the saver to restore variables from disk, and
    # do some work with the model.
    with tf.Session() as sess:
      # Restore variables from disk.
      saver.restore(sess, "/tmp/model.ckpt")
      print("Model restored.")
      # Check the values of the variables
      print("v1 : %s" % v1.eval())
      print("v2 : %s" % v2.eval())





## Choosing which Variables to Save and Restore



如果tf.train.Saver()中不传入任何参数就会默认处理所有变量。

我们可以传入一些变量名，表示处理特定的变量。例子如下：


    
    tf.reset_default_graph()
    # Create some variables.
    v1 = tf.get_variable("v1", [3], initializer = tf.zeros_initializer)
    v2 = tf.get_variable("v2", [5], initializer = tf.zeros_initializer)
    
    # Add ops to save and restore only `v2` using the name "v2"
    saver = tf.train.Saver({"v2": v2})
    
    # Use the saver object normally after that.
    with tf.Session() as sess:
      # Initialize v1 since the saver will not.
      v1.initializer.run()
      saver.restore(sess, "/tmp/model.ckpt")
    
      print("v1 : %s" % v1.eval())
      print("v2 : %s" % v2.eval())



需要注意的是:




      * **Saver object可以有任意多个，同一个变量也可以被任意多个Saver object save**
      * **restore的时候如果只是restore了一部分变量，其余的变量记得要初始化**




# Sharing variables



暂时用不上，有空补吧，困了orz






