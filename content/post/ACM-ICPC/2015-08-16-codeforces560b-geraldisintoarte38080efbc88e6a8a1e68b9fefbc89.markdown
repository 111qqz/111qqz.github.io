---
author: 111qqz
date: 2015-08-16 22:53:00+00:00
draft: false
title: codeforces 560 B. Gerald is into Art　（模拟）
type: post
url: /2015/08/codeforces560b-geraldisintoart/
categories:
- ACM
tags:
- 模拟
---



    
    /*************************************************************************
    	> File Name: code/cf/#313/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: Wed 22 Jul 2015 09:52:54 PM CST
     ************************************************************************/
    
    #include<iostream>
    #include<iomanip>
    #include<cstdio>
    #include<algorithm>
    #include<cmath>
    #include<cstring>
    #include<string>
    #include<map>
    #include<set>
    #include<queue>
    #include<vector>
    #include<stack>
    #define y0 abc111qqz
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define tm crazy111qqz
    #define lr dying111qqz
    using namespace std;
    #define REP(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef unsigned long long ULL;
    
        int a1,b1,a2,b2,a3,b3;
    bool judge (int x2,int y2,int x3,int y3)
    {
        if (x2<=a1&&x3<=a1&&y2+y3<=b1)
    	return true;
        if (y2<=b1&&y3<=b1&&x2+x3<=a1)
    	return true;
        return false;
    }
    int main()
    {
        cin>>a1>>b1>>a2>>b2>>a3>>b3;
        if (judge(a2,b2,a3,b3)||judge(b2,a2,a3,b3)||judge(b2,a2,b3,a3)||judge(a2,b2,b3,a3))
        {
    	puts("YES");
        }
        else
        {
    	puts("NO");
        }
      
    	return 0;
    }
    



