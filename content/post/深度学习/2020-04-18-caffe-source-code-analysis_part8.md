---
title: "caffe 源码学习笔记(8) loss function"
date: 2020-04-18T18:33:29+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/caffe-source-code-analysis-part8
categories:
- deep-learning

tags:

- caffe

---

## 背景

虽然不太care 训练的过程，~~但是由于容易看懂的layer都看得差不多了~~ 所以打算看一下这些loss function.


## Euclidean Loss (L2 loss)

![L2 loss.png](https://i.loli.net/2020/04/18/voT7jGEF1BabmpL.png)

一般用于“real-valued regression tasks” 。　比如之前的项目上用的人脸年龄模型，就是用了这个Loss

这个loss没什么额外的参数，实现也很简单。

```c++

template <typename Dtype>
void EuclideanLossLayer<Dtype>::Reshape(
  const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>& top) {
  LossLayer<Dtype>::Reshape(bottom, top);
  CHECK_EQ(bottom[0]->count(1), bottom[1]->count(1))
      << "Inputs must have the same dimension.";
  diff_.ReshapeLike(*bottom[0]);
}

template <typename Dtype>
void EuclideanLossLayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  int count = bottom[0]->count();
  caffe_sub(
      count,
      bottom[0]->cpu_data(),
      bottom[1]->cpu_data(),
      diff_.mutable_cpu_data());
  Dtype dot = caffe_cpu_dot(count, diff_.cpu_data(), diff_.cpu_data());
  Dtype loss = dot / bottom[0]->num() / Dtype(2);
  top[0]->mutable_cpu_data()[0] = loss;
}
```

注意要Reshape中，要求两个bottom blob（第一个为预测结果，第二个为gt)的batch维度可以不同,计算时按照预测结果的个数为准。

以及，Mean Square Error(MSE)　和L2 loss的差别只是一个系数1/2,可以放在一起说明。

![MSE](https://miro.medium.com/max/291/1*w9HQ9w30lpr_HYZqeRhm4A.png)


## MultinomialLogisticLoss


![MultinomialLogisticLoss.png](https://i.loli.net/2020/04/18/MdSGtml3JOYUzX6.png)

用于单标签多分类任务。　输入的预测blob是一个(通常是经过softmax后)得到的概率分布。

注意 **" The SoftmaxWithLossLayer should be preferred over separate SoftmaxLayer + MultinomialLogisticLossLayer as its gradient computation is more numerically stable."**

这个后面会提到。

同样，这个loss也没什么额外参数，
forward也很简单

```c++

template <typename Dtype>
void MultinomialLogisticLossLayer<Dtype>::Forward_cpu(
    const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  //  predictions,ＮxCxHxW
  const Dtype* bottom_label = bottom[1]->cpu_data();
  // labels, Nx1x1x1
  int num = bottom[0]->num();
  int dim = bottom[0]->count() / bottom[0]->num();
  // dim 表示类别总数
  Dtype loss = 0;
  //  bottom_data[i * dim + label]表示的是第i张图的gt对应的位置的预测分数
  for (int i = 0; i < num; ++i) {
    int label = static_cast<int>(bottom_label[i]);
    Dtype prob = std::max(
        bottom_data[i * dim + label], Dtype(kLOG_THRESHOLD));
    loss -= log(prob);
  }
  top[0]->mutable_cpu_data()[0] = loss / num;
}

```
需要注意的已经写在注释中了。
kLOG_THRESHOLD是一个很小的值，1E-20,防止log0炸掉


## hinge-loss


![hinge loss](https://wikimedia.org/api/rest_v1/media/math/render/svg/a5f42d461f1a28b27438e8f1641e042ff2e40102)

中文似乎叫"合页损失函数",因为很像一本书打开的样子(?

![hinge-loss](https://pic1.zhimg.com/80/v2-3c6aa9626ee8e4609b0d7c5712baf624_720w.jpg)

主要用在svm中。。。所以其实没在工作中实际接触过这个。

这个loss的特点是更加严格。。严格的意思是说，分类的结果不仅需要正确，而且需要置信度足够高，损失才会是0.

![hinge_loss_caffe.png](https://i.loli.net/2020/04/18/ZgKC2ONAmuTRYJ7.png)


forward代码稍微不是那么直接
```c++

  const Dtype* bottom_data = bottom[0]->cpu_data();
  Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();
  const Dtype* label = bottom[1]->cpu_data();
  int num = bottom[0]->num();
  int count = bottom[0]->count();
  int dim = count / num;
  // dim是类别数

  caffe_copy(count, bottom_data, bottom_diff);
  // 把预测值bottom_data拷贝到bottom_diff
  for (int i = 0; i < num; ++i) {
    bottom_diff[i * dim + static_cast<int>(label[i])] *= -1;
  }
  // 把gt的那一类的预测分数取了相反数(这里相当于算了condition函数，只不过差个负号)

  for (int i = 0; i < num; ++i) {
    for (int j = 0; j < dim; ++j) {
      bottom_diff[i * dim + j] = std::max(
        Dtype(0), 1 + bottom_diff[i * dim + j]);
    }


```

先算了一个bottom_diff。　这里其实是相当于算了condition function的结果，只不过差了一个负号。　后面我们也可以看到

```c++

bottom_diff[i * dim + j] = std::max(
        Dtype(0), 1 + bottom_diff[i * dim + j]);

```
中是计算了**bottom_diff[i * dim + j] = std::max(
        Dtype(0), 1 + bottom_diff[i * dim + j]);**



还值得一提的是,caffe的hinge loss 同时支持L1 norm和L2 norm(在L2-SVM中使用)

```protobuf

message HingeLossParameter {
  enum Norm {
    L1 = 1;
    L2 = 2;
  }
  // Specify the Norm to use L1 or L2
  optional Norm norm = 1 [default = L1];
}
```


```c++

  Dtype* loss = top[0]->mutable_cpu_data();
  switch (this->layer_param_.hinge_loss_param().norm()) {
  case HingeLossParameter_Norm_L1:
    loss[0] = caffe_cpu_asum(count, bottom_diff) / num;
    break;
  case HingeLossParameter_Norm_L2:
    loss[0] = caffe_cpu_dot(count, bottom_diff, bottom_diff) / num;
    break;
  default:
    LOG(FATAL) << "Unknown Norm";
  }
}

```



## 参考资料

- [5 Regression Loss Functions All Machine Learners Should Know](https://heartbeat.fritz.ai/5-regression-loss-functions-all-machine-learners-should-know-4fb140e9d4b0)

- [Hinge loss](https://en.wikipedia.org/wiki/Hinge_loss)