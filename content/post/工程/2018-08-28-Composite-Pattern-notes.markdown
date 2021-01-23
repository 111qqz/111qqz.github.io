---
author: 111qqz
date: 2018-08-28 06:30:59+00:00
draft: false
title: '[设计模式] 组合模式（composite） 学习笔记'
type: post
url: /2018/08/Composite-Pattern-notes/
categories:
- 其他
tags:
- 组合模式
- 设计模式
- c++
---

目的是忽略单一对象和组合对象的不同。 有点像以前写过的用链表定义一个树结构，每个节点是一个val + 多个*tree 。如果某个节点是叶子节点了，那么对应的*tree都为NULL. 只不过这里用了更加面向对象的实现。

具体看代码：

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年08月28日 星期二 14时21分51秒
    File Name :composite.cpp
    ************************************************ */
    #include <iostream>
    #include <list>
    #include <string>
    using namespace std;
    
    class Component { // 为组合中的对象声明接口，在适当情况下，实现所有类共有接口的默认行为
    protected:
        string name;
    public:
        Component(string n) { name = n; }
        virtual ~Component() {}
        virtual void Add(Component* c) = 0;
        virtual void Remove(Component* c) = 0;
        virtual void Display(int depth) = 0;
    };
    
    class Leaf : public Component { // 在组合中表示叶节点对象，叶节点没有子节点
    public:
        Leaf(string name) : Component(name) {}
        void Add(Component* c){} // 叶节点没有Add功能，但这样做能使接口具备一致性，这就是透明方式，如果不加入Add和Remove方法，那就是安全方式。
        void Remove(Component* c){} // 同上
        void Display(int depth) { cout << name << "  " << depth << endl; }
    };
    
    class Composite : public Component { // 定义有枝节点行为，用来存储子部件
    private:
        list<Component* > children;
    public:
        Composite(string name) : Component(name) {}
        void Add(Component* c) { children.push_back(c); }
        void Remove(Component* c) { children.remove(c); }
        void Display(int depth) {
            cout << name << "  " << depth << endl;
            for (auto c = children.begin(); c != children.end(); c++) {
                (*c)->Display(depth+1);
            }
        }
    };
    
    int main() { // 客户端实现代码
        Composite* root = new Composite("root");
        root->Add(new Leaf("Leaf A"));
        root->Add(new Leaf("Leaf B"));
    
        Composite* comp = new Composite("Composite X");
        comp->Add(new Leaf("Leaf XA"));
        comp->Add(new Leaf("Leaf XB"));
        root->Add(comp);
    
        Composite* comp2 = new Composite("Composite XY");
        comp2->Add(new Leaf("Leaf XYA"));
        comp2->Add(new Leaf("Leaf XYB"));
        comp->Add(comp2);
    
        root->Display(1);
    
        return 0;
    }
    




最后打印的结果为:

root 1
Leaf A 2
Leaf B 2
Composite X 2
Leaf XA 3
Leaf XB 3
Composite XY 3
Leaf XYA 4
Leaf XYB 4






