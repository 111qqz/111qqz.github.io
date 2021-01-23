---
author: 111qqz
date: 2016-11-13 10:10:47+00:00
draft: false
title: hdu 4747 Mex （线段树lazy标记）
type: post
url: /2016/11/hdu-4747-mex-lazy/
categories:
- ACM
tags:
- lazy标记
- 线段树
---

[题目连接](http://acm.hdu.edu.cn/showproblem.php?pid=4747)

题意：给出n(n<=200000)个数，问所有区间[l,r]中mex的和。 （一个区间mex的定义为，这个区间中没有出现的最小的非负数）

思路：我们观察到mex(1,i)随着i增大，是不减的。(**单调是线段树查询区间的时候非常好用的东西,这也是次题的突破口**)

mex(1,i)可以O(n)维护出

现在我们考虑左端点向右移动对答案的影响。

当i移动到i+1时，此时序列中少了a[i]，设r为最小的x，满足a[x]=a[i]，那么当右断点在区间[r+1,n]，mex值是没有改变的。

当右端点属于[i+1,r-1]时，mex大于a[i]的会变成a[i]。

由于我们知道从1到某区间的mex值是单调的，那么mex大于a[i]的点必然是连续的一段。

我们可以知道最左边的q，满足mex(1,q)大于a[i]，然后将区间[q,r-1]成段更新为a[i]

**因此整理思路，我们需要做两件事。**

**一个是每次区间求和，一个是找到最左边的q满足mex(1,q)大于a[i].**

线段树维护三个域，max域，表示该区间中mex(1,i)的最大值；

sum域，表示该区间中mex(1,i)的和

lazy域，表示延迟标记。

可以预处理出nxt数组，表示位置i上的数下次出现最近是在nxt[i]

    
    #include <cstdio>
    #include <cstring>
    #include <algorithm>
    #include <iostream>
    #include <set>
    using namespace std;
    const int N=2E5+7;
    #define lson l,m,rt<<1
    #define rson m+1,r,rt<<1|1
    typedef long long LL;
    int  n;
    int a[N];
    bool vis[N];
    int Mex[N];
    pair < int , int > b[N];
    int nxt[N];
    
    struct Tree
    {
        LL lazy;
        LL sum;
        LL mx;
    }tree[N<<2];
    void PushUp( int rt)
    {
        tree[rt].sum = tree[rt<<1].sum + tree[rt<<1|1].sum;
        tree[rt].mx = max(tree[rt<<1].mx,tree[rt<<1|1].mx);
    }
    void PushDown( int l,int r,int rt)
    {
        if (tree[rt].lazy!=-1)
        {
            int m = (l+r)>>1;
            tree[rt<<1].sum = (m+1-l)*tree[rt].lazy;
            tree[rt<<1|1].sum = (r-m)*tree[rt].lazy;
            tree[rt<<1].lazy = tree[rt<<1|1].lazy = tree[rt<<1].mx = tree[rt<<1|1].mx = tree[rt].lazy;
            tree[rt].lazy = -1;
    
        }
    }
    void update( int L,int R,int sc,int l,int r,int rt)
    {
        if (L<=l&&r<=R)
        {
            tree[rt].sum = (r-l+1)*sc;
            tree[rt].lazy = tree[rt].mx =sc;
            return;
        }
         PushDown(l,r,rt);
        int m = (l+r)>>1;
        if (L<=m) update(L,R,sc,lson);
        if (R>=m+1) update(L,R,sc,rson);
        PushUp(rt);
    }
    int queryP(int x,int l,int r,int rt)
    {
        if (tree[rt].mx<=x) return r+1;
        if (l==r) return l;
    
        PushDown(l,r,rt);
        int m = (l+r)>>1;
        if (tree[rt<<1].mx>x) return queryP(x,lson);
        else return queryP(x,rson); //先找左边，目的是找到最前面的.
    }
    int main()
    {
    
        while (~scanf("%d",&n)&&n)
        {
            for ( int i = 1 ;i  <= n ; i++)
            {
                scanf("%d",&a[i]);
              //  if (a[i]>200000) a[i] = 200001;
                b[i] = make_pair(a[i],i);
                nxt[i] = n+1;
            }
            sort(b+1,b+n+1);
            b[n+1].first = b[n].first;
            b[n+1].second = n+1;
            for ( int i = 1 ; i <=n ; i++)
                if (b[i].first == b[i+1].first) nxt[b[i].second] = b[i+1].second;
            memset(tree,0,sizeof(tree));
            memset(vis,false,sizeof(vis));
    
    
            int tmp = 0 ;
            set<int>se;
            for ( int i = 1 ; i <= n ; i++)
            {
               se.insert(a[i]);
               while (se.find(tmp)!=se.end()) tmp++;
                update(i,i,tmp,1,n,1);
            }
            LL ans = tree[1].sum;
            for ( int l =  1 ;l <= n ; l++)
            {
                update(l,l,0,1,n,1);
                int pos = queryP(a[l],1,n,1);//找到最左的r满足mex[r]>a[l]
                pos = max(l+1,pos);//该位置必须还没有被删除，维护下边界。
                update(pos,nxt[l]-1,a[l],1,n,1);
                ans += tree[1].sum;
            }
            cout<<ans<<endl;
    
    
    
        }
    }
    













