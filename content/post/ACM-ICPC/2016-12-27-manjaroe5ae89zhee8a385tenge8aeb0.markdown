---
author: 111qqz
date: 2016-12-27 04:40:53+00:00
draft: false
title: manjaro安(zhe)装(teng)记
type: post
url: /2016/12/manjarozheteng/
categories:
- 其他
---

噫。。之前x200上装的是win7+fedora25 gnome。。。

虽然感觉gnome对于09年的老电脑来说有点吃力...不过也懒得换..

结果硬盘挂了2333 于是换了块硬盘

以及被人安利了manjaro，一个基于arch的linux发行版

<del>还有就是因为平安夜又没有代码可以写又没有妹子可以陪觉得人生寂寞如雪</del>

官网下好镜像以后，一开始用dd命令做u盘，发现启动不了。

无奈到win下用了poweriso制作，成功。

安装很顺利...基本就是傻瓜操作...

装好以后...装了vim...shadowsocks...chrome...fish...搜狗输入法。。。

添加了archcn的源

发现不能切换输入法。。。

解决办法：

    
    在~/.xprofile 文件中添加如下内容
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS="@im=fcitx"


其他都挺顺利的。。

结果今天用着用着发现renkz2011这账户无法登录了。。。提示密码错误。。。

root账户是可以登录的。。。

于是我跑到root下登录。。。是可以的。。。

于是改了下renkz2011的密码。。。发现依然提示错误。。。

但是呢。。。我在root下做需要renkz2011权限的事情。。。输入密码就是没有问题的。。

我新建了一个账户。。。发现登录也没有问题。。。

奇怪啊。。。回想一下。。。我改了什么。。。

添加了archcn的源。。。

应该没关系。。。

还有就是。。。remove了zsh..?

于是我尝试着重新装回zsh...

再登录。。发现可以了。。。

回想一下。。。我在renkz2011账户下曾经设置默认shell为zsh...

卸载以后好像忘记更改了orz

但是。。。为什么和shell有关呢。。。


