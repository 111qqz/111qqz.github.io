---
author: 111qqz
date: 2015-12-29 05:21:06+00:00
draft: false
title: codeforces 16 C. Monitor
type: post
url: /2015/12/codeforces-16-c-monitor/
categories:
- ACM
tags:
- gcd
- 数论
---

http://codeforces.com/contest/16/problem/C
题意：给定长宽a,b和分辨率x:y,注意分辨率x:y未必是最简比。问将现有的size裁剪成比例为x:y，使得面积最大的长宽是多少。
思路：可以通过找 x,y能扩大的倍数为k，找到一个最大的k使得k*x<=a&&k;*y<=b。可以二分搞，但其实也可以不用。能扩大的最大的倍数其实就是 min(a/x,b/y). ps:收获了gcd更简单的一种写法。 直接 return b?gcd(b,a%b):a;

 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月28日 星期一 22时50分23秒
    File Name :code/cf/problem/16C.cpp
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
    LL a,b,x,y;
    LL ax=0,ay=0;
    LL ans = -1;
    LL GCD;
    LL gcd(LL a,LL b)
    {
        if (a<b) return gcd(b,a);
        if (a%b==0) return b;
        return gcd(b,a%b);
       // return b?gcd(b,a%b):a;
    }
    
    
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>a>>b>>x>>y;
    	GCD = gcd(x,y);
    	x /=GCD;
    	y /=GCD;
    	cout<<x*min(a/x,b/y)<<" "<<y*min(a/x,b/y)<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



 

    
     while ( l != r )
            {
                mid = (l+r+1)>>1;
                if ( x*mid <= a && y*mid <= b ) l = mid;
                else r = mid-1;
            }
            if ( x*l > a || y*l > b ) puts ( "0 0" );
            else printf ( "%I64d %I64d\n" , l*x , l*y );






