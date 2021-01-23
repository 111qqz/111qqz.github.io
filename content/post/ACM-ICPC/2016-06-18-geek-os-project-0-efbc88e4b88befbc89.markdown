---
author: 111qqz
date: 2016-06-18 09:48:06+00:00
draft: false
title: geek OS project 0 （下）
type: post
url: /2016/06/geek-os-project-0-/
categories:
- 其他
tags:
- geekOS
---

现在我们环境已经搭好了，参考 [geekos实验环境的搭建](https://111qqz.com/wordpress/2016/06/geekok-project0/)

在main.c中新加个函数，命名为projecto,函数的代码如下：





    
    /*
     * GeekOS C code entry point
     * Copyright (c) 2001,2003,2004 David H. Hovemeyer <daveho@cs.umd.edu>
     * Copyright (c) 2003, Jeffrey K. Hollingsworth <hollings@cs.umd.edu>
     * Copyright (c) 2004, Iulian Neamtiu <neamtiu@cs.umd.edu>
     * $Revision: 1.51 $
     * 
     * This is free software.  You are permitted to use,
     * redistribute, and modify it as specified in the file "COPYING".
     */
    
    #include <geekos/bootinfo.h>
    #include <geekos/string.h>
    #include <geekos/screen.h>
    #include <geekos/mem.h>
    #include <geekos/crc32.h>
    #include <geekos/tss.h>
    #include <geekos/int.h>
    #include <geekos/kthread.h>
    #include <geekos/trap.h>
    #include <geekos/timer.h>
    #include <geekos/keyboard.h>
    
    //added by 111qqz for project 0
    void project0()
    {
        Print("To Exit hit Ctrl + d.\n");
        Print("Hello from 111qqz !\n"); 
        Print("This is a test of project0 !\n");
    
              
    
        Keycode keycode;
        while(1)
        {
            if( Read_Key(&keycode) )    //读取键盘按键状态
            {
                if(!( (keycode & KEY_SPECIAL_FLAG) || (keycode & KEY_RELEASE_FLAG)) ) //只处理非特殊按键的按下事件
                {                
                     int asciiCode = keycode &  0xff;    //低8位为Ascii码
    
                    if( (keycode & KEY_CTRL_FLAG)==KEY_CTRL_FLAG  &&  asciiCode=='d')    //按下Ctrl键
                    {
                        Print("\n---------BYE!--------\n");
                        Exit(1);                      
                    }else
                    {
                        Print("%c",(asciiCode=='\r') ? '\n' : asciiCode);
                    }
                } 
            }
        }
    }
    
    
    /*
     * Kernel C code entry point.
     * Initializes kernel subsystems, mounts filesystems,
     * and spawns init process.
     */
    void Main(struct Boot_Info* bootInfo)
    {
        Init_BSS();
        Init_Screen();
        Init_Mem(bootInfo);
        Init_CRC32();
        Init_TSS();
        Init_Interrupts();
        Init_Scheduler();
        Init_Traps();
        Init_Timer();
        Init_Keyboard();
    
    
        Set_Current_Attr(ATTRIB(BLACK, GREEN|BRIGHT));
        Print("Welcome 111qqz to GeekOS!\n");
        Set_Current_Attr(ATTRIB(BLACK, GRAY));
    
    
    
       // TODO("Start a kernel thread to echo pressed keys and print counts");
        //added by 111qqz for project 0
              struct Kernel_Thread *thread;
        thread = Start_Kernel_Thread(&project0,0,PRIORITY_NORMAL,false);
          // added for project 0 end
    
    
        /* Now this thread is done. */
        Exit(0);
    }
    
    
    
    


再修改Main函数，将TODO(“…..这一行替换为以下代码：

struct Kernel_Thread *thread;
thread = Start_Kernel_Thread(&project0,0,PRIORITY_NORMAL,false);

替换的意思是，要把TODO那一行注释掉。。。

TODO语句的定义在src/project0/include/geekos/kassert.h中

    
    #define TODO(message)					\
    do {							\
        Set_Current_Attr(ATTRIB(BLUE, GRAY|BRIGHT));	\
        Print("Unimplemented feature: %s\n", (message));	\
        while (1)						\
    	;						\
    } while (0)
    


可以看到，这是一个宏打印错误提示后，就直接进入一个死循环中，也就是执行到TODO之后程序就不会继续往下运行了，所以要继续进行调试project0就必须删除或者注释掉那条TODO。



保存代码，按上一篇文章中的方法编译，并在bochs中引导系统。
运行效果如下图所示：

[![选区_121](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_121.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_121.png)





参考博客：[参考博客1](http://blog.csdn.net/cherylnatsu/article/details/6838996)
[参考博客2](http://www.cnblogs.com/wuchang/archive/2009/06/02/geekos-project0.html)
