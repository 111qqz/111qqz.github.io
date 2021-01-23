---
title: "tensorrt INT8 量化debug记录（cuda error 700）"
date: 2020-04-08T14:58:16+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/cuda-error-700-when-using-tensorrt-calibration
categories:
- deep-learning

tags:

- tensorrt

---

背景是要把某个caffe model,转换成tensorrt的INT8 模型。 然后遇到如下报错:

```bash

E0403 08:54:35.951987  5704 engine.h:62] engine.cpp (572) - Cuda Error in commonEmitTensor: 1 (invalid argument)
E0403 08:54:35.952157  5704 engine.h:62] Failure while trying to emit debug blob.
engine.cpp (572) - Cuda Error in commonEmitTensor: 1 (invalid argument)
E0403 08:54:35.952235  5704 engine.h:62] cuda/caskConvolutionLayer.cpp (355) - Cuda Error in execute: 1 (invalid argument)
E0403 08:54:35.952291  5704 engine.h:62] cuda/caskConvolutionLayer.cpp (355) - Cuda Error in execute: 1 (invalid argument)
W0403 08:54:35.952324  5704 calibrator.cpp:45] [4, 3, 224, 224]
F0403 08:54:35.992761  5704 tensor.h:149] Check failed: cudaMemcpy(raw_mutable_data(), b.raw_data(), size_in_bytes, cudaMemcpyDefault) == cudaSuccess (700 vs. 0) 
*** Check failure stack trace: ***
Aborted (core dumped)

```


cuda error 700. 原来cuda error的错误号可以这么大。。

查了下，说
> in general, CUDA error 700 is drivers or timeout related. 

看起来是个环境问题，
然后又试了下之前转的INT8的模型，依然没有报错。

我就很困惑了。。 想了下这两个模型的区别。 能转的模型是从pytorch开始转换的，中间会merge BN layer。而cuda error 700的模型是caffe 模型，保留了BN layer.  

于是把第一个BN 以及之后的layer都删除。然而仍然是这个错误。

继续删除到只剩下一个input layer,一个conv layer. 还是报错。。 事情变得过于诡异了起来。看来不是模型的问题。。


然后检查了一下做校准用的预处理参数。。**发现输入尺寸和模型的输入尺寸竟然是不一致的**。。。 跪了。。

之前的模型由于是pytorch模型，input size和预处理size 是完全通过我控制的，因此不会有问题。

但是对于要转换的caffe 模型， 模型的参数和预处理部分是用户提供给我的，而我们的代码中没有做检查(似乎也不好做检查，因为校准的逻辑是在更顶层的)

但是这个cuda error 700的报错。。。也太不友好了吧。。。

因为之前查了cuda error 700，发现似乎没人提到这种情况，所以还是写出来分享一下。











