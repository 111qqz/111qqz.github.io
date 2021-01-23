---
author: 111qqz
date: 2018-02-13 06:38:38+00:00
draft: false
title: CUDA C Best Practices Guide 阅读笔记（二） Heterogeneous Computing
type: post
url: /2018/02/cuda-c-best-practices-guide-heterogeneous-computing/
categories:
- 优化
tags:
- cuda
- c++
---

CUDA 编程涉及到在不同的平台上同时运行代码:包含CPU的host 和包含GPU的device.

所以了解host和device的对性能优化是非常重要的。



# [2.1. Differences between Host and Device](http://docs.nvidia.com/cuda/cuda-c-best-practices-guide/#differences-between-host-and-device)





## Threading resources



host 上能同时运行的线程数目比较少（比如24个）

device上能同时运行的线程数目比较多（数量级通常为1E3，1E4等）



## Threads



操作系统必须交换CPU执行通道上和下的线程以提供多线程功能。因此，上下文切换(当交换两个线程时)既慢又昂贵。

相比之下，GPU上的线程非常轻量级。在典型的系统中，成千上万的线程排队等待工作(每个线程有32个线程)。如果GPU必须等待 one warp of threads，它只需开始在另一个线程上执行工作。

**简而言之，CPU内核被设计为每次最小化一个或两个线程的等待时间，而GPU被设计为处理大量并发的轻量级线程以最大化吞吐量。**



## RAM



host和device 各自具有各自不同的附接物理存储器。host和device内存由PCI Express ( PCIe )总线分隔，因此host内存中的项目必须偶尔通过总线传送到device内存，反之亦然





# [2.2. What Runs on a CUDA-Enabled Device?](http://docs.nvidia.com/cuda/cuda-c-best-practices-guide/#what-runs-on-cuda-enabled-device)





下面谈谈应该把应用的哪些部分放在device 上运行




      * 大数据集上的算术运算
      * 为了获得最佳性能，设备上运行的相邻线程的内存访问应该具有一定的一致性。**某些内存访问模式使硬件能够将多个数据项的读或写组合并到一个操作中**。当在CUDA上的计算中使用时，无法布局以实现合并的数据，或者没有足够的局部性来有效地使用L1或纹理缓存的数据，将倾向于看到较小的加速比。
      * host和device之间的数据交换尽可能少

        * **换到device上执行的数据一定会被做足够多的运算**，不然数据从Host传送到device的代价 可能与该运算在device上并行计算的优势向抵消，甚至得不偿失。
        * **数据应尽可能长时间保存在设备上。**因为传输应该最小化，所以在同一数据上运行多个内核的程序应该倾向于在内核调用之间将数据保留在设备上，而不是将中间结果传输到主机，然后再将它们发送回设备进行后续计算。就是说，如果有一段连续的操作要处理某些数据，就算其中的部分操作在host上运行要比在device上快（比如不是算数运算而是逻辑处理），那么考虑到数据传输的巨大代价，将所有数据都放在device上处理可能会更好。这种处理原则即使相对较慢的内核也可能是有利的，如果它避免了一个或多个PCIe传输。











