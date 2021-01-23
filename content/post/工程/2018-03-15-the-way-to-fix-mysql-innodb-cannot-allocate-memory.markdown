---
author: 111qqz
date: 2018-03-15 04:56:58+00:00
draft: false
title: 'mysql 出现　innoDB: Cannot allocate memory for the buffer pool　的解决办法'
type: post
url: /2018/03/the-way-to-fix-mysql-innodb-cannot-allocate-memory/
categories:
- 其他
tags:
- linux
- mysql
---

emmm,博客的数据库又挂了。

看了下log，发现innoDB: Cannot allocate memory for the buffer pool　的error

查了下，貌似是内存不够了？　orz

用free 命令看了下，阿里云ecs貌似是默认没有swap分区的。

于是参考[云服务器 ECS Linux SWAP 配置概要说明  ](https://help.aliyun.com/knowledge_detail/42534.html)

设置了swap分区。看下还会不会挂orz


