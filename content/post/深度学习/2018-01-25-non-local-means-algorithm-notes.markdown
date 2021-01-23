---
author: 111qqz
date: 2018-01-25 02:53:52+00:00
draft: false
title: non-local means algorithm 学习笔记
type: post
url: /2018/01/non-local-means-algorithm-notes/
categories:
- deep-learning
tags:
- image denoising
- non-local means
---

终于忙完学校的事情可以干正事了orz

这里会记录一些第一遍看paper的过程中遇到的一些影响理解的概念，不过大多不会深究，只算做粗浅的理解。



1、高斯金字塔：

高斯金字塔是最基本的图像塔。首先将原图像作为最底层图像G0（高斯金字塔的第0层），利用高斯核（5*5）对其进行卷积，然后对卷积后的图像进行下采样（去除偶数行和列）得到上一层图像G1，将此图像作为输入，重复卷积和下采样操作得到更上一层图像，反复迭代多次，形成一个金字塔形的图像数据结构，即高斯金字塔。

2、拉普拉斯金字塔

在高斯金字塔的运算过程中，图像经过卷积和下采样操作会丢失部分高频细节信息。为描述这些高频信息，人们定义了拉普拉斯金字塔(Laplacian Pyramid， LP)。**用高斯金字塔的每一层图像减去其高一层图像上采样并高斯卷积之后的预测图像**，得到一系列的差值图像即为 LP 分解图像。

将Gl内插方法得到放大图像_Gl，使_Gl的尺寸与*Gl-1的尺寸相同，即放大算子Expand。

参考资料：

[Gaussian and Laplacian Pyramids](https://www.cs.utah.edu/~arul/report/node12.html)

[拉普拉斯金字塔融合](http://www.cnblogs.com/silence-hust/p/4193208.html)


