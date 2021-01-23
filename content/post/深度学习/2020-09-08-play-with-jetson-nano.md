---
title: "Jetson Nano踩坑记录"
date: 2020-09-08T14:41:34+08:00
draft: false
author: "111qqz"
type: post
url: /2020/09/jetson-nano
categories:
- deep-learning

tags:
- Jetson Nano
---
## 写在前面
主要是需要在jetson nano做模型转换，来记录下踩的坑
目前有两条路径，一条是我们现有的转换路径，也就是pytorch->onnx(->caffe)->trt的路径
在这条路径上踩了比较多的坑，最终暂时放弃，最直接的原因是**cudnn8.0升级接口发生改动，编译caffe遇到较多问题**
这里其实仍然采用了两条平行的路径，一条是直接在nano上构建环境，另外一种是基于docker(包括构建交叉编译环境用于加快编译速度)

另一条路径是基于[torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt),是一条直接pytorch->trt的路径
这里主要记录在第一条路径上踩过的坑

## 环境准备
先过一遍[开发者手册](https://developer.download.nvidia.com/assets/embedded/secure/jetson/Nano/docs/NV_Jetson_Nano_Developer_Kit_User_Guide.pdf?fwGItta2EgdDJPznNGraYrYTih0vCRJeiTOuypPs9DEvHJ3qz4HscO9-M4HOLiAdV9AVmQabvyXS-ngkemZ6pi-i9Of-1yLcC_1QpiZKKfeNjIZ4HFst2wTuVA8fSFWdPCLFWIjjQw9_1HXTLWGyxKMWeTjU6QW8O8XFbt8HVGmhjCc2jNfXheOl_otXr8EkdIc)
主要是介绍了下nano的硬件和jetpack的组件
jetpack可以理解成一个nvidia用在嵌入式设备上的SDK工具包


### 镜像烧录
然后需要烧录镜像，参考[Write Image to the microSD Card](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)
最初使用  Etcher 来烧录，没有启动起来，原因未知。使用终端命令烧录就没问题了。

### 更换国内apt源
我拿到的jeston nano是基于ubuntu 18.04 lts的版本，默认源比较慢，换成国内源。需要注意要换**arm**版本的源
```shell
wget -O /etc/apt/sources.list https://repo.huaweicloud.com/repository/conf/Ubuntu-Ports-bionic.list
apt update
```

## 基于docker的模型转换
由于在x86上模型转换的工具是基于docker的，因此最初的想法是在nano上也基于docker进行转模型，这样或许可以复用一些x86上的工作。

确认了Jetson Nano上是可以跑docker和[NVIDIA Container Runtime on Jetson (Beta)](https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson)的
但是最初发现arm的cuda docker image最低支持cuda11.0的版本
[cuda-arm64 docker image tag](https://hub.docker.com/r/nvidia/cuda-arm64/tags)
然而目前(2020年9月)最新的[jetpack4.4版本](https://developer.nvidia.com/embedded/jetpack)只支持到cuda10.2的版本
尝试了下使用cuda-arm64的docker image　发现驱动版本不够，而nano上似乎很难升级驱动版本，因此差点就放弃这条路径了。

然而发现，在nano上要用的cuda镜像并不应该是cuda-arm,而是[NVIDIA L4T Base
](https://ngc.nvidia.com/catalog/containers/nvidia:l4t-base)

### 结论

参考[https://docs.nvidia.com/jetson/archives/](jetson开发者手册归档)，发现一个可能的问题是，jetpack中cuDNN,TensorRT等库的版本不是连续的。
- jetpack4.4: CUDA10.2,TensorRT 7.1.3,cuDNN 8.0.0
- jetpack4.3: CUDA 10.0.326, TensorRT 6.0.1.10, cuDNN 7.6.3
- jetpack4.2.1: CUDA 10.0.326,TensorRT 5.1.6.1,cuDNN 7.5.0.56
- jetpack4.2.0:CUDA 10.166,TensorRT 5.0.6.3,cuDNN 7.3.1.28

发现并不能知道TensorRT7.0的版本，arm版本的库似乎官方也没有提供地址下载
最初想着是将cuDNN 7.6.3从jetpack4.3的镜像中拿出来，拷贝过去使用
然后发现TensorRT 7.1.3是依赖cuDNN8.0的。。。死了。或许可以考虑把工具链中的caffe摘除掉

### 编译opencv
这部分其实发生在上部分得到结论之前
先尝试下在这个镜像上编译opencv
提示找不到　 libjasper-dev..似乎是个可选的包，先不装试试看
然后提示fata error: LAPACKE_H_PATH-NOTFOUND 
解决办法参考　[opencv install ](https://stackoverflow.com/questions/48776408/opencv-installation)
- install package liblapacke-dev
- manually define -DLAPACKE_H_PATH=/usr/include when calling cmake

由于在nano上编译速度非常感人，因此在x86上配置了arm的交叉编译环境，所以实际上是在x86机器上的交叉编译环境中进行编译的。


### 安装caffe2TRT工具链

cmake版本3.10太低，需要升级，编译3.16版本cmake的时候报错:
Could NOT find OpenSSL                     
通过
```shell

sudo apt-get install openssl

sudo apt-get install libssl-dev
```
解决

然后需要装 libgoogle-glog-dev 和   libgflags-dev

报错: unrecognized command line option ‘-mavx2’
原因是这个是x86的编译选项，arm平台不支持，解决办法是在CMakeLists中去掉这个编译选项

编译caffe报错:
fatal error: boost/random/mersenne_twister.hpp: No such file or directory
 #include "boost/random/mersenne_twister.hpp"
 应该是boost相关的库没装
 apt install libboost-all-dev 之后解决
 
 然后报错 error: ‘iota’ is not a member of ‘std’
 解决办法是头文件添加了 #include <numeric> 

 需要装git lfs,试了下 apt install git-lfs，可以解决


发现nano的TensorRT,cuDNN的头文件在 /usr/include/aarch64-linux-gnu
动态库在 /usr/lib/aarch64-linux-gnu

编译caffe报错:
error: identifier "cublasStatus_t" is undefined
这个符号应该是定义在/usr/local/cuda/include/cublas.h中的。。
然后发现nano上，cuda10.2版本，cublas相应的头文件是在/usr/include的
相应的动态库是在: /usr/lib/aarch64-linux-gnu下的
去/usr/include下发现cublas相关的header file的大小竟然都是0...???
于是去nano上把cublas相关的头文件拷贝过来，问题解决

继续报错: error: 'iota' is not a member of 'std'
   std::iota(idxs.begin(), idxs.end(), 0);

解决办法: 添加 #include <numeric>

接着报错:
error: 'CUDNN_MAJOR' was not declared in this scope
应该是编译的时候没找到cudnn导致的
发现是cudnn8的头文件里没有了cudnn.h，caffe会去这个文件中找版本
于是加了个软链接解决

```shell
ln -s cudnn_version_v8.h  cudnn.h   
```

接下里报错:
caffe/util/cudnn.hpp(20): error: identifier "cudnnStatus_t" is undefined
make VERBOSE=1观察，是已经有了头文件所在的/usr/include的路径的

发现是cudnn8里面，头文件不止需要一个cudnn.h，拆成了好多个头文件
于是在cudnn.h里添加了
```c++
#include <cudnn_ops_infer_v8.h> 
```
解决

接下来报错 error: identifier "cudnnConvolutionDescriptor_t" is undefined
在cudnn.h里添加了
```c++
#include <cudnn_cnn_infer_v8.h> 
```
解决

要改的内容太多了，工作量不可控，放弃进一步的修改，转而采用思路是移除掉转换工具对caffe的依赖


## 直接在裸机上安装环境

### 安装pytorch 

注意由于架构不同，不能直接pip install来安装pytorch
参考 [pytorch-for-jetson-version-1-6-0-now-available](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-6-0-now-available/72048)

先尝试安装pip3,用在x86上的方式没成功。。
最后是使用https://pip.pypa.io/en/stable/installing/　中的 get-pip.py 来安装

于是尝试pip3 install torch1.5.whl
安装正常结束，但是
```shell
python -c 'import torch'
```
的时候报错:
"OSError: libmpi_cxx.so.20: cannot open shared object file: No such file or directory"
```shell
apt install libopenmpi2
```
后解决
接下来报错:
　ImportError: libopenblas.so.0: cannot open shared object file: No such file or directory

```shell
apt install  libopenblas-dev 
```
后解决

再之后直接segment falut了
参考[在Jetson TX2上安装Python,JetsonTX2,傻瓜式,pytorch](https://www.pythonf.cn/read/129464)等帖子，似乎是arm版本的pytorch 1.5安装包有问题
尝试下pytorch 1.4和pytorch 1.6 果然都没问题，有点坑
最后决定使用pytoch 1.6版本

### 安装onnx

参考[build-onnx-on-arm-64](https://github.com/onnx/onnx#build-onnx-on-arm-64)
执行了
```shell
pip3 install cython protobuf numpy
sudo apt-get install libprotobuf-dev protobuf-compiler
pip3 install onnx
```
然后在编译onnx的时候报错"报错 onnx/third_party/pybind11/include/pybind11/detail/common.h:112:10: fatal error: Python.h: No such file or directory"
参考[Make Error, fatal error: Python.h: No such file or directory compilation terminated](https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/1038),在执行
```shell
apt install python3-dev
```
后解决

之后在import caffe_pb2的时候，报错
"  options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001')), file=DESCRIPTOR),                                                                                      
TypeError: __new__() got an unexpected keyword argument 'file'"
原因是protobuf版本是3.0.0太低了。。file这个参数是protobuf 3.5之后的版本引入的。。于是升级protobuf版本到3.5.1
```shell
pip install protobuf==3.5.1
```
问题解决


 ## 在x86上交叉编译

 ### 构建交叉编译的镜像

 发现nano上编译速度过于感人，因此尝试使用交叉编译的方式
 参考[Enabling Jetson Containers on an x86 workstation (using qemu)](https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson#enabling-jetson-containers-on-an-x86-workstation-using-qemu)

 结果如下:
```shell
$ sudo apt-get install qemu binfmt-support qemu-user-static
# Check if the entries look good.
$ sudo cat /proc/sys/fs/binfmt_misc/status
enabled

# See if /usr/bin/qemu-aarch64-static exists as one of the interpreters.
$ cat /proc/sys/fs/binfmt_misc/qemu-aarch64
enabled
interpreter /usr/bin/qemu-aarch64-static
flags: OC
offset 0
magic 7f454c460201010000000000000000000200b700
mask ffffffffffffff00fffffffffffffffffeffffff

```
 注意少了个'F' flag
 > Make sure the F flag is present, if not head to the troubleshooting section, as this will result in a failure to start the Jetson container.

 参考[Running or building a container on x86 (using qemu+binfmt_misc) is failing](https://github.com/NVIDIA/nvidia-docker/wiki/NVIDIA-Container-Runtime-on-Jetson#running-or-building-a-container-on-x86-using-qemubinfmt_misc-is-failing)
 执行
 ```shell

 docker run --rm --privileged multiarch/qemu-user-static --reset -p yes -c yes
 ```
 喜提一屏幕报错
 ```shell

 Setting /usr/bin/qemu-alpha-static as binfmt interpreter for alpha
sh: write error: Invalid argument
Setting /usr/bin/qemu-arm-static as binfmt interpreter for arm
sh: write error: Invalid argument
Setting /usr/bin/qemu-armeb-static as binfmt interpreter for armeb
sh: write error: Invalid argument
sh: write error: Invalid argument
Setting /usr/bin/qemu-sparc-static as binfmt interpreter for sparc
Setting /usr/bin/qemu-sparc32plus-static as binfmt interpreter for sparc32plus
sh: write error: Invalid argument
Setting /usr/bin/qemu-sparc64-static as binfmt interpreter for sparc64
sh: write error: Invalid argument
Setting /usr/bin/qemu-ppc-static as binfmt interpreter for ppc
sh: write error: Invalid argument
Setting /usr/bin/qemu-ppc64-static as binfmt interpreter for ppc64
sh: write error: Invalid argument
Setting /usr/bin/qemu-ppc64le-static as binfmt interpreter for ppc64le
sh: write error: Invalid argument
Setting /usr/bin/qemu-m68k-static as binfmt interpreter for m68k
sh: write error: Invalid argument
sh: write error: Invalid argument
Setting /usr/bin/qemu-mips-static as binfmt interpreter for mips
Setting /usr/bin/qemu-mipsel-static as binfmt interpreter for mipsel
sh: write error: Invalid argument
Setting /usr/bin/qemu-mipsn32-static as binfmt interpreter for mipsn32
sh: write error: Invalid argument
Setting /usr/bin/qemu-mipsn32el-static as binfmt interpreter for mipsn32el
sh: write error: Invalid argument
sh: write error: Invalid argument
Setting /usr/bin/qemu-mips64-static as binfmt interpreter for mips64
Setting /usr/bin/qemu-mips64el-static as binfmt interpreter for mips64el
sh: write error: Invalid argument
Setting /usr/bin/qemu-sh4-static as binfmt interpreter for sh4
sh: write error: Invalid argument
Setting /usr/bin/qemu-sh4eb-static as binfmt interpreter for sh4eb
sh: write error: Invalid argument
Setting /usr/bin/qemu-s390x-static as binfmt interpreter for s390x
sh: write error: Invalid argument
Setting /usr/bin/qemu-aarch64-static as binfmt interpreter for aarch64
sh: write error: Invalid argument
Setting /usr/bin/qemu-aarch64_be-static as binfmt interpreter for aarch64_be
sh: write error: Invalid argument
sh: write error: Invalid argument
Setting /usr/bin/qemu-hppa-static as binfmt interpreter for hppa
Setting /usr/bin/qemu-riscv32-static as binfmt interpreter for riscv32
sh: write error: Invalid argument
Setting /usr/bin/qemu-riscv64-static as binfmt interpreter for riscv64
sh: write error: Invalid argument
Setting /usr/bin/qemu-xtensa-static as binfmt interpreter for xtensa
sh: write error: Invalid argument
Setting /usr/bin/qemu-xtensaeb-static as binfmt interpreter for xtensaeb
sh: write error: Invalid argument
Setting /usr/bin/qemu-microblaze-static as binfmt interpreter for microblaze
sh: write error: Invalid argument
Setting /usr/bin/qemu-microblazeel-static as binfmt interpreter for microblazeel
sh: write error: Invalid argument
Setting /usr/bin/qemu-or1k-static as binfmt interpreter for or1k
sh: write error: Invalid argument

```

查到[sh: write error: Invalid argument - Centos 7 ](https://github.com/multiarch/qemu-user-static/issues/100#issuecomment-566030523)

发现原因是 "-p yes"这个参数是在4.10版本的kernel后才支持的。。而我本地的机器ubuntu 14.04的kernel版本是4.2.0-27-generic

绕过去的办法是从qemu-user-static的docker里copy一些必要的文件出来


```shell
$ docker build --rm -t my-aarch64-ubuntu -<<EOF
FROM multiarch/qemu-user-static:x86_64-aarch64 as qemu
FROM arm64v8/ubuntu
COPY --from=qemu /usr/bin/qemu-aarch64-static /usr/bin
EOF

$ docker run --rm -t my-aarch64-ubuntu uname -m
aarch64
```

接下来可以参考 [Running and Building ARM Docker Containers on x86](https://www.stereolabs.com/docs/docker/building-arm-container-on-x86/)

### 编译cuda有关的库
然而上面这些步骤只是能够编译和cuda无关的部分
发现对于相同的镜像，在x86上启动时，/usr/local/cuda/lib64会少很多内容，但是在nano上启动就是正常的。
怀疑是nano的nvidia-docker做了什么事情

参考 [cross-compile-cuda-engines](https://forums.developer.nvidia.com/t/cross-compile-cuda-engines/72265)
以及[[l4t-base] Building CUDA code in a Jetson Container on an x86 workstation](https://github.com/NVIDIA/nvidia-docker/issues/1179)
发现一个workaround是把nano上cuda里面的动态库copy到镜像里面




## 参考链接

- [ arm64 和 aarch64 指令集是同一回事吗？](https://bbs.huaweicloud.com/forum/thread-28512-1-1.html)  答案是是一回事