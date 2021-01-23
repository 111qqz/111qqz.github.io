---
author: 111qqz
date: 2018-02-22 09:03:48+00:00
draft: false
title: 光流法初探
type: post
url: /2018/02/Optical-flow-notes/
categories:
- deep-learning
tags:
- 光流法
---

算是CV领域的传统算法了

只写两句话就够了。



<blockquote>**它是空间运动物体在观察成像平面上的像素运动的瞬时速度，是利用图像序列中像素在时间域上的变化以及相邻帧之间的相关性来找到上一帧跟当前帧之间存在的对应关系，从而计算出相邻帧之间物体的运动信息的一种方法。**

**研究光流场的目的就是为了从图片序列中近似得到不能直接得到的运动场。运动场，其实就是物体在三维真实世界中的运动；光流场，是运动场在二维图像平面上（人的眼睛或者摄像头）的投影。**</blockquote>





参考资料：

[光流Optical Flow介绍与OpenCV实现](http://blog.csdn.net/zouxy09/article/details/8683859)




