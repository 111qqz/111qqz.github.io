---
author: 111qqz
date: 2019-02-23 14:28:01+00:00
draft: false
title: manjaro /archlinux 下 steam 文明5/6(civilization V/VI)的运行方法
type: post
url: /2019/02/manjaro-archlinux-civilization/
categories:
- 其他
tags:
- steam
- 文明
---

系统版本为Manjaro 18.0.3 Illyria

运行文明5比较容易，只需要设置启动选项为:

LD_PRELOAD=/usr/lib32/libopenal.so.1 %command%



文明6运行会报错 undefined symbol: FT_Done_MM_Var

解决办法是 在终端中用如下办法运行steam:

LD_PRELOAD=/usr/lib/libfreetype.so steam

[参考链接](https://forum.manjaro.org/t/steam-recently-civ-vi-stops-to-launch/68244/3)


