---
author: 111qqz
date: 2018-07-19 10:46:26+00:00
draft: false
title: c++11 function 与bind  学习笔记
type: post
url: /2018/07/cpp11-function-bind-notes/
categories:
- 其他
tags:
- c++11
---

C++11 std::function 是一种通用、多态的函数封装,它的实例可以对任何可
以调用的目标实体进行存储、复制和调用操作

见下面的例子

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年07月19日 星期四 17时41分00秒
    File Name :bind.cpp
    ************************************************ */
    #include <functional>
    #include <iostream>
    using namespace std;
    float foo( int x,int y,int z){return x+y+z+1.;}
    int main()
    {
    	function<int(int,int)>func = foo;
    	int y = 10;
    	function<int(int)>fun = [&]( int value)->int
    	{
    		return 1+value+y;
    	};
    	cout<<func(15,4,9)<<endl;
    	cout<<fun(8)<<endl;
    	return 0;
    }


std::bind 则是用来绑定函数调用的参数的,它解决的需求是我们有时候可
能并不一定能够一次性获得调用某个函数的全部参数,通过这个函数,我们可以将
部分调用参数提前绑定到函数身上成为一个新的对象,然后在参数齐全后,完成调
用

看下面的例子:

    
    #include <iostream>
    #include <functional>
    using namespace std;
    int FUN( int x,int y,int z)
    {
    	return x+y+z;
    }
    int main()
    {
    	using namespace std::placeholders;
    	//int (*fp)(int ,int,int) = FUN;
    	auto bindfoo = bind(FUN,_1,1,2);
    	int ans = bindfoo(0);
    	cout<<ans<<endl;
    	return 0;
    }
    







