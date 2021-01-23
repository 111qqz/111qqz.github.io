---
author: 111qqz
date: 2017-07-22 08:56:08+00:00
draft: false
title: stanford cs 231n:常用激活函数
type: post
url: /2017/07/common-activation-functions/
categories:
- deep-learning
tags:
- 激活函数
---

#### 其实我觉得这部分可以直接黑箱。。。直接无脑上Leaky ReLU或者Maxou？不过对这些激活函数的特点有个high-level的了解应该总是没坏处的，只要别太纠结细节就好了把。。







<blockquote>每个激活函数（或非线性函数）的输入都是一个数字，然后对其进行某种固定的数学操作。下面是在实践中可能遇到的几种激活函数：

————————————————————————————————————————

![](https://pic3.zhimg.com/677187e96671a4cac9c95352743b3806_b.png)
左边是Sigmoid非线性函数，将实数压缩到[0,1]之间。右边是tanh函数，将实数压缩到[-1,1]。

————————————————————————————————————————

**Sigmoid。**sigmoid非线性函数的数学公式是![\displaystyle\sigma(x)=1/(1+e^{-x})](http://www.zhihu.com/equation?tex=displaystylesigmax11e-x)
，函数图像如上图的左边所示。在前一节中已经提到过，它输入实数值并将其“挤压”到0到1范围内。更具体地说，很大的负数变成0，很大的正数变成1。在历史上，sigmoid函数非常常用，这是因为它对于神经元的激活频率有良好的解释：从完全不激活（0）到在求和后的最大频率处的完全饱和（**saturated**）的激活（1）。然而现在sigmoid函数已经不太受欢迎，实际很少使用了，这是因为它有两个主要缺点：

> 
> 
 	  * _Sigmoid函数饱和使梯度消失_。sigmoid神经元有一个不好的特性，就是当神经元的激活在接近0或1处时会饱和：在这些区域，梯度几乎为0。回忆一下，在反向传播的时候，这个（局部）梯度将会与整个损失函数关于该门单元输出的梯度相乘。因此，如果局部梯度非常小，那么相乘的结果也会接近零，这会有效地“杀死”梯度，几乎就有没有信号通过神经元传到权重再到数据了。还有，为了防止饱和，必须对于权重矩阵初始化特别留意。比如，如果初始化权重过大，那么大多数神经元将会饱和，导致网络就几乎不学习了。
 	  * _Sigmoid函数的输出不是零中心的_。这个性质并不是我们想要的，因为在神经网络后面层中的神经元得到的数据将不是零中心的。这一情况将影响梯度下降的运作，因为如果输入神经元的数据总是正数（比如在![f=w^Tx+b](http://www.zhihu.com/equation?tex=fwTxb)
中每个元素都![x>0](http://www.zhihu.com/equation?tex=x0)
），那么关于![w](http://www.zhihu.com/equation?tex=w)
的梯度在反向传播的过程中，将会要么全部是正数，要么全部是负数（具体依整个表达式![f](http://www.zhihu.com/equation?tex=f)
而定）。这将会导致梯度下降权重更新时出现z字型的下降。然而，可以看到整个批量的数据的梯度被加起来后，对于权重的最终更新将会有不同的正负，这样就从一定程度上减轻了这个问题。因此，该问题相对于上面的神经元饱和问题来说只是个小麻烦，没有那么严重。

**Tanh。**tanh非线性函数图像如上图右边所示。它将实数值压缩到[-1,1]之间。和sigmoid神经元一样，它也存在饱和问题，但是和sigmoid神经元不同的是，它的输出是零中心的。因此，在实际操作中，_tanh非线性函数比sigmoid非线性函数更受欢迎_。注意tanh神经元是一个简单放大的sigmoid神经元，具体说来就是：![tanh(x)=2\sigma(2x)-1](http://www.zhihu.com/equation?tex=tanhx2sigma2x-1)
。

————————————————————————————————————————

![](https://pic3.zhimg.com/83682a138f6224230f5b0292d9c01bd2_b.png)
左边是ReLU（校正线性单元：Rectified Linear Unit）激活函数，当![x=0](http://www.zhihu.com/equation?tex=x0)
时函数值为0。当![x>0](http://www.zhihu.com/equation?tex=x0)
函数的斜率为1。右边是从 [Krizhevsky](http://link.zhihu.com/?target=http//www.cs.toronto.edu/fritz/absps/imagenet.pdf)等的论文中截取的图表，指明使用ReLU比使用tanh的收敛快6倍。

————————————————————————————————————————

**ReLU。**在近些年ReLU变得非常流行。它的函数公式是![f(x)=max(0,x)](http://www.zhihu.com/equation?tex=fxmax0x)
。换句话说，这个激活函数就是一个关于0的阈值（如上图左侧）。使用ReLU有以下一些优缺点：

> 
> 
 	  * 优点：相较于sigmoid和tanh函数，ReLU对于随机梯度下降的收敛有巨大的加速作用（ [Krizhevsky ](http://link.zhihu.com/?target=http//www.cs.toronto.edu/fritz/absps/imagenet.pdf)等的论文指出有6倍之多）。据称这是由它的线性，非饱和的公式导致的。
 	  * 优点：sigmoid和tanh神经元含有指数运算等耗费计算资源的操作，而ReLU可以简单地通过对一个矩阵进行阈值计算得到。
 	  * 缺点：在训练的时候，ReLU单元比较脆弱并且可能“死掉”。举例来说，当一个很大的梯度流过ReLU的神经元的时候，可能会导致梯度更新到一种特别的状态，在这种状态下神经元将无法被其他任何数据点再次激活。如果这种情况发生，那么从此所以流过这个神经元的梯度将都变成0。也就是说，这个ReLU单元在训练中将不可逆转的死亡，因为这导致了数据多样化的丢失。例如，如果学习率设置得太高，可能会发现网络中40%的神经元都会死掉（在整个训练集中这些神经元都不会被激活）。通过合理设置学习率，这种情况的发生概率会降低。

**Leaky ReLU。**Leaky ReLU是为解决“ReLU死亡”问题的尝试。ReLU中当x<0时，函数值为0。而Leaky ReLU则是给出一个很小的负数梯度值，比如0.01。所以其函数公式为![f(x)=1(x<0)(\alpha x)+1(x>=0)(x)](http://www.zhihu.com/equation?tex=fx1x0alpha+x1x0x)
其中![\alpha](http://www.zhihu.com/equation?tex=alpha)
是一个小的常量。有些研究者的论文指出这个激活函数表现很不错，但是其效果并不是很稳定。Kaiming He等人在2015年发布的论文[Delving Deep into Rectifiers](http://link.zhihu.com/?target=http//arxiv.org/abs/1502.01852)中介绍了一种新方法PReLU，把负区间上的斜率当做每个神经元中的一个参数。然而该激活函数在在不同任务中均有益处的一致性并没有特别清晰。

**Maxout。**一些其他类型的单元被提了出来，它们对于权重和数据的内积结果不再使用![f(w^Tx+b)](http://www.zhihu.com/equation?tex=fwTxb)
函数形式。一个相关的流行选择是Maxout（最近由[Goodfellow](http://link.zhihu.com/?target=http//www-etud.iro.umontreal.ca/goodfeli/maxout.html)等发布）神经元。Maxout是对ReLU和leaky ReLU的一般化归纳，它的函数是：![max(w^T_1x+b_1,w^T_2x+b_2)](http://www.zhihu.com/equation?tex=maxwT_1xb_1wT_2xb_2)
。ReLU和Leaky ReLU都是这个公式的特殊情况（比如ReLU就是当![w_1,b_1=0](http://www.zhihu.com/equation?tex=w_1b_10)
的时候）。这样Maxout神经元就拥有ReLU单元的所有优点（线性操作和不饱和），而没有它的缺点（死亡的ReLU单元）。然而和ReLU对比，它每个神经元的参数数量增加了一倍，这就导致整体参数的数量激增。

以上就是一些常用的神经元及其激活函数。最后需要注意一点：在同一个网络中混合使用不同类型的神经元是非常少见的，虽然没有什么根本性问题来禁止这样做。

**一句话**：“_那么该用那种呢？_”用ReLU非线性函数。注意设置好学习率，或许可以监控你的网络中死亡的神经元占的比例。如果单元死亡问题困扰你，就试试Leaky ReLU或者Maxout，不要再用sigmoid了。也可以试试tanh，但是其效果应该不如ReLU或者Maxout。</blockquote>
