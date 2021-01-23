---
author: 111qqz
date: 2017-08-24 09:12:58+00:00
draft: false
title: tensorflow input pipline  学习笔记
type: post
url: /2017/08/tensorflow-input-pipline-notes/
categories:
- deep-learning
tags:
- pipline
- tensorflow
---

参考资料：

[tf_doc_Reading data](https://www.tensorflow.org/api_guides/python/reading_data)

[TENSORFLOW INPUT PIPELINE EXAMPLE](https://ischlag.github.io/2016/06/19/tensorflow-input-pipeline-example/)

[tensorflow：理解tensorflow中的输入管道](http://shartoo.github.io/tensorflow-inputpipeline/)

第二个参考资料是第一个的翻译版本，翻译的水平一般，建议看原文，不是很长。

下面是我挑了文章中重点的部分+自己的理解。



# TL;DR;



一个适用于不是很大的数据集的pipline input 的例子。



# Load Data in Tensorflow



**input pipline 可以理解称一种load data的方式**。 一般有两种方式load data,一种是比较传统的，使用feed 的方式。如果数据集比较大，这种方式就不适用了，因为这种方式需要将数据全部导入到memory中。因此tf提供了pipline input的读入数据的方式。

input pipline 会处理 csv file,解码文件格式，重构数据结构，打乱数据顺序，做数据扩充或者其他预处理，然后使用线程(threads)将数据导进batch.



# Load the Label Data



确保使用正确的dataset,csv文件路径。

然后处理 得到train和test 的label

**由于我们只是读数据而没有真的打算训练，所以没有使用one-hot的编码方式**，而是直接将（本来也是由数字字符组成的）字符串，转化成int.


    
    def encode_label(label):
      return int(label)
    
    def read_label_file(file):
      f = open(file, "r")
      filepaths = []
      labels = []
      for line in f:
        filepath, label = line.split(",")
        filepaths.append(filepath)
        labels.append(encode_label(label))
      return filepaths, labels
    
    # reading labels and file path
    train_filepaths, train_labels = read_label_file(dataset_path + train_labels_file)
    test_filepaths, test_labels = read_label_file(dataset_path + test_labels_file)





# Do Some Optional Processing on Our String Lists




    
    # transform relative path into full path
    train_filepaths = [ dataset_path + fp for fp in train_filepaths]
    test_filepaths = [ dataset_path + fp for fp in test_filepaths]
    
    # for this example we will create or own test partition
    all_filepaths = train_filepaths + test_filepaths
    all_labels = train_labels + test_labels
    
    # we limit the number of files to 20 to make the output more clear!
    all_filepaths = all_filepaths[:20]
    all_labels = all_labels[:20]





# Start Building the Pipeline



确保tensor的 dtype和list中的数据的type相匹配。


    
    from tensorflow.python.framework import ops
    from tensorflow.python.framework import dtypes
    # convert string into tensors
    all_images = ops.convert_to_tensor(all_filepaths, dtype=dtypes.string)
    all_labels = ops.convert_to_tensor(all_labels, dtype=dtypes.int32)





# Lets Partition the Data



这是一个可选的步骤。可能由于我们的数据集比较大，我们先把它分成train set 和 test set

![A visualization of the dynamic partition function in tensorflow.](https://ischlag.github.io/images/DynamicPartition.png)





    
    # create a partition vector
    partitions = [0] * len(all_filepaths)
    partitions[:test_set_size] = [1] * test_set_size
    random.shuffle(partitions)
    
    # partition our data into a test and train set according to our partition vector
    train_images, test_images = tf.dynamic_partition(all_images, partitions, 2)
    train_labels, test_labels = tf.dynamic_partition(all_labels, partitions, 2)





# Build the Input Queues and Define How to Load Images





使用slice_input_producer 切分 tensor,得到一个个的实例（？）,然后使用线程 queue them up.

shuffle表示是否打乱数据，此处我们不打乱。


    
    # create input queues
    train_input_queue = tf.train.slice_input_producer(
                                        [train_images, train_labels],
                                        shuffle=False)
    test_input_queue = tf.train.slice_input_producer(
                                        [test_images, test_labels],
                                        shuffle=False)
    
    # process path and string tensor into an image and a label
    file_content = tf.read_file(train_input_queue[0])
    train_image = tf.image.decode_jpeg(file_content, channels=NUM_CHANNELS)
    train_label = train_input_queue[1]
    
    file_content = tf.read_file(test_input_queue[0])
    test_image = tf.image.decode_jpeg(file_content, channels=NUM_CHANNELS)
    test_label = test_input_queue[1]





# Group Samples into Batches



单个sample训练效率会很低，通常的做法是将若干个samples合成一个batch一起训练。每个batch中samples的个数就是所谓的batch_size

到目前为止我们只是描述了pipline大致的样子，但是tensorflow还不知道我们image数据的shape.  在使用tf.train_batch将samples合成若干个batch之前，我们需要首先定义image

tensor 的 shape


    
    # define tensor shape
    train_image.set_shape([IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNELS])
    test_image.set_shape([IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNELS])
    
    
    # collect batches of images before processing
    train_image_batch, train_label_batch = tf.train.batch(
                                        [train_image, train_label],
                                        batch_size=BATCH_SIZE
                                        #,num_threads=1
                                        )
    test_image_batch, test_label_batch = tf.train.batch(
                                        [test_image, test_label],
                                        batch_size=BATCH_SIZE
                                        #,num_threads=1
                                        )





# Run the Queue Runners and Start a Session





到目前为止我们已经构建好了input pipline.但是为了将pipline 启动，我们还需要使用线程，线程将加载queue,将数据导入tensorflow objects.


    
    with tf.Session() as sess:
      
      # initialize the variables
      sess.run(tf.initialize_all_variables())
      
      # initialize the queue threads to start to shovel data
      coord = tf.train.Coordinator()
      threads = tf.train.start_queue_runners(coord=coord)
    
      print "from the train set:"
      for i in range(20):
        print sess.run(train_label_batch)
    
      print "from the test set:"
      for i in range(10):
        print sess.run(test_label_batch)
    
      # stop our queue threads and properly close the session
      coord.request_stop()
      coord.join(threads)
      sess.close()





如下面的输出所示，tensorflow 不会关心epoch(全部数据过了一遍叫一个epoch)的数值，所以需要你自己手动统计。


    
    (tf-env)worker1:~$ python mnist_feed.py 
    I tensorflow/stream_executor/dso_loader.cc:105] successfully opened CUDA library libcublas.so locally
    I tensorflow/stream_executor/dso_loader.cc:105] successfully opened CUDA library libcudnn.so locally
    I tensorflow/stream_executor/dso_loader.cc:105] successfully opened CUDA library libcufft.so locally
    I tensorflow/stream_executor/dso_loader.cc:105] successfully opened CUDA library libcuda.so.1 locally
    I tensorflow/stream_executor/dso_loader.cc:105] successfully opened CUDA library libcurand.so locally
    input pipeline ready
    I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:900] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
    I tensorflow/core/common_runtime/gpu/gpu_init.cc:102] Found device 0 with properties: 
    name: GeForce GTX 960
    major: 5 minor: 2 memoryClockRate (GHz) 1.253
    pciBusID 0000:01:00.0
    Total memory: 2.00GiB
    Free memory: 1.77GiB
    I tensorflow/core/common_runtime/gpu/gpu_init.cc:126] DMA: 0 
    I tensorflow/core/common_runtime/gpu/gpu_init.cc:136] 0:   Y 
    I tensorflow/core/common_runtime/gpu/gpu_device.cc:755] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX 960, pci bus id: 0000:01:00.0)
    from the train set:
    [5 4 1 9 2]
    [1 3 1 3 6]
    [1 7 2 6 9]
    [5 4 1 9 2]
    [1 3 1 3 6]
    [1 7 2 6 9]
    [5 4 1 9 2]
    [1 3 1 3 6]
    [1 7 2 6 9]
    [5 4 1 9 2]
    [1 3 1 3 6]
    [1 7 2 6 9]
    [5 4 1 9 2]
    [1 3 1 3 6]
    [1 7 2 6 9]
    [5 4 1 9 2]
    [1 3 1 3 6]
    [1 7 2 6 9]
    [5 4 1 9 2]
    [1 3 1 3 6]
    from the test set:
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]
    [0 4 5 3 8]





# Complete Code for this example




    
    # Example on how to use the tensorflow input pipelines. The explanation can be found here ischlag.github.io.
    import tensorflow as tf
    import random
    from tensorflow.python.framework import ops
    from tensorflow.python.framework import dtypes
    
    dataset_path      = "/path/to/your/dataset/mnist/"
    test_labels_file  = "test-labels.csv"
    train_labels_file = "train-labels.csv"
    
    test_set_size = 5
    
    IMAGE_HEIGHT  = 28
    IMAGE_WIDTH   = 28
    NUM_CHANNELS  = 3
    BATCH_SIZE    = 5
    
    def encode_label(label):
      return int(label)
    
    def read_label_file(file):
      f = open(file, "r")
      filepaths = []
      labels = []
      for line in f:
        filepath, label = line.split(",")
        filepaths.append(filepath)
        labels.append(encode_label(label))
      return filepaths, labels
    
    # reading labels and file path
    train_filepaths, train_labels = read_label_file(dataset_path + train_labels_file)
    test_filepaths, test_labels = read_label_file(dataset_path + test_labels_file)
    
    # transform relative path into full path
    train_filepaths = [ dataset_path + fp for fp in train_filepaths]
    test_filepaths = [ dataset_path + fp for fp in test_filepaths]
    
    # for this example we will create or own test partition
    all_filepaths = train_filepaths + test_filepaths
    all_labels = train_labels + test_labels
    
    all_filepaths = all_filepaths[:20]
    all_labels = all_labels[:20]
    
    # convert string into tensors
    all_images = ops.convert_to_tensor(all_filepaths, dtype=dtypes.string)
    all_labels = ops.convert_to_tensor(all_labels, dtype=dtypes.int32)
    
    # create a partition vector
    partitions = [0] * len(all_filepaths)
    partitions[:test_set_size] = [1] * test_set_size
    random.shuffle(partitions)
    
    # partition our data into a test and train set according to our partition vector
    train_images, test_images = tf.dynamic_partition(all_images, partitions, 2)
    train_labels, test_labels = tf.dynamic_partition(all_labels, partitions, 2)
    
    # create input queues
    train_input_queue = tf.train.slice_input_producer(
                                        [train_images, train_labels],
                                        shuffle=False)
    test_input_queue = tf.train.slice_input_producer(
                                        [test_images, test_labels],
                                        shuffle=False)
    
    # process path and string tensor into an image and a label
    file_content = tf.read_file(train_input_queue[0])
    train_image = tf.image.decode_jpeg(file_content, channels=NUM_CHANNELS)
    train_label = train_input_queue[1]
    
    file_content = tf.read_file(test_input_queue[0])
    test_image = tf.image.decode_jpeg(file_content, channels=NUM_CHANNELS)
    test_label = test_input_queue[1]
    
    # define tensor shape
    train_image.set_shape([IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNELS])
    test_image.set_shape([IMAGE_HEIGHT, IMAGE_WIDTH, NUM_CHANNELS])
    
    
    # collect batches of images before processing
    train_image_batch, train_label_batch = tf.train.batch(
                                        [train_image, train_label],
                                        batch_size=BATCH_SIZE
                                        #,num_threads=1
                                        )
    test_image_batch, test_label_batch = tf.train.batch(
                                        [test_image, test_label],
                                        batch_size=BATCH_SIZE
                                        #,num_threads=1
                                        )
    
    print "input pipeline ready"
    
    with tf.Session() as sess:
      
      # initialize the variables
      sess.run(tf.initialize_all_variables())
      
      # initialize the queue threads to start to shovel data
      coord = tf.train.Coordinator()
      threads = tf.train.start_queue_runners(coord=coord)
    
      print "from the train set:"
      for i in range(20):
        print sess.run(train_label_batch)
    
      print "from the test set:"
      for i in range(10):
        print sess.run(test_label_batch)
    
      # stop our queue threads and properly close the session
      coord.request_stop()
      coord.join(threads)
      sess.close()








