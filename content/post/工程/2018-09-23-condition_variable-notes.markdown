---
author: 111qqz
date: 2018-09-23 08:42:33+00:00
draft: false
title: '[C++11]std::condition_variable  notes'
type: post
url: /2018/09/condition_variable-notes/
categories:
- 其他
tags:
- c++11
- condition_variable
---

<blockquote>condition_variable 类是同步原语，能用于阻塞一个线程，或同时阻塞多个线程，直至另一线程修改共享变量（条件）并通知 condition_variable 。</blockquote>


用人话来说,condition_variable，也就是条件变量，是线程间通信的一种方式。

线程之间在很多时候需要通信，比如经典的[生产者消费者问题](https://zh.wikipedia.org/zh-hk/)

一个比较naive的方案是，用mutex来保护一个flag,然后另一线程不停得check这个flag的状态是否改变。以及在这个方案上的改进:让另一个线程check之后，可以先睡一段时间。

但是这两种方法都不够好。第一种不好的原因当然是不停得check，肯定会耗费大量的资源。而第二种，由于没办法准确估计要休眠的时间，因此不够实际。

这个时候我们可以考虑使用条件变量。

条件变量是可以用在如下场景: 一个或者多个线程在等某个条件的成立，而这个条件由另外的线程所控制。当该条件成立时，控制该条件的线程会主动通知这些线程，将这些线程唤醒。

如下是一个最简单的例子:

    
    std::mutex mut;
    std::queue<data_chunk> data_queue;  // 1
    std::condition_variable data_cond;
    
    void data_preparation_thread()
    {
      while(more_data_to_prepare())
      {
        data_chunk const data=prepare_data();
        std::lock_guard<std::mutex> lk(mut);
        data_queue.push(data);  // 2
        data_cond.notify_one();  // 3
      }
    }
    
    void data_processing_thread()
    {
      while(true)
      {
        std::unique_lock<std::mutex> lk(mut);  // 4
        data_cond.wait(
             lk,[]{return !data_queue.empty();});  // 5
        data_chunk data=data_queue.front();
        data_queue.pop();
        lk.unlock();  // 6
        process(data);
        if(is_last_chunk(data))
          break;
      }
    }


接下来是一个较为复杂的例子，一个线程安全的队列的实现,

    
    #include <queue>
    #include <memory>
    #include <mutex>
    #include <condition_variable>
    
    template<typename T>
    class threadsafe_queue
    {
    private:
      mutable std::mutex mut;  // 1 互斥量必须是可变的 
      std::queue<T> data_queue;
      std::condition_variable data_cond;
    public:
      threadsafe_queue()
      {}
      threadsafe_queue(threadsafe_queue const& other)
      {
        std::lock_guard<std::mutex> lk(other.mut);
        data_queue=other.data_queue;
      }
    
      void push(T new_value)
      {
        std::lock_guard<std::mutex> lk(mut);
        data_queue.push(new_value);
        data_cond.notify_one();
      }
    
      void wait_and_pop(T& value)
      {
        std::unique_lock<std::mutex> lk(mut);
        data_cond.wait(lk,[this]{return !data_queue.empty();});
        value=data_queue.front();
        data_queue.pop();
      }
    
      std::shared_ptr<T> wait_and_pop()
      {
        std::unique_lock<std::mutex> lk(mut);
        data_cond.wait(lk,[this]{return !data_queue.empty();});
        std::shared_ptr<T> res(std::make_shared<T>(data_queue.front()));
        data_queue.pop();
        return res;
      }
    
      bool try_pop(T& value)
      {
        std::lock_guard<std::mutex> lk(mut);
        if(data_queue.empty())
          return false;
        value=data_queue.front();
        data_queue.pop();
        return true;
      }
    
      std::shared_ptr<T> try_pop()
      {
        std::lock_guard<std::mutex> lk(mut);
        if(data_queue.empty())
          return std::shared_ptr<T>();
        std::shared_ptr<T> res(std::make_shared<T>(data_queue.front()));
        data_queue.pop();
        return res;
      }
    
      bool empty() const
      {
        std::lock_guard<std::mutex> lk(mut);
        return data_queue.empty();
      }
    };


以及，虽然现在，这样线程安全的数据结构应该早就有人封装好了，我们直接使用就行了，比如之前用过的intel tbb的[concurrent_queue](https://software.intel.com/en-us/node/506200)，不过如果对内部实现一无所知，大概没办法感觉到这种精巧之处吧。。

参考资料:

[std::condition_variable](http://www.enseignement.polytechnique.fr/informatique/INF478/docs/Cpp/en/cpp/thread/condition_variable.html)

[std::condition_variable](https://zh.cppreference.com/w/cpp/thread/condition_variable)

以及借鉴了[ c++并发编程第四章](https://www.kancloud.cn/jxm_zn/cpp_concurrency_in_action/264954#322__96)中格式化后的代码








