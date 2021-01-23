---
author: 111qqz
date: 2016-01-01 13:06:32+00:00
draft: false
title: codeforces goodbye 2015 A. New Year and Days
type: post
url: /2016/01/codeforces-goodbye-2015-a-new-year-and-days/
categories:
- ACM
tags:
- 水题
---

http://codeforces.com/contest/611/problem/A
题意：两种查询，一种是 x of week,x为1.。7,对应输出2016年星期x有多少天。另一种为x of month ，对应输出2016年至少有x天的月份有多少天。
思路：直接搞。。。。竟然脑残被hack了。。。sad.
 

    
    
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    
    using namespace std;
    const int inf = 0x3f3f3f3f;
    int x;
    char st[25],nouse[33];
    int main()
    {
    	
    	scanf("%d %s %s",&x,nouse,st);
    	if (st[0]=='w')
    	{
    	    if (x==6||x==5)
    	    {
    		cout<<53<<endl;
    	    }
    	    else
    	    {
    		cout<<52<<endl;
    	    }
    
    	}
    	else
    	{
    	    if (x<=29)
    	    {
    		puts("12");
    	    }
    	    else if (x<=30)
    	    {
    		puts("11");
    	    }
    	    else
    	    {
    		puts("7");
    	    }
    	}
    
        return 0;
    }
    



