---
author: 111qqz
date: 2016-12-01 13:44:50+00:00
draft: false
title: 'codeforces #382 div 2 E. Ostap and Tree (树形dp)'
type: post
url: /2016/12/codeforces-382-div-2-e-ostap-and-tree-dp/
categories:
- ACM
tags:
- 树形dp
---

题目链接

题意：将一棵树的若干点染成黑色，要求满足对于任何一个点u,至少存在一个距离其k以内的点v被染成黑色，问染色方案数。

思路：还没完全搞懂。。。记录一些idea...

[![qq20161201213929](https://111qqz.com/wordpress/wp-content/uploads/2016/12/QQ图片20161201213929.jpg)
](https://111qqz.com/wordpress/wp-content/uploads/2016/12/QQ图片20161201213929.jpg)

[![qq20161201214138](https://111qqz.com/wordpress/wp-content/uploads/2016/12/QQ图片20161201214138.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/12/QQ图片20161201214138.png)



[参考题解](http://codeforces.com/blog/entry/48659#comment-328232)

以及：该题解中说的children指的是子树全体。。。坑死好吗。。。坑了一晚上。。气啊。




<blockquote>**定义状态f[i][j]:以i为根的子树中，能向上贡献j个单位/需要外界往内填补j个单位，方案数**

**如果是贡献，j为负数**

**转移的话，考虑不断合并子树,假如说当前处理x为根的子树**

> 
> **不妨把它的儿子按照输入顺序从左往右编号1~N**
> 
> 

> 
> **一开始到x的时候，初始状态f[x][-k] = f[x][1] = 1 **
> 
> 

> 
> 然后不断把儿子的信息合并给x
> 
> 

> 
> 做法是x与儿子枚举每一个可能的j值然后判断一下这样的状态转移后如何，添加到辅助数组里
> 
> 

> 
> 最后把辅助数组的值copy给f[x]，，
> 
> </blockquote>












    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年12月07日 星期三 02时10分34秒
    File Name :code/cf/#382/E.cpp
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
    const int MOD = 1E9+7;
    const int N=105;
    int n,k,ans,f[N][50],g[50];
    vector<int>edge[N];
    int F( int x)
    {
        return x+k;
    }
    int Add(LL x,LL y)
    {
        return (x+y)%MOD;
    }
    int Mul(LL x,LL y)
    {
        return x*y%MOD;
    }
    void dfs( int u,int pre)
    {
        f[u][F(-k)]=f[u][F(1)] = 1;
        for ( auto v:edge[u])
        {
    	if (v==pre) continue;
    	dfs(v,u);
    	ms(g,0);
    	for ( int i = -k ; i <= k ; i++)
    	{
    	    if (!f[u][F(i)]) continue;
    	    for ( int j = -k ; j <= k ; j++)
    	    {
    		int t = Mul(f[u][F(i)],f[v][F(j)]);
    		if (i<=0&&j<=0)
    		{
    		    int A = min(i,j+1);
    		    g[F(A)] = Add(g[F(A)],t);
    		}else if (i>0&&j>0)
    		{
    		    int A = max(i,j+1);
    		    g[F(A)] = Add(g[F(A)],t);
    		}else if (i<=0&&j>0)
    		{
    		    int A = (-i>=j)?i:j+1;
    		    g[F(A)] = Add(g[F(A)],t);
    		}else if (i>0&&j<=0)
    		{
    		    int A = (-j>=i)?j+1:i;
    		    g[F(A)] = Add(g[F(A)],t);
    		}
    	    }
    	}
    	memcpy(f[u],g,sizeof(g));
        }
    }
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("code/in.txt","r",stdin);
    #endif
        cin>>n>>k;
        for ( int i = 1; i < n ; i++)
        {
    	int x,y;
    	scanf("%d%d",&x,&y);
    	edge[x].push_back(y);
    	edge[y].push_back(x);
        }
        dfs(1,-1);
        for (int i =  0 ;i  <= k ; i++)
    	ans = (ans + f[1][i])%MOD;
        cout<<ans<<endl;
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
    








