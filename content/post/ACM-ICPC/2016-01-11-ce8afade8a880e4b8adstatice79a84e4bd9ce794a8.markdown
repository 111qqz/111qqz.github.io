---
author: 111qqz
date: 2016-01-11 06:55:04+00:00
draft: false
title: c语言中static的作用
type: post
url: /2016/01/cstatic/
categories:
- c++
---

一般有两个

    
    static int a;
    int b;
    void func(void)
    {
        static int c=0;
        int d;
    }


**在这里，a与b都是全局变量，二者的区别是，b可以被别的文件使用，a只能在本文件中使用，这是static对全局变量的作用。**
** c和d的区别是，d是一个自动变量，func函数执行完后，d会自动被释放。但c却不会被释放，下一次调用func函数时，c的值会保留上次的值继续使用(而不是初始值0，初始化只会在函数第一次被调用的时候执行)**
