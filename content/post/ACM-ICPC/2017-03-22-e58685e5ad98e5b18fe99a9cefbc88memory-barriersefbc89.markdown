---
author: 111qqz
date: 2017-03-22 05:16:53+00:00
draft: false
title: 内存屏障（Memory Barriers）
type: post
url: /2017/03/memory-barriers/
categories:
- 其他
tags:
- levelDB
- 内存屏障
---

起因是最近在看levelDB源码，其中port里的**atomic_pointer.h文件用到了内存屏障。。**

于是来学习一下。。

粗略得说下我自己的理解。

代码的顺序并不和执行的顺序完全对应，出于对效率的追求，cpu和编译器会对一些顺序指令重排，以期得到最大的执行效率。

比如下面这段代码：

    
    // example 2
        // void *ptr, v, _store;
        v = ptr;
        _store = v;
        somefunc();
        v = _store;


v的值是没有改变的，那么编译器可能会认为`_store = v; v = _store;` 是多余的，就直接把这一段给“优化”掉了。这段代码在单线程中确实是多余的，**但是在多线程环境下**，可能在`somefunc()`被调用的时候，另一个线程把v的值给改变了，而这种情况是编译器无法发现的。因此，为了避免这种情况。。。内存屏障登场！

摘自维基百科：


<blockquote>**内存屏障**，也称**内存栅栏**，**内存栅障**，**屏障指令**等，是一类[同步屏障](https://zh.wikipedia.org/wiki/)指令，是CPU或编译器在对内存随机访问的操作中的一个同步点，使得此点之前的所有读写操作都执行后才可以开始执行此点之后的操作。

大多数现代计算机为了提高性能而采取[乱序执行](https://zh.wikipedia.org/wiki/)，这使得内存屏障成为必须。

语义上，内存屏障之前的所有写操作都要写入内存；内存屏障之后的读操作都可以获得同步屏障之前的写操作的结果。因此，对于敏感的程序块，写操作之后、读操作之前可以插入内存屏障。</blockquote>




<blockquote>在多线程环境里需要使用某种技术来使程序结果尽快可见。。请先假定一个事实：一旦内存数据被推送到缓存，就会有消息协议来确保所有的缓存会对所有的共享数据同步并保持一致。这个使内存数据对CPU核可见的技术被称为**内存屏障或内存栅栏**。</blockquote>




再看一个例子

    
    // get start time
    for (int i = 0; i != 100000; i++) {
        MemoryBarrier()
    }
    // get end time


这段代码，是想知道for循环空转100000次的耗时，这里就需要加入一个**MemoryBarrier**，如果不加，那么编译器可能就会直接把这个无意义的for循环直接优化掉了。

除了编译器，cpu由于指令流水线或者超流水线等计数，也可能导致出现乱序执行的情况。

内存屏障提供了两个功能。首先，它们通过确保从另一个CPU来看屏障的两边的所有指令都是正确的程序顺序，而保持程序顺序的外部可见性；其次它们可以实现内存数据可见性，确保内存数据会同步到CPU缓存子系统。

不过内存平展由于阻碍了cpu和编译器的部分优化。。。因此对性能的影响是不忽略的。


<blockquote>为了达到最佳性能，最好是把要解决的问题模块化，这样处理器可以按单元执行任务，然后在任务单元的边界放上所有需要的内存屏障。采用这个方法可以让处理器不受限的执行一个任务单元。合理的内存屏障组合还有一个好处是：缓冲区在第一次被刷后开销会减少，因为再填充改缓冲区不需要额外工作了。</blockquote>


内存屏障的实现不同平台差别很大。。。因为我们可以看到**atomic_pointer.h文件中 一堆和平台相关的条件编译...**

    
    // Copyright (c) 2011 The LevelDB Authors. All rights reserved.
    // Use of this source code is governed by a BSD-style license that can be
    // found in the LICENSE file. See the AUTHORS file for names of contributors.
    
    // AtomicPointer provides storage for a lock-free pointer.
    // Platform-dependent implementation of AtomicPointer:
    // - If the platform provides a cheap barrier, we use it with raw pointers
    // - If <atomic> is present (on newer versions of gcc, it is), we use
    //   a <atomic>-based AtomicPointer.  However we prefer the memory
    //   barrier based version, because at least on a gcc 4.4 32-bit build
    //   on linux, we have encountered a buggy <atomic> implementation.
    //   Also, some <atomic> implementations are much slower than a memory-barrier
    //   based implementation (~16ns for <atomic> based acquire-load vs. ~1ns for
    //   a barrier based acquire-load).
    // This code is based on atomicops-internals-* in Google's perftools:
    // http://code.google.com/p/google-perftools/source/browse/#svntrunksrcbase
    
    #ifndef PORT_ATOMIC_POINTER_H_
    #define PORT_ATOMIC_POINTER_H_
    
    #include <stdint.h>
    #ifdef LEVELDB_ATOMIC_PRESENT
    #include <atomic>
    #endif
    #ifdef OS_WIN
    #include <windows.h>
    #endif
    #ifdef OS_MACOSX
    #include <libkern/OSAtomic.h>
    #endif
    
    #if defined(_M_X64) || defined(__x86_64__)
    #define ARCH_CPU_X86_FAMILY 1
    #elif defined(_M_IX86) || defined(__i386__) || defined(__i386)
    #define ARCH_CPU_X86_FAMILY 1
    #elif defined(__ARMEL__)
    #define ARCH_CPU_ARM_FAMILY 1
    #elif defined(__aarch64__)
    #define ARCH_CPU_ARM64_FAMILY 1
    #elif defined(__ppc__) || defined(__powerpc__) || defined(__powerpc64__)
    #define ARCH_CPU_PPC_FAMILY 1
    #elif defined(__mips__)
    #define ARCH_CPU_MIPS_FAMILY 1
    #endif
    
    namespace leveldb {
    namespace port {
    
    // Define MemoryBarrier() if available
    // Windows on x86
    #if defined(OS_WIN) && defined(COMPILER_MSVC) && defined(ARCH_CPU_X86_FAMILY)
    // windows.h already provides a MemoryBarrier(void) macro
    // http://msdn.microsoft.com/en-us/library/ms684208(v=vs.85).aspx
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // Mac OS
    #elif defined(OS_MACOSX)
    inline void MemoryBarrier() {
      OSMemoryBarrier();
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // Gcc on x86
    #elif defined(ARCH_CPU_X86_FAMILY) && defined(__GNUC__)
    inline void MemoryBarrier() {
      // See http://gcc.gnu.org/ml/gcc/2003-04/msg01180.html for a discussion on
      // this idiom. Also see http://en.wikipedia.org/wiki/Memory_ordering.
      __asm__ __volatile__("" : : : "memory");
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // Sun Studio
    #elif defined(ARCH_CPU_X86_FAMILY) && defined(__SUNPRO_CC)
    inline void MemoryBarrier() {
      // See http://gcc.gnu.org/ml/gcc/2003-04/msg01180.html for a discussion on
      // this idiom. Also see http://en.wikipedia.org/wiki/Memory_ordering.
      asm volatile("" : : : "memory");
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // ARM Linux
    #elif defined(ARCH_CPU_ARM_FAMILY) && defined(__linux__)
    typedef void (*LinuxKernelMemoryBarrierFunc)(void);
    // The Linux ARM kernel provides a highly optimized device-specific memory
    // barrier function at a fixed memory address that is mapped in every
    // user-level process.
    //
    // This beats using CPU-specific instructions which are, on single-core
    // devices, un-necessary and very costly (e.g. ARMv7-A "dmb" takes more
    // than 180ns on a Cortex-A8 like the one on a Nexus One). Benchmarking
    // shows that the extra function call cost is completely negligible on
    // multi-core devices.
    //
    inline void MemoryBarrier() {
      (*(LinuxKernelMemoryBarrierFunc)0xffff0fa0)();
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // ARM64
    #elif defined(ARCH_CPU_ARM64_FAMILY)
    inline void MemoryBarrier() {
      asm volatile("dmb sy" : : : "memory");
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // PPC
    #elif defined(ARCH_CPU_PPC_FAMILY) && defined(__GNUC__)
    inline void MemoryBarrier() {
      // TODO for some powerpc expert: is there a cheaper suitable variant?
      // Perhaps by having separate barriers for acquire and release ops.
      asm volatile("sync" : : : "memory");
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    // MIPS
    #elif defined(ARCH_CPU_MIPS_FAMILY) && defined(__GNUC__)
    inline void MemoryBarrier() {
      __asm__ __volatile__("sync" : : : "memory");
    }
    #define LEVELDB_HAVE_MEMORY_BARRIER
    
    #endif
    
    // AtomicPointer built using platform-specific MemoryBarrier()
    #if defined(LEVELDB_HAVE_MEMORY_BARRIER)
    class AtomicPointer {
     private:
      void* rep_;
     public:
      AtomicPointer() { }
      explicit AtomicPointer(void* p) : rep_(p) {}
      inline void* NoBarrier_Load() const { return rep_; }
      inline void NoBarrier_Store(void* v) { rep_ = v; }
      inline void* Acquire_Load() const {
        void* result = rep_;
        MemoryBarrier();
        return result;
      }
      inline void Release_Store(void* v) {
        MemoryBarrier();
        rep_ = v;
      }
    };
    
    // AtomicPointer based on <cstdatomic>
    #elif defined(LEVELDB_ATOMIC_PRESENT)
    class AtomicPointer {
     private:
      std::atomic<void*> rep_;
     public:
      AtomicPointer() { }
      explicit AtomicPointer(void* v) : rep_(v) { }
      inline void* Acquire_Load() const {
        return rep_.load(std::memory_order_acquire);
      }
      inline void Release_Store(void* v) {
        rep_.store(v, std::memory_order_release);
      }
      inline void* NoBarrier_Load() const {
        return rep_.load(std::memory_order_relaxed);
      }
      inline void NoBarrier_Store(void* v) {
        rep_.store(v, std::memory_order_relaxed);
      }
    };
    
    // Atomic pointer based on sparc memory barriers
    #elif defined(__sparcv9) && defined(__GNUC__)
    class AtomicPointer {
     private:
      void* rep_;
     public:
      AtomicPointer() { }
      explicit AtomicPointer(void* v) : rep_(v) { }
      inline void* Acquire_Load() const {
        void* val;
        __asm__ __volatile__ (
            "ldx [%[rep_]], %[val] \n\t"
             "membar #LoadLoad|#LoadStore \n\t"
            : [val] "=r" (val)
            : [rep_] "r" (&rep_)
            : "memory");
        return val;
      }
      inline void Release_Store(void* v) {
        __asm__ __volatile__ (
            "membar #LoadStore|#StoreStore \n\t"
            "stx %[v], [%[rep_]] \n\t"
            :
            : [rep_] "r" (&rep_), [v] "r" (v)
            : "memory");
      }
      inline void* NoBarrier_Load() const { return rep_; }
      inline void NoBarrier_Store(void* v) { rep_ = v; }
    };
    
    // Atomic pointer based on ia64 acq/rel
    #elif defined(__ia64) && defined(__GNUC__)
    class AtomicPointer {
     private:
      void* rep_;
     public:
      AtomicPointer() { }
      explicit AtomicPointer(void* v) : rep_(v) { }
      inline void* Acquire_Load() const {
        void* val    ;
        __asm__ __volatile__ (
            "ld8.acq %[val] = [%[rep_]] \n\t"
            : [val] "=r" (val)
            : [rep_] "r" (&rep_)
            : "memory"
            );
        return val;
      }
      inline void Release_Store(void* v) {
        __asm__ __volatile__ (
            "st8.rel [%[rep_]] = %[v]  \n\t"
            :
            : [rep_] "r" (&rep_), [v] "r" (v)
            : "memory"
            );
      }
      inline void* NoBarrier_Load() const { return rep_; }
      inline void NoBarrier_Store(void* v) { rep_ = v; }
    };
    
    // We have neither MemoryBarrier(), nor <atomic>
    #else
    #error Please implement AtomicPointer for this platform.
    
    #endif
    
    #undef LEVELDB_HAVE_MEMORY_BARRIER
    #undef ARCH_CPU_X86_FAMILY
    #undef ARCH_CPU_ARM_FAMILY
    #undef ARCH_CPU_ARM64_FAMILY
    #undef ARCH_CPU_PPC_FAMILY
    
    }  // namespace port
    }  // namespace leveldb
    
    #endif  // PORT_ATOMIC_POINTER_H_




参考资料：

[内存屏障_维基百科](https://zh.wikipedia.org/wiki/)

[内存屏障_并发编程网](http://ifeve.com/memory-barriers-or-fences/)

[LINUX内核之内存屏障](http://www.cnblogs.com/icanth/archive/2012/06/10/2544300.html)
