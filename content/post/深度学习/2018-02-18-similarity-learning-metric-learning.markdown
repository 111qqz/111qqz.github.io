---
author: 111qqz
date: 2018-02-18 08:14:10+00:00
draft: false
title: Similarity learning 和Metric learning
type: post
url: /2018/02/similarity-learning-metric-learning/
categories:
- deep-learning
tags:
- Metric learning
- Similarity learning
- triplet loss
---

## [Similarity_learning](https://en.wikipedia.org/wiki/Similarity_learning)





相似性学习（Similarity learning ）有监督机器学习，它与回归和分类密切相关，但目标是从实例中学习一个相似函数，**以衡量两个对象的相似程度或相关程度。**





Similarity learning通常有四种setups:






      * regression similarity learning  在这种方式中，给出的数据是 ![(x_{i}^{1},x_{i}^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa249357a1b4a7baf332041d67e480d6bb1f8fb)
  和他们的相似度 ![y_{i}\in R](https://wikimedia.org/api/rest_v1/media/math/render/svg/e8a6d6289f0a0adb278812a8723b4077de79a421)
.  目标是学习到一个函数![f(x_{i}^{1},x_{i}^{2})\sim y_{i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/d91180d029bb8a4f43be5d76060581b861f65fb7)
，对于![(x_{i}^{1},x_{i}^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa249357a1b4a7baf332041d67e480d6bb1f8fb)
 给出**yi**的近似值。
      * Classification similarity learning  给出数据 ![(x_{i}^{1},x_{i}^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa249357a1b4a7baf332041d67e480d6bb1f8fb)
  和他们是否相似![y_{i}\in \{0,1\}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e5c2ebeb5127a5306baf27c9c622a86aa35625f2)
 。目标是训练出一个分类器，能够完成对一组![(x_{i}^{1},x_{i}^{2})](https://wikimedia.org/api/rest_v1/media/math/render/svg/cfa249357a1b4a7baf332041d67e480d6bb1f8fb)
 是否相似的二分类判断。
      * Ranking similarity learning 给出有序三元组![(x_{i},x_{i}^{+},x_{i}^{-})](https://wikimedia.org/api/rest_v1/media/math/render/svg/1bb03478aa729d594350565f174c78a4b7d9e87c)
，其中 ![x_{i}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e87000dd6142b81d041896a30fe58f0c3acb2158)
 is known to be more similar to ![x_{i}^{+}](https://wikimedia.org/api/rest_v1/media/math/render/svg/89b5a4feb798c9d34d33200239a28f02cc6df2c4)
 than to ![x_{i}^{-}](https://wikimedia.org/api/rest_v1/media/math/render/svg/202021401f451c2ba4ab43eddb2f8644e2610249)
 。目标是训练出一个函数，使得对于新的三元组 ![(x,x^{+},x^{-})](https://wikimedia.org/api/rest_v1/media/math/render/svg/2578f37761a5f2937eedca81f4c96b0ba45fbc15)
，满足![f(x,x^{+})>f(x,x^{-})](https://wikimedia.org/api/rest_v1/media/math/render/svg/c27924f2eec770183ce65e3c653e74a5c1c79c7e)
。容易看出，这种方式采取了比回归更弱的监督形式，因为不需要提供精确的相似性度量，只需要提供相似性的相对顺序。因此，这种ranking-based的相似性学习更容易应用于实际的大规模应用
      * Locality sensitive hashing (LSH)   局部敏感哈希和普通哈希的不同就是，相似的项有更大的概率被放到同一个桶中。




顺便一提，这里有一个叫triplet loss 的概念，

![这里写图片描述](http://img.blog.csdn.net/20150707120209693)


如上图所示，triplet是一个三元组，这个三元组是这样构成的：从训练数据集中随机选一个样本，该样本称为Anchor，然后再随机选取一个和Anchor (记为x_a)属于同一类的样本和不同类的样本,这两个样本对应的称为Positive (记为x_p)和Negative (记为x_n)，由此构成一个（Anchor，Positive，Negative）三元组。

**我们发现，triplet loss 其实就是在ranking similarity learning 问题中，学习similarity function时的loss**



## Metric learning



相似性学习与距离度量学习密切相关。度量学习的目标是在对象上学习一个距离函数。度量或距离函数必须遵循四个公理:**非负性、不可分辨的恒等式、对称性和次可加性/三角形不等式**。在实际应用中，度量学习算法忽略了不可分辨物体的身份条件，学习了一个伪度量。














