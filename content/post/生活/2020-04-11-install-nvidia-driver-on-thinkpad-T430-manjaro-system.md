---
title: "thinkpad t430 manjaro系统安装nvidia驱动"
date: 2020-04-12T07:10:14+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/Install-nvidia-Driver-on-Thinkpad-T430-Manjaro 
categories:
- 其他

tags:

- linux
---

前几天装驱动把笔记本搞崩溃了..重新装了kde桌面环境的manjaro

首先根据 [Configure NVIDIA (non-free) settings and load them on Startup](https://wiki.manjaro.org/index.php?title=Configure_NVIDIA_(non-free)_settings_and_load_them_on_Startup)

直接装驱动。 装之后mhwd -li命令会显示新安装的驱动，带有nvidia字样的。

然而发现inxi -G 命令下，nvidia GPU显示的drivier是 N/A


参考[Inxi -G in Terminal: Graphics card N/A?](https://forum.manjaro.org/t/inxi-g-in-terminal-graphics-card-n-a/56000/13)

发现需要手动load driver

执行 sudo modprobe nvidia 后发现inxi -G 命令可以找到驱动了，nvidia-smi也可以正常显示了。

接下来是设置开启加载driver.

参考[Automatic module loading with systemd](https://wiki.archlinux.org/index.php/Kernel_module#Automatic_module_loading_with_systemd)

需要修改 /etc/modules-load.d/modules.conf 

加入一行

```shell

nvidia

```

重启后发现仍然不work.

然后看到[`/etc/modules-load.d/` doesn’t load `nvidia` on boot](https://forum.manjaro.org/t/etc-modules-load-d-doesnt-load-nvidia-on-boot/109802/4)

发现原因是nvidia驱动被设置为黑名单了。 在 /usr/lib/modprobe.d/bumblebee.conf 文件中，把所有内容注释掉即可。

重新启动，发现已经可以正常加载驱动了。