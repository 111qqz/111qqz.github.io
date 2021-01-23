---
author: 111qqz
date: 2017-07-18 02:42:50+00:00
draft: false
title: Inception-v4,Inception-ResNet 和残差连接对学习的影响
type: post
url: /2017/07/inception-resnet-notes/
categories:
- deep-learning
tags:
- Inception
- resnet
---

[原始论文](https://arxiv.org/abs/1602.07261)

[翻译链接](https://ask.julyedu.com/question/7711)




<blockquote>**——前言：**作者认为残差连接在训练深度卷积模型是很有必要的。至少在图像识别上，我们的研究似乎并不支持这一观点。

**摘要：**
近年来，深度卷积神经网络对图像识别性能的巨大提升发挥着关键作用。以Inception网络为例，其以相对较低的计算代价取得出色的表现。最近，与传统结构相结合的残差连接网络在2015ILSVRC挑战赛上取得非常优异的成绩；它的性能跟最新的Inception-v3 网络非常接近。因此也就引出了结合残差连接的Inception结构能否对性能进行提高的问题。本文给出实验证明，残差连接可以明显加速Inception网络的训练。同时实验也证明，相比没有残差连接的消耗相似的Inception网络，残差Inception网络在性能上具有微弱的优势。针对是否包含残差连接的Inception网络，本文同时提出了一些新的简化网络。这些网络的变体在ILSVRC2012分类任务上很明显的改善了单一框架的识别性能。本文进一步展示了适当的激活缩放如何使得很宽的残差Inception网络的训练更加稳定。本文通过对三个残差和一个Inception-v4进行组合，在top-5错误率上达到了 3.08%。

**前言：**
自从Krizhevsky等人于2012年赢得Image Net比赛，其网络“AlexNet”已在越来越多的机器视觉任务中得到成功应用，比如目标检测、分割、人体姿态估计、视频分类、目标跟踪、超分辨率等。这些都是使用深度卷积网络的成功案例。
本研究结合最近的两个想法：残差连接和最近的Inception网络结构除了直接的融合，我们也研究了Inception本身通过变得更深更宽能否能变得更加高效。为了实现这个目的，我们设计了一个新版本的Inception-v4，相比Inception-v3，它有更加统一简化的网络结构和更多的inception模块。从历史观点来看，Inception-v3继承了之前的很多方法。技术性局限主要在于使用DistBelief对分布式训练进行模型划分。
如今，将训练迁移到TensorFlow上以后，这些问题也就随之解决，这样就允许我们对结构进行简化。简化的网络结构详见第三节。
在本文中，我们将两个单一Inception变体——Inception-v3和v4与消耗相似的 InceptionResNet混合版本进行比较。这些模型的挑选主要满足以下约束条件，即和非残差模型具有相似的参数和计算复杂度。事实上我们对更深更宽的Inception-ResNet变体也进行测试，它们在ImageNet分类任务上表现性能相似。
最新的实验对组合模型的性能进行了评估。结果显示Inception-v4和Inception-ResNetv2的性能都很好，在ImageNet验证集上其性能已超过业界领先的单个框架模型，我们想看这种结合如何将业界领先水准继续推进，令人惊讶的是，我们发现单个框架性能的提升不会引起组合性能大幅的提高。尽管如此，我们仍然用四个模型组合在验证集上取得了top-5上3.1%的错误率。
在最后一部分，我们分析了分类任务失败的原因，并总结出组合模型在标注数据上的类标噪声上仍然没有达到很好的效果，同时对于预测还有很有大的提升空间。

**近期工作：**
卷积网络在大规模图像识别任务上的运用非常广泛。主要的模型有Network-in-network、VGGNet、GoogleLeNet(Inception-v1)。残差连接在引文5中提出，并指出附加残差网络对于图像识别尤其是目标检测具有很大的优势，并给出理论和实验验证。作者认为残差连接在训练深度卷积模型是很有必要的。至少在图像识别上，我们的研究似乎并不支持这一观点。然而，残差连接所带来的潜在优势可能需要在更深网络结构中来展现。在实验部分，我们展示了不使用残差连接时深度网络的训练并不难做到。然而，使用残差连接能够极大的提高训练速度，单单这一点就值的肯定。
Inception深度卷积网络被称为GoogleLeNet或Incention-v1。继而我们通过各种方法对 Inception结构进行优化，首先引入batch normalization(Inception-v2)。后来在第三代中增加factorization因子，即本文中提到的Inception-v3。

> 
> [![Image_1.png](https://ask.julyedu.com/uploads/questions/20170322/25b2acffee48ae5438f54a26871be517.png)
](https://ask.julyedu.com/uploads/questions/20170322/25b2acffee48ae5438f54a26871be517.png)
> 
> 
图1.残差连接

> 
> [![Image_2.png](https://ask.julyedu.com/uploads/questions/20170322/0e4a677a7eb7ca7450b1892f2a780e6c.png)
](https://ask.julyedu.com/uploads/questions/20170322/0e4a677a7eb7ca7450b1892f2a780e6c.png)
> 
> 
图2.优化版本的ResNet连接
**3.结构选择**
**3.1纯净的Inception模块**
我们对以前的Inception模型通过分布式进行训练，将每个副本被划分成一个含多个子网络的模型，以达到在内存中对整个模型进行拟合的目的。然而，Inception结构是高度可调的，这就意味着各层滤波器（filter）的数量可以有多种变化，而整个训练网络的质量不会受到影响。为了优化训练速度，我们对层大小进行调整以平衡不同子网络的计算。
相反，随着TensorFlow的引入，大部分最新的模型无需分布式的对副本进行训练。它通过反向传播（back propagation）进行内存优化，并仔细考虑梯度计算需要的tensors，以及通过结构化计算减少这类tensors的数量。从历史观点来讲，我们对网络结构的更迭已经做得非常保守，并限制实验改变独立网络的组分，同时保持其余网络的稳定性。 由于之前没有对网络进行简化，导致网络看起来更加复杂。在最新的实验中，针对 Inception-v4网络，我们决定丢掉不必要的包袱，对于inception块的每个网格大小进行统一。如图9，展示了大尺寸的Inceptionv4网络结构。图3至8是每个部分的详细结构。所有图中没有标记“V”的卷积使用same的填充原则，意即其输出网格与输入的尺寸正好匹配。使用“V”标记的卷积使用valid的填充原则，意即每个单元输入块全部包含在前几层中，同时输出激活图（output activation map）的网格尺寸也相应会减少。

> 
> [![Image_3.png](https://ask.julyedu.com/uploads/questions/20170322/7428387881cddb3e24e9fa6ba03ab671.png)
](https://ask.julyedu.com/uploads/questions/20170322/7428387881cddb3e24e9fa6ba03ab671.png)
> 
> 
图3 Inception-v4网络和Inception-ResNet-v2网络的结构。这是网络的输入部分。

> 
> [![Image_4.png](https://ask.julyedu.com/uploads/questions/20170322/b2bd2c7b34acb2ebfe9f71718fb396aa.png)
](https://ask.julyedu.com/uploads/questions/20170322/b2bd2c7b34acb2ebfe9f71718fb396aa.png)
> 
> 
图 4 Inception-v4网络35×35网格的框架。对应图9中Inception-A块。

> 
> [![Image_5.png](https://ask.julyedu.com/uploads/questions/20170322/8e9efd3354942ee931bab300f9564229.png)
](https://ask.julyedu.com/uploads/questions/20170322/8e9efd3354942ee931bab300f9564229.png)
> 
> 
图 5 Incep-v4网络17×17网格块的框架。对应图9中Inception-B块。

> 
> [![Image_6.png](https://ask.julyedu.com/uploads/questions/20170322/21cd0f6792a17e7973f73d921c6342be.png)
](https://ask.julyedu.com/uploads/questions/20170322/21cd0f6792a17e7973f73d921c6342be.png)
> 
> 
图 6 Inception-v4网络的8×8网格模块的框架。对应图9中Inception-C块。

> 
> [![Image_7.png](https://ask.julyedu.com/uploads/questions/20170322/a3609ab6eebc7b5db80928a52b8d9a95.png)
](https://ask.julyedu.com/uploads/questions/20170322/a3609ab6eebc7b5db80928a52b8d9a95.png)
> 
> 
图7 35×35到17×17减少模块的框架。这个块不同的变化（不同滤波器）在图9和15中使用，同时在网络Inception(-v4,-ResNet-v1,-ResNet-v2).k,l,m,n数量表示滤波器尺寸大小，如表1所示。

> 
> [![Image_8.png](https://ask.julyedu.com/uploads/questions/20170322/f68e6d9997152815047599fdf4ffe6b2.png)
](https://ask.julyedu.com/uploads/questions/20170322/f68e6d9997152815047599fdf4ffe6b2.png)
> 
> 
图 8 17×17到8×8网格缩减框架。减少的模块在图9中Inception-v4网络。

> 
> [![Image_9.png](https://ask.julyedu.com/uploads/questions/20170322/8558e817e34cb8e183e120aa74367f06.png)
](https://ask.julyedu.com/uploads/questions/20170322/8558e817e34cb8e183e120aa74367f06.png)
> 
> 
图 9 Inception-v4网络的整个框架。具体模块，见图3，4，5，6，7，8

**3.2 Inception残差块**
相较最初的Inception，针对Inception的残差版本我们使用更廉价的Inception块。每个Inception块后紧连接着滤波层（没有激活函数的1×1卷积）以进行维度变换，以实现输入的匹配。这样补偿了在Inception块中的维度降低。
我们尝试了残差Inception的几个版本。这里对其中的两个进行具体细节展示。第一个是“Inception-ResNet-v1”，计算代价跟Inception-v3大致相同，第二个“Inception-ResNet-v2”的计算代价跟Inception-v4网络基本相同。如图15是大尺寸结构。（然而，Inception-v4步长时间实际更慢，原因可能是有了更多的层）。
残差和非残差Inception的另外一个技术性区别是，在Inception-ResNet网络中，我们在传统层的顶部而非所有层的顶部中使用batch-normalization。在全部层使用 batch-normalization是合情合理的，但是我们想保持每个模型副本在单个GPU上就可以训练。结果证明，使用更大激活尺寸在GPU内存上更加耗时。在部分层的顶部忽略 batch-normalization能够充分的增加Inception块的数量。我们希望可以更好的利用计算资源，因而这种trade-off变得没有必要。

> 
> [![Image_10.png](https://ask.julyedu.com/uploads/questions/20170322/a5b05c632ca2a5484625a953f7f26ecd.png)
](https://ask.julyedu.com/uploads/questions/20170322/a5b05c632ca2a5484625a953f7f26ecd.png)
> 
> 
图 10 Inception-ResNet-v1网络使用35×35网格模块（Inception-ResNet-A）的框架

> 
> [![Image_11.png](https://ask.julyedu.com/uploads/questions/20170322/8e4a4178f7b86ae458b7c29063bf4a88.png)
](https://ask.julyedu.com/uploads/questions/20170322/8e4a4178f7b86ae458b7c29063bf4a88.png)
> 
> 
图 11 Inception-ResNet-v1网络的17×17网格模块的框架

> 
> [![Image_12.png](https://ask.julyedu.com/uploads/questions/20170322/862690e39d417e46c0cd522f4976adfb.png)
](https://ask.julyedu.com/uploads/questions/20170322/862690e39d417e46c0cd522f4976adfb.png)
> 
> 
图 12 “Reduction-B”17×17到8×8网格缩减模块。此模块在图15使用更小 Inception-ResNet-v1网络

> 
> [![Image_13.png](https://ask.julyedu.com/uploads/questions/20170322/02b6860095f5922bf4877a749437e853.png)
](https://ask.julyedu.com/uploads/questions/20170322/02b6860095f5922bf4877a749437e853.png)
> 
> 
图 13 Inception-ResNet-v1网络的8×8网格（Incepti-ResNet-C）模块的框架

> 
> [![Image_14.png](https://ask.julyedu.com/uploads/questions/20170322/2b88033f05f3cfda193ea28fa3f069ad.png)
](https://ask.julyedu.com/uploads/questions/20170322/2b88033f05f3cfda193ea28fa3f069ad.png)
> 
> 
图 14 Inception-ResNet-v1网络的主干

> 
> [![Image_15.png](https://ask.julyedu.com/uploads/questions/20170322/5577ae575f59c9ff99ac00267f0960a5.png)
](https://ask.julyedu.com/uploads/questions/20170322/5577ae575f59c9ff99ac00267f0960a5.png)
> 
> 
图 15 Inception-ResNet-v1和Inception-ResNet-v2网络的框架。
Inception-ResNet-v1使用图14,10,7,11,12,13描述的块。
Inception-ResNet-v2使用图 3,16,7,17,18,19 描述的块。
输出的尺寸涉及到Inception-ResNet-v1激活向量

> 
> [![Image_16.png](https://ask.julyedu.com/uploads/questions/20170322/8968bb6bd2f1f9d67c8b1dd40a133b31.png)
](https://ask.julyedu.com/uploads/questions/20170322/8968bb6bd2f1f9d67c8b1dd40a133b31.png)
> 
> 
图 16 Inception-ResNet-v2网络35×35网格模块（Inception-ResNet-A）的框架

> 
> [![Image_17.png](https://ask.julyedu.com/uploads/questions/20170322/850d0bd23d356e04820d6095342eadd2.png)
](https://ask.julyedu.com/uploads/questions/20170322/850d0bd23d356e04820d6095342eadd2.png)
> 
> 
图 17 Inception-ResNet-v2网络17×17网格模块（Inception-ResNet-B）的框架

> 
> [![Image_18.png](https://ask.julyedu.com/uploads/questions/20170322/1a7f08ab0dcc5f142494bc7e75ff8868.png)
](https://ask.julyedu.com/uploads/questions/20170322/1a7f08ab0dcc5f142494bc7e75ff8868.png)
> 
> 
图 18 17×15到8×8网格缩减模块的框架。Reduction-B模块使用更宽的 Inception-ResNet-v1网络，如图 15

> 
> [![Image_19.png](https://ask.julyedu.com/uploads/questions/20170322/691c0e567d64e1b7ce636ea6ab307d83.png)
](https://ask.julyedu.com/uploads/questions/20170322/691c0e567d64e1b7ce636ea6ab307d83.png)
> 
> 
图 19 Inception-ResNet-v2网络8×8网格（Inception-ResNet-C）模块的框架

**3.3对残差模块的缩放**
我们发现，如果滤波器数量超过1000，残差网络开始出现不稳定，同时网络会在训练过程早期便会出现“死亡”，意即经过成千上万次迭代，在平均池化（average pooling） 之前的层开始只生成0。通过降低学习率，或增加额外的batch-normalizatioin都无法避免这种状况。
我们发现，在将残差模块添加到activation激活层之前，对其进行放缩能够稳定训练。通常来说，我们将残差放缩因子定在0.1到0.3（如图20）。
类似不稳定的情形在引文5中也出现过， 文中建议通过两个阶段的训练来避免这种情况，其中第一个“warm-up”阶段使用极低的学习率，紧接着第二阶段使用高学习率。我们发现如果滤波器数量非常大，那么即使很低的学习率（0.00001）也不足以解决不稳定性，而且使用高学习率训练对其效果也有损伤。最终我们发现只需对残差进行缩放的方法更加可靠。
即使缩放并不是完全必须的，它似乎并不会影响最终准确率，但是放缩能有益于训练的稳定性。

> 
> [![Image_20.png](https://ask.julyedu.com/uploads/questions/20170322/5c805a434d37e323542f0d93b3f453af.png)
](https://ask.julyedu.com/uploads/questions/20170322/5c805a434d37e323542f0d93b3f453af.png)
> 
> 
表 1 三个Inception中Reduction-A模块滤波器的数量。四个参数是图7中四个卷积的参数。

> 
> [![Image_21.png](https://ask.julyedu.com/uploads/questions/20170322/3a3a322c2c278376e9bd92a1c9d262c7.png)
](https://ask.julyedu.com/uploads/questions/20170322/3a3a322c2c278376e9bd92a1c9d262c7.png)
> 
> 
图 20 结合Inception-ResNet模块的通用框架。我们期望相同的想法在resnet事例中也适用，除了Inception块任意的子网络都进行了使用。放缩模块仅仅适用于最后的线性激活。

> 
> [![Image_22.png](https://ask.julyedu.com/uploads/questions/20170322/6721f978d4cb537bd659fbe8f6250449.png)
](https://ask.julyedu.com/uploads/questions/20170322/6721f978d4cb537bd659fbe8f6250449.png)
> 
> 
图 21 在训练单纯Inception-v3和残差网络相似计算代价的Top-1错误率。评估在 ILSVRC-2012验证集上进行不加入黑名单图像测量。相对于传统Inception-v3，残差模型训练的更快，但是准确率更差

> 
> [![Image_23.png](https://ask.julyedu.com/uploads/questions/20170322/fc07051d7d7d8a5428ca9686537f89ae.png)
](https://ask.julyedu.com/uploads/questions/20170322/fc07051d7d7d8a5428ca9686537f89ae.png)
> 
> 
图 22 在训练单纯Inception-v3和残差网络相似计算代价的Top-5错误率。评估在 ILSVRC-2012验证集上进行不加入黑名单图像测量。在验证集上，残差模型训练的更快，同时召回率更好。

> 
> [![Image_24.png](https://ask.julyedu.com/uploads/questions/20170322/c5c65048b6967af33b1a45a25ac53cdf.png)
](https://ask.julyedu.com/uploads/questions/20170322/c5c65048b6967af33b1a45a25ac53cdf.png)
> 
> 
图 23 在训练单纯Inception-v3和残差网络相似计算代价的Top-1错误率。评估在 ILSVRC-2012验证集上进行不加入黑名单图像测量。相对于传统Inception-v4，残差模型训练的更快，但是准确率更高。

> 
> [![Image_26.png](https://ask.julyedu.com/uploads/questions/20170322/227c68e321ac1877b76ed75cdb649820.png)
](https://ask.julyedu.com/uploads/questions/20170322/227c68e321ac1877b76ed75cdb649820.png)
> 
> 
图 24 在训练单纯Inception-v4和残差网络相似计算代价的Top-5错误率。评估在 ILSVRC-2012验证集上进行不加入黑名单图像测量。在验证集上，残差模型训练的更快，同时召回率更好。

> 
> [![Image_27.png](https://ask.julyedu.com/uploads/questions/20170322/91dd37d73de3590dbdd67295d6bc3cfc.png)
](https://ask.julyedu.com/uploads/questions/20170322/91dd37d73de3590dbdd67295d6bc3cfc.png)
> 
> 
图 25 在四个模型（单个模型，一次裁剪）Top-5错误率。在更大模型尺寸上得到了改善。尽管残差版本收敛更快，但是最终的准确率依赖于模型尺寸

> 
> [![Image_28.png](https://ask.julyedu.com/uploads/questions/20170322/01bdbdb3f6d8a62d119a9463ca6578e7.png)
](https://ask.julyedu.com/uploads/questions/20170322/01bdbdb3f6d8a62d119a9463ca6578e7.png)
> 
> 
图 26 在四个模型（单个模型，一次裁剪）Top-1错误率。这个图同top-5评估。

**4.训练方法**
我们在TensorFlow分布式学习系统上使用随机梯度训练网络，在NvidiakeplerGPU上跑 20个副本。
**5.实验结果**
首先观察四个网络变体在训练阶段top-1和top-5validation-error上的演化。上述实验后发现，我们只在验证集的部分子集上进行了连续的评估。实验证明，和包含本团队研究在内的其他研究相比，我们得到的结果更加乐观。对于top-1差异率为0.3%，top-5差异率为0.15%。然而，由于差异率的一致性，我们认为这种比较也是很有必要。
另一方面，我们在50000张验证图像上进行裁剪和组合来进行重复实验。同样最后的组合结果在测试集进行测试并在ILSVRC测试服务器上验证我们的网络调整并没有导致过拟合。我们想强调的是，最终进行了一次验证，并在去年进行了两次结果提交：一次是BNInception论文和后来的ILSVR-2015 CLSLOC竞赛，因此我们相信测试集很好的验证了本文模型的泛化能力。
最后，我们展示了不同版本Inception和Inception-ResNet的比较结果。Inception-v3和Inception-v4模型是深度卷积网络，他们没有使用残差连接，而Inception-ResNet-v1和Inception-ResNet-v2使用了残差连接而没有使用滤波连接。
表2展示了在验证集上各种结构的单个模型以及单次裁剪的top-1和top-5错误率。

> 
> [![Image_25.png](https://ask.julyedu.com/uploads/questions/20170322/08f083a9972e0b416c2d86b212aa2f1f.png)
](https://ask.julyedu.com/uploads/questions/20170322/08f083a9972e0b416c2d86b212aa2f1f.png)
> 
> 
表 2 一次裁剪-单个模型实验结果。在ILSVRC2012进行的没有删除包围框的验证实验结果
表3展示了使用小数量裁剪的各种模型的性能比较：引文5中对ResNet做了10个裁剪，对于Inception，我们如引文14描述那样，使用12种裁剪进行验证。

> 
> [![Image_29.png](https://ask.julyedu.com/uploads/questions/20170322/8652ca193b791666b210c93058e2ec9e.png)
](https://ask.julyedu.com/uploads/questions/20170322/8652ca193b791666b210c93058e2ec9e.png)
> 
> 
表 3 10/12裁剪评估-单一模型试验结果。在ILSVRC2012的50000张图像上进行的验证
表4展示了单个模型的性能。对于残差网络dense的验证结果可参见引文14。对于Inception网络，[14]描述了针对inception网络的144种裁剪策略。

> 
> [![Image_30.png](https://ask.julyedu.com/uploads/questions/20170322/ab4333f0ffa41d66350db6aeb1e51a69.png)
](https://ask.julyedu.com/uploads/questions/20170322/ab4333f0ffa41d66350db6aeb1e51a69.png)
> 
> 
表 4 144个裁剪评估，单一模型的实验结果。在ILSVRC2012所有50000张图像上进行验证。
Table5比较了组合的结果。[5]描述了对于纯净的残差网络，6个模型的dense验证的结果。对于Inception网络4个模型的组合，144种裁剪策略正如[14]描述即可。

> 
> [![Image_31.png](https://ask.julyedu.com/uploads/questions/20170322/dd9081b3b31937eb01b55259d29d4dfa.png)
](https://ask.julyedu.com/uploads/questions/20170322/dd9081b3b31937eb01b55259d29d4dfa.png)
> 
> 
表 5 使用144裁剪/稠密进行组合结果的评估。在ILSVRC2012 50000张图像进行验证。对于Inception-v4(+残差)，组合模型由一个Inception-v4和三个Inception-ResNet-v2 模型组成。测试性能在top-5错误率达到3.08%，并且在验证集上没有过拟合。

**6 结论**
本文详细呈现了三种新的网络结构：
（1）Inception-Reset-v1：混合Inception版本，它的计算效率同Inception-v3；
（2）Inception-ResNet-v2：更加昂贵的混合Inception版本，同明显改善了识别性能；
（3）Inception-v4：没有残差链接的纯净Inception变种，性能如同Inception-ResNet-v2我们研究了引入残差连接如何显著的提高inception网络的训练速度。而且仅仅凭借增加的模型尺寸，我们的最新的模型（带和不带残差连接）都优于我们以前的网络。
完。</blockquote>
