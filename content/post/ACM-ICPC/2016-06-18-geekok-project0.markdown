---
author: 111qqz
date: 2016-06-18 08:35:49+00:00
draft: false
title: geekok project0（上）（实验环境的搭建）
type: post
url: /2016/06/geekok-project0/
categories:
- 其他
tags:
- geekOS
---

apt-get install build-essential
    apt-get install bochs bochs-x nasm


此处下载的bochs应该是比较新的...如果之后遇到


<blockquote>failed assertion in init_idt :g_handlersizenoterr == g_handlersizeerr</blockquote>


这个错误，建议安装比较老的nasm版本，比如2.08.02[链接](http://www.nasm.us/pub/nasm/releasebuilds/2.08.02/)



下载geekos-0.3软件包，地址为：
[geekOS下载地址](http://sourceforge.net/projects/geekos/files/)

然后解压到~/work目录。

然后进入到 /work/geekos-0.3.0/src/project0/build 目录下

**之后的操作都是在这个目录下进行的。**





    
    
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ make depend
    Makefile:249: depend.mak: 没有那个文件或目录
    touch depend.mak
    gcc -M -O -Wall  -Werror  -g -DGEEKOS -I../include \
    		../src/geekos/idt.c ../src/geekos/int.c ../src/geekos/trap.c ../src/geekos/irq.c ../src/geekos/io.c ../src/geekos/keyboard.c ../src/geekos/screen.c ../src/geekos/timer.c ../src/geekos/mem.c ../src/geekos/crc32.c ../src/geekos/gdt.c ../src/geekos/tss.c ../src/geekos/segment.c ../src/geekos/bget.c ../src/geekos/malloc.c ../src/geekos/synch.c ../src/geekos/kthread.c ../src/geekos/main.c \
    		| perl -n -e 's,^(\S),geekos/$1,;print' \
    		> depend.mak
    gcc -M -O -Wall  -Werror  -I../include -I../include/libc  \
    		../src/common/fmtout.c ../src/common/string.c ../src/common/memmove.c \
    		| perl -n -e 's,^(\S),common/$1,;print' \
    		>> depend.mak
    


然后执行 make

    
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ make
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/idt.c -o geekos/idt.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/int.c -o geekos/int.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/trap.c -o geekos/trap.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/irq.c -o geekos/irq.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/io.c -o geekos/io.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/keyboard.c -o geekos/keyboard.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/screen.c -o geekos/screen.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/timer.c -o geekos/timer.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/mem.c -o geekos/mem.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/crc32.c -o geekos/crc32.o
    gcc -c -O -Wall  -Werror  -g -DGEEKOS -I../include ../src/geekos/gdt.c -o geekos/gdt.o
    In file included from ../src/geekos/gdt.c:11:0:
    ../include/geekos/segment.h:43:5: error: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Werror=attributes]
         uchar_t baseHigh        PACKED ;
         ^
    cc1: all warnings being treated as errors
    make: *** [geekos/gdt.o] 错误 1
    


报错，原因是编译检查过于严格。。我们修改makefile文件，取消把warning当成错误看待。

makefile 的路径就是当前路径，也就是：


<blockquote>rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ vim Makefile</blockquote>


把149行的 -Werror 去掉。

然后再次make

    
    
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ make
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/gdt.c -o geekos/gdt.o
    In file included from ../src/geekos/gdt.c:11:0:
    ../include/geekos/segment.h:43:5: warning: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Wattributes]
         uchar_t baseHigh        PACKED ;
         ^
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/tss.c -o geekos/tss.o
    In file included from ../src/geekos/tss.c:18:0:
    ../include/geekos/segment.h:43:5: warning: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Wattributes]
         uchar_t baseHigh        PACKED ;
         ^
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/segment.c -o geekos/segment.o
    In file included from ../src/geekos/segment.c:18:0:
    ../include/geekos/segment.h:43:5: warning: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Wattributes]
         uchar_t baseHigh        PACKED ;
         ^
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/bget.c -o geekos/bget.o
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/malloc.c -o geekos/malloc.o
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/synch.c -o geekos/synch.o
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/kthread.c -o geekos/kthread.o
    gcc -c -O -Wall    -g -DGEEKOS -I../include ../src/geekos/main.c -o geekos/main.o
    nasm -I../src/geekos/ -f elf  ../src/geekos/lowlevel.asm -o geekos/lowlevel.o
    gcc -c -O -Wall    -I../include -I../include/libc  ../src/common/fmtout.c -o common/fmtout.o
    gcc -c -O -Wall    -I../include -I../include/libc  ../src/common/string.c -o common/string.o
    gcc -c -O -Wall    -I../include -I../include/libc  ../src/common/memmove.c -o common/memmove.o
    ld -o geekos/kernel.exe -Ttext 0x00010000 -e Main \
    		geekos/idt.o geekos/int.o geekos/trap.o geekos/irq.o geekos/io.o geekos/keyboard.o geekos/screen.o geekos/timer.o geekos/mem.o geekos/crc32.o geekos/gdt.o geekos/tss.o geekos/segment.o geekos/bget.o geekos/malloc.o geekos/synch.o geekos/kthread.o geekos/main.o geekos/lowlevel.o common/fmtout.o common/string.o common/memmove.o
    ld: i386 architecture of input file `geekos/lowlevel.o' is incompatible with i386:x86-64 output
    common/fmtout.o：在函数‘Format_Output’中：
    fmtout.c:(.text+0xa16)：对‘__stack_chk_fail’未定义的引用
    make: *** [geekos/kernel.exe] 错误 1
    


解决办法是把makefile文件中第148行添加编译选项


<blockquote>-fno-stack-protector</blockquote>


然后把makefile文件中的100行至109行修改为如下内容
（修改了100行，106行，109行，条件编译什么的。。可能遇到依赖的库不全的情况。。。安装就好）

    
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


然后要把以前失败的清理干净。。重新编译。。。

    
    
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ make clean
    for d in geekos common libc user tools; do \
    		(cd $d && rm -f *); \
    	done
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ make depend
    gcc -m32 -M -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include \
    		../src/geekos/idt.c ../src/geekos/int.c ../src/geekos/trap.c ../src/geekos/irq.c ../src/geekos/io.c ../src/geekos/keyboard.c ../src/geekos/screen.c ../src/geekos/timer.c ../src/geekos/mem.c ../src/geekos/crc32.c ../src/geekos/gdt.c ../src/geekos/tss.c ../src/geekos/segment.c ../src/geekos/bget.c ../src/geekos/malloc.c ../src/geekos/synch.c ../src/geekos/kthread.c ../src/geekos/main.c \
    		| perl -n -e 's,^(\S),geekos/$1,;print' \
    		> depend.mak
    gcc -m32 -M -O -Wall  -fno-stack-protector   -I../include -I../include/libc  \
    		../src/common/fmtout.c ../src/common/string.c ../src/common/memmove.c \
    		| perl -n -e 's,^(\S),common/$1,;print' \
    		>> depend.mak
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ make 
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/idt.c -o geekos/idt.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/int.c -o geekos/int.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/trap.c -o geekos/trap.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/irq.c -o geekos/irq.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/io.c -o geekos/io.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/keyboard.c -o geekos/keyboard.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/screen.c -o geekos/screen.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/timer.c -o geekos/timer.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/mem.c -o geekos/mem.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/crc32.c -o geekos/crc32.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/gdt.c -o geekos/gdt.o
    In file included from ../src/geekos/gdt.c:11:0:
    ../include/geekos/segment.h:43:5: warning: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Wattributes]
         uchar_t baseHigh        PACKED ;
         ^
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/tss.c -o geekos/tss.o
    In file included from ../src/geekos/tss.c:18:0:
    ../include/geekos/segment.h:43:5: warning: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Wattributes]
         uchar_t baseHigh        PACKED ;
         ^
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/segment.c -o geekos/segment.o
    In file included from ../src/geekos/segment.c:18:0:
    ../include/geekos/segment.h:43:5: warning: ‘packed’ attribute ignored for field of type ‘uchar_t’ [-Wattributes]
         uchar_t baseHigh        PACKED ;
         ^
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/bget.c -o geekos/bget.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/malloc.c -o geekos/malloc.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/synch.c -o geekos/synch.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/kthread.c -o geekos/kthread.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -g -DGEEKOS -I../include ../src/geekos/main.c -o geekos/main.o
    nasm -I../src/geekos/ -f elf  ../src/geekos/lowlevel.asm -o geekos/lowlevel.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -I../include -I../include/libc  ../src/common/fmtout.c -o common/fmtout.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -I../include -I../include/libc  ../src/common/string.c -o common/string.o
    gcc -m32 -c -O -Wall  -fno-stack-protector   -I../include -I../include/libc  ../src/common/memmove.c -o common/memmove.o
    ld -m elf_i386 -o geekos/kernel.exe -Ttext 0x00010000 -e Main \
    		geekos/idt.o geekos/int.o geekos/trap.o geekos/irq.o geekos/io.o geekos/keyboard.o geekos/screen.o geekos/timer.o geekos/mem.o geekos/crc32.o geekos/gdt.o geekos/tss.o geekos/segment.o geekos/bget.o geekos/malloc.o geekos/synch.o geekos/kthread.o geekos/main.o geekos/lowlevel.o common/fmtout.o common/string.o common/memmove.o
    nm geekos/kernel.exe > geekos/kernel.syms
    nasm -f bin \
    		-I../src/geekos/ \
    		-DENTRY_POINT=0x`egrep 'Main$' geekos/kernel.syms |awk '{print $1}'` \
    		../src/geekos/setup.asm \
    		-o geekos/setup.bin
    perl ../scripts/pad geekos/setup.bin 512
    objcopy -R .dynamic -R .note -R .comment -S -O binary geekos/kernel.exe geekos/kernel.bin
    perl ../scripts/pad geekos/kernel.bin 512
    nasm -f bin \
    		-I../src/geekos/ \
    		-DNUM_SETUP_SECTORS=`perl ../scripts/numsecs geekos/setup.bin` \
    		-DNUM_KERN_SECTORS=`perl ../scripts/numsecs geekos/kernel.bin` \
    		../src/geekos/fd_boot.asm \
    		-o geekos/fd_boot.bin
    cat geekos/fd_boot.bin geekos/setup.bin geekos/kernel.bin > fd.img
    


编译成功。。。
检查一下：

    
    
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ ls -a
    .  ..  .bochsrc  common  depend.mak  fd.img  geekos  libc  Makefile  tools  user
    


然后启动bochs

报错：

    
    
    rkz2013@111qqz-ThinkPad-X200 ~/work/geekos-0.3.0/src/project0/build $ bochs
    ========================================================================
                           Bochs x86 Emulator 2.4.6
                 Build from CVS snapshot, on February 22, 2011
                       Compiled at Jun  8 2013, 05:16:04
    ========================================================================
    00000000000i[     ] LTDL_LIBRARY_PATH not set. using compile time default '/usr/lib/bochs/plugins'
    00000000000i[     ] BXSHARE not set. using compile time default '/usr/share/bochs'
    00000000000i[     ] reading configuration from .bochsrc
    00000000000p[     ] >>PANIC<< .bochsrc:4: vgaromimage directive malformed.
    00000000000e[CTRL ] notify called, but no bxevent_callback function is registered
    00000000000i[CTRL ] quit_sim called with exit code 1
    


因为配置文件.bochsrc 太古老了。。。路径什么的都是错的。。。

最终修改为如下：

    
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


然后继续启动。。报错：

    
    ========================================================================
                           Bochs x86 Emulator 2.4.6
                 Build from CVS snapshot, on February 22, 2011
                       Compiled at Jun  8 2013, 05:16:04
    ========================================================================
    00000000000i[     ] LTDL_LIBRARY_PATH not set. using compile time default '/usr/lib/bochs/plugins'
    00000000000i[     ] BXSHARE not set. using compile time default '/usr/share/bochs'
    00000000000i[     ] reading configuration from .bochsrc
    00000000000i[     ] lt_dlhandle is 0x2668a40
    00000000000i[PLGIN] loaded plugin libbx_x.so
    00000000000i[     ] installing x module as the Bochs GUI
    00000000000i[     ] using log file ./bochs.out
    bochs-bin: symbol lookup error: /usr/lib/bochs/plugins/libbx_x.so: undefined symbol: XpmCreatePixmapFromData
    


这是由apt-get install bochs-x 得到的 libbx_x.so不完善造成的
解决办法： 换个显示方案。


<blockquote>sudo apt-get install bochs-sdl</blockquote>


然后在.bochsrc文件中添加


<blockquote>display_library: sdl</blockquote>


再次运行bochs  。。终于可以了。。。感动

[![选区_120](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_120.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_120.png)
