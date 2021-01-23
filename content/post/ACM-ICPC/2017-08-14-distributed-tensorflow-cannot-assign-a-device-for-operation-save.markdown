---
author: 111qqz
date: 2017-08-14 01:55:15+00:00
draft: false
title: 'Distributed Tensorflow : Cannot assign a device for operation save'
type: post
url: /2017/08/distributed-tensorflow-cannot-assign-a-device-for-operation-save/
categories:
- deep-learning
tags:
- tensorflow
---

是在使用分布式tensorflow遇到的一个错误

报错如下：

InvalidArgumentError (see above for traceback): Cannot assign a device for operation 'save/Rest│| 2 GeForce GTX 1080 On | 0000:08:00.0 Off | N/A |
oreV2_888': Operation was explicitly assigned to /job:worker/task:0/device:CPU:0 but available │| 24% 39C P8 12W / 180W | 0MiB / 8114MiB | 0% Default |
devices are [ /job:localhost/replica:0/task:0/cpu:0, /job:localhost/replica:0/task:0/gpu:0 ]. Make sure the device specification refers to a valid device.

其中看到[Distributed Tensorflow : Cannot assign a device for operation.](https://github.com/tensorflow/tensorflow/issues/11608) 中提到，可能的两个原因是：



<blockquote>****

**I have mostly seen the "cannot assign a device for operation ..." error in the case of people using GPU without specifying allow_soft_placement=True but in my case I am using just CPUs.**

**I have seen another instance of this error when users were not specifying server.target as the device of a session,thereby creating a local session but this is not the case in my code.**</blockquote>






