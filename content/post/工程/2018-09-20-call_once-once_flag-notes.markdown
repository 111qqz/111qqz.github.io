---
author: 111qqz
date: 2018-09-20 12:47:46+00:00
draft: false
title: std::call_once && std::once_flag  notes
type: post
url: /2018/09/stdcall_once-stdonce_flag-notes/
categories:
- c++
tags:
- c++11
- call_once
- once_flag
---

多线程保护数据时，一种较为特殊的情况是只需要保护资源的初始化。

资源初始化一般遵循"lazy initialization"的原则，也就是在用到该资源最近的地方再初始化。

比较容易想到的办法是用std::mutex，将资源初始化的地方锁起来，如下:

    
    std::shared_ptr<some_resource> resource_ptr;
    std::mutex resource_mutex;
    void foo()
    {
    std::unique_lock<std::mutex> lk(resource_mutex);
    if(!resource_ptr)
    {
    resource_ptr.reset(new some_resource);
    }
    lk.unlock();
    resource_ptr->do_something();
    }


这确实是一个办法。但是初始化时如果需要耗费比较多的时间，当有比较多的线程时，一个线程初始化时，其他线程会耗时间在不必要的等待上。

在c++11以后，我们可以使用std::once_flag和std::call_once来解决资源初始化时加锁的问题。**比起显示调用std::mutex的好处是，资源消耗更少。**



下面是两个例子:

    
    std::shared_ptr<some_resource> resource_ptr;
    std::once_flag resource_flag;
    b
    void init_resource()
    {
    resource_ptr.reset(new some_resource);
    }
    void foo()
    {
    std::call_once(resource_flag,init_resource);
    resource_ptr->do_something();
    }



    
    class X
    {
    private:
    connection_info connection_details;
    connection_handle connection;
    std::once_flag connection_init_flag;
    void open_connection()
    {
    connection=connection_manager.open(connection_details);
    }
    public:62
    C HAPTER 3 Sharing data between threads
    X(connection_info const& connection_details_):
    connection_details(connection_details_)
    {}
    void send_data(data_packet const& data)
    {
    std::call_once(connection_init_flag,&X::open_connection,this);
    connection.send_data(data);
    }
    data_packet receive_data()
    {
    std::call_once(connection_init_flag,&X::open_connection,this);
    return connection.receive_data();
    }
    b
    d
    c
    };


**或者更一般地，可以解决一类在多线程环境下保证某段代码只执行一次的问题。**

比如声明的一个static 变量。

参考资料:

[std::call_once](https://en.cppreference.com/w/cpp/thread/call_once)

[once_flag](https://en.cppreference.com/w/cpp/thread/once_flag)








