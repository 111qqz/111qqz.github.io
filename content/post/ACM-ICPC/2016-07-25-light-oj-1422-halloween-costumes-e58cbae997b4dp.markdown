---
author: 111qqz
date: 2016-07-25 11:24:27+00:00
draft: false
title: light oj 1422 - Halloween Costumes (区间dp)
type: post
url: /2016/07/light-oj-1422-halloween-costumes-dp/
categories:
- ACM
tags:
- dp
- 区间dp
---

[light oj 1422 题目链接](http://lightoj.com/volume_showproblem.php?problem=1422)

题意：

按顺序去参加舞会。每个舞会对衣服都有要求。可以连续穿好多件衣服。需要时候就脱下来，但是一旦脱下来，这件衣服就报废了。问最少需要几件衣服。



思路：没有思路。我连这题是dp都看不出来。。知道是dp也一点思路都没。。虽然这道题是道区间dp的入门题。。。但是不怕被鄙视。。我一点也没思路。。

参考了10多篇题解。。。终于懂了一点。。

[参考博客1](http://www.cnblogs.com/pk28/p/5541904.html)
[参考博客2](http://www.cnblogs.com/neopenx/p/4050003.html)
[参考博客3](http://www.cfanz.cn/index.php?c=article&a=read&id=172173)
[参考博客4](http://www.cnblogs.com/ziyi--caolu/archive/2013/08/01/3229668.html)




<blockquote>**当a[i]和a[j]相等的时候    dp[i][j]=dp[i][j-1] 嗯，就这一个转移。然后就是区间dp的固定写法了。**</blockquote>


这句话让我恍然大悟。。。难道。。都是套路？



dp[i][j]表示的是[i,j]之间最少需要的衣服数量。

初始化dp[i][i] = 1，表示每天都换一件新衣服，显然不优。

a[i]==a[j]时，dp[i][j] = dp[i][j-1] ，表示第j天不用新换衣服，

**然后枚举划分区间的点k,分成[i,k]和[k+1,j]两部分，取所有情况中最好的（这大概就是区间dp的套路？）**








 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年07月25日 星期一 18时49分07秒
    File Name :code/loj/1422.cpp
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
    const int N=105;
    int dp[N][N];
    int a[N];
    int n;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	int T;
    	cin>>T;
    	int cas = 0 ;
    	while (T--)
    	{
    	    ms(dp,0x3f);
    	    scanf("%d",&n);
    	    for ( int i = 1 ; i <= n ; i++) dp[i][i] = 1;
    	    for ( int i = 1 ; i <= n ; i++) scanf("%d",&a[i]);
    
    	    for ( int l =  1 ; l <= n ; l++)
    		for ( int i = 1 ; i <= n ; i++ )
    		{
    		    int j = i+l;
    		    if (j>n) continue;
    		    if (a[i]==a[j]) dp[i][j] =  dp[i][j-1];
    
    		    for ( int k = i ; k < j ; k++)
    			dp[i][j] = min(dp[i][j],dp[i][k]+dp[k+1][j]);
    
    		}
    
    	    printf("Case %d: %d\n",++cas,dp[1][n]);
    	}   
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



