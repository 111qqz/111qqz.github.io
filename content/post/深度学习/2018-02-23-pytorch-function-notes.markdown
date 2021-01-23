---
author: 111qqz
date: 2018-02-23 02:55:25+00:00
draft: false
title: pytorch 函数笔记
type: post
url: /2018/02/pytorch-function-notes/
categories:
- deep-learning
tags:
- python
- pytorch
---

记录一些常用的...总去查文档也是有点麻烦




      * 


### tensor.view 的作用是reshape 比如 a = torch.range(1, 16) 得到一个tensor  that has 16 elements from 1 to 16. 在a=a.view(4,4)就得到了一个4*4的tensor。 需要注意reshape之后元素的个数不能改变(16==4*4)  参数-1的作用是，我懒得算这一维度应该是多少,（由于元素个数不能改变）所以希望自动被计算。**需要注意的是，只有一个维度可以写-1。 **不过view和reshape有些区别：_reshape always copies memory. view never copies memory_



      * 


### torch.squeeze  将输入张量形状中的`1` 去除并返回。 如果输入是形如(A×1×B×1×C×1×D)，那么输出形状就为： (A×B×C×D)当给定`dim`时，那么挤压操作只在给定维度上。例如，输入形状为: (A×1×B), `squeeze(input, 0)` 将会保持张量不变，只有用 `squeeze(input, 1)`，形状会变成 (A×B)。注意： 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。



      * 


### torch.unsqueeze  返回一个新的张量，对输入的制定位置插入维度 1 注意： 返回张量与输入张量共享内存，所以改变其中一个的内容会改变另一个。如果`dim`为负，则将会被转化dim+input.dim()+1



    
    >>> x = torch.Tensor([1, 2, 3, 4])
    >>> torch.unsqueeze(x, 0)
     1  2  3  4
    [torch.FloatTensor of size 1x4]
    >>> torch.unsqueeze(x, 1)
     1
     2
     3
     4
    [torch.FloatTensor of size 4x1]



      * 


### tensor.expand(*size)   扩展tensor.可以保持维度数目不变，每一维度的size增加(比如A*B变到C*D,其中C>=A,D>=B).-1参数表示某一个维度的size不发生改变  . 有可以扩展tensor到更多的维度，新增加的维度会默认放在最前面，并且不能以-1作为参数。



      * 





### **tensor.contiguous  将一个tensor变成连续的。（一些ops如expand/expand_as会让tensor 不连续）**


















