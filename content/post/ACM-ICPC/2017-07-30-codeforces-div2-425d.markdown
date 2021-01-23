---
author: 111qqz
date: 2017-07-30 12:05:30+00:00
draft: false
title: 'codeforces #425 D. Misha, Grisha and Underground (dfs+rmq在线求LCA,讨论了一年)'
type: post
url: /2017/07/codeforces-div2-425d/
categories:
- ACM
tags:
- dfs
- LCA
- rmq
---

[题目链接](http://codeforces.com/contest/832/problem/D)


## 题意：


给出一棵树，以及三个点（可能重合），问两两组成的3条路径中，哪2条路径重合部分最长。


## 思路：


LCA还是一下就能想到的，rmq+dfs在线求。

然后我开始分情况讨论，讨论了一年也没讨论完，哭哭

结论是：**求出三个lca，并取深度最大的那个，就是我们要的三岔路口K，然后分别求出K到a，b，c三点的路径长度，取最大值+1就是答案。**

所以我的问题在于，没有试图往一般性的方向考虑，以为讨论一下就可以了...

这大概就是所谓的猜结论？

感性的理解的话，LCA越深，意味着另一个点到LCA的距离越远，也就是相交的路径越长

但是我的话，估计还是很难在短短不到一个小时内得出这样一般性的结论orz...

这大概就是数学方面的天赋差距把...T T

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年07月30日 星期日 15时12分34秒
    File Name :D.cpp
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
    int n,q;
    vector < pi > edge[N];
    int in[N];
    int E[2*N],R[2*N],dis[N],depth[2*N];
    int p;
    int dp[2*N][20];
    void dfs( int u,int dep,int d,int pre)
    {
    
        //  cout<<"u:"<<u<<" dep:"<<dep<<" d:"<<d<<endl;
        p++;
        E[p] = u;
        depth[p] = dep;
        R[u] = p ;
        dis[u] = d;
    
    
        int siz = edge[u].size();
        for ( int i = 0 ; i < siz ; i++)
        {
    	int v = edge[u][i].fst;
    	if (v==pre) continue;
    	dfs(v,dep+1,d+edge[u][i].sec,u);
    
    	p++;
    	E[p] = u;
    	depth[p] = dep;
        }
    }
    
    
    
    int _min( int l,int r)
    {
        if (depth[l]<depth[r]) return l;
        return r;
    }
    void rmq_init()
    {
        for ( int i = 1 ; i <= 2*n+2 ; i++) dp[i][0] = i;
    
        for ( int j = 1 ; (1<<j) <= 2*n+2 ; j++)
    	for ( int i = 1 ; i + (1<<j)-1 <= 2*n+2 ; i++)
    	    dp[i][j] = _min(dp[i][j-1],dp[i+(1<<(j-1))][j-1]);
    }
    
    int rmq_min( int l,int r)
    {
        if (l>r) swap(l,r);
        int k = 0 ;
        while (1<<(k+1)<=r-l+1) k++;
        return _min(dp[l][k],dp[r-(1<<k)+1][k]);
    }
    int D(int u,int v) //计算u,v点的距离
    {
        int LCA = E[rmq_min(R[u],R[v])];
        int res = dis[u] + dis[v] - 2*dis[LCA];
        return res;
    }
    /*
    int solve( int a,int b,int c) //a->c,b->c
    {
        int LCA = E[rmq_min(R[a],R[b])];
        int res = inf; //check分支
        printf("[%d %d] %d\n",a,b,LCA);
        printf("dis[c]:%i dis[LCA]:%i\n",dis[c],dis[LCA]);
        if (dis[LCA]>dis[c])
        {
    	int LCA3 = E[rmq_min(R[c],R[LCA])];
    
    //	if (dis[c]+D(c,LCA)==dis[LCA])
    //	    res = dis[LCA]-dis[c]+1;
    //	else
    	    if (D(c,LCA3)+D(LCA3,LCA)==D(c,LCA))
    		res = D(c,LCA)+1;
        }
        if (dis[LCA]==dis[c])
        {
    
    	if (LCA==c) res = 1;
    	else res = D(c,LCA) + 1; //直接错把LCA固定在根了。。
        }
        if (dis[LCA]<dis[c])
        {
    	int LCA1 = E[rmq_min(R[b],R[c])];
    	int LCA2 = E[rmq_min(R[a],R[c])];
    	printf("LCA1:%d LCA2:%d\n",LCA1,LCA2);
    	if (D(b,c)==D(b,a)+D(a,c))
    	{
    	    res =D(a,c)+1;
    //	    cout<<"1"<<endl;
    	}
    	else 
    	if (D(a,c)==D(a,b)+D(b,c))
    	{
    	    res = D(b,c)+1; 
    	   // cout<<"2"<<endl;
    	}
    	else 
    	if (D(LCA,a)==D(LCA,c) + D(c,a)||D(LCA,b)==D(LCA,c)+D(c,b))
    	{
    	    res  = 1; //只在c点汇合
    	  //  cout<<"3:"<<endl;
    	}
    	else
    	if (D(c,LCA1)+D(LCA1,b)==D(c,b)&&D(c,LCA)+D(LCA,b)!=D(c,b)) //在靠近b的另外分支
    	{
    	    if (D(LCA,LCA1)==dis[c]-dis[LCA1])
    	    res = D(c,LCA1)+1;
    	    else res = D(c,LCA)+1;
    	    cout<<"4:"<<endl;
    	}
    	else
    	if (D(c,LCA2)+D(LCA2,a)==D(c,a)&&D(c,LCA)+D(LCA,a)!=D(c,a))
    	{
    	    if (D(LCA,LCA2)==dis[c]-dis[LCA])
    		res = D(c,LCA2) + 1;
    	    else res = D(c,LCA)+1;
    	    cout<<"5:"<<endl;
    	}
        }
        return res;
    }
     */
    int max_dep3(int a,int b,int c)
    {
        int ret = 0;
        int mx = -1;
        if (dis[a]>mx)
        {
    	mx = dis[a];
    	ret = a;
        }
        if (dis[b]>mx)
        {
    	mx = dis[b];
    	ret = b;
        }
        if (dis[c]>mx)
        {
    	mx = dis[c];
    	ret = c;
        }
        return ret;
    }
    int max3( int a,int b, int c)
    {
        int mx = -1;
        mx = max(a,b);
        mx = max(mx,c);
        return mx;
    }
    
    int main()
    {
    #ifndef  ONLINE_JUDGE
        freopen("./in.txt","r",stdin);
    #endif
    
        ms(in,0);
        scanf("%d %d",&n,&q);
        for ( int i = 2 ; i <= n ; i++)
        {
    	int x;
    	scanf("%d",&x);
    	edge[i].push_back(make_pair(x,1));
    	edge[x].push_back(make_pair(i,1));
        }
        p = 0 ;
        dfs(1,0,0,-1);
        rmq_init();
    
        while (q--)
        {
    	int a,b,c;
    	scanf("%d%d%d",&a,&b,&c);
    	vector<int>ret;
    	int LCA = max_dep3(E[rmq_min(R[a],R[b])],E[rmq_min(R[b],R[c])],E[rmq_min(R[a],R[c])]);
    	int ans = max3(D(LCA,a),D(LCA,b),D(LCA,c))+1;
    	printf("%d\n",ans);
    //	printf("%d\n",solve(a,b,c));
        }
    #ifndef ONLINE_JUDGE
        fclose(stdin);
    #endif
        return 0;
    }
    
    





