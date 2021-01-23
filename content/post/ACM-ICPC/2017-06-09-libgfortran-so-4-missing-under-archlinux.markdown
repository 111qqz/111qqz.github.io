---
author: 111qqz
date: 2017-06-09 20:12:41+00:00
draft: false
title: libgfortran.so.4 missing under archlinux
type: post
url: /2017/06/libgfortran-so-4-missing-under-archlinux/
categories:
- 其他
tags:
- archlinux
- python
---

。。。哭了哦。。终于解决了这个bug

参考资料：

[libgfortran broken? ](https://github.com/ContinuumIO/anaconda-issues/issues/686)

[libgfortran=3.0 should not be install with numpy <= 1.9](https://github.com/conda/conda/issues/2177)

[ [SOLVED] libgfortran.so.3:cannot open shared object file: No such file](https://bbs.archlinux.org/viewtopic.php?id=226849)

[Replacing gcc-libs-libs with gcc-multilib [arch](https://www.reddit.com/r/linuxquestions/comments/1oul6x/replacing_gcclibslibs_with_gccmultilib_arch/)

[conflict with gcc-libs and gcc-libs-multilib on latest update](https://bbs.archlinux.org/viewtopic.php?id=226723)

一开始以为是anaconda相关。。。搞了半天。。。

然后又按照第一个资料里。。。试图把libgfortran用libgcc替代。。

发现删掉libgfortran会同时删掉scripy...

然后又觉得。。或许是scripy有什么问题？

查了一会也没发现什么。。。

后来又想也许是dlib的问题？

看了下dlib的github,说是pip 的安装方式可能存在问题，我又用源码安装了一边，问题依旧....

然后本来打算睡觉了。。。

突然梦到。。。也许是arch的问题呢。。。

一搜果然是。。。MGJ。。。这bug出现的时间。。。貌似是2017年5月30号以后。。。（具体参照最后一个资料的日期。。。

而且这。。。谁能想到是arch的锅啊。。。更别说是这么新鲜的bug...

所以说arch是不是不适合跑深度学习，做科学计算之类的啊orz....

最后说下解决办法：

    
    :: gcc-libs 与 gcc-libs-multilib 有冲突。删除 gcc-libs-multilib 吗？ [y/N] y
    错误：无法准备事务处理 (无法满足依赖关系)
    :: gcc-multilib：移除 gcc-libs-multilib 将破坏依赖关系 'gcc-libs-multilib=6.3.1-2'
    (tensorflow) [coder@111qqz-pc github]$ sudo pacman -S gcc-libs --force
    正在解决依赖关系...
    正在查找软件包冲突...
    :: gcc-libs 与 gcc-libs-multilib 有冲突。删除 gcc-libs-multilib 吗？ [y/N] y
    错误：无法准备事务处理 (无法满足依赖关系)
    :: gcc-multilib：移除 gcc-libs-multilib 将破坏依赖关系 'gcc-libs-multilib=6.3.1-2'
    (tensorflow) [coder@111qqz-pc github]$ sudo  pacman -Qs gcc
    local/gcc-libs-multilib 6.3.1-2
        Runtime libraries shipped by GCC for multilib
    local/gcc-multilib 6.3.1-2 (multilib-devel)
        The GNU Compiler Collection - C and C++ frontends for multilib
    local/lib32-gcc-libs 6.3.1-2
        Runtime libraries shipped by GCC (32-bit)
    (tensorflow) [coder@111qqz-pc github]$ sudo pacman -Rcusn  gcc-multilib
    正在检查依赖关系...
    
    软件包 (2) libmpc-1.0.3-2  gcc-multilib-6.3.1-2
    
    全部移去体积：  119.35 MiB
    
    :: 打算删除这些软件包吗？ [Y/n] y
    :: 正在运行事务前钩子函数...
    (1/1) Removing old entries from the info directory file...
    :: 正在处理软件包的变化...
    (1/2) 正在删除 gcc-multilib                                                                                                    [#############################################################################] 100%
    (2/2) 正在删除 libmpc                                                                                                          [#############################################################################] 100%
    :: 正在运行事务后钩子函数...
    (1/1) Arming ConditionNeedsUpdate...
    (tensorflow) [coder@111qqz-pc github]$ sudo  pacman -Qs gcc
    local/gcc-libs-multilib 6.3.1-2
        Runtime libraries shipped by GCC for multilib
    local/lib32-gcc-libs 6.3.1-2
        Runtime libraries shipped by GCC (32-bit)
    (tensorflow) [coder@111qqz-pc github]$ sudo pacman -S gcc-libs
    正在解决依赖关系...
    正在查找软件包冲突...
    :: gcc-libs 与 gcc-libs-multilib 有冲突。删除 gcc-libs-multilib 吗？ [y/N] y
    
    软件包 (2) gcc-libs-multilib-6.3.1-2 [删除]  gcc-libs-7.1.1-2
    
    下载大小:   17.41 MiB
    全部安装大小：  91.50 MiB
    净更新大小：  13.06 MiB
    
    :: 进行安装吗？ [Y/n] y
    :: 正在获取软件包......
     gcc-libs-7.1.1-2-x86_64                                                                               17.4 MiB  7.15M/s 00:02 [#############################################################################] 100%
    (1/1) 正在检查密钥环里的密钥                                                                                                   [#############################################################################] 100%
    (1/1) 正在检查软件包完整性                                                                                                     [#############################################################################] 100%
    (1/1) 正在加载软件包文件                                                                                                       [#############################################################################] 100%
    (1/1) 正在检查文件冲突                                                                                                         [#############################################################################] 100%
    (2/2) 正在检查可用硬盘空间                                                                                                     [#############################################################################] 100%
    :: 正在处理软件包的变化...
    (1/1) 正在删除 gcc-libs-multilib                                                                                               [#############################################################################] 100%
    (1/1) 正在安装 gcc-libs                                                                                                        [#############################################################################] 100%
    :: 正在运行事务后钩子函数...
    (1/2) Arming ConditionNeedsUpdate...
    (2/2) Updating the info directory file...
    



