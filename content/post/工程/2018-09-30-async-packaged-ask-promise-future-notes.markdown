---
author: 111qqz
date: 2018-09-30 06:49:27+00:00
draft: false
title: '[c++11] std::async std::packaged_task std::promise and std::future notes'
type: post
url: /2018/09/c11-async-packaged-ask-promise-future-notes/
categories:
- 其他
tags:
- async
- c++11
- future
- packaged_task
- promise
---

把std::async,std::packaged_task,std::promise三个放在一起来说,是因为他们都可以返回一个std::future对象.简单来说,当某个线程需要等待一个特定的一次性事件(one-off event),它可以用一个"future"来表示这个事件.


## std::async


有的时候可能你需要做一个花费事件比较长的计算,但是计算结果不是立刻需要.这个时候就可以用一个新的线程来做这个计算.这里比较关键的问题是如何将在新线程进行计算的结果传回到当前线程,因为std::thread并没有提供一个类似的机制.

这个时候就需要std::async登场了.

    
    #include <future>
    #include <iostream>
    int find_the_answer_to_ltuae();
    void do_other_stuff();
    int main()
    {
    std::future<int> the_answer=std::async(find_the_answer_to_ltuae);
    do_other_stuff();
    std::cout<<"The answer is "<<the_answer.get()<<std::endl;
    }


当然也可以与向std::thread包装的thread function中传参数一样,向std::async中传参数,如下:

    
    #include <string>
    #include <future>
    struct X
    {
      void foo(int,std::string const&);
      std::string bar(std::string const&);
    };
    X x;
    auto f1=std::async(&X::foo,&x,42,"hello");  // 调用p->foo(42, "hello")，p是指向x的指针
    auto f2=std::async(&X::bar,x,"goodbye");  // 调用tmpx.bar("goodbye")， tmpx是x的拷贝副本
    struct Y
    {
      double operator()(double);
    };
    Y y;
    auto f3=std::async(Y(),3.141);  // 调用tmpy(3.141)，tmpy通过Y的移动构造函数得到
    auto f4=std::async(std::ref(y),2.718);  // 调用y(2.718)
    X baz(X&);
    std::async(baz,std::ref(x));  // 调用baz(x)
    class move_only
    {
    public:
      move_only();
      move_only(move_only&&)
      move_only(move_only const&) = delete;
      move_only& operator=(move_only&&);
      move_only& operator=(move_only const&) = delete;
      
      void operator()();
    };
    auto f5=std::async(move_only());  // 调用tmp()，tmp是通过std::move(move_only())构造得到


此外,std:;async还有一个可选参数,值为std::launch::deferred或std::launch:async或std::launch::deferred|std::launch:async,第三种为默认参数.

std::launch::async表示该task会**立即**在一个新的thread上执行.

std::launch::deferred 表示该task不会被立刻执行,而是在调用get()或者wait()的时候才会执行.这里需要注意的是,调用get()或者wait()的线程,可以是和调用async()属于同一个线程,也可以属于不同线程.

笼统来说,std::launch:deferred是一种更为灵活的方式.具体请参考[cppreference_async](https://en.cppreference.com/w/cpp/thread/async)


## std::packaged_task


std::packaged_task有点类似std::function,将要在其他线程执行的对象封装了起来。

    
    #include <iostream>
    #include <cmath>
    #include <thread>
    #include <future>
    #include <functional>
     
    // unique function to avoid disambiguating the std::pow overload set
    int f(int x, int y) { return std::pow(x,y); }
     
    void task_lambda()
    {
        std::packaged_task<int(int,int)> task([](int a, int b) {
            return std::pow(a, b); 
        });
        std::future<int> result = task.get_future();
     
        task(2, 9);
     
        std::cout << "task_lambda:\t" << result.get() << '\n';
    }
     
    void task_bind()
    {
        std::packaged_task<int()> task(std::bind(f, 2, 11));
        std::future<int> result = task.get_future();
     
        task();
     
        std::cout << "task_bind:\t" << result.get() << '\n';
    }
     
    void task_thread()
    {
        std::packaged_task<int(int,int)> task(f);
        std::future<int> result = task.get_future();
     
        std::thread task_td(std::move(task), 2, 10);
        task_td.join();
     
        std::cout << "task_thread:\t" << result.get() << '\n';
    }
     
    int main()
    {
        task_lambda();
        task_bind();
        task_thread();
    }


与std::async相比，std::packaged_task不会直接执行任务，而是需要显示调用，因此可以做到将执行函数的时机和获取future的时机分离

    
    std::packaged_task<int()> task(sleep);
    
    auto f = task.get_future();
    task(); // invoke the function
    
    // You have to wait until task returns. Since task calls sleep
    // you will have to wait at least 1 second.
    std::cout << "You can see this after 1 second\n";
    
    // However, f.get() will be available, since task has already finished.
    std::cout << f.get() << std::endl;



    
    auto f = std::async(std::launch::async, sleep);
    std::cout << "You can see this immediately!\n";
    
    // However, the value of the future will be available after sleep has finished
    // so f.get() can block up to 1 second.
    std::cout << f.get() << "This will be shown after a second!\n";




## std::promise


第一次用c++11写多线程就是用的promise[promise && future leanrning notes](https://111qqz.com/2018/08/c11-promise-future-leanrning-notes/)

个人认为std::promise与std::async或者std:;packaged_task最明显的区别是，它的值不是一个函数的返回值，而是可以通过set_value来设置，因此更加灵活。

需要注意的是，**std::promise不支持拷贝构造**，因此需要使用std::move或者传promise的指针。




## In summary




<blockquote>

> 
> 
 	  * **async**：提供最高层次的抽象。如果你不需要控制线程的运行时机，就选这个。
 	  * **packaged_task**：抽象层次比`async`低。如果你需要控制线程的运行时机，且线程执行的结果即目标结果时，选这个。
 	  * **promise**：抽象层次最低。当你想在线程中设置目标结果的值，选这个。

</blockquote>




参考资料:

[货比三家：C++ 中的 task based 并发](https://segmentfault.com/a/1190000002706259)

[What is the difference between packaged_task and async](https://stackoverflow.com/questions/18143661/what-is-the-difference-between-packaged-task-and-async)

[std::promise](https://en.cppreference.com/w/cpp/thread/promise)


