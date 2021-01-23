---
author: 111qqz
date: 2017-10-31 15:26:25+00:00
draft: false
title: 在wordpress 中输入数学公式
type: post
url: /2017/10/input-formula-on-wordpress/
categories:
- 其他
tags:
- latex
---

查了一些资料。。发现不是要装各种插件（还不一定能用，比如和crayon冲突。。就是讲得很不清楚orz。。

又下一个win下的公式编辑器之类的软件是什么鬼啊？

干脆记录一下必要步骤。只有一步。




      1. 配置mathjax. 加入下面代码到该主题的header.php中 <head>和</head>之间（要放在**<?php wp_head(); ?>**）

    
    <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-MML-AM_CHTML'></script>
    






      * **换行显示（displayed mathematics）**，它的分隔符是 $$...$$和 \[...\] ，
      * **行内显示（in-line mathematics）**，它的分割符号是 \\(...\\)   (只有一个\)






不记得公式语法去[latex online](http://latex.codecogs.com/eqneditor/editor.php) 查看即可


