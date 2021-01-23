---
author: 111qqz
date: 2017-10-25 13:09:31+00:00
draft: false
title: 'codeforces #346 div 2 E. New Reform (和图有关的的计数)'
type: post
url: /2017/10/codeforces-346-div2-e/
categories:
- ACM
tags:
- 计数问题
---

# 题意：



给出n个点，条边的无向图，无重边，无自环。现在要求把所有的无向边换成有向边，使得入度为0的点最少。问最少的入度为0的点是多少。



# 思路：



对于每个联通快，如果有环，我们可以顺时针连接环上的点，以指向环的方向连接联通快上的其他点，这样就可以保证所有点的入度都不为0. 如果是树形结构，则不可避免得使得一个点的入度为0.

因此对于有环的联通块答案为0，没环的答案为1.




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年10月25日 星期三 20时57分54秒
    File Name :E.cpp
    ************************************************ */
    
    #include <bits/stdc++.h>
    #define PB push_back
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
    const int N = 1E5+7;
    vector <int>edge[N];
    bool vis[N];
    
    bool dfs( int u,int pre)
    {
        vis[u] = true;
     //   cout<<"u:"<<u<<" pre:"<<pre<<endl;
        int siz = edge[u].size();
        for ( int i = 0 ; i < siz ; i++)
        {
        int v  =  edge[u][i];
        if (v==pre) continue; //无向边
        if (vis[v]||dfs(v,u)) return true;
        }
        return false;
    }
    int n,m;
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
    
        ms(vis,false);
        cin>>n>>m;
        while (m--)
        {
            int x,y;
            scanf("%d %d",&x,&y);
            edge[x].PB(y);
            edge[y].PB(x);
        }
    
        int ans = 0 ;
        for ( int i = 1 ; i <= n  ; i++)
            if (!dfs(i,-1)) ans++;
    
        cout<<ans<<endl;
    
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




