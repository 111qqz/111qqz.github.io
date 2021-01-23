---
author: 111qqz
date: 2017-10-29 11:24:42+00:00
draft: false
title: codeforces div 1 443  A. Short Program （位运算的理解）
type: post
url: /2017/10/codeforces-div1-443a/
categories:
- ACM
tags:
- 位运算
- 思维题
---

题目链接：

[题目链接](http://codeforces.com/contest/878/problem/A)



# **题意：**



一段程序，最多5E5个操作，每个操作的格式为 <opt,x> ，opt表示位或，位异或，位与 三种位运算的一种，x表示范围0..1023的数。现在要求将该程序化简至最多 5个操作，使得对于0..1023的输入，输出与该程序同样的结果。



# 思路 ：



关键在于想起，位运算还是按照二进制位的运算。我们考虑每位即可。

如果初始是0，现在变成了1，那么实际上我们并不确定，这个操作是xor 1 还是 or 1

因此我们需要两个初始的数，一个所有二进制位上都是0，另一个所有二进制位上都是1.

也就是0和1023

对于某个二进制位

**如果初始的 （0，1）变成了 （1，1），那么说明这个位置上的位运算是or**

**如果初始的 （0，1）变成了（1，0） 那么说明这个位置上的位运算是xor**

**如果初始的 （0，1）变成了（0，0） 那么说明这个位置上的位运算是and**

**如果初始的 （0，1）变成了（1，0） 那么说明这个位置上没有进行位运算操作。**




    
    #include <bits/stdc++.h>
    using namespace std;
    int  main()
    {
        int n;
        cin>>n;
        char opt[3];
        int x;
        int a = 0;
        int b = 1023;
        for ( int i = 1 ;  i <= n ; i++)
        {
    
            cin>>opt>>x;
            if (opt[0]=='|') a |=x,b|=x;
            if (opt[0]=='^') a^=x,b^=x;
            if (opt[0]=='&') a&=x,b&=x;
        }
    
    
        // 01  no
        // 11  or
        // 10  xor
        // 00  and
    
        int OR=0,XOR=0,AND=1023;
        for ( int i  =  0 ; i < 10 ; i++)
        {
    
            int A = (a>>i)&1;
            int B = (b>>i)&1;
     //       cout<<"A:"<<A<<" B:"<<B<<endl;
            if (A&&B) OR|=(1<<i);
            if (A&&!B) XOR|=(1<<i);
            if (!A&&!B) AND-=(1<<i);
        }
        cout<<3<<endl;
        cout<<"| "<<OR<<endl;
        cout<<"^ "<<XOR<<endl;
        cout<<"& "<<AND<<endl;
    }
    














