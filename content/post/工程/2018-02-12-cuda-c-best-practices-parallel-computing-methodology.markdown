---
author: 111qqz
date: 2018-02-12 04:58:31+00:00
draft: false
title: CUDA C Best Practices Guide 阅读笔记（1） 并行计算方法论(APOD)
type: post
url: /2018/02/cuda-c-best-practices-parallel-computing-methodology/
categories:
- 优化
tags:
- cuda
- 并行计算
---

APOD指的是Assess, Parallelize, Optimize, Deploy

![Assess, Parallelize, Optimize, Deploy.](http://docs.nvidia.com/cuda/cuda-c-best-practices-guide/graphics/apod-cycle.png)


如图所示，APOD过程是一个循环的过程，每次只进行一部分，从A到P到O到D,然后再进行下一轮的APOD



## Assess



对于一个项目，第一步要做的是接触(Assess)项目，得到项目代码中每部分的执行时间。有了这部分内容，开发者就可以找到并行优化的瓶颈所在，并开始尝试用GPU加速。

根据Amdahl's and Gustafson's laws，开发者可以确定并行优化的性能上界。



## Parallelize



找到瓶颈所在并确定了优化的目标和期望，开发者就可以优化代码了。调用一些如cuBLAS, cuFFT, or Thrust 的 GPU-optimized library  可能会很有效。

另一方面，有些应用需要开发者重构代码，以此让可以被并行优化得部分被暴露出来。



## Optimize



确定了需要被并行优化的部分之后，就要考虑具体得实现方式了。

具体得实现方式通常不过只有一种，所以充分理解应用的需求是很有必要的。

要记得，APOD是一个反复迭代的过程（找到可以优化的点，实现并测试优化，验证优化效果，然后再重复）

因为对于开发者来说，没有必要最初就找到解决所有性能瓶颈的策略。

优化可以在不同的level上进行，配合性能分析工具是很有帮助的。



## Deploy



**大的原则是当优化完一处之后，立刻将这一部分部署到生产环境，而不是再去寻找其他可以优化的地方。**

这样做有很多重要的原因，比如这会使得用户尽早从这个优化中收益（尽管提速只是部分的，但是仍然有价值）

此外，每次有改动就重新部署，也使得变化是平稳而不是激进的，这有助于减少风险。



### 





## Recommendations and Best Practice



优化根据对性能影响程度的不同有不同的优先级。

**在先要处理低优先级的优化之前，一定要确保其他所有的高优先级优化都做完了。**

这种方法将倾向于为所投入的时间提供最佳结果，并且将避免过早优化的陷阱。



需要说明的一点是，教程中的代码为了方便简洁没有关于任何 check error的部分。

在实际上这是不可取的（**这不同于编写C++代码!**）










