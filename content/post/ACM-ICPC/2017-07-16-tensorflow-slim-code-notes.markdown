---
author: 111qqz
date: 2017-07-16 13:10:04+00:00
draft: false
title: tensorflow slim 源码分析
type: post
url: /2017/07/tensorflow-slim-code-notes/
categories:
- deep-learning
tags:
- tensorflow
---

py的源码看起来还是很愉快的。。。（虽然熟练成程度完全不如cpp。。。。

<!-- more -->



[![](https://111qqz.com/wordpress/wp-content/uploads/2017/07/Selection_004.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/07/Selection_004.png)

datasets里是数据集相关

deployment是部署相关

nets里给了很多网络结构

preprocessing给了几种预处理的方式

这些都和slim没有太大关系，就不多废话了。

分析的部分见代码注释...

由于刚刚入门machine learning 一周...还有很多内容还没有从理论层面接触...所以源码的理解也十分有限...希望能以后有机会补充一波

    
    # Copyright 2016 The TensorFlow Authors. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    # ==============================================================================
    r"""Downloads and converts a particular dataset.
    
    Usage:
    ```shell
    
    $ python download_and_convert_data.py \
        --dataset_name=mnist \
        --dataset_dir=/tmp/mnist
    
    $ python download_and_convert_data.py \
        --dataset_name=cifar10 \
        --dataset_dir=/tmp/cifar10
    
    $ python download_and_convert_data.py \
        --dataset_name=flowers \
        --dataset_dir=/tmp/flowers
    ```
    """
    from __future__ import absolute_import    #from __future__是为了解决python版本升级导致的兼容问题，没必要纠结
    from __future__ import division
    from __future__ import print_function
    
    import tensorflow as tf
    
    from datasets import download_and_convert_cifar10
    from datasets import download_and_convert_flowers
    from datasets import download_and_convert_mnist
    
    FLAGS = tf.app.flags.FLAGS    #FLAGS 用来传递或者设置tensforflow的参数
    
    tf.app.flags.DEFINE_string(   #设置的格式为：('参数名称',参数值,'参数的解释'）
        'dataset_name',
        None,
        'The name of the dataset to convert, one of "cifar10", "flowers", "mnist".')
    
    tf.app.flags.DEFINE_string(
        'dataset_dir',
        None,
        'The directory where the output TFRecords and temporary files are saved.')
    
    
    def main(_):
      if not FLAGS.dataset_name:
        raise ValueError('You must supply the dataset name with --dataset_name')
      if not FLAGS.dataset_dir:
        raise ValueError('You must supply the dataset directory with --dataset_dir')
    
      if FLAGS.dataset_name == 'cifar10':                #提供的三个数据集,[cifar10],[flowers],[mnist]
        download_and_convert_cifar10.run(FLAGS.dataset_dir)
      elif FLAGS.dataset_name == 'flowers':
        download_and_convert_flowers.run(FLAGS.dataset_dir)
      elif FLAGS.dataset_name == 'mnist':
        download_and_convert_mnist.run(FLAGS.dataset_dir)
      else:
        raise ValueError(
            'dataset_name [%s] was not recognized.' % FLAGS.dataset_name)  #数据经名字不属于上述三个
    
    if __name__ == '__main__':  #这种写法可以保证在该文件被import的时候不会执行main函数
      tf.app.run()



    
    # coding=utf-8
    # Copyright 2016 The TensorFlow Authors. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    # http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    # ==============================================================================
    """Generic evaluation script that evaluates a model using a given dataset."""
    
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    
    import math
    import tensorflow as tf
    
    from datasets import dataset_factory
    from nets import nets_factory
    from preprocessing import preprocessing_factory
    
    slim = tf.contrib.slim
    
    tf.app.flags.DEFINE_integer(
        'batch_size', 100, 'The number of samples in each batch.')
    
    tf.app.flags.DEFINE_integer(
        'max_num_batches', None,
        'Max number of batches to evaluate by default use all.')
    
    tf.app.flags.DEFINE_string(
        'master', '', 'The address of the TensorFlow master to use.')
    
    tf.app.flags.DEFINE_string(
        'checkpoint_path', '/tmp/tfmodel/',
        'The directory where the model was written to or an absolute path to a '
        'checkpoint file.')
    
    tf.app.flags.DEFINE_string(
        'eval_dir', '/tmp/tfmodel/', 'Directory where the results are saved to.')
    
    tf.app.flags.DEFINE_integer(
        'num_preprocessing_threads', 4,
        'The number of threads used to create the batches.')
    
    tf.app.flags.DEFINE_string(
        'dataset_name', 'imagenet', 'The name of the dataset to load.')
    
    tf.app.flags.DEFINE_string(
        'dataset_split_name', 'test', 'The name of the train/test split.')
    
    tf.app.flags.DEFINE_string(
        'dataset_dir', None, 'The directory where the dataset files are stored.')
    
    tf.app.flags.DEFINE_integer(
        'labels_offset', 0,
        'An offset for the labels in the dataset. This flag is primarily used to '
        'evaluate the VGG and ResNet architectures which do not use a background '
        'class for the ImageNet dataset.')
    
    tf.app.flags.DEFINE_string(
        'model_name', 'inception_v3', 'The name of the architecture to evaluate.')
    
    tf.app.flags.DEFINE_string(
        'preprocessing_name', None, 'The name of the preprocessing to use. If left '
        'as `None`, then the model_name flag is used.')
    
    tf.app.flags.DEFINE_float(
        'moving_average_decay', None,
        'The decay to use for the moving average.'
        'If left as None, then moving averages are not used.')
    
    tf.app.flags.DEFINE_integer(
        'eval_image_size', None, 'Eval image size')
    
    FLAGS = tf.app.flags.FLAGS
    
    
    def main(_):
      if not FLAGS.dataset_dir:
        raise ValueError('You must supply the dataset directory with --dataset_dir')
    
      tf.logging.set_verbosity(tf.logging.INFO) #设置log信息的级别，有DEBUG, INFO, WARN, ERROR, or FATAL
      with tf.Graph().as_default():  #overrides the current default graph for the lifetime of the context
                                        #注意不是线程安全的..
        tf_global_step = slim.get_or_create_global_step()
                            #slim.get_or_create_global_step可以参考tf.train.get_or_create_global_step
                            #作用同样是得到global step tensor，参数为graph,参数为空时认为参数为default graph
        ######################
        # Select the dataset #
        ######################
        dataset = dataset_factory.get_dataset(
            FLAGS.dataset_name, FLAGS.dataset_split_name, FLAGS.dataset_dir)
    
        ####################
        # Select the model #
        ####################
        network_fn = nets_factory.get_network_fn(
            FLAGS.model_name,
            num_classes=(dataset.num_classes - FLAGS.labels_offset),
            is_training=False)
    
        ##############################################################
        # Create a dataset provider that loads data from the dataset #
        ##############################################################
                                        #读取数据
        provider = slim.dataset_data_provider.DatasetDataProvider(
            dataset,
            shuffle=False,
            common_queue_capacity=2 * FLAGS.batch_size,
            common_queue_min=FLAGS.batch_size)
        [image, label] = provider.get(['image', 'label'])
        label -= FLAGS.labels_offset
    
        #####################################
        # Select the preprocessing function #
        #####################################
        preprocessing_name = FLAGS.preprocessing_name or FLAGS.model_name
        image_preprocessing_fn = preprocessing_factory.get_preprocessing(
            preprocessing_name,
            is_training=False)
        #python or的用法，flag1 or flag2 or... or flagn,如果最后逻辑值为真，
        # 返回的是（葱左至右）第一个使其为真的值（而不返回布尔值），
        #如果都为假，则返回最后一个假值
        eval_image_size = FLAGS.eval_image_size or network_fn.default_image_size
    
        image = image_preprocessing_fn(image, eval_image_size, eval_image_size)
    
        images, labels = tf.train.batch(
            [image, label],
            batch_size=FLAGS.batch_size,
            num_threads=FLAGS.num_preprocessing_threads,
            capacity=5 * FLAGS.batch_size)
    
        ####################
        # Define the model #
        ####################
        logits, _ = network_fn(images)  #python语法,序列解包
    
        #移动平均，参考 https://en.wikipedia.org/wiki/Moving_average
        if FLAGS.moving_average_decay:
          variable_averages = tf.train.ExponentialMovingAverage(
              FLAGS.moving_average_decay, tf_global_step)
          variables_to_restore = variable_averages.variables_to_restore(
              slim.get_model_variables())
          variables_to_restore[tf_global_step.op.name] = tf_global_step
        else:
          variables_to_restore = slim.get_variables_to_restore()
    
        predictions = tf.argmax(logits, 1)
        #tf.argmax(input, axis=None, name=None, dimension=None)
        #Returns the index with the largest value across axes of a tensor.
        #就是返回logits的第一维（行？）最大值的位置索引
    
    
        labels = tf.squeeze(labels) #将labels中维度是1的那一维去掉
    
        # Define the metrics:
        names_to_values, names_to_updates = slim.metrics.aggregate_metric_map({
            'Accuracy': slim.metrics.streaming_accuracy(predictions, labels),
            'Recall_5': slim.metrics.streaming_recall_at_k(
                logits, labels, 5),
        })
        #metrics.aggregate_metric_map在metrics的list很长的时候的一种简便的表达方式
        #metrics直接翻译为【度量】，不是tensorflow的概念.用来监控计算的性能指标
    
    
        # Print the summaries to screen.
        for name, value in names_to_values.items():
          summary_name = 'eval/%s' % name
          op = tf.summary.scalar(summary_name, value, collections=[])
          #tf.summary.scalar :Outputs a Summary protocol buffer containing a single scalar value
          op = tf.Print(op, [value], summary_name)
          tf.add_to_collection(tf.GraphKeys.SUMMARIES, op)
    
        # TODO(sguada) use num_epochs=1
        if FLAGS.max_num_batches:
          num_batches = FLAGS.max_num_batches
        else:
          # This ensures that we make a single pass over all of the data.
          num_batches = math.ceil(dataset.num_samples / float(FLAGS.batch_size))
    
        if tf.gfile.IsDirectory(FLAGS.checkpoint_path):#返回是否为一个目录
          checkpoint_path = tf.train.latest_checkpoint(FLAGS.checkpoint_path)
        else:
          checkpoint_path = FLAGS.checkpoint_path
    
        tf.logging.info('Evaluating %s' % checkpoint_path)  #记录log信息
    
        #Evaluates the model at the given checkpoint path.
        #Evaluates the model at the given checkpoint path.
        slim.evaluation.evaluate_once(
            master=FLAGS.master,
            checkpoint_path=checkpoint_path,
            logdir=FLAGS.eval_dir,
            num_evals=num_batches,
            eval_op=list(names_to_updates.values()),
            variables_to_restore=variables_to_restore)
    
    
    if __name__ == '__main__':
      tf.app.run()



    
    # Copyright 2017 The TensorFlow Authors. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    # http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    # ==============================================================================
    r"""Saves out a GraphDef containing the architecture of the model.
    
    To use it, run something like this, with a model name defined by slim:
    
    bazel build tensorflow_models/slim:export_inference_graph
    bazel-bin/tensorflow_models/slim/export_inference_graph \
    --model_name=inception_v3 --output_file=/tmp/inception_v3_inf_graph.pb
    
    If you then want to use the resulting model with your own or pretrained
    checkpoints as part of a mobile model, you can run freeze_graph to get a graph
    def with the variables inlined as constants using:
    
    bazel build tensorflow/python/tools:freeze_graph
    bazel-bin/tensorflow/python/tools/freeze_graph \
    --input_graph=/tmp/inception_v3_inf_graph.pb \
    --input_checkpoint=/tmp/checkpoints/inception_v3.ckpt \
    --input_binary=true --output_graph=/tmp/frozen_inception_v3.pb \
    --output_node_names=InceptionV3/Predictions/Reshape_1
    
    The output node names will vary depending on the model, but you can inspect and
    estimate them using the summarize_graph tool:
    
    bazel build tensorflow/tools/graph_transforms:summarize_graph
    bazel-bin/tensorflow/tools/graph_transforms/summarize_graph \
    --in_graph=/tmp/inception_v3_inf_graph.pb
    
    To run the resulting graph in C++, you can look at the label_image sample code:
    
    bazel build tensorflow/examples/label_image:label_image
    bazel-bin/tensorflow/examples/label_image/label_image \
    --image=${HOME}/Pictures/flowers.jpg \
    --input_layer=input \
    --output_layer=InceptionV3/Predictions/Reshape_1 \
    --graph=/tmp/frozen_inception_v3.pb \
    --labels=/tmp/imagenet_slim_labels.txt \
    --input_mean=0 \
    --input_std=255
    
    """
    
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    
    import tensorflow as tf
    
    from tensorflow.python.platform import gfile
    from datasets import dataset_factory
    from nets import nets_factory
    
    
    slim = tf.contrib.slim
    
    tf.app.flags.DEFINE_string(
        'model_name', 'inception_v3', 'The name of the architecture to save.')
    
    tf.app.flags.DEFINE_boolean(
        'is_training', False,
        'Whether to save out a training-focused version of the model.')
    
    tf.app.flags.DEFINE_integer(
        'default_image_size', 224,
        'The image size to use if the model does not define it.')
    
    tf.app.flags.DEFINE_string('dataset_name', 'imagenet',
                               'The name of the dataset to use with the model.')
    
    tf.app.flags.DEFINE_integer(
        'labels_offset', 0,
        'An offset for the labels in the dataset. This flag is primarily used to '
        'evaluate the VGG and ResNet architectures which do not use a background '
        'class for the ImageNet dataset.')
    
    tf.app.flags.DEFINE_string(
        'output_file', '', 'Where to save the resulting file to.')
    
    tf.app.flags.DEFINE_string(
        'dataset_dir', '', 'Directory to save intermediate dataset files to')
    
    FLAGS = tf.app.flags.FLAGS
    
    
    def main(_):
      if not FLAGS.output_file:
        raise ValueError('You must supply the path to save to with --output_file')
      tf.logging.set_verbosity(tf.logging.INFO)
      with tf.Graph().as_default() as graph:
        dataset = dataset_factory.get_dataset(FLAGS.dataset_name, 'train',
                                              FLAGS.dataset_dir)
        network_fn = nets_factory.get_network_fn(
            FLAGS.model_name,
            num_classes=(dataset.num_classes - FLAGS.labels_offset),
            is_training=FLAGS.is_training)
    
        #hasattr 是python语法， hasattr(object, name) -> bool，用来判断object中是否有name属性
        if hasattr(network_fn, 'default_image_size'):
          image_size = network_fn.default_image_size
        else:
          image_size = FLAGS.default_image_size
        placeholder = tf.placeholder(name='input', dtype=tf.float32,
                                     shape=[1, image_size, image_size, 3])
        network_fn(placeholder)
        graph_def = graph.as_graph_def()
        #graph.as_graph_def():Returns a serialized（序列化） GraphDef representation of this graph.
        #The serialized GraphDef can be imported into another Graph (using tf.import_graph_def) or used with the C++ Session API.
        #该方法线程安全
    
    
        # gfile。GFile 是一个无线程锁的I/O 封装
        with gfile.GFile(FLAGS.output_file, 'wb') as f:
          f.write(graph_def.SerializeToString())
    
    
    if __name__ == '__main__':
      tf.app.run()




    
    # coding=utf-8
    # Copyright 2016 The TensorFlow Authors. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    # http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    # ==============================================================================
    """Generic training script that trains a model using a given dataset."""
    
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import print_function
    
    import tensorflow as tf
    
    from datasets import dataset_factory
    from deployment import model_deploy
    from nets import nets_factory
    from preprocessing import preprocessing_factory
    
    slim = tf.contrib.slim
    
    tf.app.flags.DEFINE_string(
        'master', '', 'The address of the TensorFlow master to use.')
    
    tf.app.flags.DEFINE_string(
        'train_dir', '/tmp/tfmodel/',
        'Directory where checkpoints and event logs are written to.')
    
    tf.app.flags.DEFINE_integer('num_clones', 1,
                                'Number of model clones to deploy.')
    
    tf.app.flags.DEFINE_boolean('clone_on_cpu', False,
                                'Use CPUs to deploy clones.')
    
    tf.app.flags.DEFINE_integer('worker_replicas', 1, 'Number of worker replicas.')
    
    tf.app.flags.DEFINE_integer(
        'num_ps_tasks', 0,
        'The number of parameter servers. If the value is 0, then the parameters '
        'are handled locally by the worker.')
    
    tf.app.flags.DEFINE_integer(
        'num_readers', 4,
        'The number of parallel readers that read data from the dataset.')
    
    tf.app.flags.DEFINE_integer(
        'num_preprocessing_threads', 4,
        'The number of threads used to create the batches.')
    
    tf.app.flags.DEFINE_integer(
        'log_every_n_steps', 10,
        'The frequency with which logs are print.')
    
    tf.app.flags.DEFINE_integer(
        'save_summaries_secs', 600,
        'The frequency with which summaries are saved, in seconds.')
    
    tf.app.flags.DEFINE_integer(
        'save_interval_secs', 600,
        'The frequency with which the model is saved, in seconds.')
    
    tf.app.flags.DEFINE_integer(
        'task', 0, 'Task id of the replica running the training.')
    
    ######################
    # Optimization Flags #
    ######################
    
    tf.app.flags.DEFINE_float(
        'weight_decay', 0.00004, 'The weight decay on the model weights.')
    
    tf.app.flags.DEFINE_string(
        'optimizer', 'rmsprop',
        'The name of the optimizer, one of "adadelta", "adagrad", "adam",'
        '"ftrl", "momentum", "sgd" or "rmsprop".')
    
    tf.app.flags.DEFINE_float(
        'adadelta_rho', 0.95,
        'The decay rate for adadelta.')
    
    tf.app.flags.DEFINE_float(
        'adagrad_initial_accumulator_value', 0.1,
        'Starting value for the AdaGrad accumulators.')
    
    tf.app.flags.DEFINE_float(
        'adam_beta1', 0.9,
        'The exponential decay rate for the 1st moment estimates.')
    
    tf.app.flags.DEFINE_float(
        'adam_beta2', 0.999,
        'The exponential decay rate for the 2nd moment estimates.')
    
    tf.app.flags.DEFINE_float('opt_epsilon', 1.0, 'Epsilon term for the optimizer.')
    
    tf.app.flags.DEFINE_float('ftrl_learning_rate_power', -0.5,
                              'The learning rate power.')
    
    tf.app.flags.DEFINE_float(
        'ftrl_initial_accumulator_value', 0.1,
        'Starting value for the FTRL accumulators.')
    
    tf.app.flags.DEFINE_float(
        'ftrl_l1', 0.0, 'The FTRL l1 regularization strength.')
    
    tf.app.flags.DEFINE_float(
        'ftrl_l2', 0.0, 'The FTRL l2 regularization strength.')
    
    tf.app.flags.DEFINE_float(
        'momentum', 0.9,
        'The momentum for the MomentumOptimizer and RMSPropOptimizer.')
    
    tf.app.flags.DEFINE_float('rmsprop_decay', 0.9, 'Decay term for RMSProp.')
    
    #######################
    # Learning Rate Flags #
    #######################
    
    tf.app.flags.DEFINE_string(
        'learning_rate_decay_type',
        'exponential',
        'Specifies how the learning rate is decayed. One of "fixed", "exponential",'
        ' or "polynomial"')
    
    tf.app.flags.DEFINE_float('learning_rate', 0.01, 'Initial learning rate.')
    
    tf.app.flags.DEFINE_float(
        'end_learning_rate', 0.0001,
        'The minimal end learning rate used by a polynomial decay learning rate.')
    
    tf.app.flags.DEFINE_float(
        'label_smoothing', 0.0, 'The amount of label smoothing.')
    
    tf.app.flags.DEFINE_float(
        'learning_rate_decay_factor', 0.94, 'Learning rate decay factor.')
    
    tf.app.flags.DEFINE_float(
        'num_epochs_per_decay', 2.0,
        'Number of epochs after which learning rate decays.')
    
    tf.app.flags.DEFINE_bool(
        'sync_replicas', False,
        'Whether or not to synchronize the replicas during training.')
    
    tf.app.flags.DEFINE_integer(
        'replicas_to_aggregate', 1,
        'The Number of gradients to collect before updating params.')
    
    tf.app.flags.DEFINE_float(
        'moving_average_decay', None,
        'The decay to use for the moving average.'
        'If left as None, then moving averages are not used.')
    
    #######################
    # Dataset Flags #
    #######################
    
    tf.app.flags.DEFINE_string(
        'dataset_name', 'imagenet', 'The name of the dataset to load.')
    
    tf.app.flags.DEFINE_string(
        'dataset_split_name', 'train', 'The name of the train/test split.')
    
    tf.app.flags.DEFINE_string(
        'dataset_dir', None, 'The directory where the dataset files are stored.')
    
    tf.app.flags.DEFINE_integer(
        'labels_offset', 0,
        'An offset for the labels in the dataset. This flag is primarily used to '
        'evaluate the VGG and ResNet architectures which do not use a background '
        'class for the ImageNet dataset.')
    
    tf.app.flags.DEFINE_string(
        'model_name', 'inception_v3', 'The name of the architecture to train.')
    
    tf.app.flags.DEFINE_string(
        'preprocessing_name', None, 'The name of the preprocessing to use. If left '
        'as `None`, then the model_name flag is used.')
    
    tf.app.flags.DEFINE_integer(
        'batch_size', 32, 'The number of samples in each batch.')
    
    tf.app.flags.DEFINE_integer(
        'train_image_size', None, 'Train image size')
    
    tf.app.flags.DEFINE_integer('max_number_of_steps', None,
                                'The maximum number of training steps.')
    
    #####################
    # Fine-Tuning Flags #
    #####################
    
    tf.app.flags.DEFINE_string(
        'checkpoint_path', None,
        'The path to a checkpoint from which to fine-tune.')
    
    tf.app.flags.DEFINE_string(
        'checkpoint_exclude_scopes', None,
        'Comma-separated list of scopes of variables to exclude when restoring '
        'from a checkpoint.')
    
    tf.app.flags.DEFINE_string(
        'trainable_scopes', None,
        'Comma-separated list of scopes to filter the set of variables to train.'
        'By default, None would train all the variables.')
    
    tf.app.flags.DEFINE_boolean(
        'ignore_missing_vars', False,
        'When restoring a checkpoint would ignore missing variables.')
    
    FLAGS = tf.app.flags.FLAGS
    
    
    def _configure_learning_rate(num_samples_per_epoch, global_step):
      """Configures the learning rate.
    
      Args:
        num_samples_per_epoch: The number of samples in each epoch of training.
        global_step: The global_step tensor.
    
      Returns:
        A `Tensor` representing the learning rate.
    
      Raises:
        ValueError: if
      """
      decay_steps = int(num_samples_per_epoch / FLAGS.batch_size *
                        FLAGS.num_epochs_per_decay)
      if FLAGS.sync_replicas:
        decay_steps /= FLAGS.replicas_to_aggregate
          #dacay,衰退
    
    
        #下面是几种学习速率的变化形式，可以是指数型衰退，可以是固定不变，也可以使多项式型衰退。
      if FLAGS.learning_rate_decay_type == 'exponential':
        return tf.train.exponential_decay(FLAGS.learning_rate,
                                          global_step,
                                          decay_steps,
                                          FLAGS.learning_rate_decay_factor,
                                          staircase=True,
                                          name='exponential_decay_learning_rate')
      elif FLAGS.learning_rate_decay_type == 'fixed':
        return tf.constant(FLAGS.learning_rate, name='fixed_learning_rate')
      elif FLAGS.learning_rate_decay_type == 'polynomial':
        return tf.train.polynomial_decay(FLAGS.learning_rate,
                                         global_step,
                                         decay_steps,
                                         FLAGS.end_learning_rate,
                                         power=1.0,
                                         cycle=False,
                                         name='polynomial_decay_learning_rate')
      else:
        raise ValueError('learning_rate_decay_type [%s] was not recognized',
                         FLAGS.learning_rate_decay_type)
    
    
    
    #选择优化方法（优化器，大概是求偏导的具体数值计算方法？），tf内置了许多优化方法，类比梯度下降，细节黑箱即可。
    def _configure_optimizer(learning_rate):
      """Configures the optimizer used for training.
    
      Args:
        learning_rate: A scalar or `Tensor` learning rate.
    
      Returns:
        An instance of an optimizer.
    
      Raises:
        ValueError: if FLAGS.optimizer is not recognized.
      """
      if FLAGS.optimizer == 'adadelta':
        optimizer = tf.train.AdadeltaOptimizer(
            learning_rate,
            rho=FLAGS.adadelta_rho,
            epsilon=FLAGS.opt_epsilon)
      elif FLAGS.optimizer == 'adagrad':
        optimizer = tf.train.AdagradOptimizer(
            learning_rate,
            initial_accumulator_value=FLAGS.adagrad_initial_accumulator_value)
      elif FLAGS.optimizer == 'adam':
        optimizer = tf.train.AdamOptimizer(
            learning_rate,
            beta1=FLAGS.adam_beta1,
            beta2=FLAGS.adam_beta2,
            epsilon=FLAGS.opt_epsilon)
      elif FLAGS.optimizer == 'ftrl':
        optimizer = tf.train.FtrlOptimizer(
            learning_rate,
            learning_rate_power=FLAGS.ftrl_learning_rate_power,
            initial_accumulator_value=FLAGS.ftrl_initial_accumulator_value,
            l1_regularization_strength=FLAGS.ftrl_l1,
            l2_regularization_strength=FLAGS.ftrl_l2)
      elif FLAGS.optimizer == 'momentum':
        optimizer = tf.train.MomentumOptimizer(
            learning_rate,
            momentum=FLAGS.momentum,
            name='Momentum')
      elif FLAGS.optimizer == 'rmsprop':
        optimizer = tf.train.RMSPropOptimizer(
            learning_rate,
            decay=FLAGS.rmsprop_decay,
            momentum=FLAGS.momentum,
            epsilon=FLAGS.opt_epsilon)
      elif FLAGS.optimizer == 'sgd':
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
      else:
        raise ValueError('Optimizer [%s] was not recognized', FLAGS.optimizer)
      return optimizer
    
    
    def _get_init_fn():
      """Returns a function run by the chief worker to warm-start the training.
    
      Note that the init_fn is only run when initializing the model during the very
      first global step.
    
      Returns:
        An init function run by the supervisor.
      """
      if FLAGS.checkpoint_path is None:
        return None
    
      # Warn the user if a checkpoint exists in the train_dir. Then we'll be
      # ignoring the checkpoint anyway.
      if tf.train.latest_checkpoint(FLAGS.train_dir):
        tf.logging.info(
            'Ignoring --checkpoint_path because a checkpoint already exists in %s'
            % FLAGS.train_dir)
        return None
    
      exclusions = []  #python的list数据类型
      if FLAGS.checkpoint_exclude_scopes:
        exclusions = [scope.strip()
                      for scope in FLAGS.checkpoint_exclude_scopes.split(',')]
    
      # TODO(sguada) variables.filter_variables()
      variables_to_restore = []
      for var in slim.get_model_variables():
        excluded = False
        for exclusion in exclusions:
          if var.op.name.startswith(exclusion):
            excluded = True
            break
        if not excluded:
          variables_to_restore.append(var)
    
      if tf.gfile.IsDirectory(FLAGS.checkpoint_path):
        checkpoint_path = tf.train.latest_checkpoint(FLAGS.checkpoint_path)
      else:
        checkpoint_path = FLAGS.checkpoint_path
    
      tf.logging.info('Fine-tuning from %s' % checkpoint_path)
    
      return slim.assign_from_checkpoint_fn(
          checkpoint_path,
          variables_to_restore,
          ignore_missing_vars=FLAGS.ignore_missing_vars)
    
    
    def _get_variables_to_train():
      """Returns a list of variables to train.
    
      Returns:
        A list of variables to train by the optimizer.
      """
      if FLAGS.trainable_scopes is None:
        return tf.trainable_variables()
      else:
        scopes = [scope.strip() for scope in FLAGS.trainable_scopes.split(',')]
    
      variables_to_train = []
      for scope in scopes:
        variables = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope)
        variables_to_train.extend(variables)
      return variables_to_train
    
    
    def main(_):
      if not FLAGS.dataset_dir:
        raise ValueError('You must supply the dataset directory with --dataset_dir')
    
      tf.logging.set_verbosity(tf.logging.INFO)
      with tf.Graph().as_default():
        #######################
        # Config model_deploy #
        #######################
        deploy_config = model_deploy.DeploymentConfig(
            num_clones=FLAGS.num_clones,
            clone_on_cpu=FLAGS.clone_on_cpu,
            replica_id=FLAGS.task,
            num_replicas=FLAGS.worker_replicas,
            num_ps_tasks=FLAGS.num_ps_tasks)
    
        # Create global_step
        with tf.device(deploy_config.variables_device()):
          global_step = slim.create_global_step()
    
        ######################
        # Select the dataset #
        ######################
        dataset = dataset_factory.get_dataset(
            FLAGS.dataset_name, FLAGS.dataset_split_name, FLAGS.dataset_dir)
    
        ######################
        # Select the network #
        ######################
        network_fn = nets_factory.get_network_fn(
            FLAGS.model_name,
            num_classes=(dataset.num_classes - FLAGS.labels_offset),
            weight_decay=FLAGS.weight_decay,
            is_training=True)
    
        #####################################
        # Select the preprocessing function #
        #####################################
        preprocessing_name = FLAGS.preprocessing_name or FLAGS.model_name
        image_preprocessing_fn = preprocessing_factory.get_preprocessing(
            preprocessing_name,
            is_training=True)
    
        ##############################################################
        # Create a dataset provider that loads data from the dataset #
        ##############################################################
        with tf.device(deploy_config.inputs_device()):
          provider = slim.dataset_data_provider.DatasetDataProvider(  #还是定义一些数据的读取方式
              dataset,
              num_readers=FLAGS.num_readers,
              common_queue_capacity=20 * FLAGS.batch_size,
              common_queue_min=10 * FLAGS.batch_size)
          [image, label] = provider.get(['image', 'label'])
          label -= FLAGS.labels_offset
    
          train_image_size = FLAGS.train_image_size or network_fn.default_image_size
    
          image = image_preprocessing_fn(image, train_image_size, train_image_size)
    
          images, labels = tf.train.batch(
              [image, label],
              batch_size=FLAGS.batch_size,
              num_threads=FLAGS.num_preprocessing_threads,
              capacity=5 * FLAGS.batch_size)
          labels = slim.one_hot_encoding(    #one-hot是一种向量编码方式，n维向量只有为相应值的位置为1，其余都为0
              labels, dataset.num_classes - FLAGS.labels_offset)
          batch_queue = slim.prefetch_queue.prefetch_queue(
              [images, labels], capacity=2 * deploy_config.num_clones)
    
        ####################
        # Define the model #
        ####################
        #通过复制多个网络来实现并行
        def clone_fn(batch_queue):
          """Allows data parallelism by creating multiple clones of network_fn."""
          with tf.device(deploy_config.inputs_device()):
            images, labels = batch_queue.dequeue()  #dequeue，双端队列。。
          logits, end_points = network_fn(images)
    
          #############################
          # Specify the loss function #
          #############################
          if 'AuxLogits' in end_points:
            tf.losses.softmax_cross_entropy(   #softmax函数对应使用的cost function(loss function)
                                                #是corss_entropy,也就是交叉熵
                logits=end_points['AuxLogits'], onehot_labels=labels,
                label_smoothing=FLAGS.label_smoothing, weights=0.4, scope='aux_loss')
          tf.losses.softmax_cross_entropy(
              logits=logits, onehot_labels=labels,
              label_smoothing=FLAGS.label_smoothing, weights=1.0)
          #Label Smoothing Regularization，一种防止overfit的优化方法
          return end_points
    
        # Gather initial summaries.
        summaries = set(tf.get_collection(tf.GraphKeys.SUMMARIES))
    
        clones = model_deploy.create_clones(deploy_config, clone_fn, [batch_queue])
        first_clone_scope = deploy_config.clone_scope(0)
        # Gather update_ops from the first clone. These contain, for example,
        # the updates for the batch_norm variables created by network_fn.
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS, first_clone_scope)
    
        # Add summaries for end_points.
        end_points = clones[0].outputs
        for end_point in end_points:
          x = end_points[end_point]
          summaries.add(tf.summary.histogram('activations/' + end_point, x))
          summaries.add(tf.summary.scalar('sparsity/' + end_point,
                                          tf.nn.zero_fraction(x)))
    
        # Add summaries for losses.
        for loss in tf.get_collection(tf.GraphKeys.LOSSES, first_clone_scope):
          summaries.add(tf.summary.scalar('losses/%s' % loss.op.name, loss))
    
        # Add summaries for variables.
        for variable in slim.get_model_variables():
          summaries.add(tf.summary.histogram(variable.op.name, variable))
            #突然画图
    
        #################################
        # Configure the moving averages #  #参考moving averages的wiki
        #################################
        if FLAGS.moving_average_decay:
          moving_average_variables = slim.get_model_variables()
          variable_averages = tf.train.ExponentialMovingAverage(
              FLAGS.moving_average_decay, global_step)
        else:
          moving_average_variables, variable_averages = None, None
    
        #########################################
        # Configure the optimization procedure. #
        #########################################
        with tf.device(deploy_config.optimizer_device()):
          learning_rate = _configure_learning_rate(dataset.num_samples, global_step)
          optimizer = _configure_optimizer(learning_rate)
          summaries.add(tf.summary.scalar('learning_rate', learning_rate))
    
    
        #在分布式系统上训练的同步...
        if FLAGS.sync_replicas:
          # If sync_replicas is enabled, the averaging will be done in the chief
          # queue runner.
          optimizer = tf.train.SyncReplicasOptimizer(
              opt=optimizer,
              replicas_to_aggregate=FLAGS.replicas_to_aggregate,
              variable_averages=variable_averages,
              variables_to_average=moving_average_variables,
              replica_id=tf.constant(FLAGS.task, tf.int32, shape=()),
              total_num_replicas=FLAGS.worker_replicas)
        elif FLAGS.moving_average_decay:
          # Update ops executed locally by trainer.
          update_ops.append(variable_averages.apply(moving_average_variables))
    
        # Variables to train.
        variables_to_train = _get_variables_to_train()
    
        #  and returns a train_tensor and summary_op
        total_loss, clones_gradients = model_deploy.optimize_clones(
            clones,
            optimizer,
            var_list=variables_to_train)
        # Add total_loss to summary.
        summaries.add(tf.summary.scalar('total_loss', total_loss))
    
        # Create gradient updates.
        grad_updates = optimizer.apply_gradients(clones_gradients,
                                                 global_step=global_step)
        update_ops.append(grad_updates)
    
        update_op = tf.group(*update_ops)
        with tf.control_dependencies([update_op]):
          train_tensor = tf.identity(total_loss, name='train_op')
    
        # Add the summaries from the first clone. These contain the summaries
        # created by model_fn and either optimize_clones() or _gather_clone_loss().
        summaries |= set(tf.get_collection(tf.GraphKeys.SUMMARIES,
                                           first_clone_scope))
    
        # Merge all summaries together.
        summary_op = tf.summary.merge(list(summaries), name='summary_op')
    
    
        ###########################
        # Kicks off the training. #
        ###########################
        slim.learning.train(
            train_tensor,
            logdir=FLAGS.train_dir,
            master=FLAGS.master,
            is_chief=(FLAGS.task == 0),
            init_fn=_get_init_fn(),
            summary_op=summary_op,
            number_of_steps=FLAGS.max_number_of_steps,
            log_every_n_steps=FLAGS.log_every_n_steps,
            save_summaries_secs=FLAGS.save_summaries_secs,
            save_interval_secs=FLAGS.save_interval_secs,
            sync_optimizer=optimizer if FLAGS.sync_replicas else None)
    
    
    if __name__ == '__main__':
      tf.app.run()



