---
title: "记一次faster-rcnn debug记录"
date: 2019-12-13T16:32:14+08:00
draft: false
author: "111qqz"
type: post
url: /2019/12/debug-faster-rcnn-once-again
categories:
- deep-learning

tags:

- faster-rcnn
---

## 问题描述
**一年debug 三次faster rcnn,每次都有新感觉（不**

接到一个bug report,现象为某人脸模型，转换成trt模型，当batch size为1时结果完全正确，但是batch size大于1时结果不正确。
具体的现象是，如果跑多张不同的图，只有第一张图有结果，后面的图都没有结果。
如果跑的图中有相同的，那么和第一张相同的图都会有结果，其余的图没有结果。

``` protobuf
layer {
  name: "POD_proposal"
  type: "RPRoIFused"
  bottom: "Reshape_105"
  bottom: "Conv_100"
  bottom: "Add_95"
  bottom: "im_info"
  top: "rois"
  top: "tmp_pooling"
  rpn_proposal_param{
    feat_stride: 16
    anchor_ratios: 1
    anchor_scales: 1
    anchor_scales: 2
    anchor_scales: 4
    anchor_scales: 8
    anchor_scales: 16
    anchor_scales: 32
    test_desc_param {
        rpn_pre_nms_top_n: 2000
        rpn_post_nms_top_n: 50
        rpn_min_size: 16
        rpn_nms_thresh: 0.7
    }
  }

  roi_pooling_param{
    pooled_h: 7
    pooled_w: 7
    spatial_scale: 0.0625

  }
}


```

特别地，proposal layer中 rpn_post_nms_top_n的参数值如果使用默认的300,那么结果都是对的。把这个值改小（只要小于300)，结果就像上面所述。




## debug 经过

首先根据rpn_post_nms_top_n的值一修改，结果就是错的来看，怀疑是哪里参数写死了。
然而很快就排除了这个问题。因为faster rcnn的模型已经在另一个产品中经过长期验证了。
而且proposal layer是tensorrt自己实现的，有bug早就有人发现了。

然后根据batch size为1时结果正确，但是batch size大于1时结果错误来看，怀疑是proposal layer前面rpn做的softmax的维度 不太对。
因为rpn前景和背景的得分有两种不同的排列方式
可能是 
```
+ + + + + +
- - - - - -
```
也可能是
```
+ - + - + -
+ - + - + -
```

其中‘+’代表前景，‘-’代表背景。

前者的排列方式在softmax前的维度应该是  N×2×A×H×W

后者的排列方式在softmax前的维度应该是  N×A×2×H×W

其中N为batch size,A为anchor的个数。


排查发现pytorch模型的输出是后者的排列方式，而tensorrt proposal layer期望的排列方式是前者，也就是**N×2×A×H×W**


所以在做softmax之前要先permute 一下

```protobuf

layer {
  name: "tmp_add_for_continue"
  type: "Permute"
  bottom:"Reshape_102"
  top:"tmp_add_for_continue"
  permute_param {
    order: 0
    order: 2
    order: 1
    order: 3
  }
}

layer {
  name: "Softmax_103"
  type: "Softmax"
  bottom: "tmp_add_for_continue"
  top: "Softmax_103"
  softmax_param {
    axis:1
  }
}

```

但是。。这里，之前已经做了啊。。。
就是说其实已经考虑到前景背景排列不一致的问题了。。。

然后根据一个batch中，和第一张图片相同的图片也是有结果的。。
怀疑是nms或者哪里做sort的时候，交换没写对。。

按照之前debug faster rcnn 的经验，看一下roi的输出吧。
结果发现把同一张图，分别放在一个batch的不同位置，roi的输出是一致的。
。。。这说明proposal 似乎是没问题的？

尝试将roi_align换成roi_pooling... 发现结果似乎也是没问题的。。。

所以是roi_align 的实现有问题？

于是看了下caffe cuda的实现
发现里面有个叫num_roi_per_image的东西。。。

？？？？？


```c++
template <typename T>
__global__ void RoIAlignForwardKernel(
    const int nthreads,
    const T* bottom_data,
    const T spatial_scale,
    const bool position_sensitive,
    const int channels,
    const int height,
    const int width,
    const int pooled_height,
    const int pooled_width,
    const int sampling_ratio,
    const int num_roi_per_image,
    const T* bottom_rois,
    T* top_data) {
  CUDA_KERNEL_LOOP(index, nthreads) {
    // (n, c, ph, pw) is an element in the pooled output
    int pw = index % pooled_width;
    int ph = (index / pooled_width) % pooled_height;
    int c = (index / pooled_width / pooled_height) % channels;
    int n = index / pooled_width / pooled_height / channels;

//    const T* offset_bottom_rois = bottom_rois + n * 5;
    const T* offset_bottom_rois = bottom_rois + n * 4;
    int roi_batch_ind = n / num_roi_per_image;
```

**int roi_batch_ind = n / num_roi_per_image;**

这什么鬼了。。
于是跑去看caffe.proto。。。。
果然。。。

```protobuf
message RoIAlignParameter {
  optional uint32 pooled_h = 1 [default = 0];
  optional uint32 pooled_w = 2 [default = 0];
  optional float spatial_scale = 3 [default = 1];
  optional int32 sample_ratio = 4 [default = -1];
  optional bool position_sensitive = 5 [default = false];
  optional uint32 num_roi_per_image = 6 [default = 300];
}
```

这个num_roi_per_image有个默认值。。。跪了。。

所以当修改 rpn_post_nms_top_n 的时候，由于这个默认值一直是300
所以就会把后面若干图片的roi都当成第一张图的roi来处理。。


## 经验总结

caffe的源码还是要看的。。。


希望2020年可以看完orz






