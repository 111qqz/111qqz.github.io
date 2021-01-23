---
author: 111qqz
date: 2018-02-22 02:25:00+00:00
draft: false
title: Pose-driven Deep Convolutional Model for Person Re-identification 阅读笔记
type: post
url: /2018/02/pose-driven-deep-convolutional-model-for-person-re-identification/
categories:
- deep-learning
tags:
- Pose-driven
- reid
---

[1709.08325](https://arxiv.org/abs/1709.08325)

Reid问题指的是判断一个probe person 是否在被不同的camera捕获的gallery person 中出现。

通常是如下情景：给出一个特定camera下某个特定人的probe image 或者 video sequence，从其他camera处询问这个人的图像，地点，时间戳。



ReID问题至今没有很好得解决，主要原因是，不同camera下，人的姿势（pose),观察的视角(viewpoint) 变化太大了。

传统方法主要在两个大方向上努力:




      1. **用一些在图像上抽取的不变量来作为人的特征feture**
      2. **去学习一个不同的距离度量方式，以至于同一个人在不同camera之间的距离尽可能小。**


但是由于在实际中，行人的pose和 摄像机的viewpoint不可控，因此与之相关的feture可能不够健壮。

学习新的不同的距离度量方式需要每对camera分别计算距离，然而这是O(n^2)的时间复杂度，凉凉。



近些年Deep learning发展迅猛，并且在很多CV任务上表现良好。所以自然有人想把Deep learning 方法应用到Reid任务上。

目前Deep learning的做法一般分为两部分：


      * 使用softmax loss 结合person ID labels得到一个global representation
      * 首先用预定义好的body 刚体模型去得到local representation,然后将global 和local representation 融合。


目前用deep learning的方法效果已经不错了，比传统方法要好。但是目前的deep learning方法没有考虑到**人的姿势(pose)的变化。**

虽然目前也有些deep learning的办法在处理Reid问题时使用pose estimation algorithms 来预测行人的pose,

但是这种办法是手动完成而不是一个end-to-end（[什么是end-to-end 神经网络](https://111qqz.com/wordpress/2018/02/end-to-end-/)） 的过程

所以考虑pose的潜力还没有被完全发掘。

这篇paper主要做了以下工作：




      * 提出了一种新的深层结构，将身体部分转化成相应的特征表示，以此来克服pose变化带来的问题
      * 提出了一个用来自动学习各部分权值的sub-network


这两部分工作都是end-to-end的












