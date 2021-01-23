---
author: 111qqz
date: 2018-07-18 06:57:38+00:00
draft: false
title: intel tbb 学习笔记
type: post
url: /2018/07/intel-tbb-notes/
categories:
- 其他
tags:
- Threading Building Blocks
---

tbb是**Threading Building Blocks library的缩写,**是一个为开发者提供并行解决方案的库.

先放个文档https://www.threadingbuildingblocks.org/intel-tbb-tutorial

再放一个代码示例:

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年07月18日 星期三 14时20分54秒
    File Name :parallel_for.cpp
    ************************************************ */
    #include <iostream>
    #include "tbb/tbb.h"
    #include <chrono>
    
    using namespace std;
    using namespace tbb;
    
    const int N=1E9+7;
    float a[N+5];
    void Foo(float &x) { x -= 100; }
    void SerialApplyFoo( float a[], size_t n ) {
    for( size_t i=0; i!=n; ++i )
    Foo(a[i]);
    }
    
    class ApplyFoo
    {
        float *const my_a;
    
      public:
        void operator()(const blocked_range<size_t> &r) const
        {
            float *a = my_a;
            for (size_t i = r.begin(); i != r.end(); ++i)
            {
    
                Foo(a[i]);
                //printf("%.4f\n", a[i]);
            }
        }
        ApplyFoo(float a[]) : my_a(a)
        {
        }
    };
    
    void ParallelApplyFoo(float a[], size_t n)
    {
        parallel_for(blocked_range<size_t>(0, n), ApplyFoo(a));
    }
    
    void print(float a[])
    {
        for (int i = 0; i < N; i++)
            printf("%.4f%c", a[i], i == 9 ? '\n' : ' ');
    }
    int main()
    {
        for (int i = 0; i < N; i++)
            a[i] = 1. * i;
    
        auto t1 = std::chrono::high_resolution_clock::now();
        SerialApplyFoo(a,N);
    
        //ParallelApplyFoo(a, N);
        auto t2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::milli> fp_ms = t2 - t1;
         std::cout << "f() took " << fp_ms.count() << " ms, "<<std::endl;
        
        //print(a);
        return 0;
    }






编译选项为: g++ -std=c++11 parallel_for.cpp -L/home/sensetime/workspace/graph/3rdparty/tbb/lib/intel64/gcc4.7 -ltbb -o parallel_for






