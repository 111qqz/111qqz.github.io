---
author: 111qqz
date: 2017-08-20 08:21:57+00:00
draft: false
title: tensorflow Session 学习笔记
type: post
url: /2017/08/tensorflow-session-notes/
categories:
- deep-learning
tags:
- tensorflow
---

[tensorflow-session官方文档](https://www.tensorflow.org/api_docs/python/tf/Session)

说下我自己的理解：

session中文一般叫会话，可以理解成op执行时候需要的一层虚拟化的封装。

op必须在session中才能执行。

tensor也是在tensor中才可以存在（tf.variable和tensor几乎是一回事，只是tf.variable的会话不要求session，也可以理解成tf.variable在session中就成了tensor.

需要注意的是session一般会占据资源，所以在使用完记得释放，或者写成with的形式（看到with总想叫成开域语句...感觉暴露年龄orz

下面这两种形式是等价的：


    
    # Using the `close()` method.
    sess = tf.Session()
    sess.run(...)
    sess.close()
    
    # Using the context manager.
    with tf.Session() as sess:
      sess.run(...)



session本身有一些配置，我们使用configproto：


    
    # Launch the graph in a session that allows soft device placement and
    # logs the placement decisions.
    sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                            log_device_placement=True))



allow_soft_placement的作用是自动选择可用的设备（如果指定的设备不可用（？）），防止指定的设备不可用而挂掉的情况。

log_device_placement :To find out which devices your operations and tensors are assigned to.










