---
title: "【施工中】torch2trt　学习笔记"
date: 2020-09-18T11:02:50+08:00
draft: false
author: "111qqz"
type: post
url: /2020/09/torch2trt
categories:
- deep-learning

tags:
- Jetson Nano
- 模型转换

---

## 前言

偶然发现了 [torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt) 的模型转换方案，思路是直接将pytorch op映射到TensorRT的python api. 在pytorch进行每个op　forward的时候，tensorrt也相应往network上添加op.
这里会先涉及torch2trt的使用，后面会补充这个转换工具的代码学习


### 使用torch2trt
[torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)
pytorch可以直接安装，但是torchvision根据 [pytorch-for-jetson-version-1-6-0-now-available](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-6-0-now-available/72048/15?u=hust.111qqz) 中的说法，需要编译安装
```shell 
git clone  https://github.com/pytorch/vision 
```
然后切换到tag v0.7.0
执行
```shell
sudo python3 setup.py  install 
```
可以正常安装

然后报错:
ModuleNotFoundError: No module named 'termcolor'

尝试  sudo apt install python3-termcolor  后解决


接下来尝试trt samples中的　/python/network_api_pytorch_mnist
发现安装pycuda报错找不到cuda.h的头文件
参考　[pycuda installation failure on jetson nano](https://forums.developer.nvidia.com/t/pycuda-installation-failure-on-jetson-nano/77152/12?u=hust.111qqz)
执行了如下命令后成功:
```shell
export LIBRARY_PATH=/usr/local/cuda/targets/aarch64-linux/lib/:$LIBRARY_PATH
export CPATH=/usr/local/cuda/include:$CPATH 

```

然后尝试使用TensorRT  python api对一个engine file 做inference的时候，报错:
pycuda._driver.LogicError: explicit_context_dependent failed: invalid device context - no currently active context?
在　import pycuda.autoinit　后解决

然后在尝试修改inference的input时报错:
pycuda._driver.LogicError: cuMemcpyHtoDAsync failed: invalid argument
参考[pycuda._driver.LogicError: cuMemcpyHtoDAsync failed: invalid argument](https://forums.developer.nvidia.com/t/pycuda-driver-logicerror-cumemcpyhtodasync-failed-invalid-argument/83132/5?u=hust.111qqz)
发现原因是numpy的类型不太对，修改为:
```python
 inputs[0].host = inp.astype(np.float32)
 ```
 就可以了

 接下来是在plan文件前面加签名
 一开始用了numpy.tobytes() 。。发现每个字符占了4byte..与c++的caffe-tensorrt行为不一致
 后来尝试 c = bytes(header,'utf-8') + model_data  问题似乎解决
 
### torch2trt源码分析