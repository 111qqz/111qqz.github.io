---
author: 111qqz
date: 2018-08-15 13:12:17+00:00
draft: false
title: 记录一次因动态库符号表可见性导致的未定义的引用(undefined reference)
type: post
url: /2018/08/Undefined-references-caused-by-dynamic-library-symbol-table-visibility/
categories:
- 其他
tags:
- 符号表
- c++
---

编译某代码，发现报错某函数未定义的引用。该函数的是先前编译得到的动态库中。

先去check了该函数的实现，还有接口与头文件中的声明是否统一。发现没有问题。

然后怀疑.cpp文件没有被编译到，于是在该函数中添加





#pragma message("******************************8")




发现的确被编译到了。




使用nm来查看动态库中的符号表，发现也可以找到这个函数的符号。







于是怀疑编译代码的时候没有链接到该动态库。




于是在make的时候打印详细信息。make VERBOSE=1




发现也的确链接了动态库....




见鬼了Orz




然后用readelf -s 来查看动态库，惊讶得发现要找的那个符号的BIND怎么是LOCAL..也就是只有文件内可见。







最后发现...是公司内部的工具和CMakeLists中的add_library冲突...




虽然这个坑的解决方案没什么价值...不过因为这个坑了解了一些之前没有了解的部分，也算值得。







关于动态库的符号可见性：




控制的原因是，如果不控制，那么不同的cpp文件可能有相同的变量名字，如果把所有的符号都暴露，很可能在链接时产生冲突。 另外一个原因是，暴露没有必要的符号，会导致符号表的size变大，从而使得link时速度变慢。













参考资料:




[Introduction to symbol visibility](https://www.ibm.com/developerworks/aix/library/au-aix-symbol-visibility/index.html)




[readelf elf文件格式分析](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/readelf.html)




[Hiding what's exposed in a shared library](http://blog.fesnel.com/blog/2009/08/19/hiding-whats-exposed-in-a-shared-library/)




[Why is the new C++ visibility support so useful?](https://gcc.gnu.org/wiki/Visibility)









