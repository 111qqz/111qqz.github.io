---
author: 111qqz
date: 2015-12-25 10:53:05+00:00
draft: false
title: codeforces 456 C. Boredom
type: post
url: /2015/12/codeforces-456-c-boredom/
categories:
- ACM
tags:
- dp
---

http://codeforces.com/contest/456/problem/C
题意：给出n(1E5)个数（1E5），每次可以选一个数a[k]并删掉a[k],a[k]-1,a[k]+1得到a[k]分，问最多能得到的分数。
思路：裸dp.f[i]表示选到数i的时候能达到的最大分数。开一个计数数组cnt[x]表示数字x出现的次数。那么显然有f[0]=0,f[1]=cnt[1],f[i(i>=2)] = max(f[i-1]，f[i-2]+f[i]*cnt[i]);答案为f[max(a[i])]，注意要开long long
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月25日 星期五 18时17分05秒
    File Name :code/cf/problem/455A.cpp
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
    const int N=1E5+7;
    int n ;
    int a[N];
    LL cnt[N];
    LL dp[N];
    
    bool cmp( int a,int b)
    {
        return a>b;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n;
    	ms(cnt,0);
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    scanf("%d",&a[i]);
    	    cnt[a[i]]++;
    	}
    
    	dp[0] = 0 ;  //dp[i]表示到数字i时能得到的最多分数
    	dp[1] = cnt[1];
    	for ( int i = 2 ; i <= 1E5 ; i++)
    	{
    	    dp[i] = max(dp[i-1],dp[i-2]+i*cnt[i]);
    	}
    	cout<<dp[100000]<<endl;
    	
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



