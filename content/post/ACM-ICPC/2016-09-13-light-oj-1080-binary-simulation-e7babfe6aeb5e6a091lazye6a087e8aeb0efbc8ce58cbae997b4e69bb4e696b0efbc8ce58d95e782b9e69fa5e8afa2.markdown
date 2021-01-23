---
author: 111qqz
date: 2016-09-13 17:41:49+00:00
draft: false
title: light oj 1080 Binary Simulation (线段树lazy标记，区间更新，单点查询)
type: post
url: /2016/09/light-oj-1080-binary-simulation-lazy/
categories:
- ACM
tags:
- lazy标记
- 线段树
---

[题目链接](http://vjudge.net/contest/131848#problem/A)

题意：给出一个长度为n的数列，每个位置是0或者1，给出q个操作，操作有两种类型，分别是将一段区间中反转，和询问当前某位置是0还是1

思路：lazy标记。lazy[i]记录以i节点为根节点的子树对应的区间中被翻转的次数，初始为0.然后查询的时候，根据被翻转次数的奇偶性确定答案。

wa了好多发。。。比较致命的是。。PushDown函数忘记改了。。。还按照染色的方法直接赋值的。。。然而这里是统计次数。。。所以是累加。。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :Wed 14 Sep 2016 12:59:07 AM CST
    File Name :code/loj/1080.cpp
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
    int lazy[N<<2];//记录翻转次数
    int n;
    string st;
    int a[N];
    void PushDown( int rt)
    {
        if (lazy[rt])
        {
    	lazy[rt<<1] +=lazy[rt];
    	lazy[rt<<1|1]+=lazy[rt];
    	lazy[rt] =  0;
        }
    }
    void build(int l,int r,int rt)
    {
        if (l==r)
        {
    	lazy[rt] = 0;
    	return;
        }
        int m = (l+r)>>1;
        build(lson);
        build(rson);
    }
    void update(int L,int R,int l,int r,int rt)
    {
        if (L<=l&&r<=R)
        {
    	lazy[rt]++;
    	return;
        }
        PushDown(rt);
        int m = (l+r)>>1;
        if (L<=m) update(L,R,lson);
        if (R>=m+1) update(L,R,rson);
    }
    int query( int p,int l,int r,int rt)
    {
        if (l==r) return lazy[rt];
        PushDown(rt);
        int m = (l+r)>>1;
        //int res;
        if (p<=m)  query(p,lson);
        else  query(p,rson);
      //  return res;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int T;
    	cin>>T;
    	int cas= 0 ;
    	while (T--){
    	    ms(lazy,0);
    	    ms(a,0);
    	    cin>>st;    
    	    n = st.length();
    	    for ( int i = 0 ; i < n ; i++)
    	    {
    		a[i+1] = st[i]-'0';
    	    }
    	    build(1,n,1);
    		printf("Case %d:\n",++cas);
    	    int q;
    	    cin>>q;
    	    while (q--)
    	    {
    		char opt[3];
    		int x,y;
    		scanf("%s",opt);
    		if (opt[0]=='I')
    		{
    		    scanf("%d%d",&x,&y);
    		    update(x,y,1,n,1);
    		}
    		else
    		{
    		    scanf("%d",&x);
    		    int p = query(x,1,n,1);
    		    int ans;
    		    if (p%2==1) ans = 1-a[x];
    		    else ans = a[x];
    		    printf("%d\n",ans);
    		}
    	    }
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



