---
author: 111qqz
date: 2018-09-09 13:01:45+00:00
draft: false
title: '[c++11 ]std::move  右值引用  转移语义  完美转发 notes'
type: post
url: /2018/09/c11-stdmove-notes/
categories:
- 其他
tags:
- c++11
- move
- 右值引用
- 完美转发
- 转移语义
---

起因是在看<CplusplusConcurrencyInAction_PracticalMultithreading>，里面讲到转移一个std::thread的ownership提到了std::move.

之前[[C++11 ] std::ref&&std::reference_wrapper notes](https://111qqz.com/2018/09/c11_ref_notes/) 提到的情况是在我们想要用引用的时候却进行了拷贝，得到不符合期望的结果。现在的情况是，有些object或许是不支持拷贝构造的。比如std::unique_str,std::ifstream，这个时候如果我们需要传参数进去，就可以使用std::move来实现。比如下面这个例子:

    
    void process_big_object(std::unique_ptr<big_object>);
    std::unique_ptr<big_object> p(new big_object);
    p->prepare_data(42);
    std::thread t(process_big_object,std::move(p));


当然这只是使用std::move的一种情形，即传递不允许拷贝构造的object作为参数。

<del>另外，std::move可以更有效率地传递资源。内容之后补orz</del>

实际上std::move()的作用是传进去一个object,返回这个object的右值引用（_rvalue reference）_

首先区分左值和右值，这其实是一个c语言中就有的概念（作为区分，**右值引用**是C++11中新引入的概念）

一般来说，右值是不能被取地址的值。在C++11之前，右值是不能被引用的。

语法上为了区分C++11之前的引用（也就是左值引用&）,右值引用的符号为&&

    
    void process_value(int& i) { 
     std::cout << "LValue processed: " << i << std::endl; 
    } 
     
    void process_value(int&& i) { 
     std::cout << "RValue processed: " << i << std::endl; 
    } 
     
    int main() { 
     int a = 0; 
     process_value(a); 
     process_value(1); 
    }
    LValue processed: 0 
    RValue processed: 1


那么为什么要引入“右值引用”这个概念？ 主要有两个目的：**完美转发(Perfect Forwarding)**和**转移语义(Move Sementics)**


<blockquote>转移语义可以将资源 ( 堆，系统对象等 ) 从一个对象转移到另一个对象，这样能够减少不必要的临时对象的创建、拷贝以及销毁。转移语义是和拷贝语义相对的，可以类比文件的剪切与拷贝，当我们将文件从一个目录拷贝到另一个目录时，速度比剪切慢很多。</blockquote>


完美转发，也叫精确传递，指的是“需要将一组参数原封不动的传递给另一个函数”。

原封不动的含义是说:数值不变，左值/右值属性不变，const/non-const属性不变。

在泛型函数中，这样的需求非常普遍。

比如下面这个例子:

    
    template <typename T> void forward_value(const T& val) { 
     process_value(val); 
    } 
    template <typename T> void forward_value(T& val) { 
     process_value(val); 
    }
    
    int a = 0; 
     const int &b = 1; 
     forward_value(a); // int& 
     forward_value(b); // const int& 
    forward_value(2); // int&


在右值引用出现，模板的每个参数都必须重载两个类型，总的重载次数是指数级的orz，<del>警察听了想打人</del>

然而有了右值引用，不管模板右多少个参数，我们只需要定义一次，接受一个右值引用的参数，就能够将所有的参数类型原封不动的传递给目标函数。

    
    template <typename T> void forward_value(T&& val) { 
     process_value(val); 
    }
    
    int a = 0; 
    const int &b = 1; 
    forward_value(a); // int& 
    forward_value(b); // const int& 
    forward_value(2); // int&&




那么最后说回std::move. std::move的作用就是传入左值，返回右值引用，从而使用右值引用带来的好处（节省资源，实现完美转发等）

    
    #include <iostream>
    #include <utility>
    #include <vector>
    #include <string>
     
    int main()
    {
        std::string str = "Hello";
        std::vector<std::string> v;
     
        // 使用 push_back(const T&) 重载，
        // 表示我们将带来复制 str 的成本
        v.push_back(str);
        std::cout << "After copy, str is \"" << str << "\"\n";
     
        // 使用右值引用 push_back(T&&) 重载，
        // 表示不复制字符串；而是
        // str 的内容被移动进 vector
        // 这个开销比较低，但也意味着 str 现在可能为空。
        v.push_back(std::move(str));
        std::cout << "After move, str is \"" << str << "\"\n";
     
        std::cout << "The contents of the vector are \"" << v[0]
                                             << "\", \"" << v[1] << "\"\n";
    }
    After copy, str is "Hello"
    After move, str is ""
    The contents of the vector are "Hello", "Hello"










参考资料:



 	  * [Move Constructors and Move Assignment Operators (C++)](https://msdn.microsoft.com/en-us/library/dd293665.aspx)
 	  * [std::move](https://zh.cppreference.com/w/cpp/utility/move)
 	  * [cpluscplus_std::move](http://www.cplusplus.com/reference/utility/move/)
 	  * [右值引用与转移引用](https://www.ibm.com/developerworks/cn/aix/library/1307_lisl_c11/index.html)
 	  * [What is std::move(), and when should it be used?](https://stackoverflow.com/questions/3413470/what-is-stdmove-and-when-should-it-be-used)
 	  * [如何评价 C++11 的右值引用（Rvalue reference）特性？](https://www.zhihu.com/question/22111546)**(吐血推荐，讲得非常好）**




