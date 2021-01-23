---
author: 111qqz
date: 2016-09-13 09:41:38+00:00
draft: false
title: light oj 1045 Digits of Factorial (k进制数的位数)
type: post
url: /2016/09/digits-of-factorial-k/
categories:
- ACM
tags:
- log
- math
---

[题目链接](http://vjudge.net/problem/26765)
题意：求n！在k进制表示下有多少位。
思路：答案为[ log(1)+log(2)+...+log(N) ]+1  其中log的底数都是K

由于有多组数据，预处理一个log的前缀和。



    
    /* ***********************************************
    Author :111qqz
    Created Time :Tue 13 Sep 2016 05:13:15 PM CST
    File Name :code/loj/1045.cpp
    ************************************************ */
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <set>-digits-of-factorial-k进制数的位
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
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
    const int N=1E6+7;
    int n;
    int base;
    double sum[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	sum[0] = 0 ;
    	for ( int i = 1 ; i < N ; i++) sum[i] = sum[i-1] + log(i);
    	int T;
    	cin>>T;
    	int cas = 0 ;
    	while (T--)
    	{
    	    scanf("%d%d",&n,&base);
    	    double ans = sum[n]/log(base)+1;
    	    printf("Case %d: %d\n",++cas,int(ans));
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



