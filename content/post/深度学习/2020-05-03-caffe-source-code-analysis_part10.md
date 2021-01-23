---
title: "caffe 源码学习笔记(10) eltwise layer"
date: 2020-05-03T17:53:22+08:00
draft: false
author: "111qqz"
type: post
url: /2020/05/caffe-source-code-analysis-part10
categories:
- deep-learning

tags:

- caffe 

---

## 背景

这个layer和reduce layer有一些相似,就干脆一起看了.
作用是输入至少两个blob,然后对每个blob中的元素所一些运算,最后得到一个blob.

caffe 支持的运算有"PROD","SUM","MAX"三种

顺便提一句,TensorRT支持的要多一些:

```c++

enum class ElementWiseOperation : int
{
    kSUM = 0,  //!< Sum of the two elements.
    kPROD = 1, //!< Product of the two elements.
    kMAX = 2,  //!< Maximum of the two elements.
    kMIN = 3,  //!< Minimum of the two elements.
    kSUB = 4,  //!< Substract the second element from the first.
    kDIV = 5,  //!< Divide the first element by the second.
    kPOW = 6   //!< The first element to the power of the second element.
};

```


## proto 

```protobuf 

message EltwiseParameter {
  enum EltwiseOp {
    PROD = 0;
    SUM = 1;
    MAX = 2;
  }
  optional EltwiseOp operation = 1 [default = SUM]; // element-wise operation
  repeated float coeff = 2; // blob-wise coefficient for SUM operation

  // Whether to use an asymptotically slower (for >2 inputs) but stabler method
  // of computing the gradient for the PROD operation. (No effect for SUM op.)
  optional bool stable_prod_grad = 3 [default = true];
}


```

proto里面的coeff是对于SUM操作,可以给每一个bottom blob一个加权系数, stable_prod_grad是backward用的,不用管.


## c++ 实现

```c++

代码比较容易看懂,加了一些注释. 有两个地方可以提一下. 一个是PROD和MAX的做法,都是先求前两个,再把得到的结果和后面的blob进行运算.(其实是很自然的操作...似乎也没什么可说的orz)

另外一个是mask这个变量,是在MAX操作时用来标记在哪个bottom blob 取到了最大值,反向传播时要用.



template <typename Dtype>
void EltwiseLayer<Dtype>::Reshape(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
  for (int i = 1; i < bottom.size(); ++i) {
    CHECK(bottom[i]->shape() == bottom[0]->shape());
  }
  //  check所有的bottom blob的shape都一样. 至少存在两个bottom blob
  top[0]->ReshapeLike(*bottom[0]);
  // If max operation, we will initialize the vector index part.
  if (this->layer_param_.eltwise_param().operation() ==
      EltwiseParameter_EltwiseOp_MAX && top.size() == 1) {
    max_idx_.Reshape(bottom[0]->shape());
  }
}

template <typename Dtype>
void EltwiseLayer<Dtype>::Forward_cpu(
    const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>& top) {
  int* mask = NULL;
  const Dtype* bottom_data_a = NULL;
  const Dtype* bottom_data_b = NULL;
  const int count = top[0]->count();
  Dtype* top_data = top[0]->mutable_cpu_data();
  switch (op_) {
  case EltwiseParameter_EltwiseOp_PROD:
    caffe_mul(count, bottom[0]->cpu_data(), bottom[1]->cpu_data(), top_data);
    for (int i = 2; i < bottom.size(); ++i) {
      caffe_mul(count, top_data, bottom[i]->cpu_data(), top_data);
    }
    //  先算前两个,然后把结果和后面的每一个blob(如果还有的话)做运算
    break;
  case EltwiseParameter_EltwiseOp_SUM:
    caffe_set(count, Dtype(0), top_data);
    // 初始化top data为0
    // TODO(shelhamer) does BLAS optimize to sum for coeff = 1?
    for (int i = 0; i < bottom.size(); ++i) {
      caffe_axpy(count, coeffs_[i], bottom[i]->cpu_data(), top_data);
    }
    break;
  //  mask干啥用的??? 
  //  forward应该用不到,是backward求梯度需要知道在哪个位置得到了最大值
  case EltwiseParameter_EltwiseOp_MAX:
    // Initialize
    mask = max_idx_.mutable_cpu_data();
    caffe_set(count, -1, mask);
    caffe_set(count, Dtype(-FLT_MAX), top_data);
    // bottom 0 & 1
    bottom_data_a = bottom[0]->cpu_data();
    bottom_data_b = bottom[1]->cpu_data();
    for (int idx = 0; idx < count; ++idx) {
      if (bottom_data_a[idx] > bottom_data_b[idx]) {
        top_data[idx] = bottom_data_a[idx];  // maxval
        mask[idx] = 0;  // maxid
      } else {
        top_data[idx] = bottom_data_b[idx];  // maxval
        mask[idx] = 1;  // maxid
      }
    }
    // bottom 2++
    for (int blob_idx = 2; blob_idx < bottom.size(); ++blob_idx) {
      bottom_data_b = bottom[blob_idx]->cpu_data();
      for (int idx = 0; idx < count; ++idx) {
        if (bottom_data_b[idx] > top_data[idx]) {
          top_data[idx] = bottom_data_b[idx];  // maxval
          mask[idx] = blob_idx;  // maxid
        }
      }
    }
    break;
  default:
    LOG(FATAL) << "Unknown elementwise operation.";
  }
}

```
