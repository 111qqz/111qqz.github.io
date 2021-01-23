---
title: "caffe 源码学习笔记(7) slice layer"
date: 2020-04-13T21:22:54+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/caffe-source-code-analysis-part7
categories:
- deep-learning

tags:

- caffe 
---


## 背景　

ocr组那边有个shuffle net 的网络,里面有个pytorch op叫chunk,转成的onnx对应的op是 [split](https://github.com/onnx/onnx/blob/master/docs/Operators.md#Split)  

作用是:

>Split a tensor into a list of tensors, along the specified 'axis'. Lengths of the parts can be specified using argument 'split'. Otherwise, the tensor is split to equal sized parts.

然后发现这个op模型转换里不支持转到caffe的layer,于是想办法支持了一下. 发现是要转到caffe的slice layer.(**caffe也有一个split layer,但是这个split layer是除了一个输出blob作为多个layer的输入时用的**)


## proto

```protobuf

message SliceParameter {
  // The axis along which to slice -- may be negative to index from the end
  // (e.g., -1 for the last axis).
  // By default, SliceLayer concatenates blobs along the "channels" axis (1).
  optional int32 axis = 3 [default = 1];
  repeated uint32 slice_point = 2;

  // DEPRECATED: alias for "axis" -- does not support negative indexing.
  optional uint32 slice_dim = 1 [default = 1];
}


```

看起来slice_dim和axis是新旧两种写法,slice_point应该就是切割点.  这个layer文档仍然是"to do"状态,因此只能看代码了.


## c++实现

```c++

template <typename Dtype>
void SliceLayer<Dtype>::LayerSetUp(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
  const SliceParameter& slice_param = this->layer_param_.slice_param();
  CHECK(!(slice_param.has_axis() && slice_param.has_slice_dim()))
      << "Either axis or slice_dim should be specified; not both.";
  slice_point_.clear();
  std::copy(slice_param.slice_point().begin(),
      slice_param.slice_point().end(),
      std::back_inserter(slice_point_));
}

```
layerSetUp就是单纯把slice_point用成员函数来存储.


reshape 其实是比较重点的部分,注意不提供slice_point的默认情况. 其他部分很好懂,就是把切割点计算成每一部分切割线段的长度.



```c++
template <typename Dtype>
void SliceLayer<Dtype>::Reshape(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
  const int num_axes = bottom[0]->num_axes();
  const SliceParameter& slice_param = this->layer_param_.slice_param();
  if (slice_param.has_slice_dim()) {
    slice_axis_ = static_cast<int>(slice_param.slice_dim());
    // Don't allow negative indexing for slice_dim, a uint32 -- almost
    // certainly unintended.
    CHECK_GE(slice_axis_, 0) << "casting slice_dim from uint32 to int32 "
        << "produced negative result; slice_dim must satisfy "
        << "0 <= slice_dim < " << kMaxBlobAxes;
    CHECK_LT(slice_axis_, num_axes) << "slice_dim out of range.";
  } else {
    slice_axis_ = bottom[0]->CanonicalAxisIndex(slice_param.axis());
  }
  vector<int> top_shape = bottom[0]->shape();
  const int bottom_slice_axis = bottom[0]->shape(slice_axis_);
  // bottom_slice_axis为切割的那个维度的总数
  num_slices_ = bottom[0]->count(0, slice_axis_);
  //  计算[0,slice_axis_)的count
  slice_size_ = bottom[0]->count(slice_axis_ + 1);
  //  计算[slice_axis_+1,num_axes()]的体积
  int count = 0;
  if (slice_point_.size() != 0) {
    CHECK_EQ(slice_point_.size(), top.size() - 1);
    //  n个点把一条线段切割成n+1(top.size())份
    CHECK_LE(top.size(), bottom_slice_axis);
    //  抽屉原理,保证每一个输出blob至少有一份.
    int prev = 0;
    vector<int> slices;
    //  slices保存每一个切割的长度
    for (int i = 0; i < slice_point_.size(); ++i) {
      CHECK_GT(slice_point_[i], prev);
      slices.push_back(slice_point_[i] - prev);
      prev = slice_point_[i];
    }
    slices.push_back(bottom_slice_axis - prev);
    for (int i = 0; i < top.size(); ++i) {
      top_shape[slice_axis_] = slices[i];
      top[i]->Reshape(top_shape);
      count += top[i]->count();
    }
  } else {
    // 如果不填写 slice_point,默认是把slice维度平均分给所有输出的blob
    // 比如输入为[1,3,M,224],在M所在的维度所slice,输出为3个blob
    //  那么就会得到三个shape为 [1,3,M/3,224]的blob,并且保证M%3==0; 
    CHECK_EQ(bottom_slice_axis % top.size(), 0)
        << "Number of top blobs (" << top.size() << ") should evenly "
        << "divide input slice axis (" << bottom_slice_axis << ")";
    top_shape[slice_axis_] = bottom_slice_axis / top.size();
    for (int i = 0; i < top.size(); ++i) {
      top[i]->Reshape(top_shape);
      count += top[i]->count();
    }
  }
  CHECK_EQ(count, bottom[0]->count());
  if (top.size() == 1) {
    top[0]->ShareData(*bottom[0]);
    top[0]->ShareDiff(*bottom[0]);
  }
}

```

然后是forward,没什么好说的.

```c++

template <typename Dtype>
void SliceLayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
  if (top.size() == 1) { return; }
  int offset_slice_axis = 0;
  const Dtype* bottom_data = bottom[0]->cpu_data();
  const int bottom_slice_axis = bottom[0]->shape(slice_axis_);
  for (int i = 0; i < top.size(); ++i) {
    Dtype* top_data = top[i]->mutable_cpu_data();
    const int top_slice_axis = top[i]->shape(slice_axis_);
    for (int n = 0; n < num_slices_; ++n) {
      const int top_offset = n * top_slice_axis * slice_size_;
      const int bottom_offset =
          (n * bottom_slice_axis + offset_slice_axis) * slice_size_;
      caffe_copy(top_slice_axis * slice_size_,
          bottom_data + bottom_offset, top_data + top_offset);
    }
    offset_slice_axis += top_slice_axis;
  }
}

```