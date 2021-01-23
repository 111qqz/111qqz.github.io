---
author: 111qqz
date: 2017-08-02 01:34:58+00:00
draft: false
title: 峰度（Kurtosis）和偏度（Skewness）
type: post
url: /2017/08/kurtosisskewness/
categories:
- 其他
tags:
- 偏度
- 峰度
---

昨天pinduoduo笔试遇到了，看心情蒙的2333，来学习一下

** 峰度（Kurtosis）和偏度（Skewness）**

**重点：正太分布的峰度和偏度都是0**

峰度是描述总体中所有取值分布形态陡缓程度的统计量。这个统计量需要与正态分布相比较，**峰度为0表示该总体数据分布与正态分布的陡缓程度相同**；峰度大于0表示该总体数据分布与正态分布相比较为陡峭，为尖顶峰；峰度小于0表示该总体数据分布与正态分布相比较为平坦，为平顶峰。峰度的绝对值数值越大表示其分布形态的陡缓程度与正态分布的差异程度越大。

峰度的具体计算公式为：
<table cellspacing="0" align="center" border="1" class="ln" bgcolor="#ddddd" >
<tbody >
<tr >

<td bgcolor="#ffffff" >[![](http://images.51cto.com/files/uploadimg/20100408/161046770.jpg)
](http://images.51cto.com/files/uploadimg/20100408/161046770.jpg)
</td>
</tr>
</tbody>
</table>
偏度与峰度类似，它也是描述数据分布形态的统计量，其描述的是某总体取值分布的对称性。这个统计量同样需要与正态分布相比较，**偏度为0表示其数据分布形态与正态分布的偏斜程度相同**；偏度大于0表示其数据分布形态与正态分布相比为正偏或右偏，即有一条长尾巴拖在右边，数据右端有较多的极端值；偏度小于0表示其数据分布形态与正态分布相比为负偏或左偏，即有一条长尾拖在左边，数据左端有较多的极端值。偏度的绝对值数值越大表示其分布形态的偏斜程度越大。

偏度的具体计算公式为：
<table cellspacing="0" align="center" border="1" class="ln" bgcolor="#ddddd" >
<tbody >
<tr >

<td bgcolor="#ffffff" >[![](http://images.51cto.com/files/uploadimg/20100408/161111811.jpg)
](http://images.51cto.com/files/uploadimg/20100408/161111811.jpg)
</td>
</tr>
</tbody>
</table>
