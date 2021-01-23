---
author: 111qqz
date: 2016-04-10 08:58:22+00:00
draft: false
title: 'BZOJ 1643: [Usaco2007 Oct]Bessie''s Secret Pasture 贝茜的秘密草坪(母函数)'
type: post
url: /2016/04/bzoj-1643-usaco2007-octbessies-secret-pasture-/
categories:
- ACM
tags:
- 母函数
---




## 1643: [Usaco2007 Oct]Bessie's Secret Pasture 贝茜的秘密草坪


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 330  Solved: 278
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1643)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1643)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1643)]


## Description






农夫约翰已经从他的牧场中取得了数不清块数的正方形草皮，草皮的边长总是整数（有时农夫约翰割草皮的刀法不合适，甚至切出了边长为0的正方形草皮），他已经把草皮放在了一个奶牛贝茜已经知道的地方。 贝茜总是希望把美味的草皮放到她的秘密庄园里，她决定从这些草皮中取出恰好4块搬到她的秘密庄园中，然后把它们分成1×1的小块，组成一个面积为N(1<=N<=10,000)个单位面积的部分。 贝茜对选出这样四块草皮的方法数很感兴趣，如果她得到了一个4个单位面积的部分，那么她可以有5中不同的方法选4块草皮：(1,1,1,1),(2,0,0,0),(0,2,0,0),(0,0,0,2).顺序是有效的：(4,3,2,1)和(1,2,3,4)是不同的方法。






## Input






第一行：一个单独的整数N。






## Output






单独的一行包含一个整数，表示贝茜选四块草皮的方案数。






## Sample Input




4




## Sample Output




5








思路：母函数。把四个位置看作四个式子。每个式子的i可以取从0到i*i<=n的最大值。






 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月10日 星期日 16时34分31秒
    File Name :code/bzoj/1643.cpp
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
    const int N=1E4+7;
    int n;
    int a[N],tmp[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	scanf("%d",&n);
    	ms(tmp,0);
    	for ( int i =  0 ; i*i <= n ; i++)
    	{
    	    a[i*i] = 1;
    	}
    	for ( int i = 2 ; i <= 4 ; i++)
    	{
    	    for ( int j = 0 ; j <= n ; j++)
    	    {
    		for ( int k = 0 ; k*k+j <= n ; k++)
    		{
    		    tmp[j+k*k] += a[j];
    		}
    	    }
    
    	    for ( int j = 0 ; j <= n ; j++)
    	    {
    		a[j] = tmp[j];
    		tmp[j] = 0 ;
    	    }
    	}
    
    	printf("%d\n",a[n]);
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



