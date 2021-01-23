---
title: "caffe 源码学习笔记(3) Net"
date: 2020-01-12T19:18:15+08:00
draft: false
author: "111qqz"
type: post
url: /2020/01/caffe-source-code-analysis-part3
categories:
- deep-learning


tags:

- caffe

---

## Net 基本介绍

网络通过组成和自微分共同定义一个函数及其梯度。

网络是一些Layer组成的DAG,也就是有向无环图，在caffe中通常由prototxt定义．

比如

```protobuf
name: "LogReg"
layer {
  name: "mnist"
  type: "Data"
  top: "data"
  top: "label"
  data_param {
    source: "input_leveldb"
    batch_size: 64
  }
}
layer {
  name: "ip"
  type: "InnerProduct"
  bottom: "data"
  top: "ip"
  inner_product_param {
    num_output: 2
  }
}
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  bottom: "ip"
  bottom: "label"
  top: "loss"
}
```


定义了


![网络结构](https://caffe.berkeleyvision.org/tutorial/fig/logreg.jpg)


值得强调的是，**caffe中网络结构的定义与实现是无关的**,这点比pytorch之类的深度学习框架不知高到哪里去了，也是caffe作为部署端的事实标准的重要原因．

## Net 实现细节

我们先看下NetParameter的proto

```proto

    message NetParameter {
      optional string name = 1; // consider giving the network a name
      // DEPRECATED. See InputParameter. The input blobs to the network.
      repeated string input = 3;
      // DEPRECATED. See InputParameter. The shape of the input blobs.
      repeated BlobShape input_shape = 8;

      // 4D input dimensions -- deprecated.  Use "input_shape" instead.
      // If specified, for each input blob there should be four
      // values specifying the num, channels, height and width of the input blob.
      // Thus, there should be a total of (4 * #input) numbers.
      repeated int32 input_dim = 4;

      // Whether the network will force every layer to carry out backward operation.
      // If set False, then whether to carry out backward is determined
      // automatically according to the net structure and learning rates.
      optional bool force_backward = 5 [default = false];
      // The current "state" of the network, including the phase, level, and stage.
      // Some layers may be included/excluded depending on this state and the states
      // specified in the layers' include and exclude fields.
      optional NetState state = 6;

      // Print debugging information about results while running Net::Forward,
      // Net::Backward, and Net::Update.
      optional bool debug_info = 7 [default = false];

      // The layers that make up the net.  Each of their configurations, including
      // connectivity and behavior, is specified as a LayerParameter.
      repeated LayerParameter layer = 100;  // ID 100 so layers are printed last.

      // DEPRECATED: use 'layer' instead.
      repeated V1LayerParameter layers = 2;
    }

```

都很好理解，除了NetState不知道是个什么东西．．．

继续往下看，看到和NetState有关的两个proto定义如下:

```proto

message NetState {
  optional Phase phase = 1 [default = TEST];
  optional int32 level = 2 [default = 0];
  repeated string stage = 3;
}

message NetStateRule {
  // Set phase to require the NetState have a particular phase (TRAIN or TEST)
  // to meet this rule.
  optional Phase phase = 1;

  // Set the minimum and/or maximum levels in which the layer should be used.
  // Leave undefined to meet the rule regardless of level.
  optional int32 min_level = 2;
  optional int32 max_level = 3;

  // Customizable sets of stages to include or exclude.
  // The net must have ALL of the specified stages and NONE of the specified
  // "not_stage"s to meet the rule.
  // (Use multiple NetStateRules to specify conjunctions of stages.)
  repeated string stage = 4;
  repeated string not_stage = 5;
}
```

参考　[
[Discussion] How to specify all-in-one networks #3864](https://github.com/BVLC/caffe/issues/3864) 
得知，这些参数的主要目的是为了解决部署和训练时，需要多个prototxt的问题．　

实际上，部署和训练的protoxt可能大部分都是一样的，只不过是输入，输出以及少部分layer有些差别．如果分为多个文件，会带来的问题就是，如果要修改一些共同的layer,就需要修改两次．

于是可以通过这些参数来控制网络结构，使得部署和训练使用相同的prototxt
，得到一个"all-in-one network"


接下来值得看的是网络的构建部分．

对于一个Net，会顺序构建每个Layer

对于每个Layer,大致分为AppendTop,AppendBottom，AppendParam　三部分．我们重点关注前两部分．


```c++

// Helper for Net::Init: add a new bottom blob to the net.
template <typename Dtype>
int Net<Dtype>::AppendBottom(const NetParameter& param, const int layer_id,
    const int bottom_id, set<string>* available_blobs,
    map<string, int>* blob_name_to_idx) {
  const LayerParameter& layer_param = param.layer(layer_id);
  const string& blob_name = layer_param.bottom(bottom_id);
  if (available_blobs->find(blob_name) == available_blobs->end()) {
    LOG(FATAL) << "Unknown bottom blob '" << blob_name << "' (layer '"
               << layer_param.name() << "', bottom index " << bottom_id << ")";
  }
  const int blob_id = (*blob_name_to_idx)[blob_name];
  LOG_IF(INFO, Caffe::root_solver())
      << layer_names_[layer_id] << " <- " << blob_name;
  bottom_vecs_[layer_id].push_back(blobs_[blob_id].get());
  bottom_id_vecs_[layer_id].push_back(blob_id);
  // 　？？？　怎么就erase了，一个top后面可以接多个layer的啊
  available_blobs->erase(blob_name);
  bool need_backward = blob_need_backward_[blob_id];
  // Check if the backpropagation on bottom_id should be skipped
  if (layer_param.propagate_down_size() > 0) {
    need_backward = layer_param.propagate_down(bottom_id);
  }
  bottom_need_backward_[layer_id].push_back(need_backward);
  return blob_id;
}

```

```c++

// Helper for Net::Init: add a new top blob to the net.
template <typename Dtype>
void Net<Dtype>::AppendTop(const NetParameter& param, const int layer_id,
                           const int top_id, set<string>* available_blobs,
                           map<string, int>* blob_name_to_idx) {
  shared_ptr<LayerParameter> layer_param(
      new LayerParameter(param.layer(layer_id)));
  const string& blob_name = (layer_param->top_size() > top_id) ?
      layer_param->top(top_id) : "(automatic)";
  // Check if we are doing in-place computation
  if (blob_name_to_idx && layer_param->bottom_size() > top_id &&
      blob_name == layer_param->bottom(top_id)) {
    // In-place computation
    LOG_IF(INFO, Caffe::root_solver())
        << layer_param->name() << " -> " << blob_name << " (in-place)";
    top_vecs_[layer_id].push_back(blobs_[(*blob_name_to_idx)[blob_name]].get());
    top_id_vecs_[layer_id].push_back((*blob_name_to_idx)[blob_name]);
  } else if (blob_name_to_idx &&
             blob_name_to_idx->find(blob_name) != blob_name_to_idx->end()) {
    // If we are not doing in-place computation but have duplicated blobs,
    // raise an error.
    LOG(FATAL) << "Top blob '" << blob_name
               << "' produced by multiple sources.";
  } else {
    // Normal output.
    if (Caffe::root_solver()) {
      LOG(INFO) << layer_param->name() << " -> " << blob_name;
    }
    shared_ptr<Blob<Dtype> > blob_pointer(new Blob<Dtype>());
    const int blob_id = blobs_.size();
    // 　先取blob_id，再push_back 说明blob_id是从0开始递增的整数．
    //  blob_id都是在appendTop时定义的
    blobs_.push_back(blob_pointer);
    blob_names_.push_back(blob_name);
    blob_need_backward_.push_back(false);
    if (blob_name_to_idx) { (*blob_name_to_idx)[blob_name] = blob_id; }
    top_id_vecs_[layer_id].push_back(blob_id);
    top_vecs_[layer_id].push_back(blob_pointer.get());
  }
  // 　维护一个出现过的top　blob集合，目的是判断后面所接layer的bottom blob名称的合法性
  // 　这里要判断　available_blobs　是否为NULL是因为，可能构造匿名的top blob,此时available_blobs
  //  和　blob_name_to_idx　都会传NULL 值
  if (available_blobs) { available_blobs->insert(blob_name); }
}

```

代码比较好懂，解析部分见注释...
唯一值得注意的地方是available_blobs这部分的维护．在AppendBottom中

```c++

  // 　？？？　怎么就erase了，一个top后面可以接多个layer的啊
  available_blobs->erase(blob_name);

```

每次处理完一个bottom就从available_blobs 去掉．

然而，一个top blob明明是可以输入给多个layer的．．．
？？？？？　不明白

查阅资料看到　[What does InsertSplit() / SplitLayer do? #767](https://github.com/BVLC/caffe/issues/767)

原来

>   // Create split layer for any input blobs used by other layers as bottom
>     // blobs more than once.

对于被多个layer用作bottom的top blob,做了分身...



![分身](https://images2017.cnblogs.com/blog/861394/201708/861394-20170810170352980-1492701664.png)


可以参考[Net的网络层的构建(源码分析)](https://www.cnblogs.com/liuzhongfeng/p/7340273.html)




