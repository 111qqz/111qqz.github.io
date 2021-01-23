---
author: 111qqz
date: 2016-06-17 04:09:37+00:00
draft: false
title: OS课设之geek os 非最终版
type: post
url: /2016/06/osgeek-os-/
categories:
- 其他
tags:
- geekOS
---

[参考了这篇博客](http://blog.csdn.net/cherylnatsu/article/details/6838459)

流程部分不再具体描述，可以参考上面的博客。

只详细给出我遇到的问题。

我的pc环境是：Linux 111qqz-ThinkPad-X200 3.16.0-38-generic #52~14.04.1-Ubuntu SMP Fri May 8 09:43:57 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux

linux mint 17.2 cinnamon

    
    apt-get install build-essential  
    apt-get install bochs bochs-x nasm


http://sourceforge.net/projects/geekos/files/ 下载geekos软件包并且解压

    
    $ cd ~/geekos-0.3.0/src/project0/build$ 
    $ make depend
    $ make
    


报错。。

解法办法：修改/home/rkz2013/geekos-0.3.0/src/project0/build

目录下的Makefile文件。



    
    CC_GENERAL_OPTS := $(GENERAL_OPTS) -Werror  改为
    CC_GENERAL_OPTS := $(GENERAL_OPTS)


make后再次出现错误：

    
    fmtout.c:(.text+0xa16)：对‘__stack_chk_fail’未定义的引用


解决办法：



    
    在project0/build 目录下的makefile文件的148行
    添加编译选项 -fno-stack-protector


然后又报错

    
    i386 architecture of input file `geekos/lowlevel.o' is incompatible with i386:x86-64 output




解决办法：

修改/home/rkz2013/geekos-0.3.0/src/project0/build目录下的Makefile的100行至109行如下。
（改动了100行，106行，109行。。。交叉编译什么的，因为做OS大作业的时候搞过这个。。。如果之前没有交叉编译过可能出现库依赖不全的情况。。。？ 缺什么安什么就好了。）

    
    100 TARGET_CC := $(TARGET_CC_PREFIX)gcc -m32                                                  
    101 
    102 # Host C compiler.  This is used to compile programs to execute on                        
    103 # the host platform, not the target (x86) platform.  On x86/ELF
    104 # systems, such as Linux and FreeBSD, it can generally be the same                        
    105 # as the target C compiler.                                                               
    106 HOST_CC := gcc -m32                                                                       
    107 
    108 # Target linker.  GNU ld is probably to only one that will work.                          
    109 TARGET_LD := $(TARGET_CC_PREFIX)ld  -m elf_i386


新建一个.bochsrc的配置文件

放入一下内容

    
    # An example .bochsrc file.
    # You will need to edit these lines to reflect your system.
    vgaromimage: file=/usr/share/vgabios/vgabios.bin
    romimage: file=/usr/share/bochs/BIOS-bochs-latest
    megs: 8
    boot: a
    floppya: 1_44=fd.img, status=inserted
    #floppya: 1_44=fd_aug.img, status=inserted
    log: ./bochs.out
    keyboard_serial_delay: 200
    vga_update_interval: 300000
    mouse: enabled=0
    private_colormap: enabled=0
    i440fxsupport: enabled=0
    # Uncomment this to write all bochs debugging messages to
    # bochs.out.  This produces a lot of output, but can be very
    # useful for debugging the kernel.
    #debug: action=report


保存在主目录下。

然后再启动bochs
再次报错

    
    
    bochs-bin: symbol lookup error: /usr/lib/bochs/plugins/libbx_x.so: undefined symbol: XpmCreatePixmapFromData
    


解决办法：

 

    
    
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libXpm.so.4






