---
author: 111qqz
date: 2015-12-04 13:18:18+00:00
draft: false
title: 'codeforces #327 A. Wizards'' Duel'
type: post
url: /2015/12/codeforces-327-a-wizards-duel/
categories:
- ACM
tags:
- math
---

题意：一个长度为l的走廊。两个人站在两端点。互相向对方发射某种魔法。A的魔法速度为p米/秒，B的魔法速度为q米/s,魔法相遇以后会反射。反射会发射人那里会再次发射。问两种魔法第二次相遇的时候距离A的距离。
思路：由于每种魔法的速度保持肯定不变。。所以不管第几次相遇。相遇点都是同一个。。。ans=p*(p+q)/l;
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月04日 星期五 19时12分56秒
    File Name :code/cf/#327/A.cpp
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
    
    
    
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    double p,q,l;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>l>>p>>q;
    	double ans;
    	ans = p/(p+q)*l;
    	cout<<ans<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





