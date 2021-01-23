---
author: 111qqz
date: 2018-07-10 02:26:50+00:00
draft: false
title: C++ 记录代码运行时间
type: post
url: /2018/07/Record-code-run-time-with-cpp/
categories:
- 其他
tags:
- c++11
---

以前用的办法太老土啦

看到一个since C++11的方法，我觉得比较优雅

    
    #include <iostream>
    #include <chrono>
    //#include <ratio>
    #include <thread>
     
    void f()
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
     
    int main()
    {
        auto t1 = std::chrono::high_resolution_clock::now();
        f();
        auto t2 = std::chrono::high_resolution_clock::now();
    	
        // floating-point duration: no duration_cast needed
        std::chrono::duration<double, std::milli> fp_ms = t2 - t1;
     
        // integral duration: requires duration_cast
        auto int_ms = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1);
     
        // converting integral duration to integral duration of shorter divisible time unit:
        // no duration_cast needed
        std::chrono::duration<long, std::micro> int_usec = int_ms;
     
        std::cout << "f() took " << fp_ms.count() << " ms, "
                  << "or " << int_ms.count() << " whole milliseconds "
                  << "(which is " << int_usec.count() << " whole microseconds)" << std::endl;
    }





