---
author: 111qqz
date: 2016-10-10 12:08:41+00:00
draft: false
title: 二次剩余（Cipolla's algorithm）学习笔记
type: post
url: /2016/10/cipollas-algorithm/
categories:
- ACM
tags:
- number theory
- 二次剩余
- 剩余系
---

先放资料。



* * *






### **前置技能点：**
[剩余系](http://baike.baidu.com/link?url=7nEL8QRUFHmQQor4elIUVpLVJG0i63Q3iRRXhrzzr1p2bhJ4qq4d-whxKrZhx6O8GEBf_iv_wsM2bWH1NJaJDVyLM8Mft0PCPAhMnYj6eNG2zh4lTNt5YvGDn1R4vrYE)




<blockquote>

> 
> **剩余系****:****设模为****m,****则根据余数可将所有的整数分成****m****类，分别记成****[0],[1],[2],****…****[m-1]****，**
> 
> 

> 
> **这****m****个数****{0,1,2,****…****m-1}****称为一个完全剩余系，**
> 
> 

> 
> **每个数称为相应类的代表元。**
> 
> 

> 
> 当m=10（偶数）时候，则{0,1,2,3,4,5,6,7,8,9}是最小非负完全剩余系
> 
> 

> 
> {-5,-4,-3,-2,-1,0,1,2,3,4,5} 是绝对值最小完全剩余系
> 
> 

> 
> {-4,-3,-2,-1,0,1,2,3,4,5} 绝对值最小
> 
> 

> 
> {1,2,3,4,5,6,7,8,9,10}是最小正完全剩余系
> 
> 

> 
> 

> 
> 

> 
> 

> 
> **简化剩余系:在每个剩余类选取至1个与m互素代表元构成简化剩余系。**
> 
> 

> 
> 当m=10则,{0,1,2,3,4,5,6,7,8,9} 完全剩余系
> 
> 

> 
> {1,3,7,9}是简化剩余系(x,10)=1
> 
> 

> 
> 当m=5则，{0,1,2,3,4}为完全剩余系,
> 
> 

> 
> {1,2,3,4}是简化剩余系，因为除去余0(正好是倍数)外，其它都互素。
> 
> 

> 
> **f(m)=欧拉函数=|{t|0<t<m, (t, m)=1}|**
> 
> 

> 
> **=简化剩余系的元素个数**
> 
> 

> 
> </blockquote>


<!-- more -->



[维基百科_高斯引理](https://zh.wikipedia.org/wiki/)


<blockquote>设_p_为奇[质数](https://zh.wikipedia.org/wiki/)，_a_是一个与_p_[互质](https://zh.wikipedia.org/wiki/)的整数。考虑以下数组：![{\displaystyle a,2a,3a,\dots ,{\frac {p-1}{2}}a}](https://wikimedia.org/api/rest_v1/media/math/render/svg/82941c63fd5e49cf0b57612ee5e895d1e1c9096c)
以及它们对_p_的[最小非负剩余](https://zh.wikipedia.org/w/index.php?title=&action=edit&redlink=1)。这些剩余两两不等（**kk:这些剩余两两不等的证明：可以考虑反证，假设两个不同的数x,y对于p同余， 那么x-y和0关于p同余，而x-y同时关于a同余，a与p互质，矛盾。因此这些剩余两两不等**），因此我们共有![\frac{p-1}{2}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a733b8495b0d55ed5bc9d795b7b6821efb1d858b)
个两两不等的介于1和_p（_**kk:这里似乎有问题，如果剩余是在1..p之间，那么前面应该是说最小正剩余而不是最小非负剩余，最小非负剩余应该是在0..p-1之间**_）_之间的整数：![{\displaystyle t_{1},t_{2},t_{3},\dots ,t_{\frac {p-1}{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7992b0d1c192f11821dce891b5f16dffdb35c536)
。设其中有_n_个数比_p_/2大，那么高斯引理声称：![{\displaystyle \left({\frac {a}{p}}\right)=(-1)^{n}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1b89fef980b3b0a785356b6960fd49e257aa2b16)


上式左边是[勒让德符号](https://zh.wikipedia.org/wiki/)，当其值为+1时，表示_a_是模_p_的二次剩余；其值为-1时，表示_a_是模_p_的二次非剩余。

用通俗的语言来说，就是：![{\displaystyle t_{1},t_{2},t_{3},\dots ,t_{\frac {p-1}{2}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7992b0d1c192f11821dce891b5f16dffdb35c536)
里面比_p_/2大的有[偶数](https://zh.wikipedia.org/wiki/)个，那么_a_是模_p_的二次剩余，如果有[奇数](https://zh.wikipedia.org/wiki/)个，那么_a_是模_p_的二次非剩余。</blockquote>





* * *





### **正片：**


[维基百科_勒让德符号](https://zh.wikipedia.org/wiki/)

定义：


<blockquote>勒让德符号![({\tfrac {a}{p}})](https://wikimedia.org/api/rest_v1/media/math/render/svg/6ebb252decd96b7adf4d3fffdda2c15b718c7420)
（有时为了印刷上的方便，写成(_a_|_p_))有下列定义：


> 
>     
<table border="0" >
<tbody >
<tr >

> <td rowspan="3" >![\left({\frac {a}{p}}\right)={\begin{cases}\quad 0\\+1\\-1\end{cases}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ddbfff4690a7d39fe7c2fcd69885dc8f36f2ed7c)

> </td>

> <td rowspan="3" >
> </td>

> <td >如果![a\equiv 0{\pmod {p}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/30d65a6f62fe8c414ef6c4b123da631d1125594f)

> </td>
</tr>
<tr >

> <td >如果![a\not \equiv 0{\pmod {p}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/520a34d8efca5436576b29f6765af091ad07b271)
，且对于某个整数![x,x^{2}\equiv \;a{\pmod {p}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/065799916443b503df9e3adc2d007ccd5a1aafc4)

> </td>
</tr>
<tr >

> <td >如果不存在整数![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4)
，使得![x^{2}\equiv \;a{\pmod {p}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/787894eeb27239e1dfdbe6f6d8ba080dab3eeb73)
。
> </td>
</tr>
</tbody>
</table>

> 如果(_a_|_p_) = 1，_a_ 便称为[二次剩余](https://zh.wikipedia.org/wiki/)(mod _p_)；如果(_a_|_p_) = −1，则 _a_ 称为[二次非剩余](https://zh.wikipedia.org/wiki/)(mod p)。通常把零视为一种特殊的情况。</blockquote>


性质：


<blockquote>勒让德符号有许多有用的性质，可以用来加速计算。它们包括：

> 
> 
	  * ![\left({\frac {ab}{p}}\right)=\left({\frac {a}{p}}\right)\left({\frac {b}{p}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/0c8876ab646dd7c9976bc54dd7487527f77bd202)
（它是一个**[完全积性函数](https://zh.wikipedia.org/wiki/)**(kk:g(a)*g(b)=g(a*b)对于任意正整数a,b都成立，不需要gcd(a,b)=1，完全积性真是爽哭了。。。。)。这个性质可以进一步理解为：两个剩余或非剩余的乘积是剩余，一个剩余与一个非剩余的乘积是非剩余。（kk:因为负负得正，正正得正...））


	  * 如果_a_ ≡ _b_ (mod _p_)，则![\left({\frac {a}{p}}\right)=\left({\frac {b}{p}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/22c53d660aed6373e99b8e0feb7d9801186b2d41)



	  * ![\left({\frac {a^{2}}{p}}\right)=1](https://wikimedia.org/api/rest_v1/media/math/render/svg/d5b6f43df4f40202dbf365146ae39d7037387df5)



	  * ![{\displaystyle \left({\frac {-1}{p}}\right)=(-1)^{\frac {p-1}{2}}={\begin{cases}+1{\mbox{ if }}p\equiv 1{\pmod {4}}\\-1{\mbox{ if }}p\equiv 3{\pmod {4}}\end{cases}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/dd3bcfb31b3ac3ef72a6838ba0d0c58a2f236f74)


这个性质称为二次互反律的第一补充。

	  * ![{\displaystyle \left({\frac {2}{p}}\right)=(-1)^{\frac {p^{2}-1}{8}}={\begin{cases}+1{\mbox{ if }}p\equiv 1{\mbox{ or }}7{\pmod {8}}\\-1{\mbox{ if }}p\equiv 3{\mbox{ or }}5{\pmod {8}}\end{cases}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d90e3a78bfe75d1c4f4bfdd49690bd3af4673562)


这个性质称为二次互反律的第二补充。一般的二次互反律为：

	  * 如果_p_和_q_是奇素数，则![\left({\frac {q}{p}}\right)=\left({\frac {p}{q}}\right)(-1)^{{{\frac {p-1}{2}}{\frac {q-1}{2}}}}.](https://wikimedia.org/api/rest_v1/media/math/render/svg/966e6a0e5a66971e0c4d850b4a1627a598863d46)


参见[二次互反律](https://zh.wikipedia.org/wiki/)和[二次互反律的证明](https://zh.wikipedia.org/w/index.php?title=&action=edit&redlink=1)。

以下是一些较小的_p_的值的公式：

> 
> 
	  * 对于奇素数_p_，![\left({\frac {3}{p}}\right)=(-1)^{\left\lceil {\frac {p+1}{6}}\right\rceil }={\begin{cases}+1{\mbox{ if }}p\equiv 1{\mbox{ or }}11{\pmod {12}}\\-1{\mbox{ if }}p\equiv 5{\mbox{ or }}7{\pmod {12}}\end{cases}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1d1c563452f82cfaf77baaecb82ed16888381a6b)



	  * 对于奇素数_p_，![\left({\frac {5}{p}}\right)=(-1)^{\left\lfloor {\frac {p-2}{5}}\right\rfloor }={\begin{cases}+1{\mbox{ if }}p\equiv 1{\mbox{ or }}4{\pmod 5}\\-1{\mbox{ if }}p\equiv 2{\mbox{ or }}3{\pmod 5}\end{cases}},](https://wikimedia.org/api/rest_v1/media/math/render/svg/8e1ed5877d9a39798e4afdb699e61d13b8071e59)


但一般直接把剩余和非剩余列出更简便：

	  * 对于奇素数_p_，![\left({\frac {7}{p}}\right)={\begin{cases}+1{\mbox{ if }}p\equiv 1,3,9,19,25,{\mbox{ or }}27{\pmod {28}}\\-1{\mbox{ if }}p\equiv 5,11,13,15,17,{\mbox{ or }}23{\pmod {28}}\end{cases}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/a70b4a7cc4d99b0842fa9b6bc71209398f6f8eeb)


勒让德符号(_a_|_p_)是一个[狄利克雷特征](https://zh.wikipedia.org/wiki/)(mod _p_)。</blockquote>


计算勒让德符号的一个例子：

![\left({\frac {12345}{331}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/827ce8eb12cd064d538fba78851cdcf32f5237e9)


![=\left({\frac {3}{331}}\right)\left({\frac {5}{331}}\right)\left({\frac {823}{331}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/239c0bd33998501f6f040a0a53f0757f665b1cb8)
 （完全积性）

![=\left({\frac {3}{331}}\right)\left({\frac {5}{331}}\right)\left({\frac {161}{331}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/e27dfd260354631933b8f1a96998af6093847c45)
 （161和823关于331同余）

![=\left({\frac {3}{331}}\right)\left({\frac {5}{331}}\right)\left({\frac {7}{331}}\right)\left({\frac {23}{331}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/827eecd5ac37c8bb9f0e1708f0752d2741785690)
 （完全积性）

![=(-1)\left({\frac {331}{3}}\right)\left({\frac {331}{5}}\right)(-1)\left({\frac {331}{7}}\right)(-1)\left({\frac {331}{23}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/e15893c92c8e69189b6dbe3fc84878f80016cf56)
 （二次互反律）

![=-\left({\frac {1}{3}}\right)\left({\frac {1}{5}}\right)\left({\frac {2}{7}}\right)\left({\frac {9}{23}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/d9f3d05e8faa1196ae844ff490e380543cf4cd9d)
 （同余数）

![=-\left({\frac {1}{3}}\right)\left({\frac {1}{5}}\right)\left({\frac {2}{7}}\right)\left({\frac {3}{23}}\right)^{2}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4ab36b474cf5d1e547a7c818815d1588f528dcff)
 （完全积性，平方的形式值一定为1）

![=-\left(1\right)\left(1\right)\left(1\right)\left(1\right)=-1.](https://wikimedia.org/api/rest_v1/media/math/render/svg/4cf73f630b227bdea61d980f4d945bb8fc2dfafc)
 （分别计算，可以参考小素数时的分段函数，具体的计算方法见下文）



[维基百科_欧拉准则](https://zh.wikipedia.org/wiki/)（用来计算勒让德符号）


<blockquote>若![p](https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36)
是奇[质数](https://zh.wikipedia.org/wiki/)且![p](https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36)
不能整除![d](https://wikimedia.org/api/rest_v1/media/math/render/svg/e85ff03cbe0c7341af6b982e47e9f90d235c66ab)
，则：


> 
>     ![d](https://wikimedia.org/api/rest_v1/media/math/render/svg/e85ff03cbe0c7341af6b982e47e9f90d235c66ab)
是模![p](https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36)
的二次剩余[当且仅当](https://zh.wikipedia.org/wiki/)：![{\displaystyle d^{\frac {p-1}{2}}\equiv 1{\pmod {p}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ab89b7999dc3ab653bd541ec9384c7f0ce5f1295)

> 
>     ![d](https://wikimedia.org/api/rest_v1/media/math/render/svg/e85ff03cbe0c7341af6b982e47e9f90d235c66ab)
是模![p](https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36)
的非二次剩余当且仅当：![{\displaystyle d^{\frac {p-1}{2}}\equiv -1{\pmod {p}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a7379bad3d1f0af0228c293f5179398426161e4)

> **以[勒让德符号](https://zh.wikipedia.org/wiki/)表示，即为： ![{\displaystyle d^{\frac {p-1}{2}}\equiv \left({\frac {d}{p}}\right){\pmod {p}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/351772a3d94b31369024d0855de23d25bb18924d)
**

> 
> ### **例子一：对于给定数，寻找其为二次剩余的模数**
> 
> 
令_a_ = 17。对于怎样的质数_p_，17是模_p_的二次剩余呢？

根据判别法里给出的准则，我们可以从小的质数开始检验。

首先测试_p_ = 3。我们有：17(3 − 1)/2 = 171 ≡ 2 (mod 3) ≡ -1 (mod 3)，因此17不是模3的二次剩余。

再来测试_p_ = 13。我们有：17(13 − 1)/2 = 176 ≡ 1 (mod 13)，因此17是模13的二次剩余。实际上我们有：17 ≡ 4 (mod 13)，而22 = 4.

运用同余性质和[勒让德符号](https://zh.wikipedia.org/wiki/)可以加快检验速度。继续算下去，可以得到：


> 
>     对于质数_p_ =![{\displaystyle 13,19,\cdots }](https://wikimedia.org/api/rest_v1/media/math/render/svg/13f9e1c9d7777e4eaa86f9c200cb0a5dfa30ae89)
，(17/_p_) = +1（也就是说17是模这些质数的二次剩余）。
>     对于质数_p_ =![{\displaystyle 3,5,7,11,23,\cdots }](https://wikimedia.org/api/rest_v1/media/math/render/svg/0ce5efd99278b3d8563cec3f661de8071a7c7b0a)
，(17/_p_) = -1（也就是说17是模这些质数的[二次非剩余](https://zh.wikipedia.org/wiki/)）。
>     （**kk:简单得说，就是从小到大枚举质数p，验证a^((p-1)/2)）%p等于1还是-1.）**
>     

> 
> ### 
> 
> 

> </blockquote>





<blockquote>

> 
> <blockquote>    

>> 
>> ### **例子二：对指定的质数_p_，寻找其二次剩余**
>> 
>> 
哪些数是模17的二次剩余？

我们可以手工计算：（**kk:手算考虑数的平方是因为，勒让德符号是完全积性函数&&![\left({\frac {a^{2}}{p}}\right)=1](https://wikimedia.org/api/rest_v1/media/math/render/svg/d5b6f43df4f40202dbf365146ae39d7037387df5)
）**




>> 
>>     12 = 1
>>     22 = 4
>>     32 = 9
>>     42 = 16
>>     52 = 25 ≡ 8 (mod 17)
>>     62 = 36 ≡ 2 (mod 17)
>>     72 = 49 ≡ 15 (mod 17)
>>     82 = 64 ≡ 13 (mod 17)
>> 于是得到：所有模17的二次剩余的集合是![{\displaystyle {1,2,4,8,9,13,15,16}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/8ad07be15fb1a6748c3baa2a8901312bbefd7df1)
。**要注意的是我们只需要算到8，因为9=17-8，9的平方与8的平方模17是同余的**：92 = (−8)2 = 82 ≡ 13 (mod 17).（同理不需计算比9大的数）。

**但是对于验证一个数是不是模17的二次剩余，就不必将所有模17的二次剩余全部算出**。比如说要检验数字3是否是模17的二次剩余，只需要计算3(17 − 1)/2 = 38 ≡ 812 ≡ ( − 4)2 ≡ − 1 (mod 17)，然后由欧拉准则判定3不是模17的二次剩余。


>> </blockquote>
> 
> 
</blockquote>




[维基百科_二次互反律](https://zh.wikipedia.org/wiki/)




<blockquote>对于两个奇[素数](https://zh.wikipedia.org/wiki/)![p](https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36)
和 ![q](https://wikimedia.org/api/rest_v1/media/math/render/svg/06809d64fa7c817ffc7e323f85997f783dbdf71d)
，![\left({\frac {p}{q}}\right)\cdot \left({\frac {q}{p}}\right)=(-1)^{{{\frac {(p-1)(q-1)}{4}}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/ea3d157eba9f88a16c19f7606afa04873c76a2b9)


其中![\left({\tfrac {p}{q}}\right)](https://wikimedia.org/api/rest_v1/media/math/render/svg/da5461d3ff8c55b4d5989cc4cb741a0fcb4c4622)
是[勒让德符号](https://zh.wikipedia.org/wiki/)。</blockquote>




关于二次互反律的证明就不多说了。。。据说高斯一次给出了五个（还是七个？)，到现在一共有200+种证明。



**然后。。。感觉。。。。二次互反律。。。。太神了。。。。太美了。。。。真的被震撼到了orz**



[wiki_Cipolla's algorithm](https://en.wikipedia.org/wiki/Cipollas_algorithm)

[acdreamer_二次同余方程的解](http://blog.csdn.net/acdreamers/article/details/10182281)
[ 二次剩余Cipolla算法学习小记](http://blog.csdn.net/a_crazy_czy/article/details/51959546)
