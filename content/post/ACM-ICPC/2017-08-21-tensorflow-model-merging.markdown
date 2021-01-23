---
author: 111qqz
date: 2017-08-21 06:56:22+00:00
draft: false
title: tensorflow 合并模型
type: post
url: /2017/08/tensorflow-model-merging/
categories:
- deep-learning
tags:
- tensorflow
---

在这里存个备份，还有些问题没有解决。

raise ValueError("GraphDef cannot be larger than 2GB.")

记录一些思路好了。现在是没有生成.meta文件，爆掉应该是因为所有的变量都加载到了默认图里。

也就是说我处理完checkpoint 0 之后开始处理checkpoint1,但是checkpoint0的那些变量还是存在的...所以越来越多？

目前有两个想法，第一个想法是是受[TensorFlow极简教程：创建、保存和恢复机器学习模型](https://zhuanlan.zhihu.com/p/25906127)  中启发，用多个saver，每个saver指定要搞的图（但是这样好像要每个checkpoint都是不同的saver才有意义？）

第二个想法是，每次save完变量之后，将图恢复成默认状态（可以把图中所有变量清空。。



想法二大失败：

会遇到if self.stack[-1] is not default: │
IndexError: list index out of range   的问题。。

根据 [reset_default_graph awkwardly breaks graph nesting        ](https://github.com/tensorflow/tensorflow/issues/11121)

中提到了。。。reset_default_graph本身就不舍被设计成放在graph中清空变量用的。。。然后tf的代码也写得很不友好。。。没有 指明这个错误的原因。。。



<blockquote>For historical context, `tf.reset_default_graph()` was never designed to be used with `with g.as_default():` context managers. I think the proper fix here is to make `tf.reset_default_graph()` fail with an informative error message when used inside a `with g.as_default():` context. I think this could be done by checking that `ops._default_graph_stack` is empty before resetting.</blockquote>




    
    import sys, getopt
    import argparse
    import tensorflow as tf
    import os
    import shutil
    import numpy as np
    
    # fix out ,not log_
    def fix_var_name(id,var_name): 
        prefix = var_name[0:3]
        if id<10:
          suffix = var_name[4:]
        if id>=10 and id<100:
          suffix = var_name[5:]
        if id>=100 and id<1000:
          suffix = var_name[6:]
        if id>=1000 and id<10000:
          suffix = var_name[7:]
        ret = prefix + str(id+1) + suffix
        print('id=%d var_name=%s prefix=%s suffix=%s ret=%s' %(id,var_name,prefix,suffix,ret))
        return ret
    # only concat full_link_layer 
    def merge_full_link_layer(checkpoint_list,dry_run=False):
        with tf.Session() as sess:
          log_num = len(checkpoint_list) # a int range [0,1000)
          print("log_num:%d"%log_num)
          for var_name,_ in tf.contrib.framework.list_variables('log_0'):
            if not var_name.startswith('out'):
              var_tmp = tf.contrib.framework.load_variable('log_0',var_name)
              var = tf.Variable(var_tmp,name=var_name)
              continue
            print("var_name:%s"%var_name)
            for id in range(0,log_num): 
              # need to change the string  out0->out1,out2,out3 ... out15
              if id!=0:
                var_name = fix_var_name(id-1,var_name)
              checkpoint_dir = 'log_'+str(id)
              print('checkpoint_dir:%s'%checkpoint_dir)
    
           # for id,checkpoint_dir in enumerate(checkpoint_list):
           #  var_name = fix_var_name(id+1,var_name)
              var_tmp = tf.contrib.framework.load_variable(checkpoint_dir,var_name)
              #print("type(var_tmp):%s"%type(var_tmp))
           #   print(var_tmp)
              if 'weights' in var_name:
                if 'Momentum' in var_name:
                  if id == 0:
                    mom_weights = var_tmp
                    #print("mom_weights:%s"%type(mom_weights))
                  else:
                    mom_weights = np.concatenate((mom_weights,var_tmp),axis=1)
                else:
                  if id == 0:
                    weights = var_tmp
                  else:
                    weights = np.concatenate((weights,var_tmp),axis=1)
              else:
                if 'Momentum' in var_name:
                  if id == 0:
                    mom_biases = var_tmp
                  else:
                    mom_biases = np.concatenate((mom_biases,var_tmp),axis=0)
    
                else:
                  if id == 0:
                    biases = var_tmp
                  else: 
                    biases = np.concatenate((biases,var_tmp),axis=0)
            if not dry_run:
                flag1 = 'weights' in var_name
                flag2 = 'Momentum' in var_name
                if flag1 and flag2:
                  mom_weights = tf.Variable(mom_weights, name='out/weights/Momentum' )
                if flag1 and not flag2:
                  weights = tf.Variable(weights,name='out/weights')
                if not flag1 and flag2:
                  mom_biases = tf.Variable(mom_biases,name='out/biases/Momentum')
                if not flag1 and not flag2:
                  biases = tf.Variable(biases,name='out/biases')
          if not dry_run:
            print("writer running")
            #writer = tf.summary.FileWriter('./graphs', sess.graph)
            saver = tf.train.Saver()
            #sess.run(tf.global_variables_initializer())
            saver.save(sess,'./final_16_out',write_meta_graph=False)
        #writer.close()
    def merge_ckpt(checkpoint_dir,  dry_run=False):
      merge_full_link_layer(checkpoint_dir,False)
    def get_dir():
      checkpoint_list=[]
      dir_list = os.listdir('./')
      for line in dir_list:
        if line.startswith('log') and os.path.isdir(line):
          checkpoint_list.append(line)
      return checkpoint_list 
    def main():
      os.environ['CUDA_VISIBLE_DEVICES']="" 
      checkpoint_dir = get_dir()
      #checkpoint_dir = ['log_0','log_1','log_2']
      print (checkpoint_dir)
      merge_ckpt(checkpoint_dir, dry_run=False)
    if __name__ == '__main__':
      main()
    





嘛。。先不管了。。。据数据那边说已经够用了。下面是最终版本,没有合并动量，因为对验证没有作用。


    
    import sys, getopt
    import argparse
    import tensorflow as tf
    import os
    import shutil
    import numpy as np
    
    # fix out ,not log_
    def fix_var_name(id,var_name): 
        prefix = var_name[0:3]
        if id<10:
          suffix = var_name[4:]
        if id>=10 and id<100:
          suffix = var_name[5:]
        if id>=100 and id<1000:
          suffix = var_name[6:]
        if id>=1000 and id<10000:
          suffix = var_name[7:]
        ret = prefix + str(id+1) + suffix
        print('id=%d var_name=%s prefix=%s suffix=%s ret=%s' %(id,var_name,prefix,suffix,ret))
        return ret
    # only concat full_link_layer
    def merge_full_link_layer(checkpoint_list):
        with tf.Session() as sess:
          log_num = len(checkpoint_list) # a int range [0,1000)
          print("log_num:%d"%log_num)
          for var_name,_ in tf.contrib.framework.list_variables('log_0'):
            if not var_name.startswith('out'):
              var_tmp = tf.contrib.framework.load_variable('log_0',var_name)
              var = tf.Variable(var_tmp,name=var_name)
              continue
            if 'Momentum' in var_name:
              continue
            print("var_name:%s"%var_name)
            for id in range(0,log_num): 
              # need to change the string  out0->out1,out2,out3 ... out15
              if id!=0:
                var_name = fix_var_name(id-1,var_name)
              checkpoint_dir = 'log_'+str(id)
              print('checkpoint_dir:%s'%checkpoint_dir)
              var_tmp = tf.contrib.framework.load_variable(checkpoint_dir,var_name)
              if 'weights' in var_name:
                if 'Momentum' in var_name:
                  if id == 0:
                    mom_weights = var_tmp
                  else:
                    mom_weights = np.concatenate((mom_weights,var_tmp),axis=1)
                else:
                  if id == 0:
                    weights = var_tmp
                  else:
                    weights = np.concatenate((weights,var_tmp),axis=1)
              else:
                if 'Momentum' in var_name:
                  if id == 0:
                    mom_biases = var_tmp
                  else:
                    mom_biases = np.concatenate((mom_biases,var_tmp),axis=0)
                else:
                  if id == 0:
                    biases = var_tmp
                  else: 
                    biases = np.concatenate((biases,var_tmp),axis=0)
            flag1 = 'weights' in var_name
            flag2 = 'Momentum' in var_name
            if flag1 and not flag2:
              weights = tf.Variable(weights,name='out/weights')
            if not flag1 and not flag2:
              biases = tf.Variable(biases,name='out/biases')
          print("writer running")
            #writer = tf.summary.FileWriter('./graphs', sess.graph)
          saver = tf.train.Saver()
          sess.run(tf.global_variables_initializer())
          saver.save(sess,'./final_result',write_meta_graph=False)
        #writer.close()
    def get_dir():
      checkpoint_list=[]
      dir_list = os.listdir('./')
      for line in dir_list:
        if line.startswith('log') and os.path.isdir(line):
          checkpoint_list.append(line)
      return checkpoint_list 
    def main():
      os.environ['CUDA_VISIBLE_DEVICES']="" 
      checkpoint_dir = get_dir()
      # get_dir return the all the log_dir in './'  the log_dir format is 'log_%d',such as log_0,log_1
    
    
      #checkpoint_dir=['log_0','log_1','log_2']
      #checkpoint_dir = ['log_0','log_1','log_2','log_3','log_4','log_5','log_6','log_7','log_8','log_9','log_10','log_11']
      print (checkpoint_dir)
      merge_full_link_layer(checkpoint_dir)
    if __name__ == '__main__':
      main()
    





20170822update:去掉了卷基层的动量，添加了一些超参


    
    import sys, getopt
    import argparse
    import tensorflow as tf
    import os
    import shutil
    import numpy as np
    
    
    
    
    tf.flags.DEFINE_string('fc_prefix', 'out',
                                   """the prefix of full_link_layer output name """)
    
    
    
    
    FLAGS = tf.flags.FLAGS
    # fix out ,not log_
    def fix_var_name(id,var_name):
        len = len(FLAGS.fc_prefix)
        prefix = var_name[0:len]
        if id<10:
          suffix = var_name[len+1:]
        if id>=10 and id<100:
          suffix = var_name[len+2:]
        if id>=100 and id<1000:
          suffix = var_name[len+3:]
        if id>=1000 and id<10000:
          suffix = var_name[len+4:]
        ret = prefix + str(id+1) + suffix
        print('id=%d var_name=%s prefix=%s suffix=%s ret=%s' %(id,var_name,prefix,suffix,ret))
        return ret
    # only concat full_link_layer
    def merge_full_link_layer(checkpoint_list):
        with tf.Session() as sess:
          log_num = len(checkpoint_list) # a int range [0,1000)
          print("log_num:%d"%log_num)
          for var_name,_ in tf.contrib.framework.list_variables('log_0'):
            if 'Momentum' in var_name:
              continue
            if not var_name.startswith(FLAGS.fc_prefix):
              var_tmp = tf.contrib.framework.load_variable('log_0',var_name)
              var = tf.Variable(var_tmp,name=var_name)
              continue
            print("var_name:%s"%var_name)
            for id in range(0,log_num): 
              # need to change the string  out0->out1,out2,out3 ... out15
              if id!=0:
                var_name = fix_var_name(id-1,var_name)
              checkpoint_dir = 'log_'+str(id)
              print('checkpoint_dir:%s'%checkpoint_dir)
              var_tmp = tf.contrib.framework.load_variable(checkpoint_dir,var_name)
              if 'weights' in var_name:
                if 'Momentum' in var_name:
                  if id == 0:
                    mom_weights = var_tmp
                  else:
                    mom_weights = np.concatenate((mom_weights,var_tmp),axis=1)
                else:
                  if id == 0:
                    weights = var_tmp
                  else:
                    weights = np.concatenate((weights,var_tmp),axis=1)
              else:
                if 'Momentum' in var_name:
                  if id == 0:
                    mom_biases = var_tmp
                  else:
                    mom_biases = np.concatenate((mom_biases,var_tmp),axis=0)
                else:
                  if id == 0:
                    biases = var_tmp
                  else: 
                    biases = np.concatenate((biases,var_tmp),axis=0)
            flag1 = 'weights' in var_name
            flag2 = 'Momentum' in var_name
            if flag1 and not flag2:
              weights = tf.Variable(weights,name='%s/weights'%FLAGS.fc_prefix)
            if not flag1 and not flag2:
              biases = tf.Variable(biases,name='%s/biases'%FLAGS.fc_prefix)
          print("writer running")
            #writer = tf.summary.FileWriter('./graphs', sess.graph)
          saver = tf.train.Saver()
          sess.run(tf.global_variables_initializer())
          saver.save(sess,'./final_result',write_meta_graph=False)
        #writer.close()
    def get_dir():
      checkpoint_list=[]
      dir_list = os.listdir('./')
      for line in dir_list:
        if line.startswith('log') and os.path.isdir(line):
          checkpoint_list.append(line)
      return checkpoint_list 
    def main():
      os.environ['CUDA_VISIBLE_DEVICES']="" 
      checkpoint_dir = get_dir()
      # get_dir return the all the log_dir in './'  the log_dir format is 'log_%d',such as log_0,log_1
    
    
      #checkpoint_dir=['log_0','log_1','log_2']
      #checkpoint_dir = ['log_0','log_1','log_2','log_3','log_4','log_5','log_6','log_7','log_8','log_9','log_10','log_11']
      print (checkpoint_dir)
      merge_full_link_layer(checkpoint_dir)
    if __name__ == '__main__':
      main()




