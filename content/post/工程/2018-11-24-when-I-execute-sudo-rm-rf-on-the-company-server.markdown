---
author: 111qqz
date: 2018-11-24 08:31:19+00:00
draft: false
title: 我在公司的服务器上执行了sudo rm -rf /*
type: post
url: /2018/11/when-I-execute-sudo-rm-rf-on-the-company-server/
categories:
- 其他
tags:
- docker
---

TL;DR



 	  * 依靠人的小心谨慎是不靠谱的，人总有失误的时候
 	  * 看了下docker volume的权限机制，貌似是从docker image中继承。
 	  * 写了两个脚本，用来把rm alias到mv，避免手滑



又是一个<del>可以摸鱼的</del>周五晚上，sensespider系统测试了一天，fix了几个Bug,似乎可以发布了。系统一直是部署在了docker中..这几天测试产生了不少结果文件在host的volume中... 看着不舒服，干脆删一下好了

嗯？怎么所有者是root。。。那我sudo一下，也没什么大不了的嘛

然而手滑了... 打了个 sudo rm -rf /*   ...

![](https://pic3.zhimg.com/v2-609298615e427d75a6c420f83096b622_b.gif)




提示无法删除/boot  device is busy...

吓了一跳，下意识Ctrl-C...

从新在本地ssh到服务器，发现已经登不上去了...报错在找不到sh

看了一下，果然服务器的/bin 目录已经被删干净了...

google了一些从rm中恢复文件的帖子...

试图用 sudo apt-get install  装一些工具包...

这个时候已经提示我找不到apt-get 了。。。

非常慌。<del>花了3分钟思考了我到目前为止的一生</del>

看了下scp命令还在，赶紧趁着这个终端回话还没关，把本地的/bin目录拷贝了上来。

试了下，ssh命令可以用了。 这样至少后续的修复（在不麻烦IT同事的情况下)不用跑机房了。有些镇定。

然后发现apt-get 命令还是用不了。。。思考了1分钟。。。

然后发现服务器用的是centos.......

再试了各种常用命令，试了docker相关的各种命令，都可以正常工作。

然而整个人都被吓傻了....睡了一觉才回过神。

又查了下docker volume权限的事情，发现挂载目录继承docker image中用户的权限是feature  [Volumes files have root owner when running docker with non-root user.](https://github.com/moby/moby/issues/3124)   那似乎就没办法了。

以及写了两个脚本，来避免手滑，分别是zsh环境和bash环境下的。

[kkrm](https://github.com/111qqz/kkrm)






