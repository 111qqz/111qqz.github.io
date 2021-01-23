---
author: 111qqz
date: 2017-10-26 09:16:15+00:00
draft: false
title: 2016 ICPC 大连 区域赛  A Wrestling Match  （交叉染色法判断二分图）
type: post
url: /2017/10/2016-icpc-dalian-regional-A/
categories:
- ACM
tags:
- 二分图
- 交叉染色法
---

# 题意：



给出n个点m条边，以及已知的好点和坏点。一个边连接的2个点一定是一好一坏，问是否有合法方案，使得每个点被确定好坏。



# 思路：



判断二分图。

先染已知的，再染未知的。

注意判掉没有出现的点。

注意有多个联通块。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年10月26日 星期四 12时53分06秒
    File Name :A.cpp
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
    const int N=1005;
    const int M=1E4+7;
    int n,m,a,b;
    vector <int>edge[N];
    int col[N];
    set<int>se;
    bool dfs( int u,int x)
    {
        col[u] = x;
        int siz = edge[u].size();
        for ( int i = 0 ;i  < siz ; i++)
        {
        int v  = edge[u][i];
        if (col[v]==1-x) continue;
        if (col[v]==x) return false;
        if (!dfs(v,1-x)) return false;
        }
        return true;
    }
    void pr(int a[])
    {
        for ( int i = 1 ; i <= n ; i++) printf("%d%c",a[i],i==n?'\n':' ');
    }
    vector <int> A,B;
    bool appear[N];
    bool ran[N];
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        while (~scanf("%d %d %d %d",&n,&m,&a,&b))
        {
    
            bool die = false;
            ms(col,-1);
            A.clear();
            B.clear();
            ms(appear,false);
            ms(ran,false);
            for ( int i = 0 ; i <= n ; i++) edge[i].clear();
            for ( int i = 1 ; i <= m ; i++)
            {
            int u,v;
            scanf("%d %d",&u,&v);
            appear[u]=appear[v] = true;
            edge[u].PB(v);
            edge[v].PB(u);
            }
            for ( int i = 1 ; i <= a ; i++)
            {
            int x;
            scanf("%d",&x);
            appear[x] = true;
            A.PB(x);
            col[x] = 0 ;  //0 for good player
            }
            for ( int i =1 ; i <= b ; i++)
            {
            int x;
            scanf("%d",&x);
            appear[x] = true;
            B.PB(x);
            col[x] = 1;
            }
    
            for ( int i = 1 ; i <= n ; i++) if (!appear[i])
            {
            die = true;
            break;
            }
            if (die)
            {
            puts("NO");
            continue;
            }
    
            //可能有多个联通块
            //
            int siz = A.size();
            for ( int i = 0 ; i < siz; i++)
            {
            int v = A[i];
            if (!dfs(v,0))
            {
                die = true;
                break;
            }
            }
            if (die)
            {
            puts("NO");
            continue;
            }
            
            siz = B.size();
            for ( int i = 0 ; i < siz; i++)
            {
            int v = B[i];
            if (!dfs(v,1))
            {
                die = true;
                break;
            }
            }
            if (die)
            {
            puts("NO");
            continue;
            }
    
            for ( int i = 1 ; i <= n ; i++ )
            {
            if (col[i]==-1)
            {
                if (!dfs(i,0))
                {
                die = true;
                break;
                }
            }
            }
    
            if (die)
            {
            puts("NO");
            continue;
            }
            puts("YES");
        }
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    








