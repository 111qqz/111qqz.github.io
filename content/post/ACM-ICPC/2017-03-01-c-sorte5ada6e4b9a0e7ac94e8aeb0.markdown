---
author: 111qqz
date: 2017-03-01 07:27:12+00:00
draft: false
title: C++ sort学习笔记
type: post
url: /2017/03/c-sort/
categories:
- c++
tags:
- cpp
- sort
---

回想起大一的时候打cf...那个时候对C++还不怎么熟悉。。。用sort不会自定义排序方式。。

于是手写快排。。。直接取中间元素没加随机化。。。跪了。。。

后来知道sort怎么写以后。。发现sort是可以通过的。。。

于是我就一直以为sort是带随机化的快排。。。

然而实际上是：

**sort在数据量比较大的时候用quick_sort...当分段后的数据量小于某个门槛，为了避免对此递归带来的额外负担。。采取插入排序的策略。。**

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/03/Workspace-1_015.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/03/Workspace-1_015.png)

以及。。。快排在最快情况下还是会到达平方的复杂度。。。

于是有人发明了introsort...中文翻译叫内省排序。。。？

[维基百科_introsort](https://zh.wikipedia.org/wiki/)

这个算法其实就是。。对于数据量大的时候。。。一开始还是快排。。。但是当递归深度过深时。。用堆排。。。

据说现在的STL一般都是用了introsort....


