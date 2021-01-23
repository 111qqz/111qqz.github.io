---
author: 111qqz
date: 2017-08-21 02:03:45+00:00
draft: false
title: tensorflow checkpoint 学习笔记
type: post
url: /2017/08/tensorflow-checkpoint-notes/
categories:
- deep-learning
tags:
- tensorflow
---

参考资料：

[What is the TensorFlow checkpoint meta file?](https://stackoverflow.com/questions/36195454/what-is-the-tensorflow-checkpoint-meta-file)

[TensorFlow: Restoring variables from from multiple checkpoints](https://stackoverflow.com/questions/35733917/tensorflow-restoring-variables-from-from-multiple-checkpoints)

合并模型的时候发现.meta一直在累加，而其他数据文件没有改变。因此来探究一下checkpoint的几个文件的含义。



<blockquote>This file contains a serialized [`MetaGraphDef` protocol buffer](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/protobuf/meta_graph.proto). The `MetaGraphDef` is designed as a serialization format that includes all of the information required to restore a training or inference process (including the [`GraphDef`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/graph.proto) that describes the dataflow, and additional annotations that describe the variables, input pipelines, and other relevant information). For example, the `MetaGraphDef` is used by [TensorFlow Serving](https://tensorflow.github.io/serving/serving_basic.html) to start an inference service based on your trained model. We are investigating other tools that could use the `MetaGraphDef` for training.

Assuming that you still have the Python code for your model, you do not need the `MetaGraphDef`to restore the model, because you can reconstruct all of the information in the `MetaGraphDef` by re-executing the Python code that builds the model. To restore from a checkpoint, you only need the checkpoint files that contain the trained weights, which are written periodically to the same directory.</blockquote>



提到了.meta文件包含了恢复训练的所有信息。。。主要是为了其他工具可以快速恢复训练？

如果还是用python的话，恢复checkpoint没有必要使用.meta文件。




      * **meta file**: describes the saved graph structure, includes GraphDef, SaverDef, and so on; then apply `tf.train.import_meta_graph('/tmp/model.ckpt.meta')`, will restore `Saver` and `Graph`.
      * **index file**: it is a string-string immutable table(tensorflow::table::Table). Each key is a name of a tensor and its value is a serialized BundleEntryProto. Each BundleEntryProto describes the metadata of a tensor: which of the "data" files contains the content of a tensor, the offset into that file, checksum, some auxiliary data, etc.
      * **data file**: it is TensorBundle collection, save the values of all variables.






# Checkpoint



checkpoint文件可以理解成一个table，每次save之后会被更新，内容是最近一次的checkpoint文件名。

restore的时候，会先去checkpoint里看到最新的checkpoint文件是什么，然后只加载最新的。


