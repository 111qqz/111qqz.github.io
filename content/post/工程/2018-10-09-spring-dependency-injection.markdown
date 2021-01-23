---
author: 111qqz
date: 2018-10-09 07:45:17+00:00
draft: false
title: 'spring 依赖注入'
type: post
url: /2018/10/spring-dependency-injection/
categories:
- 其他
tags:
- 依赖注入
- java
- spring
---

真是个不明觉厉的术语...其实是个特别简单的概念orz

用白话讲，如果一个class A中用到了class B的实例，那么class B的实例就是class A的依赖，如果不是在class A中定义class B的实例，而是通过某个接口，将class B的实例传入classA,就叫依赖注入。

    
    public class Example { 
     // private DatabaseThingie myDatabase; 
    
     // public Example() { 
     //   myDatabase = new DatabaseThingie(); 
     // } 
    
      public Example(DatabaseThingie useThisDatabaseInstead) { 
        myDatabase = useThisDatabaseInstead; 
      }
    
      public void DoStuff() { 
        ... 
        myDatabase.GetData(); 
        ... 
      } 
    }





<blockquote>

> 
> 

> 
> 

> 
> 

依赖注入（DI）和控制反转（IOC）基本是一个意思，因为说起来谁都离不开谁。

简单来说，a依赖b，但a不控制b的创建和销毁，仅使用b，那么b的控制权交给a之外处理，这叫控制反转（IOC），而a要依赖b，必然要使用b的instance，那么

> 
> 
 	  1. 通过a的接口，把b传入；
 	  2. 通过a的构造，把b传入；
 	  3. 通过设置a的属性，把b传入；

这个过程叫依赖注入（DI）。

那么什么是IOC Container？

随着DI的频繁使用，要实现IOC，会有很多重复代码，甚至随着技术的发展，有更多新的实现方法和方案，那么有人就把这些实现IOC的代码打包成组件或框架，来避免人们重复造轮子。

所以实现IOC的组件或者框架，我们可以叫它IOC Container。


> 
> 

> 
> 

> 
> 

> 
> 

> 
> 
作者：phoenix
链接：https://www.zhihu.com/question/32108444/answer/220819349
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
> 
> </blockquote>


参考资料:

[Dependency Injection Demystified](https://www.jamesshore.com/Blog/Dependency-Injection-Demystified.html)

[What is dependency injection?](https://stackoverflow.com/questions/130794/what-is-dependency-injection)






