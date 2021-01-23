---
author: 111qqz
date: 2015-08-16 19:26:00+00:00
draft: false
title: codeforces 567 E President and Roads (优先队列＋迪杰斯特拉＋tarjan)
type: post
url: /2015/08/codeforces567epresidentandroadstarjan/
categories:
- ACM
tags:
- dijkstra
- stl
- Tarjan
---

题意是说，给定一个有向图，对于每一条边，问是否是s到t的最短路上一定会经过的边．

如果是就输出yes

如果不是，问能否通过减少这条边的权值（减少的权值就是修理费用），使得这条边成为新的最短路上的边．

对于一条边是否一定是最短路上的边，我们可以从s做一遍最短路，然后反响建边，从t再做一遍最短路．

得到两个d1,d2数组

如果一条边d1[u] + d2[v] + w(u, v) = 最短路，那这条边在最短路上的边．但是未必不能缺少．

我们还要判断这条边是否是不能缺少的．

不能缺少的意思是说，如果没有这条边，就不能构成最短路．

那么这条边一定是桥．

我们可以用tarjan算法求桥．



据说是水题，不过图论还没怎么刷，所以对我来说还是很有难度的．

只是基本懂了

下面的代码是我仿照其他人的代码写出来的....求不鄙视　＞＜
 

    
    /*************************************************************************
    	> File Name: code/cf/#314/E.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月17日 星期一 03时09分39秒
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
    typedef pair<LL,LL> P;
    const int maxn = 200005;
    const LL mod1 = 1e9 + 7;
    const LL mod2 = 99999991;
    const LL inf = 1e15;
    struct Nod{
        LL b,val,next,idx;
        void init(LL b,LL val,LL next,LL idx){
            this->b=b;this->val=val;this->next=next;this->idx=idx;
        }
    }buf[2][maxn];
    LL len[2],E[2][maxn];
    LL n,m,s,t;
    LL dis[2][maxn],cnt[2][2][maxn],ans1[maxn],ans2[maxn];
    priority_queue<P,vector<P>,greater<P> > q;
    void init()
    {
        memset(E,-1,sizeof(E));
        memset(cnt,0,sizeof(cnt));
        len[0] = len[1] = 0;
    }
    void add_edge(LL a,LL b,LL val,LL idx)
    {
        buf[0][len[0]].init(b,val,E[0][a],idx);E[0][a]=len[0]++;
        buf[1][len[1]].init(a,val,E[1][b],idx);E[1][b]=len[1]++;
    }
    void dij(LL s,LL o)
    {
        while(!q.empty()) q.pop();
        fill(dis[o],dis[o]+maxn,inf);
        dis[o][s] = 0;cnt[o][0][s] = cnt[o][1][s] = 1;
        q.push(P(dis[o][s],s));
        LL u,v,i;
        while(!q.empty())
        {
            P p = q.top();q.pop();
            u = p.second;
            if(dis[o][u] != p.first) continue;
            for(i=E[o][u];i!=-1;i=buf[o][i].next)
    	{
                v = buf[o][i].b;
                if(dis[o][v] > dis[o][u] + buf[o][i].val)
    	    {
                     dis[o][v] = dis[o][u] + buf[o][i].val;
                    cnt[o][0][v] = cnt[o][0][u];
                    cnt[o][1][v] = cnt[o][1][u];
                    q.push(P(dis[o][v],v));
                }else if(dis[o][v] == dis[o][u] + buf[o][i].val){
                     cnt[o][0][v] = (cnt[o][0][v] + cnt[o][0][u]) % mod1;
                    cnt[o][1][v] = (cnt[o][1][v] + cnt[o][1][u]) % mod2;
                }
            }
        }
    }
    int main()
    {
        init();
        LL u,v,i,a,b,val;
        LL cost;
        cin>>n>>m>>s>>t;
        for(i=1;i<=m;i++){
            cin>>a>>b>>val;
            add_edge(a,b,val,i);
        }
        dij(s,0);dij(t,1);
        for(u=1;u<=n;u++)
        {
            for(i=E[0][u];i!=-1;i=buf[0][i].next){
                v = buf[0][i].b;
                if(dis[0][u]+dis[1][v]+buf[0][i].val==dis[0][t]){
                     if(cnt[0][0][u]*cnt[1][0][v]%mod1 == cnt[0][0][t]&&
                       cnt[0][1][u]*cnt[1][1][v]%mod2 == cnt[0][1][t]){
                         ans1[buf[0][i].idx] = 1;
                        continue;
                    }
                }
                cost = dis[0][u]+dis[1][v]+buf[0][i].val-dis[0][t]+1;
                if(buf[0][i].val - cost > 0){
                    ans1[buf[0][i].idx] = 0;
                    ans2[buf[0][i].idx] = cost; 
                }else{
                    ans1[buf[0][i].idx] = -1;
                }
            }
        }
        for(i=1;i<=m;i++){
            if(ans1[i] == 1) printf("YES\n");
            else if(ans1[i] == -1) printf("NO\n");
            else{
    	    printf("CAN %I64d\n",ans2[i]);
            }
        }
        return 0;
    }
    



