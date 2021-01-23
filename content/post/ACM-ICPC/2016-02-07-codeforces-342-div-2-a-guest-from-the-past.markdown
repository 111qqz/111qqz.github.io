---
author: 111qqz
date: 2016-02-07 11:24:07+00:00
draft: false
title: 'codeforces #342 div 2 A. Guest From the Past'
type: post
url: /2016/02/codeforces-342-div-2-a-guest-from-the-past/
categories:
- ACM
tags:
- math
---

http://codeforces.com/contest/625/problem/A
题意：有n块钱，塑料瓶饮料a元一瓶，玻璃瓶饮料b元一瓶，退还玻璃瓶可以得到c元。问最多能买多少瓶饮料。
思路：贪心。如果塑料瓶比玻璃瓶的实际价格便宜，那么一定买塑料瓶的，否则先买玻璃瓶，再用塑料瓶填。注意一些边界的判断。。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年02月07日 星期日 17时02分32秒
    File Name :code/cf/#342/A.cpp
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
    LL a,b,c,n;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    //	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n;
    	cin>>a>>b>>c;
    	LL ans=0;
    	if (b-c>a)
    	{
    	    ans = n/a;
    	}
    	else
    	{
    	    while (n-b>=b-c)
    	    {
    		LL tmp = (n-b)/(b-c);
    		ans += tmp;
    		n-=tmp*(b-c);
    		
    	    }
    
    	    while (n>=b)
    	    {
    		LL tmp =n/b;
    		ans +=tmp;
    		n-=tmp*(b-c);
    	    }
    
    
    	ans +=n/a;
    	}
    	
    	cout<<ans<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



