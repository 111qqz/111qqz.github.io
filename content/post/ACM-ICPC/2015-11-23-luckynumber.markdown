---
author: 111qqz
date: 2015-11-23 14:59:00+00:00
draft: false
title: uva 6692 Lucky Number
type: post
url: /2015/11/luckynumber/
categories:
- ACM
tags:
- 水题
---

https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid;=8&page;=show_problem&problem;=4704

题目大意是说，定义一个数的lucky number是距离i最远的j且满足（a[i]<a[j] i<j）。

问对所有数最大的lucky number是什么。

不必线段树。

我们可以先处理出a[i]的最远点。倒着扫一遍即可。

然后可以处理出大于等于a[i]的最远位置。

 

    
    /*************************************************************************
    	> File Name: code/hust/20151115/A.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年11月23日 星期一 22时13分15秒
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
    #include<cctype>
    #define fst first              
    #define sec second      
    #define lson l,m,rt<<1
    #define rson m+1,r,rt<<1|1
    #define ms(a,x) memset(a,x,sizeof(a))
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int N=1E5+6;
    typedef long long LL;
    int a[N];
    int n;
    int p[N];
    const int inf = 0x3f3f3f3f;
    int main()
    {
      #ifndef  ONLINE_JUDGE 
       freopen("in.txt","r",stdin);
      #endif
    
       int T;
       scanf("%d",&T);
       while (T--)
       {
           scanf("%d",&n);
           int mx = -1;
           for ( int i = 1 ; i <= n ; i++ ) scanf("%d",&a[i]),mx = max(mx,a[i]);
    
           
           ms(p,-1);
           for ( int i  = 1 ; i <= n ; i++)
    	   p[a[i]] = max(p[a[i]],i);   //最远的a[i]的位置
           for ( int i = mx ; i >= 1 ; i--)
    	   p[i] = max(p[i],p[i+1]);//cout<<"p[i]:"<<p[i]<<endl; //最远的>= a[i]的位置
    
    	int ans =  0;
    	for ( int i = 1 ; i <= n ; i++)
    	    ans = max(ans,p[a[i]+1]-i);
           printf("%d\n",ans);
    
       }
    
        
      
       
     #ifndef ONLINE_JUDGE  
      #endif
      fclose(stdin);
    	return 0;
    }
    



