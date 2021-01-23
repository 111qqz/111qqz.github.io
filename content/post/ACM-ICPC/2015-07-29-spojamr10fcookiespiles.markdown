---
author: 111qqz
date: 2015-07-29 13:51:00+00:00
draft: false
title: SPOJ AMR10F Cookies Piles
type: post
url: /2015/07/spojamr10fcookiespiles/
categories:
- ACM
---

## AMR10F - Cookies Piles







水.



  ```c++  

    
    /*************************************************************************
    	> File Name: code/2015summer/#4/F.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年07月29日 星期三 21时47分23秒
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
    const int inf = 0x7fffffff;
    int main()
    {
        int T;
        int n,a,d;
        cin>>T;
        while (T--)
        {
    	scanf("%d %d %d",&n,&a,&d);
    	cout<<n*a+n*(n-1)/2*d<<endl;
        }
      
    	return 0;
    }
    


```
