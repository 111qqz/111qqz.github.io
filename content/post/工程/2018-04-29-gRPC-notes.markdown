---
author: 111qqz
date: 2018-04-29 16:18:47+00:00
draft: false
title: gRPC学习笔记
type: post
url: /2018/04/grpc-notes/
categories:
- 其他
tags:
- gRPC
---

gRPC 是 google 最新发布的开源 RPC 框架, 声称是"一个高性能，开源，将移动和HTTP/2放在首位的通用的RPC框架.". 技术栈非常的新, 基于HTTP/2, netty4.1, proto3, 拥有非常丰富而实用的特性, 堪称新一代RPC框架的典范.

<del>//上面这段话是我抄的，其实我之前连RPC是什么都不知道，</del>

关于RPC，如果你和我一样根本不知道是什么，请参考[这里 ](https://www.zhihu.com/question/25536695)

我对RPC的理解就是，一层封装，使得不在同一个机器上的程序A可以一个调用另一个程序B，而不需要考虑这两台机器，以及这两个程序使用的语言的不同。

而gRPC是诸多RPC框架中比较新，也比较好用的一个。

学习gRPC需要会使用protobuf3,关于protobuf，可以参考[protobuf学习笔记](https://111qqz.com/wordpress/2018/04/protobuf/)

[官方文档](https://grpc.io/docs/) 还是要给出的，虽然我没怎么看就是了orz


### gRPC的安装


参考[这个](https://github.com/grpc/grpc/blob/master/INSTALL.md)，从源码编译安装

    
     $ [sudo] apt-get install build-essential autoconf libtool pkg-config
     $ [sudo] apt-get install libgflags-dev libgtest-dev
     $ [sudo] apt-get install clang libc++-dev
     $ git clone -b $(curl -L https://grpc.io/release) https://github.com/grpc/grpc
     $ cd grpc
     $ git submodule update --init
     $ make
     $ [sudo] make install
    


如果出现

    
    configure: error: cannot find install-sh, install.sh, or shtool <span class="pl-k">in</span> <span class="pl-s"><span class="pl-pds">"</span>.<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>./..<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>./../..<span class="pl-pds">"</span></span>


参考

[Compile fails on Ubuntu 14.04 ?](https://github.com/grpc/grpc/issues/4105)  发现是protobuf的锅，需要手动编译一下：

    
    cd third_party/protobuf
    sudo ./autogen.sh (not sure why this requires sudo - maybe it has been
    fixed now)
    sudo ./configure CC=clang CXX=clang++ (requires sudo because previous step
    polluted things) (clang is optional)
    sudo make (requires sudo because previous step polluted things)
    sudo make install
    sudo ldconfig





### gRPC的使用


grpc/examples下有一些例子，自己搞搞就会写基本的了。(已经硬着头皮用gRPC写了一个项目的通信部分了orz...其实还挺容易的。但是项目的代码没办法放上来。。。所以。。直接看examples的代码就好了。




