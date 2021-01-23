---
author: 111qqz
date: 2017-05-12 13:12:30+00:00
draft: false
title: 'codeforces #413 A. Carrot Cakes (模拟)'
type: post
url: /2017/05/codeforces-div2-413a/
categories:
- ACM
tags:
- math
- 模拟
---

[题目链接](http://codeforces.com/contest/799/problem/A)

题意：初始有一个锅，每t分钟可以做好k个饼，现在需要N个饼。还可以另外建一个锅，花费d时间，建好以后两个锅可以并行烙饼。问是否应该建锅？（以期减少烙饼时间）

思路：求出两种情况下的总时间，比较一下。

只有一个锅的情况很好求。

两个锅的情况比较麻烦，不如模拟时间流逝？

反正最多也就1E6的时间。。。模拟一下。。。稳。。



    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年05月11日 星期四 15时29分43秒
    File Name :A.cpp
    ************************************************ */
    
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #define PB push_back
    #define fst first
    #define sec second
    #define lson l,m,rt<<1
    #define rson m+1,r,rt<<1|1
    #define ms(a,x) memset(a,x,sizeof(a))
    typedef long long LL;
    #define pi pair < int ,int >
    #define MP make_pair
    
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int n,t,k,d;
    	int ans1,ans2;
    	cin>>n>>t>>k>>d;
    	ans1 = ((n-1)/k+1)*t;
    	int num1 = 0 ;
    	for ( int i = 1 ; i <= 200000 ; i++)
    	{
    	    if (i%t==0) num1+=k;
    	    if (num1>=n) 
    	    {
    		ans2 = i ;
    		break;
    	    }
    	    if (i>=d)
    	    {
    		int ii = i-d;
    		if (ii%t==0&&ii>0) num1+=k;
    		if (num1>=n)
    		{
    		    ans2 = i;
    		    break;
    		}
    	    }
    	}
    //	ans2+=d;
    	cout<<"ans1:"<<ans1<<"ans2:"<<ans2<<endl;
    	if (ans1>ans2) puts("YES");
    	else puts("NO");
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



