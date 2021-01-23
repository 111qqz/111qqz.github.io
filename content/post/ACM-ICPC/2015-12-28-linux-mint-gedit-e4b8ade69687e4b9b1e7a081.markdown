---
author: 111qqz
date: 2015-12-28 12:46:05+00:00
draft: false
title: linux mint  gedit 中文乱码
type: post
url: /2015/12/linux-mint-gedit-/
categories:
- 其他
tags:
- gedit
- linux mint
---



    
    gconftool-2 --set --type=list --list-type=string /apps/gedit-2/preferences/encodings/auto_detected "[UTF-8,CURRENT,GB18030,ISO-8859-15,UTF-16]"



