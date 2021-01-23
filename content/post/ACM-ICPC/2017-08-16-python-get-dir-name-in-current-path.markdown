---
author: 111qqz
date: 2017-08-16 08:21:41+00:00
draft: false
title: python只获取当前目录下的文件夹及文件名
type: post
url: /2017/08/python-get-dir-name-in-current-path/
categories:
- 其他
tags:
- python
---

list = os.listdir(rootdir)#列出目录下的所有文件和目录
    for line in list:
        filepath = os.path.join(rootdir,line)
        if os.path.isdir(filepath):#如果filepath是目录
            print "dir:" + filepath
        else:
            print "file:" + filepath



如果需要遍历文件夹下的所以文件，可以使用os.walk()方法。


    
    os.walk()返回一个三元素的tuple：当前路径、子文件夹名称、文件列表。
    import os
    for root, dirs, files in os.walk(path):
        for filename in files:
            print filename
        for dirname in dirs:
            print dirname



举个列处当前目录所有文件夹的例子：


    
    from os import listdir
    from os.path import isfile, join
    import os
    
    dir =os.listdir()
    for line in dir:
      if os.path.isdir(line):
        print (line)
    
    





[参考资料](http://www.pewees.com/article/14599980083468NDsZKENddescPcn56EWwKHpef.html)
