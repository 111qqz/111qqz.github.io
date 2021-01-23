---
author: 111qqz
date: 2016-06-18 19:43:34+00:00
draft: false
title: geekos project 1 （ELF文件相关）
type: post
url: /2016/06/geekos-project-1-elf/
categories:
- 其他
tags:
- geekOS
- linux
---

一、目的
熟悉ELF文件格式，了解GeekOS系统如何将ELF格式的可执行程序装入到内存，建立内核进程并运行的实现技术。
二、流程
1、修改/geekos/elf.c文件：在函数Parse_ELF_Executable( )中添加代码，分析ELF格式的可执行文件（包括分析得出ELF文件头、程序头，获取可执行文件长度，代码段、数据段等信息），并填充Exe_Format数据结构中的域值。
2、在Linux环境下编译系统得到GeekOS镜像文件。
3、编写一个相应的bochs配置文件。
4、在bochs中运行GeekOS系统显示结果。



编译以及启动bochs同project0...
project0遇到的那些错误还是都会遇到一遍233.

然后在project1/src/geekos/ 目录下的elf.c中添加函数：int Parse_ELF_Executable(char *exeFileData, ulong_t exeFileLength,
struct Exe_Format *exeFormat)

原理部分不过多阐释，具体可见我参考的博客。

最后实现为：



    
    int Parse_ELF_Executable(char *exeFileData, ulong_t exeFileLength,
          struct Exe_Format *exeFormat)
      {
          elfHeader* header = exeFileData;
          programHeader* pHeader = (exeFileData+header->phoff);
          exeFormat->numSegments = header->phnum;
          exeFormat->entryAddr = header->entry;
          int i = 0;
          for (; i< header->phnum; i++) {
              exeFormat->segmentList[i].offsetInFile = pHeader->offset;
              exeFormat->segmentList[i].lengthInFile = pHeader->fileSize;
              exeFormat->segmentList[i].startAddress = pHeader->vaddr;
              exeFormat->segmentList[i].sizeInMemory = pHeader->memSize;
              exeFormat->segmentList[i].protFlags = pHeader->flags;
              pHeader++;
          }
          
          return 0; //!!
      
          //TODO("Parse an ELF executable image");
      }
    


**然后由于编译之后比project0多生成了一个diskc.img文件**

所以还需要相应得修改配置文件.bochsrc

最后内容如下：

    
    config_interface: textconfig
    romimage: file=/usr/share/bochs/BIOS-bochs-latest
    megs: 8
    vgaromimage: file=/usr/share/vgabios/vgabios.bin
    floppya: 1_44=./fd.img, status=inserted
    ata0: enabled=1, ioaddr1=0x1f0, ioaddr2=0x3f0, irq=14
    ata1: enabled=0, ioaddr1=0x170, ioaddr2=0x370, irq=15
    #ata2: enabled=0, ioaddr1=0x1e8, ioaddr2=0x3e0, irq=11
    #ata3: enabled=0, ioaddr1=0x168, ioaddr2=0x360, irq=9
    ata0-master: type=disk, path=./diskc.img, mode=flat, cylinders=40, heads=8, spt=64
    #ata0-slave: type=cdrom, path="/dev/cdrom", status=inserted
    boot: a
    #ips: 1000000
    log:./bochs.out
    vga_update_interval: 300000
    keyboard_serial_delay: 250
    keyboard_paste_delay: 100000
    private_colormap: enabled=0
    
    display_library: sdl


project0遇到的启动bochs的那些问题project1也会遇到一遍233



然后。。。启动。。。

报错如下：

[![选区_123](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_123.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_123.png)



查了好多。。。一无所获。。。

最后看到一遍博客： [参考博客1](http://blog.csdn.net/wu5795175/article/details/8560805)

那篇博客里虽然和我遇到的问题不一致。。。

但是死马当做活马医。。。

objdump -d a.exe 查看了反汇编代码。。。。a.exe的路径是project1/build/user/



    
    00001000 <_Entry>:
        1000:	83 ec 1c             	sub    $0x1c,%esp
        1003:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%esp)
        100a:	00 
        100b:	c7 04 24 00 00 00 00 	movl   $0x0,(%esp)
        1012:	e8 06 00 00 00       	call   101d <main>
        1017:	c9                   	leave  
        1018:	cb                   	lret   
        1019:	83 c4 1c             	add    $0x1c,%esp
        101c:	c3                   	ret    
    
    0000101d <main>:
        101d:	55                   	push   p
        101e:	89 e5                	mov    %esp,p
        1020:	83 e4 f0             	and    $0xfffffff0,%esp
        1023:	83 ec 40             	sub    $0x40,%esp
        1026:	c7 44 24 18 48 69 20 	movl   $0x21206948,0x18(%esp)
        102d:	21 
        102e:	c7 44 24 1c 20 54 68 	movl   $0x69685420,0x1c(%esp)
        1035:	69 
        1036:	c7 44 24 20 73 20 69 	movl   $0x73692073,0x20(%esp)
        103d:	73 
        103e:	c7 44 24 24 20 74 68 	movl   $0x65687420,0x24(%esp)
        1045:	65 
        1046:	c7 44 24 28 20 73 65 	movl   $0x63657320,0x28(%esp)
        104d:	63 
        104e:	c7 44 24 2c 6f 6e 64 	movl   $0x20646e6f,0x2c(%esp)
        1055:	20 
        1056:	c7 44 24 30 73 74 72 	movl   $0x69727473,0x30(%esp)
        105d:	69 
        105e:	c7 44 24 34 6e 67 0a 	movl   $0xa676e,0x34(%esp)
        1065:	00 
        1066:	c7 44 24 38 00 00 00 	movl   $0x0,0x38(%esp)
        106d:	00 
        106e:	c7 44 24 3c 00 00 00 	movl   $0x0,0x3c(%esp)
        1075:	00 
        1076:	c7 04 24 00 21 00 00 	movl   $0x2100,(%esp)
        107d:	e8 13 00 00 00       	call   1095 <ELF_Print>
        1082:	8d 44 24 18          	lea    0x18(%esp),x
        1086:	89 04 24             	mov    x,(%esp)
        1089:	e8 07 00 00 00       	call   1095 <ELF_Print>
        108e:	b8 00 00 00 00       	mov    $0x0,x
        1093:	c9                   	leave  
        1094:	c3                   	ret    
    
    00001095 <ELF_Print>:
        1095:	8b 44 24 04          	mov    0x4(%esp),x
        1099:	cd 90                	int    $0x90
        109b:	c3                   	ret


可以看到在_Entry入口处的汇编，首先

sub    $0x1c,%esp

然而程序却抢先在

add    $0x1c,%esp

之前使用leave和lret长跳转返回了，这样程序当然出错了。


我这里是将




  __asm__ __volatile__ ("leave");
__asm__ __volatile__ ("lret");




改成了







**  __asm__ __volatile__ ("add $0x1c, %esp");    （注意，原文作者这里把%esp写成$esp,坑死小白啊。。还写错两次）**




  __asm__ __volatile__ ("lret");





就能正常工作了。



[![选区_125](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_125.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/06/选区_125.png)
