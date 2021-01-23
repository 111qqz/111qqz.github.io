---
author: 111qqz
date: 2017-05-16 06:40:03+00:00
draft: false
title: g++ 编译多个源文件（转载）
type: post
url: /2017/05/g++-compile-multi-file/
categories:
- 其他
tags:
- g++
---

[参考资料](http://www.cnblogs.com/haimingwey/archive/2012/04/15/2451008.html)




一. 常用编译命令选项
假设源程序文件名为test.c。

1. 无选项编译链接
用法：#gcc test.c
作用：将test.c预处理、汇编、编译并链接形成可执行文件。这里未指定输出文件，默认输出为a.out。

2. 选项 -o
用法：#gcc test.c -o test
作用：将test.c预处理、汇编、编译并链接形成可执行文件test。-o选项用来指定输出文件的文件名。

3. 选项 -E
用法：#gcc -E test.c -o test.i
作用：将test.c预处理输出test.i文件。

4. 选项 -S
用法：#gcc -S test.i
作用：将预处理输出文件test.i汇编成test.s文件。

5. 选项 -c
用法：#gcc -c test.s
作用：将汇编输出文件test.s编译输出test.o文件。

6. 无选项链接
用法：#gcc test.o -o test
作用：将编译输出文件test.o链接成最终可执行文件test。

7. 选项-O
用法：#gcc -O1 test.c -o test
作用：使用编译优化级别1编译程序。级别为1~3，级别越大优化效果越好，但编译时间越长。

二. 多源文件的编译方法

如果有多个源文件，基本上有两种编译方法：
[假设有两个源文件为test.c和testfun.c]

1. 多个文件一起编译
**用法：#gcc testfun.c test.c -o test **
**作用：将testfun.c和test.c分别编译后链接成test可执行文件。**

**2. 分别编译各个源文件，之后对编译后输出的目标文件链接。 **
**用法： **
**#gcc -c testfun.c //将testfun.c编译成testfun.o **
**#gcc -c test.c //将test.c编译成test.o **
**#gcc -o testfun.o test.o -o test //将testfun.o和test.o链接成test**

**以上两种方法相比较，第一中方法编译时需要所有文件重新编译，而第二种方法可以只重新编译修改的文件，未修改的文件不用重新编译。**

3. 如果要编译的文件都在同一个目录下，可以用通配符gcc *.c -o 来进行编译。

你是否会问，如果是一个项目的话，可能会有上百个文件，这样的编译法，人不是要累死在电脑前吗，或者等到你编译成功了，岂不是头发都白了，呵呵，所以我们要把上述的编译过程写进以下一个文本文件中：
Linux下称之为makefile
#这里可以写一些文件的说明
MyFirst: MyFirst.o hello.o
g++ MyFirst.o hello.o -o MyFirst
Hello.o:Hello.cpp
g++ -c Hello.cpp -o Hello.o
MyFirst.o:MyFirst.cpp
g++ -c MyFirst.cpp -o MyFirst.o
makefile 编写规则：
（1）以“＃”开始的行为注释
（2）文件依赖关系为：
target:components
rule
存盘为MyFirst，在终端输入：make MyFist，程序出现了错误可是所有程序员共同的敌人，在编写程序时我们应该尽量的去避免错误的出现，不过编写的时候再怎么都不可避免的出现这样那样的错误，对程序 进行必要的调试是一个好主意，那我们怎么来调试程序呢，看下面：
gdb ./文件名 ////////////////在这里我修改下要想下面可以调试，在上面编译的 时候必须加上参数g，g++ -g hello.cpp -o hello
以下为调试状态下的可以用到的命令（可以仅输入单词的输入，如break可简为b），尖括号中为说明
list <显示源代码>
break 行号 <设置断点>
run <运行程序>
continue <继续从断点处执行>
print 变量 <调试时查看变量的值>
del 行号 <删除断点>
step <单步执行，可跟踪到函数内部>
next <单步执行，不可跟踪到函数内部>
quit <退出>
makefile 的编写不是件容易的事情，因为自己写的makefile可能不能在所有的unix/linux类操作系统下通用。因此在很多项目中都用automake.autoconf或者是Cmake等工具。








