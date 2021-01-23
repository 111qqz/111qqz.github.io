---
author: 111qqz
date: 2018-04-30 05:54:33+00:00
draft: false
title: vim  插件 NERDTree 学习笔记
type: post
url: /2018/04/vim-NERDTree-plugin/
categories:
- 其他
tags:
- NERDTree
- vim
---

迫于要在服务器上写cpp代码，又由于各种原因，没办法把同步到本地。因此要在服务器上配置一个cpp的环境orz.

我是用vim-plug来管理插件的，只需要添加

Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }  就好了。
下面记录一些会用到的快捷键:

**ctrl+w类似tmux里面的功能键。**

crtl+w+w: 光标自动在左右侧窗口切换

cril+w+r:调换左右侧窗口的布局位置

t 在新 Tab 中打开选中文件/书签，并跳到新 Tab
T 在新 Tab 中打开选中文件/书签，但不跳到新 Tab
gT 前一个 tab
gt 后一个 tab
