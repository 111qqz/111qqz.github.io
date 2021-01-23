---
author: 111qqz
date: 2018-02-18 10:46:35+00:00
draft: false
title: Deep Mutual Learning（相互学习） 阅读笔记
type: post
url: /2018/02/deep-mutual-learning-notes/
categories:
- deep-learning
tags:
- Model distillation
- Mutual Learning
---

[原始论文](https://arxiv.org/abs/1706.00384)

DNN在很多问题上效果很不错，但是由于深度和宽度过大，导致需要的执行时间和内存过大。我们需要讨论一些能快速执行并且对内存的需要不大的模型。

已经有很多方法来做这件事，比较重要的是Model distillation（模型蒸馏）

基于蒸馏的模型压缩的有效性是基于一个发现：**小的网络有和大的网络一样的表达能力，只不过是更难以训练找到合适的参数。**

也就是说，难点在于优化(以找到合适的参数）而不在于网络的尺寸。

蒸馏的模型的做法是把一个有效的(deep or/and wide) network 作为teacher network,让一个size 较小的 student network 模仿teacher network.

这样做的好处是，size小的多的student network训练如何模仿teacher network通常要比直接训练得到目标函数容易，而效果上与teacher network相当，甚至超过teacher network.



在这篇paper中，作者提出了一个和蒸馏模型相关但是不同的模型: Deep Mutual Learning (相互学习，以下缩写为**DML**)

蒸馏模型开始于一个强大的教师网络，并通过教师网络**单向(one way)**教授学生网络知识。

相反，DML中,开始于一群没有经受过训练的学生网络。

具体来说，每个学生训练有两种损失:




      * **常规的监督学习损失和对齐的模仿损失**
      * **每个学生的在班级中落后于其他学生的概率。**


结果表明，DML的方式：比每个学生网络单独学习要好，也比传统的传统的蒸馏模型要好。

此外，我们发现，对几个tearcher network  使用 DML，要往往有更好的结果。

另外一些发现：


      * 效果随着班级中学生网络的数量的增加而增加
      * 它适用于各种网络体系结构和异构群组


关于DML为什么有效的直觉讨论：


      * 常规的监督学习损失保证每个学生单独学习时，整体上结果是越来越好的。
      * 由于初始条件不同，对下一个最可能的class的预测概率不同，这是额外信息的来源。

























