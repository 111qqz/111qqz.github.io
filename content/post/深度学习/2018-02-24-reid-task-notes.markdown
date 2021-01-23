---
author: 111qqz
date: 2018-02-24 04:34:02+00:00
draft: false
title: reid 相关任务记录
type: post
url: /2018/02/reid-task-notes/
categories:
- deep-learning
tags:
- reid
---

被师兄（同事？）普及了一番实验规范orz...

我还是太年轻了

所谓的一个fc的版本是右边的．一个放着不动，另一个在sequence_len（１０）的维度上做ave,然后再expand成原来的维度．如下图．

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/02/433671689.jpg)
](https://111qqz.com/wordpress/wp-content/uploads/2018/02/433671689.jpg)





任务命名规则：

如D1V2_a_1,D1表示使用第一个数据集，V2表示是第二个大版本，ａ表示在V２大版本上的微调，最后的数字表示这是第几次运行该任务（跑三次以减少波动的影响）

logdir的地址为:/mnt/lustre/renkuanze/Data_t1/reid/log/｛$jobname｝






      * D1:使用ilivids 数据集

        * D1V1表示最初始的　baseline model
        * D1V2表示改为使用一个fc

          * D1V2_a是一个在一个FC上，不添加光流的修改版本
          * D1V2_b是在一个FC上的baseline版本（也就是有光流）
          * D1V2_c是在一个FC上，有光流，batchsize从３２改为６４，gpu数目从4改为8的版本


        * D1V3表示将softmax改为sigmod

          * D1V3_b表示将softmax改为sigmod的baseline版本




      * D2:使用prid2011数据集

        * D2V1表示初始的baseline model
        * D2V2表示改为使用一个fc

          * D2V2_b是在一个FC上的baseline版本




      * 











