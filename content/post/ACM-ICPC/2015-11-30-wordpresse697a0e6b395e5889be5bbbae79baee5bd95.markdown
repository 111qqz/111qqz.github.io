---
author: 111qqz
date: 2015-11-30 02:44:19+00:00
draft: false
title: wordpress无法创建目录/没有写权限的解决方案
type: post
url: /2015/11/wordpress/
categories:
- 其他
post_format:
- 日志
---

终于解决了。

的确是权限问题。

但是由于初始化的时候，我错误的设置了数据库目录。应该为/alidata/www/serve/mysql ，而我设置成了/home/mysql

之前一直是在改alidata下的权限...现在可以了QAQ
