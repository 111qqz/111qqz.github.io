---
title: "tensorRT 模型兼容性说明"
date: 2020-03-24T12:26:01+08:00
draft: false
author: "111qqz"
type: post
url: /2020/03/tensorrt-model-compatibility-notes/
categories:
- 优化

tags:

- tensorrt

---

## 名词说明

- CUDA. 一般来说指的是CUDA SDK. 目前经常使用的是CUDA 8.0和CUDA 10.1两个版本. 8.0和10.1都是SDK的版本号.
- CUDNN. The NVIDIA CUDA® Deep Neural Network library (cuDNN). 是一个可以为神经网络提供GPU加速的库
- compute capability.  是GPU的固有参数,可以理解为GPU的版本.越新的显卡该数值往往越高. 
- tensorRT.NVIDIA TensorRT™ is an SDK for high-performance deep learning inference. 是一个深度学习推理库,旨在提供高性能的推理速度.
- plan file,也称为 engine plan. 是生成的tensorRT 模型文件.


## 兼容性说明

**Engine plan 的兼容性依赖于GPU的compute capability 和 TensorRT 版本, 不依赖于CUDA和CUDNN版本.**

简单来说,在使用同样TensorRT版本的前提下,在具有相同compute capability 的GPU上的模型是可以通用的.



但是cuda版本是依赖于GPU的compute capability的. 也就是比较新的GPU(对应较高的compute capability)无法使用低版本的cuda.

- CUDA SDK 8.0 support for compute capability 2.0 – 6.x
- CUDA SDK 9.0 – 9.2 support for compute capability 3.0 – 7.2
- CUDA SDK 10.0 – 10.2 support for compute capability 3.0 – 7.5
 


## TroubleShooting
- 如果是compute capability 导致的兼容性问题,会报错: [2018-12-17 06: 41: 24 ERROR] The engine plan file is generated on an incompatible device, expecting compute 7.5 got compute 6.1, please rebuild.
- 如果是TensorRT 版本导致的兼容性问题,会报错: [2018-12-17 06: 48: 13 ERROR] The engine plan file is incompatible with this version of TensorRT, expecting 5.0.4.3got 5.0.2.6, please rebuild.

## 参考链接
- https://devtalk.nvidia.com/default/topic/1045375/tensorrt/problem-loading-trt-engine-plan-on-another-machine-/
- https://en.wikipedia.org/wiki/CUDA






