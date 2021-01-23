---
author: 111qqz
date: 2018-03-18 10:27:26+00:00
draft: false
title: cmake 学习笔记
type: post
url: /2018/03/cmake-notes/
categories:
- 其他
tags:
- cmake
- c++
---

前置技能点：

[gnu make](https://www.gnu.org/software/make/)

[linux下.so,.a,.o文件](https://111qqz.com/wordpress/2018/03/linux--o--a-so/)

cmake是一个工具，也可以看成一门语言。

<del>学习cmake最大的障碍在于看不懂全是大写的英文</del>

学习cmake主要参考了《cmake practice》

不过感觉作者有些啰嗦...不重要的东西讲了半天，重要的东西却一带而过。。。表述得也不是特别流畅。。。但是还是感谢作者的分享吧orz...

<!-- more -->

cmake的定位是**大型项目**构建工具。

目前适用于C/C++/JAVA的项目。

可以不需要自己写makefile文件。

既然cmake可以看做一门语言，那么自然就有语法。

下面只是列举一些常用的。不常用的可以用到的时候再去查。这里也会不定期补充。

cmake的语法中，对于变量大小写敏感，对于cmake的关键字大小写不敏感，不过习惯于全部大写。

cmake有两种编译方式，一种叫in source 编译（就是直接在工程目录编译）

一种叫out of source 编译，就是在工程目录下新建build,然后在build文件夹里编译。

一般都采用out of source的方式编译，这样可以使得编译得到的结果都存放在build文件夹里，不会和源代码混在一起。

set 命令用来定义变量：

SET(HELLO_SRC main.SOURCE_PATHc)

然后就可以用${HELLO_SRC}　来引用这个变量了（**例外：在if语句中，是直接使用变量名引用，而不需要${}**）

**ADD_EXECUTABLE来定义生成的可执行文件的名字：**

ADD_EXECUTABLE(hello SRC_LIST)

表示源文件是SRC_LIST 中定义的源文件列表，生成一个文件名为hello的可执行文件。

如果有多个参数，可以写成：

ADD_EXECUTABLE(hello main.c func.c)或者
ADD_EXECUTABLE(hello main.c;func.c)

**ADD_SUBDIRECTORY指令：**

ADD_SUBDIRECTORY(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
这个指令用于向当前工程添加存放源文件的子目录,并可以指定中间二进制和目标二进制存
放的位置。EXCLUDE_FROM_ALL 参数的含义是将这个目录从编译过程中排除,比如,工程
的 example,可能就需要工程构建完成后,再进入 example 目录单独进行构建(当然,你
也可以通过定义依赖来解决此类问题)。



ADD_LIBRARY(hello **SHARED** ${LIBHELLO_SRC})：生成动态(共享)库

语法为：ADD_LIBRARY(libname
[SHARED|STATIC|MODULE]
[EXCLUDE_FROM_ALL]
source1 source2 ... sourceN)

常用到的是SHARED动态库，STATIC静态库

**SET_TARGET_PROPERTIES：可以修改生成的库的名字**

**SET_TARGET_PROPERTIES(hello_static PROPERTIES OUTPUT_NAME "hello")**

**INCLUDE_DIRECTORIES：添加头文件搜寻目录**

**LINK_DIRECTORIES：为target 添加非标准的共享库搜索路径**




































