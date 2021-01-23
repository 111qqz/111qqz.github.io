---
author: 111qqz
date: 2018-09-30 08:59:31+00:00
draft: false
title: '解决ubuntu 14.04 下 壁纸软件 variety 崩溃 ValueError: bad marshal data (unknown type
  code) 的问题'
type: post
url: /2018/09/the-way-to-fix-variety-crash-on-ubuntu-14-04/
categories:
- 其他
tags:
- linux
- variety
---

系统为ubuntu 14.04

迫于特别想定时换壁纸，查了下解决方案。

发现只要删除掉/usr目录下所有的'.pyc'文件就可以

命令为:sudo find /usr -name '*.pyc' -delete
