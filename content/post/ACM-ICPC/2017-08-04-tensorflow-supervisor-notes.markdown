---
author: 111qqz
date: 2017-08-04 09:22:44+00:00
draft: false
title: tensorflow Supervisor 学习笔记
type: post
url: /2017/08/tensorflow-supervisor-notes/
categories:
- deep-learning
tags:
- supervisor
- tensorflow
---

update:supervisor的缺点是遇到问题只会抛异常，所以现在有一个better的管理工具,[MonitoredSession](https://www.tensorflow.org/api_docs/python/tf/train/MonitoredSession)

master,chief worker,Supervisor 这几个概念有点搞不清（我最菜.jpg  因此来学习一下。



## 概述



原生的tensorflow 是各种东西都需要自己手动，如果是小规模的训练问题倒是不大，但是如果是训练的数据量比较大，可能需要训练几天或者几个月。。。

那原生的tensorflow的健壮性可能就比较堪忧。。。

万一断电了之类。。。

这时候我们就可以使用supervisor

其主要提供下面三个功能，以增强训练的健壮性：




      * Handles shutdowns and crashes cleanly.
      * Can be resumed after a shutdown or a crash.
      * Can be monitored through TensorBoard.


supervisor可以看做一个工具，或者说是对原生tensorflow的一层封装，目的主要是通过定期save的方法增强训练健壮性，

就算程序挂掉了也可以从上一次save的checkpoint恢复，而不是从头再来（虽然这些也可以手动实现（？）

同时也可以简化代码量

除了supervisor,还有tf.learn库，里面提供对原生tensorflow更高层的封装，也提供更丰富的功能。





## 实例



来举个具体的例子好了：

在不使用supervisor的时候，我们的训练代码如下：


    
    variables
    ...
    ops
    ...
    summary_op
    ...
    merge_all_summarie
    saver
    init_op
    
    with tf.Session() as sess:
      writer = tf.tf.train.SummaryWriter()
      sess.run(init)
      saver.restore()
      for ...:
        train
        merged_summary = sess.run(merge_all_summarie)
        writer.add_summary(merged_summary,i)
      saver.save



如果使用supervisor，代码如下：


    
    import tensorflow as tf
    a = tf.Variable(1)
    b = tf.Variable(2)
    c = tf.add(a,b)
    update = tf.assign(a,c)
    tf.scalar_summary("a",a)
    init_op = tf.initialize_all_variables()
    merged_summary_op = tf.merge_all_summaries()
    sv = tf.train.Supervisor(logdir="/home/keith/tmp/",init_op=init_op) #logdir用来保存checkpoint和summary
    saver=sv.saver #创建saver
    with sv.managed_session() as sess: #会自动去logdir中去找checkpoint，如果没有的话，自动执行初始化
        for i in xrange(1000):
            update_ = sess.run(update)
            print update_
            if i % 10 == 0:
                merged_summary = sess.run(merged_summary_op)
                sv.summary_computed(sess, merged_summary,global_step=i)
            if i0 == 0:
                saver.save(sess,logdir="/home/keith/tmp/",global_step=i)







## 结论



从上面代码可以看出，`Supervisor`帮助我们处理一些事情
（1）自动去checkpoint加载数据或初始化数据
（2）自身有一个`Saver`，可以用来保存checkpoint
（3）有一个`summary_computed`用来保存`Summary`
所以，我们就不需要：
（1）手动初始化或从`checkpoint`中加载数据
（2）不需要创建`Saver`，使用`sv`内部的就可以
（3）不需要创建`summary writer`





参考资料：

[tensorflow学习笔记（二十二）：Supervisor](http://blog.csdn.net/u012436149/article/details/53341372http://blog.csdn.net/u012436149/article/details/53341372)

[Supervisor: Training Helper for Days-Long Trainings.](https://www.tensorflow.org/programmers_guide/supervisor)


