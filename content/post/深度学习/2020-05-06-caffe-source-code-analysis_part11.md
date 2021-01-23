---
title: "caffe 源码学习笔记(11) argmax layer"
date: 2020-05-06T21:26:03+08:00
draft: false
author: "111qqz"
type: post
url: /2020/05/caffe-source-code-analysis-part11
categories:
- deep-learning

tags:

- caffe 
---


## 背景

似乎没什么背景,继续看caffe代码

argmax的作用是返回一个blob某个维度或者batch_size之后的维度的top_k的index(或者pair(index,value))


## proto

还是先看proto 


```protobuf

message ArgMaxParameter {
  // If true produce pairs (argmax, maxval)
  optional bool out_max_val = 1 [default = false];
  optional uint32 top_k = 2 [default = 1];
  // The axis along which to maximise -- may be negative to index from the
  // end (e.g., -1 for the last axis).
  // By default ArgMaxLayer maximizes over the flattened trailing dimensions
  // for each index of the first / num dimension.
  optional int32 axis = 3;
}


```

out_max_val为真表示输出(index,val)的pair,否则只输出index(?,存疑)

top_k应该是要取最大的top k个元素

axis是要求最大的维度,默认情况是把batch_size之后的维度flatten之后求argmax.



## c++ 实现


先看Reshape的部分


```c++

template <typename Dtype>
void ArgMaxLayer<Dtype>::Reshape(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
  int num_top_axes = bottom[0]->num_axes();
  if ( num_top_axes < 3 ) num_top_axes = 3;
  std::vector<int> shape(num_top_axes, 1);
  if (has_axis_) {
    // Produces max_ind or max_val per axis
    shape = bottom[0]->shape();
    shape[axis_] = top_k_;
    //  axis非默认参数的case: 只有求max的那个维度会变,其他都不变
    //  问题: out_max_val似乎只适用在axis为默认参数的情况?
  } else {
    shape[0] = bottom[0]->shape(0);
    // Produces max_ind
    shape[2] = top_k_;
    //  不是只拿到第top_k,而是拿到top_k的k个结果
    if (out_max_val_) {
      // Produces max_ind and max_val
      shape[1] = 2;
    }
    //  默认axis参数得到的top blob的shape 为(batch_size,1或者2,top_k)
    //  因为会把batch后面的维度flatten 然后求max
  }
  top[0]->Reshape(shape);
}

```

添加了一些注释. 有一个疑问是,axis和out_max_val_这两个参数似乎不支持同时处理

继续看forward


```c++

template <typename Dtype>
void ArgMaxLayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  Dtype* top_data = top[0]->mutable_cpu_data();
  int dim, axis_dist;
  if (has_axis_) {
    dim = bottom[0]->shape(axis_);
    // dim表示做argmax的维度一共有多少个值
    // Distance between values of axis in blob
    axis_dist = bottom[0]->count(axis_) / dim;
    //  因为可能不在最末尾的维度做argmax,因此值在内存中未必是连续的
  } else {
    dim = bottom[0]->count(1);
    //  从batch_size之后的维度数到最后
    axis_dist = 1;
    //  把末尾的几个维度flatten之后做argmax,在内存上这些值是连续的,因此axis_dist是1
  }
  int num = bottom[0]->count() / dim;
  std::vector<std::pair<Dtype, int> > bottom_data_vector(dim);
  for (int i = 0; i < num; ++i) {
    for (int j = 0; j < dim; ++j) {
      bottom_data_vector[j] = std::make_pair(
        bottom_data[(i / axis_dist * dim + j) * axis_dist + i % axis_dist], j);
    }
  //  通过axis_dist控制,把要做argmax的元素从内存中不连续的位置传到一个连续的vector中,目的是做sort
    std::partial_sort(
        bottom_data_vector.begin(), bottom_data_vector.begin() + top_k_,
        bottom_data_vector.end(), std::greater<std::pair<Dtype, int> >());
      //  使得前top_k是最大的top_k个元素,后面的元素顺序任意
    for (int j = 0; j < top_k_; ++j) {
      if (out_max_val_) {
        if (has_axis_) {
          // Produces max_val per axis
          top_data[(i / axis_dist * top_k_ + j) * axis_dist + i % axis_dist]
            = bottom_data_vector[j].first;
            //这个地方感觉有点问题... 就算是有axis参数不支持out_max_val... 输出的不也应该是index吗?
        } else {
          // Produces max_ind and max_val
          top_data[2 * i * top_k_ + j] = bottom_data_vector[j].second;
          top_data[2 * i * top_k_ + top_k_ + j] = bottom_data_vector[j].first;
        }
      } else {
        // Produces max_ind per axis
        top_data[(i / axis_dist * top_k_ + j) * axis_dist + i % axis_dist]
          = bottom_data_vector[j].second;
      }
    }
  }
}



```

值得注意的是,由于可能不在末尾的维度求max,因此求max的值可能在内存上是不连续的,
**注意看axis_dist这个变量.表示的就是要求argmax的相邻元素在内存中的距离.**


然后接下来的代码有些让人困惑... 即使是不同时支持out_max_val和axis这两个参数...只有一个输出,那么输出的不也应该也是index吗?

这个输出好像不是很对啊?????  去官方的caffe确认了一下,也是这样写的.

不是很确定这是不是预期的行为.


update:

看来不止我发现了这个问题 [some doubts about argmax_layer (may be bug) ](https://github.com/BVLC/caffe/issues/6823) 可惜caffe看起来已经没人维护了2333