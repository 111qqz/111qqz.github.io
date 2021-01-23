---
author: 111qqz
date: 2017-09-05 12:30:17+00:00
draft: false
title: 反向传播学习笔记
type: post
url: /2017/09/back-propagation-notes/
categories:
- deep-learning
tags:
- 反向传播
---

先说下自己目前很笼统的理解：

反向传播是用来快速计算梯度的一种方法；

过程大概是把计算过程用计算图表示，这样每一个中间步骤都有一个节点，每一个local gradient都会比较容易计算；

思想涉及 chain rule + 计算图 + 记忆化

因为计算不同自变量的偏导数会存在很多共同路径，这部分就只计算了一次，因此可以加快计算速度。

所以核心的东西大概是两点：




      * 用计算图表示计算，局部gradient 替代繁琐的微积分计算
      * 共同部分只计算一次，类似一个记忆化。





