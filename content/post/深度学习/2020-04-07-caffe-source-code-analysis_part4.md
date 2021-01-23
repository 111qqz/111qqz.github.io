---
title: "caffe 源码学习笔记(4) 激活函数"
date: 2020-04-07T23:21:40+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/caffe-source-code-analysis-part4
categories:
- deep-learning

tags:

- caffe

---


在看过caffe代码的三个核心部分,blob,layer,net之后，陷入了不知道以什么顺序继续看的困境。

blob,layer,net只是三个最基本的概念，关键还是在于各个layer. 但是layer这么多，要怎么看呢？  想了一下决定把相同作用的layer放在一起分析。  今天打算先分析一下激活函数。


## sigmoid

![sigmoid函数](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Sigmoid_function_01.png/220px-Sigmoid_function_01.png)

表达式为 f(t) = 1/(1+e^-t)


caffe GPU实现，非常直接

```c++

template <typename Dtype>
__global__ void SigmoidForward(const int n, const Dtype* in, Dtype* out) {
  CUDA_KERNEL_LOOP(index, n) {
    out[index] = 1. / (1. + exp(-in[index]));
  }
}

```

sigmoid激活函数的一大优点是求导非常容易，因此backward函数其实也很简单。

```c++

template <typename Dtype>
__global__ void SigmoidBackward(const int n, const Dtype* in_diff,
    const Dtype* out_data, Dtype* out_diff) {
  CUDA_KERNEL_LOOP(index, n) {
    const Dtype sigmoid_x = out_data[index];
    out_diff[index] = in_diff[index] * sigmoid_x * (1 - sigmoid_x);
  }
}

```

然后proto里面也没什么内容。因为sigmoid函数没什么参数

``` proto

message SigmoidParameter {
  enum Engine {
    DEFAULT = 0;
    CAFFE = 1;
    CUDNN = 2;
  }
  optional Engine engine = 1 [default = DEFAULT];
}

```


还值得注意的是sigmoid有文件里的注释:

> /**
> @brief Sigmoid function non-linearity @f$
>         y = (1 + \exp(-x))^{-1}
>     @f$, a classic choice in neural networks.
>
> Note that the gradient vanishes as the values move away from 0.
> The ReLULayer is often a better choice for this reason.
>

sigmoid函数大概是早期的一个比较常用的选择。但是其有几个缺点:

- 梯度弥散（除了中间的位置，其他位置的梯度都接近0)
- sigmoid函数的输出不是0均值的,导致权重的梯度全部为正或者为负，只能往一个方向更新，学习的效率比较低。
- 算exp比较慢

因此现在已经几乎不会用sigmoid来做激活函数了。

**但是sigmoid函数其实还有其他用途，比如对于一个多标签的分类任务，常常在fc后面接sigmoid作为神经网络的输出，来判断是否包含这些标签中的一个或者几个。**

（多标签和多分类任务的区别在于，多分类任务通常只有一个标签，一个物体属于这个类别就不会属于另外的类别。）


## tanh

和sigmoid比较相似，比起sigmoid的优点是值域在[-1,1]，均值是为0的，梯度更新的效率比sigmoid好一些。

没什么可说的，直接放代码吧

工业界用得也不太多

```c++

template <typename Dtype>
void TanHLayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  Dtype* top_data = top[0]->mutable_cpu_data();
  const int count = bottom[0]->count();
  for (int i = 0; i < count; ++i) {
    top_data[i] = tanh(bottom_data[i]);
  }
}

template <typename Dtype>
void TanHLayer<Dtype>::Backward_cpu(const vector<Blob<Dtype>*>& top,
    const vector<bool>& propagate_down,
    const vector<Blob<Dtype>*>& bottom) {
  if (propagate_down[0]) {
    const Dtype* top_data = top[0]->cpu_data();
    const Dtype* top_diff = top[0]->cpu_diff();
    Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();
    const int count = bottom[0]->count();
    Dtype tanhx;
    for (int i = 0; i < count; ++i) {
      tanhx = top_data[i];
      bottom_diff[i] = top_diff[i] * (1 - tanhx * tanhx);
    }
  }
}

```


## relu及其变种

表达式为f(x) = max(0,x) 

![relu](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Ramp_function.svg/325px-Ramp_function.svg.png)


我们看caffe的proto,发现relu和leaky relu是在一起实现的，因此干脆一起说了。


```protobuf

// Message that stores parameters used by ReLULayer
message ReLUParameter {
  // Allow non-zero slope for negative inputs to speed up optimization
  // Described in:
  // Maas, A. L., Hannun, A. Y., & Ng, A. Y. (2013). Rectifier nonlinearities
  // improve neural network acoustic models. In ICML Workshop on Deep Learning
  // for Audio, Speech, and Language Processing.
  optional float negative_slope = 1 [default = 0];
  enum Engine {
    DEFAULT = 0;
    CAFFE = 1;
    CUDNN = 2;
  }
  optional Engine engine = 2 [default = DEFAULT];
}

```

leaky relu是relu的改进，表达式为 ![leaky relu](https://wikimedia.org/api/rest_v1/media/math/render/svg/7ef462b36056ff49700914fc305a39cd0d8c1ef1)

其中lambda是一个用户设定的超参，就是上面的negative_slope

看一下代码. backward部分也很简单，就一起看一下。


```c++

template <typename Dtype>
void ReLULayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  Dtype* top_data = top[0]->mutable_cpu_data();
  const int count = bottom[0]->count();
  Dtype negative_slope = this->layer_param_.relu_param().negative_slope();
  for (int i = 0; i < count; ++i) {
    top_data[i] = std::max(bottom_data[i], Dtype(0))
        + negative_slope * std::min(bottom_data[i], Dtype(0));
  }
}

template <typename Dtype>
void ReLULayer<Dtype>::Backward_cpu(const vector<Blob<Dtype>*>& top,
    const vector<bool>& propagate_down,
    const vector<Blob<Dtype>*>& bottom) {
  if (propagate_down[0]) {
    const Dtype* bottom_data = bottom[0]->cpu_data();
    const Dtype* top_diff = top[0]->cpu_diff();
    Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();
    const int count = bottom[0]->count();
    Dtype negative_slope = this->layer_param_.relu_param().negative_slope();
    for (int i = 0; i < count; ++i) {
      bottom_diff[i] = top_diff[i] * ((bottom_data[i] > 0)
          + negative_slope * (bottom_data[i] <= 0));
    }
  }
}
```

relu激活函数应该是目前业界默认的激活函数，简单，效果也挺不错。 优点是:
- 收敛速度快
- 在x>0的区域，不会出现梯度饱和和梯度消失的情况。
- 计算复杂度低，不需要进行指数运算，只要一个阈值就可以得到激活值。

当然也有一些缺点:

- ReLU的输出不是0均值的。
- Dead ReLU Problem(神经元坏死现象)：ReLU在负数区域被kill的现象叫做dead relu。ReLU在训练的时很“脆弱”。在x<0时，梯度为0。这个神经元及之后的神经元梯度永远为0，不再对任何数据有所响应，导致相应参数永远不会被更新。
产生这种现象的两个原因：参数初始化问题；learning rate太高导致在训练过程中参数更新太大。
解决方法：采用Xavier初始化方法，以及避免将learning rate设置太大或使用adagrad等自动调节learning rate的算法。


leaky relu主要是为了解决dead relu 现象提出来的。。。 因为避免出现了激活值总为0的问题。 

**但是在实际应用中，并不明显比relu效果好，因此人们还是经常用relu**


---

leaky relu中的lambda是一个用户设定的超参，如果不手动设定，而是把这个参数通过数据学习出来，就是prelu(p for Parametric)

具体的区别在于:
- negative slope是通过数据学习得到的。
- 每个channel可以学到不同的negative slope(也可以设置所有channel的negative slope统一)

> @brief Parameterized Rectified Linear Unit non-linearity @f$
>        y_i = \max(0, x_i) + a_i \min(0, x_i)
>        @f$. The differences from ReLULayer are 1) negative slopes are
>       learnable though backprop and 2) negative slopes can vary across
>        channels. The number of axes of input blob should be greater than or
>        equal to 2. The 1st axis (0-based) is seen as channels.


我们先看一下proto

```protobuf

message PReLUParameter {
  // Parametric ReLU described in K. He et al, Delving Deep into Rectifiers:
  // Surpassing Human-Level Performance on ImageNet Classification, 2015.

  // Initial value of a_i. Default is a_i=0.25 for all i.
  optional FillerParameter filler = 1;
  // Whether or not slope paramters are shared across channels.
  optional bool channel_shared = 2 [default = false];
}
```

这里面的filler的作用是决定每个channel的lambda的初始值



forward函数和之前比较相似，重点关注一下 slope_data

```c++

template <typename Dtype>
void PReLULayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  Dtype* top_data = top[0]->mutable_cpu_data();
  const int count = bottom[0]->count();
  const int dim = bottom[0]->count(2);
  const int channels = bottom[0]->channels();
  const Dtype* slope_data = this->blobs_[0]->cpu_data();

  // For in-place computation
  if (bottom[0] == top[0]) {
    caffe_copy(count, bottom_data, bottom_memory_.mutable_cpu_data());
  }

  // if channel_shared, channel index in the following computation becomes
  // always zero.
  const int div_factor = channel_shared_ ? channels : 1;
  for (int i = 0; i < count; ++i) {
    int c = (i / dim) % channels / div_factor;
    top_data[i] = std::max(bottom_data[i], Dtype(0))
        + slope_data[c] * std::min(bottom_data[i], Dtype(0));
  }
}
```

然后在backward部分，我们可以看到 slope_data是通过BP学习得到的。


```c++

template <typename Dtype>
void PReLULayer<Dtype>::Backward_cpu(const vector<Blob<Dtype>*>& top,
    const vector<bool>& propagate_down,
    const vector<Blob<Dtype>*>& bottom) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  const Dtype* slope_data = this->blobs_[0]->cpu_data();
  const Dtype* top_diff = top[0]->cpu_diff();
  const int count = bottom[0]->count();
  const int dim = bottom[0]->count(2);
  const int channels = bottom[0]->channels();

  // For in-place computation
  if (top[0] == bottom[0]) {
    bottom_data = bottom_memory_.cpu_data();
  }

  // if channel_shared, channel index in the following computation becomes
  // always zero.
  const int div_factor = channel_shared_ ? channels : 1;

  // Propagte to param
  // Since to write bottom diff will affect top diff if top and bottom blobs
  // are identical (in-place computaion), we first compute param backward to
  // keep top_diff unchanged.
  if (this->param_propagate_down_[0]) {
    Dtype* slope_diff = this->blobs_[0]->mutable_cpu_diff();
    for (int i = 0; i < count; ++i) {
      int c = (i / dim) % channels / div_factor;
      slope_diff[c] += top_diff[i] * bottom_data[i] * (bottom_data[i] <= 0);
    }
  }
  // Propagate to bottom
  if (propagate_down[0]) {
    Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();
    for (int i = 0; i < count; ++i) {
      int c = (i / dim) % channels / div_factor;
      bottom_diff[i] = top_diff[i] * ((bottom_data[i] > 0)
          + slope_data[c] * (bottom_data[i] <= 0));
    }
  }
}


```

这个东西的优点基本上是leaky relu的优点，再加上参数可以通过数据学习，更加鲁棒。

然而在工业界，这东西用得很少，在加上tensorrt5现在还不支持prelu（似乎是caffe parser的锅）

[PReLU cant be converted #177](https://github.com/NVIDIA/TensorRT/issues/179)


---

还有个类似的叫elu


![elu](https://www.zhihu.com/equation?tex=f%28z%29%3D%5Cleft%5C%7B%5Cbegin%7Barray%7D%7Bll%7D%7Bz%7D+%26+%7Bz%3E0%7D+%5C%5C+%7B%5Calpha%28%5Cexp+%28z%29-1%29%7D+%26+%7Bz+%5Cleq+0%7D%5Cend%7Barray%7D%5Cright.)



和leaky relu其实非常类似，没什么好说的。


效果并不确定完全比relu好，而且还要做exp运算，差评。

```c++


template <typename Dtype>
void ELULayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  Dtype* top_data = top[0]->mutable_cpu_data();
  const int count = bottom[0]->count();
  Dtype alpha = this->layer_param_.elu_param().alpha();
  for (int i = 0; i < count; ++i) {
    top_data[i] = std::max(bottom_data[i], Dtype(0))
        + alpha * (exp(std::min(bottom_data[i], Dtype(0))) - Dtype(1));
  }
}

template <typename Dtype>
void ELULayer<Dtype>::Backward_cpu(const vector<Blob<Dtype>*>& top,
    const vector<bool>& propagate_down,
    const vector<Blob<Dtype>*>& bottom) {
  if (propagate_down[0]) {
    const Dtype* bottom_data = bottom[0]->cpu_data();
    const Dtype* top_data = top[0]->cpu_data();
    const Dtype* top_diff = top[0]->cpu_diff();
    Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();
    const int count = bottom[0]->count();
    Dtype alpha = this->layer_param_.elu_param().alpha();
    for (int i = 0; i < count; ++i) {
      bottom_diff[i] = top_diff[i] * ((bottom_data[i] > 0)
          + (alpha + top_data[i]) * (bottom_data[i] <= 0));
    }
  }
}

```


## 总结


无脑上relu一般效果不会太差。






