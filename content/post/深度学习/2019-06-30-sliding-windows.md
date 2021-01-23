---
title: "目标检测领域的滑动窗口算法"
date: 2019-06-30T16:55:40+08:00
draft: false
author: "111qqz"
type: post
url: /2019/06/sliding-windows/
categories:
- deep-learning

tags:
- sliding Windows
- Object Detection

---

对象检测（Object Detection）的目的是”识别对象并给出其在图中的确切位置”，其内容可解构为三部分：

- 识别某个对象（Classification）；
- 给出对象在图中的位置（Localization）；
- 识别图中所有的目标及其位置（Detection）。

本文将介绍**滑动窗口**这一方法.

## 滑动窗口 

滑动窗口是这些方法中最暴力的一个.简单来说,就是暴力枚举侯选框的尺寸和位置,每次crop得到一张小图,将每个小图送进后面的分类器进行分类.
早年后面通常会接一个计算量比较小的分类器,比如SVM,随着算力的提升,现在常常后面会接CNN.
![滑动窗口演示图](https://www.pyimagesearch.com/wp-content/uploads/2015/03/sliding-window-animated-adrian.gif)

值得一提的是,原始的滑动窗口方法是将每个小图,分别放入后面的分类器.但是实际上,小图和小图之间,是有overlap的,也就是说做了很多重复的计算.
因此一个显然的改进是使用CNN来实现滑动窗口算法,
![CNN改进的滑动窗口算法](https://i.loli.net/2019/06/30/5d18adf01d6d377943.png)

这种方法的优点是比较无脑,实现和理解起来都很简单.缺点是计算量还是比较大.





## 参考链接
-  [Sliding Windows for Object Detection with Python and OpenCV](https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/)

- [深度学习基础 - 对象检测（滑窗、CNN、YOLO）](https://pnyuan.github.io/blog/ml_practice/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%9F%BA%E7%A1%80%20-%20%E5%AF%B9%E8%B1%A1%E6%A3%80%E6%B5%8B%EF%BC%88CNN+%E6%BB%91%E7%AA%97+YOLO%EF%BC%89/)








