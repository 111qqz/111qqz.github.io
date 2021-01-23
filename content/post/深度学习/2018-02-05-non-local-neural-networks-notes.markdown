---
author: 111qqz
date: 2018-02-05 02:24:34+00:00
draft: false
title: Non-local Neural Networks 阅读笔记
type: post
url: /2018/02/non-local-neural-networks-notes/
categories:
- deep-learning
tags:
- Non-local Neural Networks
---

先粗略读了2遍orz.可能不够严谨，先写一些high-level的理解。

对于序列或者图片数据，如果想获得一个long-range的依赖，通常的做法是循环神经网络（对于序列）或者深层的卷积神经网络（对于图片数据）

但是循环操作（当前的处理依赖于前面有限的若干个）和卷积操作都是一种局部操作。

但是这种局部操作是有一些局限的，比如不好优化，计算代价比较大等。

这篇paper提出了non-local 这个操作。

non-local操作是计算机视觉中广泛使用的一种降噪算法，即non-local mean的一般化。

non-local operation被认为是一个可以被广泛使用的操作，几乎可以和当前神经网络的其他部件结合。

含有non-local opetation的一个基本操作单元我们称之为一个 non-local block

含有non-local block 的神经网络我们可以称之为Non-local Neural Networks

non-local operation是非常有效的，及时神经网络只有很少的几层（比如5）

non-local operation和《Attention is all you need》 中提出的self-attention是相似的

全连接操作可以看做non-local operation的一个特例。

[Non-local Neural Networks 原始论文](https://drive.google.com/open?id=1c99OEFGyByLju8Jh1eYWUA2njiyhcc5C)
