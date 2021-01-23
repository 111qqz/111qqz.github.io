---
author: 111qqz
date: 2015-09-16 03:24:00+00:00
draft: false
title: 'codeforces #319 B - Modulo Sum (抽屉原理，dp)'
type: post
url: /2015/09/codeforces319b-modulosumdp/
categories:
- ACM
tags:
- 01背包
- dp
- 抽屉原理
---



背包还是理解的不够透彻．．

因为每次都是用那个一维形式的．

这道题的做法类似01背包.

此外还可以有一个优化...

当n>m的时候．．．根绝抽屉原理．．一定为yes..

复杂度可以从o(nm)优到　o(m^2)




 

    
    /*************************************************************************
    	> File Name: code/cf/#319/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月15日 星期二 19时54分44秒
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
    const int N=1E3+7;
    int n,m;
    int a[N];
    int dp[N];
    void OneZeroPack(int cost,int value)
    {
        for ( int v = m ; v--; v >=cost)
        {
    	dp[v] = max(dp[v],dp[v-cost]+value);
        }
    }
    int main()
    {
      #ifndef  ONLINE_JUDGE 
         
      #endif
        cin>>n>>m;
        if (n>=m)
        {
    	puts("YES");
    	return 0;
        }
        int k = 0;
        for ( int i = 0 ; i < n ; i++)
        {
    	int x;
    	scanf("%d",&x);
    	if (x>m) continue;  //大于背包容量的肯定直接舍去
    	k++;
    	a[k] = x;
        }
      //  for ( int i = 1 ; i <= k ; i++) cout<<"a[i]:"<<a[i]<<endl;
        for ( int i = 0 ; i <= m ; i++)
    	dp[i] = -inf;
        dp[0] = 0 ;
        for ( int i = 1 ; i <= k ; i++)
        {
    	OneZeroPack(a[i],a[i]);
        } 
        for ( int i = 0 ; i <= m ; i++) cout<<i<<" "<<dp[i]<<endl;
        if (dp[m]==-inf)
        {
    	puts("NO");
        }
        else
        {
    	puts("YES");
        }
      
      
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



