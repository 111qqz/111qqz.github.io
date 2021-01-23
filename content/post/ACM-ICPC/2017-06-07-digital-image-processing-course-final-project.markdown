---
author: 111qqz
date: 2017-06-07 06:53:36+00:00
draft: false
title: 数字图像处理大作业(初步）
type: post
url: /2017/06/digital-image-processing-course-final-project/
categories:
- 其他
tags:
- python
- 数字图像处理
---

...先随便记录一下好了。。。



 	  * 神经网络识别数字或者字母？
 	  * 识别车牌号？
 	  * not hot dog?





安装python pandas [pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)

发现之前装caffe的时候...装了这个东西。。。

但是就是检测不到？于是卸载重装。。。。

需要注意的是，如果是python2,要用pip2 install pandas,如果是python3,要用pip3 install pandas.



<del>安装tensorflow...直接sudo pacman -Syu python-tensorflow 即可。。。</del>

然后装好之后检测不到orz...感觉还是pip的安装方式比较靠谱。。。

pip2 install tensorflow

[tensorflow_pip安装](https://www.tensorflow.org/versions/r0.10/get_started/os_setup#pip_installation)

我的环境是python2.7

    
    # Ubuntu/Linux 64-bit, CPU only, Python 2.7
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
    
    sudo pip install --upgrade $TF_BINARY_URL


安装成功。。然后发现。。numpy挂了（？？？？？

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/06/tensorflow安装成功后numpy报错.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/06/tensorflow安装成功后numpy报错.png)



[SO上给出的建议](https://stackoverflow.com/questions/39908504/numpy-version-error-when-importing-tensorflow)
<del>
感觉之后还会各种遇到不同python版本导致的问题。。。。那就上anaconda好了。。。</del>

试了anaconda...想法挺好。。但是貌似还不成熟.。。比如用anaconda安装numpy会报错orz..

最后解决办法是。。。卸载了python-numpy以及所有依赖python-numpy的a包；卸载了python2-numpy以及所有a依赖python２-numpy的包

然后重新安装了python2-numpy

以及发现。。。还有些坑是shellaa相关的.。。y所以暂时不要用fish了。。。



然后提示Missing required dependencies ['dateutil']

解决办法是安装python2-datautil

**以及各种pip安装。。都记得要pip2而不是pip**

中间缺少一堆库。。。大部分直接安装就好了。。。记得要安装python2对应的版本。。。

然后对于ImportError: No module named tensorboard.plugins

[解决办法](https://github.com/buriburisuri/speech-to-text-wavenet/issues/34)　是将tensorflow升级到1.0以上（安装之后的版本默认为0.1)

sudo proxychains4 pip2 install tensorflow --upgrade














