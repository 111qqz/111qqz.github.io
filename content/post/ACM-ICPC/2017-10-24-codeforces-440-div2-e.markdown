---
author: 111qqz
date: 2017-10-24 06:39:27+00:00
draft: false
title: 'codeforces # 440 div2  E. Points, Lines and Ready-made Titles (和图有关的计数，思维题)'
type: post
url: /2017/10/codeforces-440-div2-e/
categories:
- ACM
tags:
- 思维题
- 计数问题
---

[题目链接](http://codeforces.com/contest/872/problem/E)

题意：有n个整点，每个点处可以什么都不画，或者画一条垂直方向的直线，或者画一条水平方向的直线。

现在给出n个点的坐标，问最多右多少种不同的图案。(只要有一处不同，就认为两个不同）

思路：

[参考题解](http://www.cnblogs.com/kkkkahlua/p/7679526.html)

好菜啊不会做，转载一段题解。



<blockquote>和[bzoj 1854](http://www.cnblogs.com/kkkkahlua/p/7666811.html)的并查集思路蜜汁契合 // 看完了题解的我这样想道

首先显然可以将图分为若干个联通块。

且慢，哪里来的图？ 那就先考虑建图？ 不急不急，先来想想看每一个联通块的性质。

如果该联通块中有环的话，肯定每条边都能取到；如果联通块是一棵树，那么必有一条边取不到（具体阐述见上[bzoj 1854](http://www.cnblogs.com/kkkkahlua/p/7666811.html)），所以只需要知道

> 
> 
      1. 这个联通块中有多少条边
      2. 这个联通块是不是环

这两个信息就可以了

那么可以直接上并查集。

什么样的点可以并到一起呢？横坐标相同的或者纵坐标相同的。

有没有环怎么维护呢？看有没有加进去的边的端点本身就在一个集合里。

联通块中边的数目又怎么知道呢？这倒还挺有意思的，其实只要直接看出现过多少个横坐标或者纵坐标就可以了，因为一个横坐标或者一个纵坐标就代表一条可以选的直线，所以这块联通块的贡献就是2^(x+y)或者2^(x+y)-1

然后呢？就做完了。

然而呢？比赛结束。一天了。</blockquote>




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年10月23日 星期一 15时51分51秒
    File Name :E.cpp
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
    const int N=1E5+7;
    const LL mod = 1E9+7;
    struct point 
    {
        int x,y;
        int id;
        bool operator < ( point b)
        {
        return  id < b.id;
        }
    }p[N];
    
    
    vector < int>edge[N];
    bool cmpx ( point a,point b) { return a.x < b.x;}
    bool cmpy( point a,point b){ return a.y<b.y;}
    
    int n;
    int cnt;
    set<int>X,Y;
    bool vis[N];
    LL ksm ( LL a,LL b)
    {
        LL res = 1;
        while (b)
        {
        if (b&1) res = res * a % mod;
        b = b >> 1LL;
        a = a * a % mod;
        }
        return res;
    }
    void dfs  ( int u)
    {
        X.insert(p[u].x);
        Y.insert(p[u].y);
        vis[u] = true;
        cnt++;
        for ( auto v : edge[u])
        if (!vis[v]) dfs(v);
    }
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
    
        cin>>n;
        for ( int i = 1 ; i <= n ; i++) cin>>p[i].x >> p[i].y,p[i].id = i;
        sort(p+1,p+n+1,cmpx);
        for ( int i = 2 ; i <= n  ; i++) 
            if (p[i].x==p[i-1].x)
            {
            edge[p[i].id].push_back(p[i-1].id);
            edge[p[i-1].id].push_back(p[i].id);
            }
    
        sort(p+1,p+n+1,cmpy);
        for ( int i = 2 ; i <= n ; i++)
            if (p[i].y==p[i-1].y)
            {
            edge[p[i].id].PB(p[i-1].id);
            edge[p[i-1].id].PB(p[i].id);
            }
        
        ms(vis,false);
        sort(p+1,p+n+1);
        LL ans = 1LL;
        for ( int i = 1 ; i <= n ; i++)if (!vis[i])
        {
            X.clear();
            Y.clear();
            cnt = 0;
            dfs(i);
            int sum = X.size() + Y.size();
            //cout<<"sum:"<<sum<<endl;
            if (sum<=cnt) ans = ans * ksm(2,sum) % mod;
            else ans = ans * (ksm(2,sum)-1 + mod) % mod;
        }
        cout<<ans<<endl;
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }



相关并且有趣的题目:bzoj1854
codeforces  #346 div2
