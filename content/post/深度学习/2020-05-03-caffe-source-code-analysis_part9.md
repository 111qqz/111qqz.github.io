---
title: "caffe 源码学习笔记(9) reduce layer"
date: 2020-05-03T15:16:53+08:00
draft: false
author: "111qqz"
type: post
url: /2020/05/caffe-source-code-analysis-part9
categories:
- deep-learning

tags:

- caffe 

---


## 背景


其实没什么背景,继续啃caffe代码而已2333

reduce layer其实就是做reduce操作,把一个任意shape的blob通过某种运算变成一个scalar.

caffe目前支持求和(SUM),绝对值的和(ASUM),平方和(SUMSQ),以及对得到的scalar的总数求平均的求和(MEAN).

说句题外话,TensorRT支持的操作是求和,求积,max,min和ave. 还是有一些gap的

## proto 

先看proto 


```protobuf

message ReductionParameter {
  enum ReductionOp {
    SUM = 1;
    ASUM = 2;
    SUMSQ = 3;
    MEAN = 4;
  }

  optional ReductionOp operation = 1 [default = SUM]; // reduction operation

  // The first axis to reduce to a scalar -- may be negative to index from the
  // end (e.g., -1 for the last axis).
  // (Currently, only reduction along ALL "tail" axes is supported; reduction
  // of axis M through N, where N < num_axes - 1, is unsupported.)
  // Suppose we have an n-axis bottom Blob with shape:
  //     (d0, d1, d2, ..., d(m-1), dm, d(m+1), ..., d(n-1)).
  // If axis == m, the output Blob will have shape
  //     (d0, d1, d2, ..., d(m-1)),
  // and the ReductionOp operation is performed (d0 * d1 * d2 * ... * d(m-1))
  // times, each including (dm * d(m+1) * ... * d(n-1)) individual data.
  // If axis == 0 (the default), the output Blob always has the empty shape
  // (count 1), performing reduction across the entire input --
  // often useful for creating new loss functions.
  optional int32 axis = 2 [default = 0];

  optional float coeff = 3 [default = 1.0]; // coefficient for output
}

```

operation不用说,表示要进行哪种reduce操作.
coeff也比较简单,就是最后结果中每个元素都可以乘一个额外的系数,默认是1.

axis的含义是,从axis这个维度开始做reduce. 

比如blob的shape是(a,b,c,axis,d,e)

那么就需要对  (axis,d,e)这部分做a\*b\*c次reduce,得到 a\*b\*c个标量.

**需要注意,目前只支持从某个维度一直到最后的维度都去做reduce,不支持中间的几个维度去做reduce**



## c++ 代码

头文件中有两个成员变量num_,dim_值得一说

```c++

template <typename Dtype>
class ReductionLayer : public Layer<Dtype> {
 public:
//    ...省略无关部分

  /// @brief the reduction operation performed by the layer
  ReductionParameter_ReductionOp op_;
  /// @brief a scalar coefficient applied to all outputs
  Dtype coeff_;
  /// @brief the index of the first input axis to reduce
  int axis_;
  /// @brief the number of reductions performed
  int num_;
  /// @brief the input size of each reduction
  int dim_;
  /// @brief a helper Blob used for summation (op_ == SUM)
  Blob<Dtype> sum_multiplier_;
};


num_表示的是要做reduce操作的次数
dim_表示的是每次reduce的维度部分的count

Reshape部分,主要就是计算了几个成员变量 num_,dim_,coeff_
```c++

template <typename Dtype>
void ReductionLayer<Dtype>::Reshape(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
  axis_ = bottom[0]->CanonicalAxisIndex(
      this->layer_param_.reduction_param().axis());
  // In the output, we'll keep all axes up to the reduction axis, but
  // throw away any after that.
  // Note: currently reducing along non-tail axes is not supported; otherwise,
  // we'd need to also copy any axes following an "end_axis".
  vector<int> top_shape(bottom[0]->shape().begin(),
                        bottom[0]->shape().begin() + axis_);
  top[0]->Reshape(top_shape);
  //  count都是左闭又开,一个参数就是到末尾
  num_ = bottom[0]->count(0, axis_);
  //  num_表示的是要做reduce操作的次数
  //  range [0,axis_)
  dim_ = bottom[0]->count(axis_);
  //  dim_表示的是reduce操作部分的count
  //  range [axis_,num_axes())
  CHECK_EQ(num_, top[0]->count());
  if (op_ == ReductionParameter_ReductionOp_SUM ||
      op_ == ReductionParameter_ReductionOp_MEAN) {
    vector<int> sum_mult_shape(1, dim_);
    // sum_mult_shape[0] = dim_
    sum_multiplier_.Reshape(sum_mult_shape);

    caffe_set(dim_, Dtype(1), sum_multiplier_.mutable_cpu_data());
    // sum_multiplier_是dim_长度的vector,值都为1
  }
  coeff_ = this->layer_param().reduction_param().coeff();
  if (op_ == ReductionParameter_ReductionOp_MEAN) {
    coeff_ /= dim_;
  }
}

```
注意到求和的计算是通过构造了一个dim_长度的都是为1的向量来和bottom做点积实现的.

```c++

template <typename Dtype>
void ReductionLayer<Dtype>::Forward_cpu(
    const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>& top) {
  const Dtype* bottom_data = bottom[0]->cpu_data();
  const Dtype* mult_data = NULL;
  if (sum_multiplier_.count() > 0) {
    mult_data = sum_multiplier_.cpu_data();
  }
  Dtype* top_data = top[0]->mutable_cpu_data();
  // 得到num_个结果
  for (int i = 0; i < num_; ++i) {
    switch (op_) {
    case ReductionParameter_ReductionOp_SUM:
    case ReductionParameter_ReductionOp_MEAN:
      *top_data = caffe_cpu_dot(dim_, mult_data, bottom_data);
      break;
    case ReductionParameter_ReductionOp_ASUM:
      *top_data = caffe_cpu_asum(dim_, bottom_data);
      break;
    case ReductionParameter_ReductionOp_SUMSQ:
      *top_data = caffe_cpu_dot(dim_, bottom_data, bottom_data);
      break;
    default:
      LOG(FATAL) << "Unknown reduction op: "
          << ReductionParameter_ReductionOp_Name(op_);
    }
    bottom_data += dim_;
    ++top_data;
  }
  //  coeff_是每一个位置的系数,默认为1
  //  此时才真的把系数放在每一个元素上
  if (coeff_ != Dtype(1)) {
    // Reset the top_data pointer.
    top_data = top[0]->mutable_cpu_data();
    caffe_scal(num_, coeff_, top_data);
  }
}
```


