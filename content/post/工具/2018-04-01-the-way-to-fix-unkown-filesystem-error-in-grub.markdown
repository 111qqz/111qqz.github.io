---
author: 111qqz
date: 2018-04-01 06:28:30+00:00
draft: false
title: 'linux/win双系统 更新win后 grub 出现 Error: unknown filesystem 的解决办法'
type: post
url: /2018/04/the-way-to-fix-unkown-filesystem-error-in-grub/
categories:
- 其他
tags:
- grub
- linux
---

windows自己更新把grub更新挂了....

更新的时候要重启几次,重启一次挂一次...

讲真,windows(或者说win10?) 是我见过的最辣鸡的OS了...  自己把自己弄挂这事不是一两次了.

下面说修复办法:

先ls,得到一堆诸如(hd0,gpt7) 这种

然后选设X=第一个(x,y)形式的输出

之后


    
    <code>set root=X
    set prefix=X/boot/grub
    insmod normal
    normal
    </code>



然后记得要进入linux分区.....
执行:
sudo update-grub
sudo grub-install /dev/sda



# 总结:**珍爱生命,远离辣鸡windows!!!!!**





# **珍爱生命,远离辣鸡windows!!!!!**





# **珍爱生命,远离辣鸡windows!!!!!**




