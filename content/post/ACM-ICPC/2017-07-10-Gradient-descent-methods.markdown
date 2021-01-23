---
author: 111qqz
date: 2017-07-10 01:49:04+00:00
draft: false
title: 几种梯度下降(GD)法的比较（转载）
type: post
url: /2017/07/Gradient-descent-methods/
categories:
- deep-learning
tags:
- 梯度下降
---

[参考资料](https://en.wikipedia.org/wiki/Gradient_descent)

机器学习中梯度下降（Gradient Descent， GD）算法只需要计算损失函数的一阶导数，计算代价小，非常适合训练数据非常大的应用。

梯度下降法的物理意义很好理解，就是沿着当前点的梯度方向进行线搜索，找到下一个迭代点。但是，为什么有会派生出 batch、mini-batch、online这些GD算法呢？

<!-- more -->

原来，batch、mini-batch、SGD、online的区别在于训练数据的选择上：
<table align="center" border="0" >
<tbody >
<tr >

<td >** **
</td>

<td >**batch**
</td>

<td >**mini-batch**
</td>

<td >**Stochastic**
</td>

<td >**Online**
</td>
</tr>
<tr >

<td >**训练集**
</td>

<td >固定
</td>

<td >固定
</td>

<td >固定
</td>

<td >实时更新
</td>
</tr>
<tr >

<td >**单次迭代样本数**
</td>

<td >整个训练集
</td>

<td >训练集的子集
</td>

<td >单个样本
</td>

<td >根据具体算法定
</td>
</tr>
<tr >

<td >**算法复杂度**
</td>

<td >高
</td>

<td >一般
</td>

<td >低
</td>

<td >低
</td>
</tr>
<tr >

<td >**时效性**
</td>

<td >低
</td>

<td >一般（delta 模型）
</td>

<td >一般（delta 模型）
</td>

<td >高
</td>
</tr>
<tr >

<td >**收敛性**
</td>

<td >稳定
</td>

<td >较稳定
</td>

<td >不稳定
</td>

<td >不稳定
</td>
</tr>
</tbody>
</table>


**1. batch GD**

每次迭代的梯度方向计算由所有训练样本共同投票决定，

batch GD的损失函数是：


J(θ)=12m∑i=1m(hθ(x(i))−y(i))2J(θ)=12m∑i=1m(hθ(x(i))−y(i))2


训练算法为：


repeate{θ:=θ−α1m∑i=1m(hθ(x(i))−y(i))x(i)j}repeate{θ:=θ−α1m∑i=1m(hθ(x(i))−y(i))xj(i)}


什么意思呢，batch GD算法是计算损失函数在**整个训练集**上的梯度方向，沿着该方向搜寻下一个迭代点。”batch“的含义是训练集中所有样本参与每一轮迭代。

**2. mini-batch GD**

batch GD每一轮迭代需要所有样本参与，对于大规模的机器学习应用，经常有billion级别的训练集，计算复杂度非常高。因此，有学者就提出，反正训练集只是数据分布的一个采样集合，我们能不能在每次迭代只利用部分训练集样本呢？这就是mini-batch算法。

假设训练集有m个样本，每个mini-batch（训练集的一个子集）有b个样本，那么，整个训练集可以分成m/b个mini-batch。我们用ωω表示一个mini-batch, 用ΩjΩj表示第j轮迭代中所有mini-batch集合，有：


Ω={ωk:k=1,2...m/b}Ω={ωk:k=1,2...m/b}


那么， mini-batch GD算法流程如下：


repeate{repeate{foreachωkinΩ:θ:=θ−α1b∑i=1b(hθ(x(i))−y(i))x(i)}for(k=1,2...m/b)}repeate{repeate{foreachωkinΩ:θ:=θ−α1b∑i=1b(hθ(x(i))−y(i))x(i)}for(k=1,2...m/b)}


**3. Stochastic GD （SGD）**

随机梯度下降算法（SGD）是mini-batch GD的一个特殊应用。SGD等价于b=1的mini-batch GD。即，每个mini-batch中只有一个训练样本。

**4. Online GD**

随着互联网行业的蓬勃发展，数据变得越来越“廉价”。很多应用有实时的，不间断的训练数据产生。在线学习（Online Learning）算法就是充分利用实时数据的一个训练算法。

Online GD于mini-batch GD/SGD的区别在于，所有训练数据只用一次，然后丢弃。这样做的好处是可以最终模型的变化趋势。比如搜索广告的点击率(CTR)预估模型，网民的点击行为会随着时间改变。用batch算法（每天更新一次）一方面耗时较长（需要对所有历史数据重新训练）；另一方面，无法及时反馈用户的点击行为迁移。而Online Leaning的算法可以实时的最终网民的点击行为迁移。
