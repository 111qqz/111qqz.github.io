---
author: 111qqz
date: 2015-08-16 20:34:00+00:00
draft: false
title: codeforces 520 B. Two Buttons  (bfs)
type: post
url: /2015/08/codeforces520b-twobuttonsbfs/
categories:
- ACM
tags:
- bfs
---




做过一道类似的题




因为是问最短，很容易想到是bfs




对于点x，可以到达点x-1,和点2*x




需要注意的是上界限。




并不是max(m,n)




因为可能先达到比m大，之后再减回来的情况是更优的。




max(2*m,2*n)肯定是足够的


 

    
    /*************************************************************************
    	> File Name: code/cf/#295/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月17日 星期一 04时16分51秒
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
    const int N=1E4+7;
    int n,m;
    int d[N];
    int mx;
    
    void bfs()
    {
        memset(d,-1,sizeof(d));
        d[n] = 0 ;
        queue<int>q;
        q.push(n);
        while (!q.empty())
        {
    	int px = q.front();q.pop();
    	if (px==m)
    	{
    	    cout<<d[m]<<endl;
    	    return;
    	}
    
    	int nxt[2];
    	nxt[0] = px - 1;
    	nxt[1] = 2*px;
    	for ( int i = 0 ; i < 2 ; i++)
    	{
    	    if (nxt[i]>=1&&nxt[i]<=mx&&d[nxt[i]]==-1)
    	    {
    		d[nxt[i]] = d[px] + 1;
    		q.push(nxt[i]);
    	    }
    	}
        }
    }
    int main()
    {
        scanf("%d %d",&n,&m);
        mx = max(n,m);
        bfs();
    
      
    return 0;
    }
    



