---
author: 111qqz
date: 2016-03-08 08:56:54+00:00
draft: false
title: 'codeforces #345 div 2 C. Watchmen (容斥)'
type: post
url: /2016/03/codeforces-345-div-2-c-watchmen-/
categories:
- ACM
tags:
- 容斥原理
---

[题目链接](http://codeforces.com/contest/651/problem/C)
题意：求曼哈顿距离和平方根距离相等的点的对数？
思路：化简发现是绝对值乘积等于0，容斥搞搞。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年03月07日 星期一 18时43分02秒
    File Name :code/C.cpp
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
    const int N=2E6+7;
    
    struct node
    {
        int x,y;
    
        bool operator < (node b)const
        {
    	if (x==b.x) return y<b.y;
    	return x<b.x;
        }
    }p[N];
    
    
    
    bool cmp( node a,node b)
    {
        return a.y<b.y;
    }
    LL cal( LL x)
    {
        LL res = x*(x+1)/2;
        return res;
    }
    int n;
    LL a,b,c;
    LL cnta,cntb,cntc;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	ios::sync_with_stdio(false);
    	cin>>n;
    	for ( int i = 1 ;i  <= n ; i++) cin>>p[i].x>>p[i].y;
    
    	sort(p+1,p+n+1);
    
    	a=b=c=0LL;
    	cnta=cntb=cntc=0LL;
    
    
    	for ( int i = 1 ; i <= n-1 ; i++)
    	{
    	    if (p[i].x==p[i+1].x)
    	    {
    		cnta++;
    	    }
    	    else
    	    {
    		a+=cal(cnta);
    		cnta = 0 ;
    	    }
    	}
    	a +=cal(cnta);
    
    
    	for ( int i = 1 ; i <= n-1 ; i++)
    	{
    	    if (p[i].x==p[i+1].x&&p[i].y==p[i+1].y)
    	    {
    		cntc++;
    	    }
    	    else
    	    {
    		c +=cal(cntc);
    		cntc = 0 ;
    	    }
    	}
    
    	c+=cal(cntc);
    
    
    
    	sort(p+1,p+n+1,cmp);
    	for ( int i =  1 ; i  <= n-1 ; i ++)
    	{
    	    if (p[i].y==p[i+1].y)
    	    {
    		cntb++;
    	    }
    	    else
    	    {
    		b +=cal(cntb);
    		cntb = 0 ;
    	    }
    	}
    	b +=cal(cntb);
    
    	LL ans=0LL;
    	ans = a+b-c;
    	cout<<ans<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }




