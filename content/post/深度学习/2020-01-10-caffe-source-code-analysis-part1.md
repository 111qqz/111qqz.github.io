---
title: "caffe 源码学习笔记(1) Blob"
date: 2020-01-10T11:24:23+08:00
draft: false
author: "111qqz"
type: post
url: /2020/01/caffe-source-code-analysis-part1
categories:
- deep-learning

tags:

- caffe 
---


迫于生计，开始看caffe代码。
会侧重于分析inference部分。

## blob 整体介绍

### blob的含义及目的

blob在逻辑上表示的就是所谓的tensor,blob是tensor在caffe中的叫法。
在框架层面上，blob的意义在于对数据进行封装，提供统一的接口。
这里的数据包含训练/inference时用的数据，也包含模型参数，导数等数据。
深度学习离不开在GPU上的计算。 blob对数据的封装使得用户不必关心和cuda有关的数据传输细节。

### blob的表示

对于图像数据，blob通常为４-dim，也就是**N\*C\*H\*W**
其中N表示number,也就是batch_num
C表示channel
H表示height
W表示width

在内存中，blob是按照"C-contiguous fashion"存储的，也就是"row-major "

因此，位于(n,c,h,w)的下标在OS中的位置是　((n * C + c) * H + h) * W + w.

在代码blob.hpp中，我们也可以看到名为offset的函数是其对应的实现。

```c++
  inline int offset(const int n, const int c = 0, const int h = 0,
      const int w = 0) const {
    CHECK_GE(n, 0);
    CHECK_LE(n, num());
    CHECK_GE(channels(), 0);
    CHECK_LE(c, channels());
    CHECK_GE(height(), 0);
    CHECK_LE(h, height());
    CHECK_GE(width(), 0);
    CHECK_LE(w, width());
    return ((n * channels() + c) * height() + h) * width() + w;
  }
  //  给一个indices,计算这是第几个值。
  inline int offset(const vector<int>& indices) const {
    CHECK_LE(indices.size(), num_axes());
    int offset = 0;
    for (int i = 0; i < num_axes(); ++i) {
      offset *= shape(i);
      if (indices.size() > i) {
        CHECK_GE(indices[i], 0);
        CHECK_LT(indices[i], shape(i));
        offset += indices[i];
      }
    }
    return offset;
  }
```


需要说明的是，存在一个overload的offset的原因是，对于常见的图像任务，blob是四维的，但是blob也可以是其他数目的维度。

后面我们可以看到，很多函数都有一个overload的版本，一个版本是适用于经典的图像任务，另外一个版本是适用于更一般的任务。




## blob 实现细节

我们注意到，对于data,diff等数据，blob除了区分了在CPU还是GPU上，还区分了数据是否可以改变:

```c++
const Dtype* cpu_data() const;
Dtype* mutable_cpu_data();
```

这样设计的原因是，blob中包含了GPU和CPU上的数据，为了尽可能减少不必要的数据传输，我们可以在确定不会修改数据的情况下使用const版本

同时，区分可变数据和不可变数据也有助于减少bug.

需要注意的是,blob class是禁止copy和assign的。
在C++11及以后，这可以通过将相应的copy control member 设置为"=delete"来实现
而在c++11之前，是通过将这些函数这只为private实现的。

```c++
#define DISABLE_COPY_AND_ASSIGN(classname) \
private:\
  classname(const classname&);\
  classname& operator=(const classname&)
```


此外，我们可以重点看一下reshape 函数

```c++
template <typename Dtype>
void Blob<Dtype>::Reshape(const int num, const int channels, const int height,
    const int width) {
  vector<int> shape(4);
  shape[0] = num;
  shape[1] = channels;
  shape[2] = height;
  shape[3] = width;
  Reshape(shape);
}

template <typename Dtype>
void Blob<Dtype>::Reshape(const vector<int>& shape) {
  CHECK_LE(shape.size(), kMaxBlobAxes);
  count_ = 1;
  shape_.resize(shape.size());
  if (!shape_data_ || shape_data_->size() < shape.size() * sizeof(int)) {
    shape_data_.reset(new SyncedMemory(shape.size() * sizeof(int)));
  }
  int* shape_data = static_cast<int*>(shape_data_->mutable_cpu_data());
  for (int i = 0; i < shape.size(); ++i) {
    CHECK_GE(shape[i], 0);
    if (count_ != 0) {
      CHECK_LE(shape[i], INT_MAX / count_) << "blob size exceeds INT_MAX";
    }
    count_ *= shape[i];
    shape_[i] = shape[i];
    shape_data[i] = shape[i];
  }
  if (count_ > capacity_) {
    capacity_ = count_;
    data_.reset(new SyncedMemory(capacity_ * sizeof(Dtype)));
    diff_.reset(new SyncedMemory(capacity_ * sizeof(Dtype)));
  }
}
```

和之前的offset该函数相同，仍然是两个版本。
这里值得注意的是，其一是如果有不同接口的多个overload 函数，往往只有一个函数做了真正的工作，而其他函数都是调用该函数来完成。

此外，caffe中使用了shared_ptr来管理数据
当reshape后需要分配新的内存时，
```c++
  if (count_ > capacity_) {
    capacity_ = count_;
    data_.reset(new SyncedMemory(capacity_ * sizeof(Dtype)));
    diff_.reset(new SyncedMemory(capacity_ * sizeof(Dtype)));
  }
```








