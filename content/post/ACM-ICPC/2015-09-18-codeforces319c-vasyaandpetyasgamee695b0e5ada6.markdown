---
author: 111qqz
date: 2015-09-18 12:46:00+00:00
draft: false
title: 'codeforces #319 C - Vasya and Petya''s Game  (数学)'
type: post
url: /2015/09/codeforces319c-vasyaandpetyasgame/
categories:
- ACM
tags:
- math
---




因为每一个正整数可以唯一分解质因数...




要看能猜多少次，只要知道不大于n的质因子数有多少个即可（相同的算多




由于n才是１０００．所以素数表随便搞就好....不用筛也行...


 

    
    /*************************************************************************
    	> File Name: code/cf/#319/C.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月18日 星期五 20时29分00秒
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
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define ms(a,x) memset(a,x,sizeof(a))
    #define lr dying111qqz
    using namespace std;
    #define For(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef double DB;
    const int inf = 0x3f3f3f3f;
    const int N=1E3+5;
    int pri[N];
    int cnt;
    int n;
    int ans[N];
    bool prime( int x)
    {
        if (x<=3) return true;
        for ( int i = 2 ; i *i <= x ; i++)
        {
    	if (x%i==0) return false;
        }
        return true;
    }
    int main()
    {
      #ifndef  ONLINE_JUDGE 
      //  freopen("in.txt","r",stdin); 
      #endif
        ms(pri,0);
        cnt  = 0 ;
    
        for ( int i = 2 ; i <= 1005 ; i++)
        {
    	if (prime(i))
    	{
    	    cnt++;
    	    pri[cnt] = i ;
    	}
        }
        scanf("%d",&n);
        ms(ans,0);
        int num = 0 ;
        for ( int i = 1 ; pri[i] <= n&&i<=cnt ; i++)
        {
    	int tmp = pri[i];
    	while (tmp<=n)
    	{
    	    num++;
    	    ans[num] = tmp;
    	    tmp = tmp * pri[i];
    	    
    	}
        }
        cout<<num<<endl;
        for ( int i = 1 ; i <= num  ; i++)
        {
    	cout<<ans[i]<<" ";
        }
    
      
      
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



