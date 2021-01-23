---
author: 111qqz
date: 2019-01-23 11:51:46+00:00
draft: false
title: 优化学习笔记(1):Loop unrolling
type: post
url: /2019/01/loop-unrolling/
categories:
- 优化
tags:
- halide
- 编译原理
---

<del>迫于生计，</del>最近要学习[halide](http://halide-lang.org/)

先去学习/复习一下常见的编译优化技巧。

loop unrolling，也就是循环展开，顾名思义，就是把循环展开来写。

    
    normal loop:
    int x;
     for (x = 0; x < 100; x++)
     {
         delete(x);
     }
    
    after loop unrolling:
    int x; 
     for (x = 0; x < 100; x += 5 )
     {
         delete(x);
         delete(x + 1);
         delete(x + 2);
         delete(x + 3);
         delete(x + 4);
     }


循环展开是一种优化，可以手动实现也可以编译器自动实现。


### 为什么要将循环展开？





 	  * 循环每次都需要判断终止条件，展开后可以消除这部分开销。
 	  * 减少[分支预测](https://en.wikipedia.org/wiki/Branch_predictor)开销。循环里的分支是指“跳出循环”还是“进行下一次迭代”
 	  * [vectorization](https://en.wikipedia.org/wiki/Automatic_vectorization)

    
    for (int y = 0; y < 4; y++) {
                for (int x_outer = 0; x_outer < 2; x_outer++) {
                    // The loop over x_inner has gone away, and has been
                    // replaced by a vectorized version of the
                    // expression. On x86 processors, Halide generates SSE
                    // for all of this.
                    int x_vec[] = {x_outer * 4 + 0,
                                   x_outer * 4 + 1,
                                   x_outer * 4 + 2,
                                   x_outer * 4 + 3};
                    int val[] = {x_vec[0] + y,
                                 x_vec[1] + y,
                                 x_vec[2] + y,
                                 x_vec[3] + y};
                    printf("Evaluating at <%d, %d, %d, %d>, <%d, %d, %d, %d>:"
                           " <%d, %d, %d, %d>\n",
                           x_vec[0], x_vec[1], x_vec[2], x_vec[3],
                           y, y, y, y,
                           val[0], val[1], val[2], val[3]);
                }
            }zhichi


可以看到最里面一层循环被展开以实现向量化.向量化是一种优化计算的手段。该优化的实现基于[SIMD](https://en.wikipedia.org/wiki/SIMD) 和[Advanced_Vector_Extensions(AVX)](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions)指令集架构的支持。
 	  * 消除和loop counter(i)有关的除法计算。

    
         for (int fused = 0; fused < 4*4; fused++) {
                int y = fused / 4;
                int x = fused % 4;
                printf("Evaluating at x = %d, y = %d: %d\n", x, y, x + y);
            }



 	  * 消除循环内部的分支。比如loop counter奇数和偶数时会进入不同的分支，那么将循环展开后，就消除了该分支。



### 有什么缺点？





 	  * 代码体积增加了。这对于嵌入式设备等往往是不可接受的。
 	  * 代码可读性变差了。
 	  * 单一指令可能会使用更多的寄存器，导致性能下降。
 	  * 如果循环内部包含函数调用，那么和函数的内联(inline)优化会有冲突。原因是，循环展开＋函数展开...代码的体积会爆炸。



### 参考资料





 	  * [Optimizing subroutines in assembly language An optimization guide for x86 platforms(chapter 12.12)](https://www.agner.org/optimize/optimizing_assembly.pdf)
 	  * [Loop unrolling](https://en.wikipedia.org/wiki/Loop_unrolling)




