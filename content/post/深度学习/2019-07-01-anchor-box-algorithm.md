---
title: "Anchor Box Algorithm"
date: 2019-07-01T19:53:24+08:00
draft: false
author: "111qqz"
type: post
url: /2019/07/Anchor-Box-Algorithm/
categories:
- deep-learning

tags:
- Object Detection
- Anchor box 
---


## 动机
将一张图分成多个grid cell进行检测之后,每个cell只能检测到一个object.
如果这个grid cell中不止有一个物体要怎么办呢? 因此提出了anchor box algorithm来解决这个问题.

## 什么是anchor
anchor其实就是一组预设的参考框,每个框有不同的长宽比和大小.
提供参考框可以将问题转换为"这个固定参考框中有没有认识的目标，目标框偏离参考框多远". 这样如果一个grid cell中有多个物体,那么就可以形状最姐姐的anchor box来负责检测该物体.
![anchor box sample](https://i.loli.net/2019/07/01/5d19f9e2869ad32385.jpg)


## anchor的其他用途

实际上当grid cell很多的时候,一个grid cell中有多个object的情况是很少的.但是anchor box仍然是十分重要的.因为我们可以通过预设一些特殊的anchor box,来帮助检测到一些极端形状的物体(比如很长的物体或者很宽的物体)

## 输出结果

有了anchor之后,每个grid cell的输出可能不再唯一.
于是从之前的每个grid cell对应一个输出结果,变成了每个二元组(grid_cell,anchor box)对应一个结果.
结果的格式呢,一图胜千言:
![anchor box algorithm的输出格式](https://i.loli.net/2019/07/01/5d19f97b2fe3b98042.jpg)

## 局限性
由于anchor box是要预设的,那么如果我只预设了两个anchor box,但是一个grid cell中有三个object,怎么办呢? 很遗憾,是没有办法的.
另外一个case是,如果两个object都与其中一个anchor的形状最为接近,也是没有办法检测出两个物体的.

## anchor box的生成
最初anchor box是通过人手工设定的,之后的YOLO的paper中提出了使用k-means的算法来生成anchor box.