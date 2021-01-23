---
author: 111qqz
date: 2016-08-25 08:58:50+00:00
draft: false
title: fedora 24 cannot modify keyboard delay and rate
type: post
url: /2016/08/fedora-24-cannot-modify-keyboard-delay-and-rate/
categories:
- 其他
tags:
- fedora
---

最近入手了x1 c

然后发现没办法支持 f22.....

没办法，只好上f24了。。。虽然明知道一堆bug...

最近发现。。之前在系统设置->键盘->打字  中的调整键盘延迟和速率的选项。。。不见了。。。

找了好久终于找到了解决办法：

    
    /××××××××××××××××××××××××××××××××××××××××××××××××/
    
    xset r rate 250 30


[![2016-08-25 16-56-37 的屏幕截图](https://111qqz.com/wordpress/wp-content/uploads/2016/08/2016-08-25-16-56-37-的屏幕截图.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/08/2016-08-25-16-56-37-的屏幕截图.png)

链接：[参考](https://superuser.com/questions/576453/cannot-modify-keyboard-delay-and-rate/576502#576502?newreg=8580befe210f4d9a98a3fe062d24016e)
