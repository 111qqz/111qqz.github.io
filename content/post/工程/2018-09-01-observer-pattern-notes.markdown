---
author: 111qqz
date: 2018-09-01 09:27:40+00:00
draft: false
title: '[设计模式] 观察者( Observer )模式学习笔记'
type: post
url: /2018/09/observer-pattern-notes/
categories:
- 其他
tags:
- 观察者模式
- 设计模式
---

最近在学习node.js，里面讲到node.js的事件机制使用了观察者模式，因此来学习一下。

观察者模式的目的是定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。

因此观察者模式又叫发布-订阅模式。

下面放一个简化之后的例子:

    
    #include <iostream>
    #include <vector>
    #include <string>
    using namespace std;
    class Secretary;
    // 看股票的同事类（观察对象，观察者）
    class StockObserver
    {
    public:
    	StockObserver(string strName, Secretary* strSub)
    	{
    		name = strName;
    		sub = strSub;
    	}
     
    	void Update();
     
    private:
    	string name;
    	Secretary* sub;我所理解的设计模式（C++实现）——观察者模式（Observer Pattern）
    };
     
    // 秘书类（主题对象，通知者）
    class Secretary
    {
     
    public:
    	string action;
    	void Add(StockObserver ob) { observers.push_back(ob); }
    	void Remove(int addIndex)
    	{
    		if(addIndex >=0 && addIndex < observers.size())
    		observers.erase(observers.begin() + addIndex);
    	}
    	void Notify()
    	{
    		vector<StockObserver>::iterator it;
    		for (it=observers.begin(); it!=observers.end(); ++it)
    		{
    			(*it).Update();
    		}
    	}
     
    private:
    	vector<StockObserver> observers;
    };
     
     
     
     
    void StockObserver::Update()
    {
    	cout << name << " : " << sub->action << ", begin to work" << endl;
    }
     
    int main()
    {
    	// 创建通知者
    	Secretary* p = new Secretary();
     
    	// 观察者
    	StockObserver* s1 = new StockObserver("Lazy", p);
    	StockObserver* s2 = new StockObserver("SnowFire", p);
     
    	// 加入通知队列
    	p->Add(*s1);
    	p->Add(*s2);
     
    	// 事件
    	p->action = "The boss is coming...";
     
    	// 通知
    	p->Notify();
     
    	// 动态删除
    	p->Remove(0);
    	
    	p->Notify();
     
    	return 0;
     
    




update:怪不得觉得熟悉，原来Qt的信号槽机制[Signals_and_slots ](https://en.wikipedia.org/wiki/Signals_and_slots)就是使用了观察者模式。

参考资料:

[观察者模式-菜鸟教程](http://www.runoob.com/design-pattern/observer-pattern.html)

[我所理解的设计模式（C++实现）——观察者模式（Observer Pattern）](https://blog.csdn.net/lcl_data/article/details/9208561)






