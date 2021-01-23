---
title: "caffe 源码学习笔记(6) reshape layer"
date: 2020-04-09T21:03:06+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/caffe-source-code-analysis-part6
categories:
- deep-learning

tags:

- caffe
---


## 背景　

最近在魔改 tensorRT 的caffe parser
之前caffe模型转到trt模型时，有一个修改是需要将reshape　layer的param末尾补1,比较繁琐，于是看了下caffe的reshape layer的实现．

## proto


```protobuf

message ReshapeParameter {
  // Specify the output dimensions. If some of the dimensions are set to 0,
  // the corresponding dimension from the bottom layer is used (unchanged).
  // Exactly one dimension may be set to -1, in which case its value is
  // inferred from the count of the bottom blob and the remaining dimensions.
  // For example, suppose we want to reshape a 2D blob "input" with shape 2 x 8:
  //
  //   layer {
  //     type: "Reshape" bottom: "input" top: "output"
  //     reshape_param { ... }
  //   }
  //
  // If "input" is 2D with shape 2 x 8, then the following reshape_param
  // specifications are all equivalent, producing a 3D blob "output" with shape
  // 2 x 2 x 4:
  //
  //   reshape_param { shape { dim:  2  dim: 2  dim:  4 } }
  //   reshape_param { shape { dim:  0  dim: 2  dim:  4 } }
  //   reshape_param { shape { dim:  0  dim: 2  dim: -1 } }
  //   reshape_param { shape { dim:  0  dim:-1  dim:  4 } }
  //
  optional BlobShape shape = 1;

  // axis and num_axes control the portion of the bottom blob's shape that are
  // replaced by (included in) the reshape. By default (axis == 0 and
  // num_axes == -1), the entire bottom blob shape is included in the reshape,
  // and hence the shape field must specify the entire output shape.
  //
  // axis may be non-zero to retain some portion of the beginning of the input
  // shape (and may be negative to index from the end; e.g., -1 to begin the
  // reshape after the last axis, including nothing in the reshape,
  // -2 to include only the last axis, etc.).
  //
  // For example, suppose "input" is a 2D blob with shape 2 x 8.
  // Then the following ReshapeLayer specifications are all equivalent,
  // producing a blob "output" with shape 2 x 2 x 4:
  //
  //   reshape_param { shape { dim: 2  dim: 2  dim: 4 } }
  //   reshape_param { shape { dim: 2  dim: 4 } axis:  1 }
  //   reshape_param { shape { dim: 2  dim: 4 } axis: -3 }
  //
  // num_axes specifies the extent of the reshape.
  // If num_axes >= 0 (and axis >= 0), the reshape will be performed only on
  // input axes in the range [axis, axis+num_axes].
  // num_axes may also be -1, the default, to include all remaining axes
  // (starting from axis).
  //
  // For example, suppose "input" is a 2D blob with shape 2 x 8.
  // Then the following ReshapeLayer specifications are equivalent,
  // producing a blob "output" with shape 1 x 2 x 8.
  //
  //   reshape_param { shape { dim:  1  dim: 2  dim:  8 } }
  //   reshape_param { shape { dim:  1  dim: 2  }  num_axes: 1 }
  //   reshape_param { shape { dim:  1  }  num_axes: 0 }
  //
  // On the other hand, these would produce output blob shape 2 x 1 x 8:
  //
  //   reshape_param { shape { dim: 2  dim: 1  dim: 8  }  }
  //   reshape_param { shape { dim: 1 }  axis: 1  num_axes: 0 }
  //
  optional int32 axis = 2 [default = 0];
  optional int32 num_axes = 3 [default = -1];
}

```

emmm,是不是稍微复杂了点．．　其实主要复杂在两个可选参数axis和num_axes上．　
如果不考虑这两个参数，那么　reshape的维度只有两点需要注意．一个是0表示该维度不变，一个是-1表示该维度是需要推断出来．

> 0 means “copy the respective dimension of the bottom layer”. That is, if the bottom has 2 as its 1st dimension, the top will have 2 as its 1st dimension as well, given dim: 0 as the 1st target dimension.


>-1 stands for “infer this from the other dimensions”. This behavior is similar to that of -1 in numpy’s or [] for MATLAB’s reshape: this dimension is calculated to keep the overall element count the same as in the bottom layer. At most one -1 can be used in a reshape operation.

然后axis和num_axes两个参数可以一起看．

其实就是表示只对输入维度的[axis, axis+num_axes]做reshape,其他维护维持现状．

不过axis的使用例子写错了，所以弄得有些费解,还是看了代码才弄清楚．给caffe提了个pr [fix an error of axis parameter in the example of ReshapeParameter #6936](https://github.com/BVLC/caffe/pull/6936) 能不能merge随缘吧2333

然后还有两个case，其一是num_axes的默认情况，表示要处理"all remaining axes"
另外一个是axis为负数，此时不使用num_axes　参数


值得一提的是
> specifying reshape_param { shape { dim: 0 dim: -1 } } makes the layer behave in exactly the same way as the Flatten layer.



## c++实现

先看 LayerSetUp. 我们似乎很少关注layer的这部分．．原因是大部分layer这部分其实都没什么好关注的

```c++

template <typename Dtype>
void ReshapeLayer<Dtype>::LayerSetUp(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  CHECK_NE(top[0], bottom[0]) << this->type() << " Layer does not "
      "allow in-place computation.";
  inferred_axis_ = -1;
  copy_axes_.clear();
  const BlobShape& top_blob_shape = this->layer_param_.reshape_param().shape();
  const int top_num_axes = top_blob_shape.dim_size();
  constant_count_ = 1;
  for (int i = 0; i < top_num_axes; ++i) {
    const int top_dim = top_blob_shape.dim(i);
    if (top_dim == 0) {
      copy_axes_.push_back(i);
    } else if (top_dim == -1) {
      CHECK_EQ(inferred_axis_, -1) << "new shape contains multiple "
          << "-1 dims; at most a single (1) value of -1 may be specified";
      inferred_axis_ = i;
    } else {
      constant_count_ *= top_dim;
    }
  }
}

```

特殊处理了dim为0和-1的情况，然后把需要变换的维度count放在constant_count_，盲猜是之后做推断用．



接下来我们看下Reshape

```c++
template <typename Dtype>
void ReshapeLayer<Dtype>::Reshape(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {
  const int input_start_axis = this->layer_param_.reshape_param().axis();
  const int start_axis = (input_start_axis >= 0) ? input_start_axis :
      bottom[0]->num_axes() + input_start_axis + 1;
  CHECK_GE(start_axis, 0) << "axis " << input_start_axis << " out of range";
  CHECK_LE(start_axis, bottom[0]->num_axes()) << "axis " << input_start_axis
      << " out of range for " << bottom[0]->num_axes() << "-D input blob";
  const int num_axes = this->layer_param_.reshape_param().num_axes();
  CHECK_GE(num_axes, -1) << "num_axes must be >= 0, or -1 for all";
  const int end_axis =
      (num_axes == -1) ? bottom[0]->num_axes() : (start_axis + num_axes);
  CHECK_LE(end_axis, bottom[0]->num_axes())
      << "end_axis = axis + num_axes is out of range";
  const int num_axes_replaced = end_axis - start_axis;
  const int num_axes_retained = bottom[0]->num_axes() - num_axes_replaced;
  const BlobShape& top_blob_shape = this->layer_param_.reshape_param().shape();
  const int num_new_axes = top_blob_shape.dim_size();
  vector<int> top_shape(num_axes_retained + num_new_axes);
  int top_shape_index = 0;
  for (int i = 0; i < start_axis; ++i) {
    top_shape[top_shape_index++] = bottom[0]->shape(i);
  }
  for (int i = 0; i < num_new_axes; ++i) {
    top_shape[top_shape_index++] = top_blob_shape.dim(i);
  }
  for (int i = end_axis; i < bottom[0]->num_axes(); ++i) {
    top_shape[top_shape_index++] = bottom[0]->shape(i);
  }
  CHECK_EQ(top_shape_index, top_shape.size());
  for (int i = 0; i < copy_axes_.size(); ++i) {
    const int copy_axis_index = copy_axes_[i];
    CHECK_GT(bottom[0]->num_axes(), start_axis + copy_axis_index)
        << "new shape contains a 0, but there was no corresponding bottom axis "
        << "to copy";
    top_shape[start_axis + copy_axis_index] =
        bottom[0]->shape(start_axis + copy_axis_index);
  }
  if (inferred_axis_ >= 0) {
    // A -1 dim was specified; infer the correct dimension by computing the
    // product of the other dimensions.
    int explicit_count = constant_count_;
    explicit_count *= bottom[0]->count(0, start_axis);
    explicit_count *= bottom[0]->count(end_axis);
    for (int i = 0; i < copy_axes_.size(); ++i) {
      const int copy_axis_index = copy_axes_[i];
      explicit_count *= top_shape[start_axis + copy_axis_index];
    }
    CHECK_EQ(0, bottom[0]->count() % explicit_count) << "bottom count ("
        << bottom[0]->count() << ") must be divisible by the product of "
        << "the specified dimensions (" << explicit_count << ")";
    const int inferred_dim = bottom[0]->count() / explicit_count;
    top_shape[start_axis + inferred_axis_] = inferred_dim;
  }
  top[0]->Reshape(top_shape);
  CHECK_EQ(top[0]->count(), bottom[0]->count())
      << "output count must match input count";
  top[0]->ShareData(*bottom[0]);
  top[0]->ShareDiff(*bottom[0]);
}

INSTANTIATE_CLASS(ReshapeLayer);
REGISTER_LAYER_CLASS(Reshape);

}  // namespace caffe

```

代码似乎有些长，实际上很简单．后半部分是推断维度的，前半部分也很直观，就是做了比较多的check．

然后Reshape Layer是没有Forward函数的，因为没有做任何计算，只是改变了blob的reshape,也不存在数据的拷贝．






