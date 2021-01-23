---
author: 111qqz
date: 2017-07-19 06:21:40+00:00
draft: false
title: how to copy & modify nets model on tensorflow slim
type: post
url: /2017/07/how-to-copy-modify-nets-model-on-tensorflow-slim/
categories:
- deep-learning
tags:
- slim
- tensorflow
---

想要修改tensorflow-slim 中 nets中的某个model,例如明明为kk_v2.py

观察到train_image_classifier.py中调用模型的部分

    
    network_fn = nets_factory.get_network_fn(
            FLAGS.model_name,
            num_classes=(dataset.num_classes - FLAGS.labels_offset),
            weight_decay=FLAGS.weight_decay,
            is_training=True)


调用了nets_factory.get_network_fn，get_network如下：

    
    def get_network_fn(name, num_classes, weight_decay=0.0, is_training=False):
      """Returns a network_fn such as `logits, end_points = network_fn(images)`.
    
      Args:
        name: The name of the network.
        num_classes: The number of classes to use for classification.
        weight_decay: The l2 coefficient for the model weights.
        is_training: `True` if the model is being used for training and `False`
          otherwise.
    
      Returns:
        network_fn: A function that applies the model to a batch of images. It has
          the following signature:
            logits, end_points = network_fn(images)
      Raises:
        ValueError: If network `name` is not recognized.
      """
      if name not in networks_map:
        raise ValueError('Name of network unknown %s' % name)
      func = networks_map[name]
      @functools.wraps(func)
      def network_fn(images):
        arg_scope = arg_scopes_map[name](weight_decay=weight_decay)
        with slim.arg_scope(arg_scope):
          return func(images, num_classes, is_training=is_training)
      if hasattr(func, 'default_image_size'):
        network_fn.default_image_size = func.default_image_size
    
      return network_fn
    




我们看到model name 是通过 networks_map映射到func的

因此需要添加对于我们新的model,kk_v2的映射

    
    networks_map = {'alexnet_v2': alexnet.alexnet_v2,
                    'cifarnet': cifarnet.cifarnet,
                    'overfeat': overfeat.overfeat,
                    'vgg_a': vgg.vgg_a,
                    'vgg_16': vgg.vgg_16,
                    'vgg_19': vgg.vgg_19,
                    'inception_v1': inception.inception_v1,
                    'inception_v2': inception.inception_v2,
                    'inception_v3': inception.inception_v3,
                    'inception_v4': inception.inception_v4,
                    'inception_resnet_v2': inception.inception_resnet_v2,
                    'kk_v2':inception.inception_resnet_v2,
                    'lenet': lenet.lenet,
                    'resnet_v1_50': resnet_v1.resnet_v1_50,
                    'resnet_v1_101': resnet_v1.resnet_v1_101,
                    'resnet_v1_152': resnet_v1.resnet_v1_152,
                    'resnet_v1_200': resnet_v1.resnet_v1_200,
                    'resnet_v2_50': resnet_v2.resnet_v2_50,
                    'resnet_v2_101': resnet_v2.resnet_v2_101,
                    'resnet_v2_152': resnet_v2.resnet_v2_152,
                    'resnet_v2_200': resnet_v2.resnet_v2_200,
                    'mobilenet_v1': mobilenet_v1.mobilenet_v1,
                   }


由于train_image_classifier.py中有如下参数，

    
    tf.app.flags.DEFINE_string(
        'preprocessing_name', None, 'The name of the preprocessing to use. If left '
        'as `None`, then the model_name flag is used.'



    
    preprocessing_name = FLAGS.preprocessing_name or FLAGS.model_name


因此还需要修改预处理的映射表

    
     preprocessing_fn_map = {
          'cifarnet': cifarnet_preprocessing,
          'inception': inception_preprocessing,
          'inception_v1': inception_preprocessing,
          'inception_v2': inception_preprocessing,
          'inception_v3': inception_preprocessing,
          'inception_v4': inception_preprocessing,
          'inception_resnet_v2': inception_preprocessing,
          'kk_v2': inception_preprocessing,
          'lenet': lenet_preprocessing,
          'mobilenet_v1': inception_preprocessing,
          'resnet_v1_50': vgg_preprocessing,
          'resnet_v1_101': vgg_preprocessing,
          'resnet_v1_152': vgg_preprocessing,
          'resnet_v1_200': vgg_preprocessing,
          'resnet_v2_50': vgg_preprocessing,
          'resnet_v2_101': vgg_preprocessing,
          'resnet_v2_152': vgg_preprocessing,
          'resnet_v2_200': vgg_preprocessing,
          'vgg': vgg_preprocessing,
          'vgg_a': vgg_preprocessing,
          'vgg_16': vgg_preprocessing,
          'vgg_19': vgg_preprocessing,
      }


还要修改arg_scopes_map，添加kk_v2的key

    
    arg_scopes_map = {'alexnet_v2': alexnet.alexnet_v2_arg_scope,
                      'cifarnet': cifarnet.cifarnet_arg_scope,
                      'overfeat': overfeat.overfeat_arg_scope,
                      'vgg_a': vgg.vgg_arg_scope,
                      'vgg_16': vgg.vgg_arg_scope,
                      'vgg_19': vgg.vgg_arg_scope,
                      'inception_v1': inception.inception_v3_arg_scope,
                      'inception_v2': inception.inception_v3_arg_scope,
                      'inception_v3': inception.inception_v3_arg_scope,
                      'inception_v4': inception.inception_v4_arg_scope,
                      'inception_resnet_v2':
                      inception.inception_resnet_v2_arg_scope,
                      'kk_v2':
                      inception.inception_resnet_v2_arg_scope,
                      'lenet': lenet.lenet_arg_scope,
                      'resnet_v1_50': resnet_v1.resnet_arg_scope,
                      'resnet_v1_101': resnet_v1.resnet_arg_scope,
                      'resnet_v1_152': resnet_v1.resnet_arg_scope,
                      'resnet_v1_200': resnet_v1.resnet_arg_scope,
                      'resnet_v2_50': resnet_v2.resnet_arg_scope,
                      'resnet_v2_101': resnet_v2.resnet_arg_scope,
                      'resnet_v2_152': resnet_v2.resnet_arg_scope,
                      'resnet_v2_200': resnet_v2.resnet_arg_scope,
                      'mobilenet_v1': mobilenet_v1.mobilenet_v1_arg_scope,
                     }
    



