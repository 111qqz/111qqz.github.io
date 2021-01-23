---
author: 111qqz
date: 2018-08-23 02:45:53+00:00
draft: false
title: '[C++11] promise && future leanrning notes'
type: post
url: /2018/08/promise-future-notes/
categories:
- 其他
tags:
- c++11
- future
- promise
---

![std::promise and std::future](https://thispointer.com//wp-content/uploads/2015/06/promise.png)




用人话就是，主线程传给附属线程一个promise Object,然后主线程想要获取附属线程set给promise Object的值（也就是该线程返回的某个结果），需要通过主线程中的promise object 得到对应的future object(每个promise 对应一个 future),然后调用future 的get方法。如果附属线程没有执行作为参数传入的promise的set方法去返回结果，那么程序就会block住。

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年08月23日 星期四 10时37分07秒
    File Name :future_sample.cpp
    ************************************************ */
    
    #include <iostream>
    #include <thread>
    #include <future>
     
    void initiazer(std::promise<int> * promObj)
    {
        //std::cout<<"Inside Thread"<<std::endl;     
        for ( int i = 1 ; i <= 2000000000 ; i++);
        //promObj->set_value(35);
    }
     
    int main()
    {
        std::promise<int> promiseObj;
        std::future<int> futureObj = promiseObj.get_future();
        std::thread th(initiazer, &promiseObj);
        std::cout<<futureObj.get()<<std::endl;
        th.join();
        return 0;
    }
    




参考资料:

[C++11 Multithreading – Part 7: Condition Variables Explained](https://thispointer.com/c11-multithreading-part-8-stdfuture-stdpromise-and-returning-values-from-thread/)




