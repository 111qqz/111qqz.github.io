---
author: 111qqz
date: 2017-03-21 09:24:56+00:00
draft: false
title: Lock-free vs wait-free concurrency
type: post
url: /2017/03/lock-free-vs-wait-free-concurrency/
categories:
- c++
tags:
- levelDB
---

[参考资料](https://rethinkdb.com/blog/lock-free-vs-wait-free-concurrency/)

看leveldb源码中遇到的，关于lock-free 和 wait-free..感觉这个讲得不错，我试着翻译一下？


<blockquote>There are two types of [non-blocking thread synchronization](http://en.wikipedia.org/wiki/Non-blocking_synchronization) algorithms - lock-free, and wait-free. Their meaning is often confused. In lock-free systems, while any particular computation may be blocked for some period of time, all CPUs are able to continue performing other computations. To put it differently, while a given thread might be blocked by other threads in a lock-free system, all CPUs can continue doing other useful work without stalls. Lock-free algorithms increase the overall throughput of a system by occassionally increasing the latency of a particular transaction. Most high- end database systems are based on lock-free algorithms, to varying degrees.</blockquote>


有两种 [无阻塞线程同步算法](https://en.wikipedia.org/wiki/Non-blocking_algorithm)，一种是lock-free，一种是wait-free，它们的含义经常被搞混。在一个lock-free系统中，尽管某个特定的计算会被阻碍一段时间，所有的cpu还是能够继续其他计算。换一种说法，尽管在一个lock-free的系统里，一个线程可能被其他线程阻碍，所有的cpu仍然可以继续做其他工作而不做停顿。lock-free算法通过偶然增加一个特定事物的延迟，增加了系统总体的吞吐率。大多数高端数据库系统都在某种程度上基于lock-free 算法。




<blockquote>By contrast, wait-free algorithms ensure that in addition to all CPUs continuing to do useful work, no computation can ever be blocked by another computation. Wait-free algorithms have stronger guarantees than lock-free algorithms, and ensure a high thorughput without sacrificing latency of a particular transaction. They’re also much harder to implement, test, and debug. The [lockless page cache](http://lwn.net/Articles/291826/)patches to the Linux kernel are an example of a wait-free system.</blockquote>


与此相反，wait-free算法除了保证所有cpu继续做其他工作以外，还保证不会有任何计算被另一个计算阻止。wait-free算法比lock-free算法有更强的保证，确保了在不牺牲某一事物的延迟的基础上，拥有更高的吞吐率.wait-free算法因此也更加难以实现，测试，调试。linux内核的无锁页面缓存（？）就是一个wait-free系统的例子。




<blockquote>In a situation where a system handles dozens of concurrent transactions and has [soft latency requirements](http://en.wikipedia.org/wiki/Real-time_computing#Hard_and_soft_real-time_systems), lock-free systems are a good compromise between development complexity and high concurrency requirements. A database server for a website is a good candidate for a lock-free design. While any given transaction might block, there are always more transactions to process in the meantime, so the CPUs will never stay idle. The challenge is to build a transaction scheduler that maintains a good mean latency, and a well bounded standard deviation.</blockquote>


在一个系统处理几十个并发事务并且对延迟要求不高的情况下，lock-free系统是开发复杂性和高并发性要求之间的良好折衷。一个网站的数据库服务器是lock-free系统的很好的体现。尽管某个特定的事物可能被阻塞，但同时也有更多的事务要处理，所以CPU永远不会空闲。面临的挑战是建立一个好的事物调度表，以此来获得尽可能低的平均延迟和一个有界的标准偏差。


<blockquote>In a scenario where a system has roughly as many concurrent transactions as CPU cores, or has hard real-time requirements, the developers need to spend the extra time to build wait-free systems. In these cases blocking a single transaction isn’t acceptable - either because there are no other transactions for the CPUs to handle, minimizing the throughput, or a given transaction needs to complete with a well defined non-probabilistic time period. Nuclear reactor control software is a good candidate for wait-free systems.</blockquote>



















在一个场景中，系统与CPU内核大致相同数量的并发事务，或者有硬实时要求，开发人员需要花费额外的时间来构建wait-free系统。在这种情况下，阻塞单个事务是不可接受的，要么是因为CPU没有其他事务要处理从而减少了吞吐量，要么是给定的事务需要用一个定义良好的非概率时间段来完成（相对比较确定的时间的意思？）。核反应堆控制软件是wait-free系统的一个很好的体现。

















<blockquote></blockquote>
