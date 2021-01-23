---
author: 111qqz
date: 2017-02-28 07:21:49+00:00
draft: false
title: cpp vector学习笔记
type: post
url: /2017/02/cpp-vector/
categories:
- c++
tags:
- cpp
- vector
---

起因是百度实习二面的时候被问了一道类似这样的题：

给我下面的代码，问有没有什么问题。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年02月28日 星期二 14时49分37秒
    File Name :vector.cpp
    ************************************************ */
    #include <cstdio>
    #include <vector>
    #include <ctime>
    using namespace std;
    int func( int x ) //此处函数的条件是不单调...这样才可以触发问题.
    {
        return (x-50)*(x-50)+1;
    }
    int main()
    {
    
        vector<int>vec;
        int *pint = NULL;
        for ( int i = 0 ; i < 100 ; i++)
        {
    	int x = func(i);
    	vec.push_back(x);
    	if (x<500)
    	{
    	    pint = & vec[0];
    	}
        }
        if (pint)
    	*pint = 0 ;
        int siz = vec.size();
        for ( int i = 0  ; i < siz ; i++) printf("%d\n",vec[i]);
        return 0;
    }


面试的时候只给了部分代码，func函数没有给出。

当时没有看出问题在哪里...

后来知道了，这道题其实考的是vector的底层实现...

以下内容参考《STL源码解析》4.2章 侯捷著

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/02/無限延伸你的視野-qpdfview_011.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/02/無限延伸你的視野-qpdfview_011.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/02/無限延伸你的視野-qpdfview_012.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/02/無限延伸你的視野-qpdfview_012.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/02/無限延伸你的視野-qpdfview_013.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/02/無限延伸你的視野-qpdfview_013.png)


#### **vector是动态增加空间，但是并不是在原空间后面增加新空间（因为不能保证原空间之后是否还有可以配置的空间），而是以原大小的两倍另外配置一块较大空间，然后将原内容拷贝过来，之后才开始在原内容后面构建新内容，并释放原空间。**


**因此，对vector的任何操作，一旦引起对空间重新配置，指向原vector的所有迭代器都失效了！**

**因此，对vector的任何操作，一旦引起对空间重新配置，指向原vector的所有迭代器都失效了！**

**因此，对vector的任何操作，一旦引起对空间重新配置，指向原vector的所有迭代器都失效了！**



vector采取的是存储方式是连续线性空间，用两个迭代器start和finsh分别指向当前配置的空间中已经使用的部分的开始和结尾，用另一个迭代器end_of_storage指向当前配置的整块连续空间（包含备用部分）的尾端。

当我们用push_back()将元素插入vector尾端时，push_back()会先检查是是否还有备用空间，如果有就直接在备用空间上构建元素，并调整迭代器finsh，使vector变大。如果没有备用空间了，就扩充空间。



可以用以下代码来测试：

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年02月28日 星期二 14时33分10秒
    File Name :vector1.cpp
    ************************************************ */
    #include <cstdio>
    #include <vector>
    #include <iostream>
    using namespace std;
    int main()
    {
        vector<int>a;
        a.push_back(0);
        int lst = -1;
        for ( int i = 0 ; i < 200 ; i++)
        {
    	a.push_back(-1);
    //	if (a.capacity()!=lst)
    	printf("i:%d %d ",i,a.capacity());
    	cout<<&a[0]<<endl;
    	lst = a.capacity();
        }
        return 0;
    }


结果如下：

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/02/Guake！_014.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/02/Guake！_014.png)
