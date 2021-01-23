---
author: 111qqz
date: 2017-08-18 19:18:25+00:00
draft: false
title: leetcode 146. LRU Cache(list+unordered_map)
type: post
url: /2017/08/leetcode-146-lru-cache/
categories:
- 面试
tags:
- LRU
---

请实现最近最少使用缓存(Least Recently Used (LRU) cache)类,需要支持 get,
set,操作。
get 操作,给出 key,获取到相应的 value (value 为非负数),如果不存在返回-1,
如果存在此 key 算作被访问过。
set 操作,设置 key,如果 key 存在则覆盖之前的 value (此时相当于访问过一次)。
如果 key 不存在,需要进行插入操作,如果此时已经 key 的数量已经到达 capacity,
这样需要淘汰掉最近最少使用(也就是上次被使用的时间距离现在最久的)的那
一项。

要求get和set的时间复杂度都是O(1)


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年08月18日 星期五 00时00分22秒
    File Name :LRU.cpp
     ************************************************ */
    
    class LRUCache{
        private:
        //map:<key,Value>
        //Value:pair<value,time>
        //time:vector? list?
        typedef  unordered_map<int, pair<int , list<int>::iterator > >Cache;
        Cache cache;
        list<int>hit_seq; //头部最新元素，尾部最旧元素
        int siz;
    
            #define fst first 
            #define sec  second 
            #define MP make_pair
        void hit(Cache::iterator it) //access once
        {
            int key = it->fst;
            hit_seq.erase(it->sec.sec);
            hit_seq.push_front(key); //更新访问序列
            it->sec.sec = hit_seq.begin(); //更新该key的最后访问时间
    
        }
        public:
        LRUCache(int capacity) 
        {
            siz = capacity;
        }
        int get(int key) 
        {
            auto it = cache.find(key);
            if (it==cache.end()) return -1;
            hit(it);
            return it->sec.fst; 
        }
        void put(int key, int value) 
        {
            auto it = cache.find(key);
            if (it != cache.end()) hit(it);
            else
            {
            if (siz == cache.size())
            {
                cache.erase(hit_seq.back());
                //淘汰hit序列最后的，也就是最旧的
                hit_seq.pop_back();
            }
            hit_seq.push_front(key);
            }
            cache[key]=MP(value,hit_seq.begin());
    
        }
    };
    




