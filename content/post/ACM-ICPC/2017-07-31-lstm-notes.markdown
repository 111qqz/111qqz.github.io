---
author: 111qqz
date: 2017-07-31 10:05:01+00:00
draft: false
title: Long Short-Term Memory （LSTM） 网络 学习笔记
type: post
url: /2017/07/lstm-notes/
categories:
- deep-learning
tags:
- LSTM
- RNN
---

### 参考资料：


[维基百科_长短期记忆(LSTM)](https://zh.wikipedia.org/wiki/)

[Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

[[译] 理解 LSTM 网络](http://www.jianshu.com/p/9dc9f41f0b29)

[LSTM笔记](http://blog.leanote.com/post/petra_yu/LSTM)



翻译的比较一般，建议看原文....比如cell还是不要翻译成【细胞】比较好吧...让人以为和生物学的【细胞】有什么关系呢orz



说下我自己的理解：

LSTM是一种特殊的[RNN](https://zh.wikipedia.org/wiki/)，所谓RNN,也就是循环神经网络，对之前的信息存在“记忆”，可以解决带有时序性的问题。

所谓时序性的问题，简单理解就是，当前的结果依赖于之前的信息。

比如“我来自内蒙古，我能讲一口流利的____” 横线处大概率填写“蒙语”，这是因为前面的信息“内蒙古”

LSTM的全称是long short term memory, LSTM默认就可以记住长期信息，从而实现信息的持久化。

LSTM的本质是一种构造法，通过特定的设计完成信息的持久化。

LSTM有如下结构：


## 1、cell单元


最基本的单元，从上一个时间节点到当前时间节点是线性控制的。LSTM能够通过门结构增加或者减少信息。
![cell](https://leanote.com/api/file/getImage?fileId=5762cee2ab64415d8b00409b)

门结构上有sigmoid层（输出0~1）作用，信息通过乘上一个0~1的来决定能够通过多少信息。
![sigmoid门](https://leanote.com/api/file/getImage?fileId=5762cee2ab64415d8b004093)



## 2、forget门


forget门决定有多少历史信息能够通过，这一层通过ht−1ht−1和xtxt决定，ft=sigmoid(w(f)xt+u(i)ht−1)∈[0,1]ft=sigmoid(w(f)xt+u(i)ht−1)∈[0,1]作用到Ct−1Ct−1上。
![forget门](https://leanote.com/api/file/getImage?fileId=5762cee2ab64415d8b004099)



## 3、input门和新的cell


input门是一个sigmoid层决定需要更新多少信息，新的cell是一个tanh层决定要添加多少信息进入记忆单元cell。分别为it=sigmoid(wixt+u(i)ht−1)it=sigmoid(wixt+u(i)ht−1)，与ct~=tanh(w(c)xt+ucht−1)ct~=tanh(w(c)xt+ucht−1)
![](https://leanote.com/api/file/getImage?fileId=5762cee2ab64415d8b004097)



## 4、更新记忆单元


forget门作用在ct−1ct−1上，input门和新的cell结合加入组合成新的记忆单元ct=ft.∗ct−1+it.∗ct~ct=ft.∗ct−1+it.∗ct~
![c_t](https://leanote.com/api/file/getImage?fileId=5762cee2ab64415d8b004091)



## 5、output门


添加sigmoid 的output门决定cell单元的信息有多少输出，而cell上套一个tanh使输出在-1到1之间，ot=sigmoid(w(o)xt+u(o)ht−1)ot=sigmoid(w(o)xt+u(o)ht−1)，ht=ot.∗tanh(ct)ht=ot.∗tanh(ct)。
![](https://leanote.com/api/file/getImage?fileId=5762cee2ab64415d8b004095)

