---
author: 111qqz
date: 2017-05-28 04:10:35+00:00
draft: false
title: 安装win10后导致grub 引导缺失的解决办法
type: post
url: /2017/05/missing-grub-after-install-windows10/
categories:
- 其他
---

我之前是单系统manjaro，装了win10以后，grub menu直接消失不见...

ubuntu 的live cd进去，用神器boot-repair也没作用...

最后的解决办法是：



1. 用随便一个什么linux的live cd,进入live模式

2. 使用某种方法（fdisk?gparted?自己记得？）确认linux安装在哪个分区（如果有安装了多个，应该以最后一个为准）我的linux安装在了sda5

3. 挂载linux分区:

    
    sudo mount /dev/sda5 /mnt  #Replace sda5 with your partition number
    
    


4.挂载其他必要的文件夹

    
    for i in /sys /proc /run /dev; do sudo mount --bind "$i" "/mnt$i"; done
    


5:chroot进你的系统

    
    sudo chroot /mnt


6.重装并更新grub引导

    
    grub-install /dev/sda
    update-grub
    exit
    sudo reboot




完美解决！
