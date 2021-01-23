---
author: 111qqz
date: 2016-04-09 17:41:46+00:00
draft: false
title: 'BZOJ 1641: [Usaco2007 Nov]Cow Hurdles 奶牛跨栏 (floyd)'
type: post
url: /2016/04/bzoj-1641-usaco2007-novcow-hurdles--floyd/
categories:
- ACM
tags:
- floyd
---




## 1641: [Usaco2007 Nov]Cow Hurdles 奶牛跨栏


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 531  Solved: 344
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1641)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1641)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1641)]


## Description






Farmer John 想让她的奶牛准备郡级跳跃比赛，贝茜和她的伙伴们正在练习跨栏。她们很累，所以她们想消耗最少的能量来跨栏。 显然，对于一头奶牛跳过几个矮栏是很容易的，但是高栏却很难。于是，奶牛们总是关心路径上最高的栏的高度。 奶牛的训练场中有 N (1 ≤ N ≤ 300) 个站台，分别标记为1..N。所有站台之间有M (1 ≤ M ≤ 25,000)条单向路径，第i条路经是从站台Si开始，到站台Ei，其中最高的栏的高度为Hi (1 ≤ Hi ≤ 1,000,000)。无论如何跑，奶牛们都要跨栏。 奶牛们有 T (1 ≤ T ≤ 40,000) 个训练任务要完成。第 i 个任务包含两个数字 Ai 和 Bi (1 ≤ Ai ≤ N; 1 ≤ Bi ≤ N)，表示奶牛必须从站台Ai跑到站台Bi，可以路过别的站台。奶牛们想找一条路径从站台Ai到站台Bi，使路径上最高的栏的高度最小。 你的任务就是写一个程序，计算出路径上最高的栏的高度的最小值。






## Input






行 1: 两个整数 N, M, T 行

2..M+1: 行 i+1 包含三个整数 Si , Ei , Hi 行 M+2..M+T+1: 行 i+M+1 包含两个整数，表示任务i的起始站台和目标站台: Ai , Bi






## Output






行 1..T: 行 i 为一个整数，表示任务i路径上最高的栏的高度的最小值。如果无法到达，输出 -1。






## Sample Input




5 6 3
1 2 12
3 2 8
1 3 5
2 5 3
3 4 4
2 4 8
3 4
1 2
5 1





## Sample Output




4
8
-1





## HINT







## Source






[Silver](http://www.lydsy.com/JudgeOnline/problemset.php?search=Silver)






思路：floyd.

坑成傻逼。

BZOJ用CIN/COUT会迷之RE!!!

BZOJ用CIN/COUT会迷之RE!!!

BZOJ用CIN/COUT会迷之RE!!!







 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月09日 星期六 20时39分07秒
    File Name :code/bzoj/1641.cpp
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
    const int N=305;
    int n;
    int dp[N][N];
    int m,t;
    int main()
    {
    
    	cin>>n>>m>>t;
    	//scanf("%d %d %d",&n,&m,&t);
    	ms(dp,0x3f);
    //	cout<<dp[0][0]<<endl;
    	for ( int i = 1 ; i <= m ; i++)
    	{
    	    int u,v,w;
    	    cin>>u>>v>>w;
    	   // scanf("%d %d %d",&u,&v,&w);
    	    dp[u][v] = min(dp[u][v],w);
    	}
    
    	for ( int k = 1 ; k <= n ; k++)
    	    for ( int i = 1 ; i <= n ; i++)
    		for ( int j = 1 ; j <= n ; j++)
    		    dp[i][j] = min(dp[i][j],max(dp[i][k],dp[k][j]));
    
    	while (t--)
    	{
    	    int u,v;
    	    cin>>u>>v;
    	   // scanf("%d %d",&u,&v);
    	    if (dp[u][v]==inf)  dp[u][v] = -1;
    	    cout<<dp[u][v]<<endl;
    	   // printf("%d\n",dp[u][v]);
    	}
    //  #ifndef ONLINE_JUDGE  
    //  fclose(stdin);
    //  #endif
        return 0;
    }
    



