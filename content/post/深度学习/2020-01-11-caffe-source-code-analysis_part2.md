---
title: "caffe 源码学习笔记(2) Layer"
date: 2020-01-11T17:47:05+08:00
draft: false
author: "111qqz"
type: post
url: /2020/01/caffe-source-code-analysis-part2
categories:
- deep-learning

tags:

- caffe

---

## layer 整体介绍

layer是模型计算的基本单元
类似于pytorch或者其他深度学习框架的op
layer中的数据流向为,输入若干个blob，称之为"bottom blob",然后经过layer的计算，输出若干个blob,称之为"top blob"

也就是数据是从“bottom”流向“top”

![layer数据流向](https://caffe.berkeleyvision.org/tutorial/fig/layer.jpg)


layer通常会进行两种计算，forward和backward

forward是指，根据bottom blob计算得到top blob
backward是指，根据top blob的结果和参数值计算得到的gradient,回传给前面的layer.


## layer 实现细节


layer作为一个base class,实现了所有layer都需要的common的部分。
比如:

```c++
  /**
   * @brief Implements common layer setup functionality.
   *
   * @param bottom the preshaped input blobs
   * @param top
   *     the allocated but unshaped output blobs, to be shaped by Reshape
   *
   * Checks that the number of bottom and top blobs is correct.
   * Calls LayerSetUp to do special layer setup for individual layer types,
   * followed by Reshape to set up sizes of top blobs and internal buffers.
   * Sets up the loss weight multiplier blobs for any non-zero loss weights.
   * This method may not be overridden.
   */
  void SetUp(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
    CheckBlobCounts(bottom, top);
    LayerSetUp(bottom, top);
    Reshape(bottom, top);
    SetLossWeights(top);
  }
  ```
  SetUp可以理解成layer的初始化函数。


这部分代码比较容易看懂，可以说的不多。
值得注意的是，下面这段代码:

```c++
 /** @brief Using the CPU device, compute the layer output. */
  virtual void Forward_cpu(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) = 0;
  /**
   * @brief Using the GPU device, compute the layer output.
   *        Fall back to Forward_cpu() if unavailable.
   */
  virtual void Forward_gpu(const vector<Blob<Dtype>*>& bottom,
      const vector<Blob<Dtype>*>& top) {
    // LOG(WARNING) << "Using CPU code as backup.";
    return Forward_cpu(bottom, top);
  }

```
只有cpu上的forward(backward同理)被定义成纯虚函数，而base class上gpu上的forward被定义调用基类的forward_cpu

这样做使得每个layer必须定义自己的Forward_cpu函数，同时使得某个layer没有自己的Forward_gpu函数时，会fall back到相应的cpu版本。

## layer对blob的限制

2020.05.03补充:

看了一些layer的具体实现后,我们发现有一个信息我们是没办法通过proto看出来的. 就是一个layer的输出和输出的blob的个数.

caffe的做法是在layer的基类中定义**ExactNumBottomBlobs()**, **MinTopBlobs()** 等. 可以限制bottom blob和top blob的范围或者具体的值. 也可以通过 **EqualNumBottomTopBlobs()** 来控制bottom和top blob的个数一致.

```c++
  /**
   * @brief Returns the exact number of bottom blobs required by the layer,
   *        or -1 if no exact number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some exact number of bottom blobs.
   */
  virtual inline int ExactNumBottomBlobs() const { return -1; }
  /**
   * @brief Returns the minimum number of bottom blobs required by the layer,
   *        or -1 if no minimum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some minimum number of bottom blobs.
   */
  virtual inline int MinBottomBlobs() const { return -1; }
  /**
   * @brief Returns the maximum number of bottom blobs required by the layer,
   *        or -1 if no maximum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some maximum number of bottom blobs.
   */
  virtual inline int MaxBottomBlobs() const { return -1; }
  /**
   * @brief Returns the exact number of top blobs required by the layer,
   *        or -1 if no exact number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some exact number of top blobs.
   */
  virtual inline int ExactNumTopBlobs() const { return -1; }
  /**
   * @brief Returns the minimum number of top blobs required by the layer,
   *        or -1 if no minimum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some minimum number of top blobs.
   */
  virtual inline int MinTopBlobs() const { return -1; }
  /**
   * @brief Returns the maximum number of top blobs required by the layer,
   *        or -1 if no maximum number is required.
   *
   * This method should be overridden to return a non-negative value if your
   * layer expects some maximum number of top blobs.
   */
  virtual inline int MaxTopBlobs() const { return -1; }
  /**
   * @brief Returns true if the layer requires an equal number of bottom and
   *        top blobs.
   *
   * This method should be overridden to return true if your layer expects an
   * equal number of bottom and top blobs.
   */
  virtual inline bool EqualNumBottomTopBlobs() const { return false; }

  ```

  然后具体的layer再override掉需要限制的部分.

  
  然后在layer SetUp的时候,会去 check这些blob的个数


```c++


/**
   * Called by the parent Layer's SetUp to check that the number of bottom
   * and top Blobs provided as input match the expected numbers specified by
   * the {ExactNum,Min,Max}{Bottom,Top}Blobs() functions.
   */
  virtual void CheckBlobCounts(const vector<Blob<Dtype>*>& bottom,
                               const vector<Blob<Dtype>*>& top) {
    if (ExactNumBottomBlobs() >= 0) {
      CHECK_EQ(ExactNumBottomBlobs(), bottom.size())
          << type() << " Layer takes " << ExactNumBottomBlobs()
          << " bottom blob(s) as input.";
    }
    if (MinBottomBlobs() >= 0) {
      CHECK_LE(MinBottomBlobs(), bottom.size())
          << type() << " Layer takes at least " << MinBottomBlobs()
          << " bottom blob(s) as input.";
    }
    if (MaxBottomBlobs() >= 0) {
      CHECK_GE(MaxBottomBlobs(), bottom.size())
          << type() << " Layer takes at most " << MaxBottomBlobs()
          << " bottom blob(s) as input.";
    }
    if (ExactNumTopBlobs() >= 0) {
      CHECK_EQ(ExactNumTopBlobs(), top.size())
          << type() << " Layer produces " << ExactNumTopBlobs()
          << " top blob(s) as output.";
    }
    if (MinTopBlobs() >= 0) {
      CHECK_LE(MinTopBlobs(), top.size())
          << type() << " Layer produces at least " << MinTopBlobs()
          << " top blob(s) as output.";
    }
    if (MaxTopBlobs() >= 0) {
      CHECK_GE(MaxTopBlobs(), top.size())
          << type() << " Layer produces at most " << MaxTopBlobs()
          << " top blob(s) as output.";
    }
    if (EqualNumBottomTopBlobs()) {
      CHECK_EQ(bottom.size(), top.size())
          << type() << " Layer produces one top blob as output for each "
          << "bottom blob input.";
    }
  }

```


然后还有个问题,就是如果有多个blob,怎么规定顺序呢? 目前来看,是没有什么办法强制规定的,这部分主要取决于layer实现作者的意愿. 好在这种不同blob的含义不同的layer不是特别多..



## layer factory 介绍

~~等待补充~~

layor factory 可以用来registry layers.

```c++
  typedef shared_ptr<Layer<Dtype> > (*Creator)(const LayerParameter&);
  typedef std::map<string, Creator> CreatorRegistry;
```

我们可以看到LayerRegistry class template 定义了两个类型
一个是函数指针Creator,类型为　
```c++
 shared_ptr<Layer<Dtype> >　(const LayerParameter&）;
```
另一个是CreatorRegistry，建立起了某种映射。

下面我们看到成员函数Registry

```c++
  static CreatorRegistry& Registry() {
    static CreatorRegistry* g_registry_ = new CreatorRegistry();
    return *g_registry_;
  }

```
这里用到了单例模式(Singleton),使得整个class只有唯一的一个CreatorRegistry实例

单例模式可以参考[这里](https://en.wikibooks.org/wiki/C%2B%2B_Programming/Code/Design_Patterns#Singleton)


接下来我们看到成员函数AddCreator

```c++
  // Adds a creator.
  static void AddCreator(const string& type, Creator creator) {
    CreatorRegistry& registry = Registry();
    // layer type需要在 CreatorRegistry 表中唯一
    CHECK_EQ(registry.count(type), 0)
        << "Layer type " << type << " already registered.";
    registry[type] = creator;
  }
```

此时我们知道，CreatorRegistry的这个table是用来存layer type到相应layer的creator的映射关系的。


接下来我们看到成员函数CreateLayer，见注释

```c++
  // Get a layer using a LayerParameter.
  static shared_ptr<Layer<Dtype> > CreateLayer(const LayerParameter& param) {
    if (Caffe::root_solver()) {
      LOG(INFO) << "Creating layer " << param.name();
    }
    const string& type = param.type();
    CreatorRegistry& registry = Registry();
    CHECK_EQ(registry.count(type), 1) << "Unknown layer type: " << type
        << " (known types: " << LayerTypeListString() << ")";
    // registry[type]返回一个creator
    //  creator是第一个　函数指针，类型为　shared_ptr<Layer<Dtype> >　(const LayerParameter&）
    // 因此最终的返回值类型为shared_ptr<Layer<Dtype> >,也就是layer的指针。
    return registry[type](param);
  }

```

接下来是成员函数LayerTypeList,作用是列出目前注册过的所有layer type的名称。

```c++
  static vector<string> LayerTypeList() {
    CreatorRegistry& registry = Registry();
    vector<string> layer_types;
    // 　在模板实例化之前，编译器无法知道scope operator（::）后是"static members“还是”type members“
    //  默认情况下，scope operator后接的是static merbers
    // 　所以这里需要使用typename　关键词，显式告诉编译器，后面是一个type name
    for (typename CreatorRegistry::iterator iter = registry.begin();
         iter != registry.end(); ++iter) {
      layer_types.push_back(iter->first);
    }
    return layer_types;
  }

```
值得注意的是此处typename　关键词的使用，原因见注释。


最后可以看到两个宏定义


```c++

#define REGISTER_LAYER_CREATOR(type, creator)                                  \
  static LayerRegisterer<float> g_creator_f_##type(#type, creator<float>);     \
  static LayerRegisterer<double> g_creator_d_##type(#type, creator<double>)    \

#define REGISTER_LAYER_CLASS(type)                                             \
  template <typename Dtype>                                                    \
  shared_ptr<Layer<Dtype> > Creator_##type##Layer(const LayerParameter& param) \
  {                                                                            \
    return shared_ptr<Layer<Dtype> >(new type##Layer<Dtype>(param));           \
  }                                                                            \
  REGISTER_LAYER_CREATOR(type, Creator_##type##Layer)

```


对应了两种register a layer 的方式

一种是可以直接通过layer的constructor来创建，另一种是通过一个其他的creator函数来创建。

从这两个宏定义中可以看出，**REGISTER_LAYER_CREATOR**　是真正做工作的部分。　**REGISTER_LAYER_CLASS**　可以看做没有提供creator的特殊情况，此时先通过layer的constructor来定义一个creator,再去调用**REGISTER_LAYER_CREATOR**


可能值得一提的是宏定义中## 符号，称为 macro operator
作用是将两个token，合成一个token
```
<token> ## <token>
```

我们观察layer_factory.cpp中，发现使用其他creator来创建layer的一种情况是，某个layer可能有cudnn对应的实现。要根据是否有use_cudnn的编译选项，来返回一个cudnn版本的layer还是普通版本的layer.

比如下面这个conv layer


```c++

// Get convolution layer according to engine.
template <typename Dtype>
shared_ptr<Layer<Dtype> > GetConvolutionLayer(
    const LayerParameter& param) {
  ConvolutionParameter conv_param = param.convolution_param();
  ConvolutionParameter_Engine engine = conv_param.engine();
#ifdef USE_CUDNN
  bool use_dilation = false;
  for (int i = 0; i < conv_param.dilation_size(); ++i) {
    if (conv_param.dilation(i) > 1) {
      use_dilation = true;
    }
  }
#endif
  if (engine == ConvolutionParameter_Engine_DEFAULT) {
    engine = ConvolutionParameter_Engine_CAFFE;
#ifdef USE_CUDNN
    if (!use_dilation) {
      engine = ConvolutionParameter_Engine_CUDNN;
    }
#endif
  }
  if (engine == ConvolutionParameter_Engine_CAFFE) {
    return shared_ptr<Layer<Dtype> >(new ConvolutionLayer<Dtype>(param));
#ifdef USE_CUDNN
  } else if (engine == ConvolutionParameter_Engine_CUDNN) {
    if (use_dilation) {
      LOG(FATAL) << "CuDNN doesn't support the dilated convolution at Layer "
                 << param.name();
    }
    return shared_ptr<Layer<Dtype> >(new CuDNNConvolutionLayer<Dtype>(param));
#endif
  } else {
    LOG(FATAL) << "Layer " << param.name() << " has unknown engine.";
    throw;  // Avoids missing return warning
  }
}

REGISTER_LAYER_CREATOR(Convolution, GetConvolutionLayer);
```






















