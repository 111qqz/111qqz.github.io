---
author: 111qqz
date: 2017-06-07 05:50:27+00:00
draft: false
title: vundle error detected while processing function
type: post
url: /2017/06/vundle-error-detected-while-processing-function/
categories:
- 其他
tags:
- fish
- vim
- vundle
---

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/06/Screenshot_20170607_133416.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/06/Screenshot_20170607_133416.png)


### 好久没装新插件了，最新要配下python,发现安装时候满屏的错误。。。




### 最后发现是shell的锅，因为我用的是fish,在.vimrc文件中添加



    
    set shell=/bin/bash




### 即可。




### 以及说下可能的其他原因，虽然我没遇到





 	  * 对于arch系，可能从aur中安装的版本out ot data
 	  * 可能没有把.vimrc中vundle的配置从set rtp+=~/.vim/bundle/vundle更新成set rtp+=~/.vim/bundle/vundle.vim
 	  * 可能项目名称用了" 而不是'






### 以及顺手查了下bundle和Plugin的区别。。。




### 简单来说。。Plugin是新写法，bundle是正在被淘汰的写法，不过由于兼容性的原因，仍然在使用。。。




### 以后使用plugin的写法就好。


[参考资料](https://github.com/VundleVim/Vundle.vim/issues/690)


