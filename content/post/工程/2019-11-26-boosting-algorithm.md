---
title: "rankboost 算法学习笔记"
date: 2019-11-26T20:59:04+08:00
draft: false
author: "111qqz"
type: post
url: /2019/11/rankboost-Algorithm
categories:
- deep-learning

tags:

- boosting 

---

## boosting 算法是什么．
机缘使然，接触到了 Boosting 算法．Boosting是一种通过组合弱学习器来产生强学习器的通用且有效的方法.

动机是基于如下观察:尽管委员会中每个成员只提供一些不成熟的判断,但整个委员会却产生较为准确的决策。通过组合多个弱学习器来解决学习问题。给定训练数据,弱学习算法(如决策树)可以训练产生弱学习器,这些弱学习器只需要比随机猜测的准确率好一些。用不同的训练数据训练可以得到不同的弱学习器。这些弱学习器作为委员会成员,共同决策。

## ranking task是什么

此处的ranking task指的的pairwise ranking

排名(ranking)的学习问题出现在许多现代应用程序中，包括搜索引擎，信息提取平台和电影推荐系统的设计。 在这些应用程序中，返回文档或电影的顺序是系统的关键方面。 在二进制情况下，对分类进行排名的主要动机是资源的限制：对于非常大的数据集，显示或处理由分类器标记为相关的所有项目可能是不切实际的，甚至是不可能的。 搜索引擎的标准用户不愿意查询响应查询而返回的所有文档，而只查询前十名左右。 同样，信用卡公司欺诈检测部门的成员不能调查被分类为潜在欺诈的数千笔交易，而只能调查几十个最可疑的交易。

所以到底什么才是一个ranking task呢?

ranking task是一种有监督学习，通过label 信息，来对所有的数据点做出排名的预测．这里的label是一种关系信息，与数据点对一一对应的．设label函数为f,一般来说，假设有数据点x1,x2,那么有
```c
f(x1,x2) = 1 if x1 ranks higher than x2
f(x1,x2) = -1 if x1 ranks lower than x2
f(x1,x2) = 0 if there is no enough info to compare x1 and x2
```
需要注意的是，通常来说label并没有传递性．也就是说，从f(x1,x2) = 1和　f(x2,x3) =1 并不能推断出f(x1,x3) = 1.原因是在比较x1,x2,x3时，可能使用了不同的feature(通俗的解释就是，我喜欢A胜过B是因为A比B有钱，我喜欢B胜过C是因为B比C可爱，但是我可能因为其他原因喜欢C胜过A)


## rankboost 算法
字面理解，rankboost算法就是将boosting算法用于pairwise ranking task.
该过程的伪代码为:
![rankboost.png](https://i.loli.net/2019/12/01/ZR61l3JWuGsxMYz.png)

要注意的是算法的输入为
```c
S=((x1,x1',y1),...(xm,xm',ym))
```
其中　(x1,x1')为一个pair,y1为与这个pair对应的label.

这与传统的分类，回归问题明显不同．　前者是每一个数据对应一个label,但是后者是每一个pair对应一个label. 可能需要对数据做一些预处理．
一般来说，对于n个数据样本，并不会直接生成n*n个pair，而是从中随机生成指定个数个pair.
此时


## Bipartite ranking 
Bipartite ranking是pairwise ranking task中一种特殊的情形．
在这种情形下，样本被分为不相交的正负两部分
ranking问题变成了使得正样本的rank高于负样本．
对于这个情形，算法的输入变为
```c
S+ =(x1',x2',...,xm')
S- =(x1,x2,...,xn)
```
没有了label.原因是正负样本的集合本来就暗含了label信息．
如果直接按照一般的rankboost算法实现，复杂度是O(n*m)的，其中m和n为正负样本的个数．

但是通过一种高效的实现，复杂度可以降低为O(m+n)
这种实现基于算法的目标函数是指数函数，指数函数是积性函数．
因此可以将目标函数分为正负样本两部分分别计算，每部分只与自身相关．
具体的证明可以参考"Foundations of Machine Learning" 9.5节．
该高校实现的伪代码为:

![brankboost.png](https://i.loli.net/2019/12/01/be5ULxSguvDca7z.png)




## 参考资料

[An Efficient Boosting Algorithm for Combining Preferences](http://www.ai.mit.edu/projects/jmlr/papers/volume4/freund03a/freund03a.pdf)

[Foundations of Machine Learning](https://cs.nyu.edu/~mohri/mlbook/)

[Intuitive explanation of Learning to Rank (and RankNet, LambdaRank and LambdaMART)
](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418)

[手把手教你实现一个 AdaBoost](https://www.ibm.com/developerworks/cn/analytics/library/machine-learning-hands-on6-adaboost/index.html)

[Ranklib on github](https://github.com/jobandtalent/RankLib)













