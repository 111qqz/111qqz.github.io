---
author: 111qqz
date: 2016-09-17 12:01:43+00:00
draft: false
title: spoj DQUERY - D-query (询问区间中不同数的个数，线段树(离线) or 莫队算法（离线） or 主席树（在线）)
type: post
url: /2016/09/spoj-dquery/
categories:
- ACM
tags:
- 主席树
- 分块
- 可持久化数据结构
- 线段树
- 莫队算法
---

[题目链接](http://www.spoj.com/problems/DQUERY/)
题意：给出n个数，然后m个询问，每个询问一个区间[l,r],问该区间中不同的数有多少个。

思路：离线处理+线段树的做法不多说了：


    
    /* ***********************************************
    Author :111qqz
    Created Time :Fri 16 Sep 2016 11:34:32 PM CST
    File Name :code/spoj/dquery.cpp
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
    const int N=3E4+7;
    const int M=2E5+7;
    int n,Q;
    int a[N];
    int tree[N<<2];
    map<int,int>mp;
    struct node
    {
        int l,r;
        int id;
        bool operator < (node b)const
        {
        if (r==b.r) return l<b.l;
        return r<b.r;
        }
    }q[M];
    void PushUp( int rt)
    {
        tree[rt] = tree[rt<<1] + tree[rt<<1|1];
    }
    void update( int p,int sc,int l,int r ,int rt)
    {
        if (l==r)
        {
        tree[rt]+=sc;
        return;
        }
        int m = (l+r)>>1;
        if (p<=m) update(p,sc,lson);
        else update(p,sc,rson);
        PushUp(rt);
    }
    int query(int L,int R,int l,int r,int rt)
    {
        if (L<=l&&r<=R) return tree[rt];
        int m = (l+r)>>1;
        int ret = 0 ;
        if (L<=m)  ret += query(L,R,lson);
        if (R>=m+1) ret+=query(L,R,rson);
        return ret;
    }
    int ans[M];
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("code/in.txt","r",stdin);
      #endif
        cin>>n;
        for ( int i = 1 ; i <= n ; i++) scanf("%d",&a[i]);
        cin>>Q;
        for ( int i = 1 ; i <= Q ; i++) scanf("%d %d",&q[i].l,&q[i].r),q[i].id = i ;
        sort(q+1,q+Q+1);
        int cur = 1;
        for ( int i = 1 ; i <= Q ; i++)
        {
            for ( ; cur <= q[i].r ; cur++)
            {
            if (mp[a[cur]]) update(mp[a[cur]],-1,1,n,1);
            mp[a[cur]] = cur;
            update(mp[a[cur]],1,1,n,1);
            }
            ans[q[i].id] = query(q[i].l,q[i].r,1,n,1);
        }
        for ( int i = 1 ; i <= Q ; i++) printf("%d\n",ans[i]);
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



<del>之后补一个主席树的做法</del>

先来补一个莫队的做法。

因为a[i]<=1E6,可以很方便得统计每个数出现的次数，update的时候，如果是1变成0，那么区间中不同的数的个数减1，如果是0变成1，那么区间中不同数个数+1


    
    /* ***********************************************
    Author :111qqz
    Created Time :Fri 16 Sep 2016 11:34:32 PM CST
    File Name :code/spoj/dquery.cpp
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
    const int MAXN = 1E6+7;
    const int N=3E4+7;
    const int M=2E5+7;
    int n,Q;
    int a[N];
    int pos[N];
    int sum;
    int cnt[MAXN]={0};
    struct node
    {
        int l,r;
        int id;
        bool operator < (node b)const
        {
        if (pos[l]==pos[b.l]) return r<b.r;
        return pos[l] < pos[b.l];
        }
    }q[M];
    
    int ans[M];
    void update ( int x,int d)
    {
        cnt[a[x]]+=d;
        if (d==1&&cnt[a[x]]==1) sum++;
        if (d==-1&&cnt[a[x]]==0) sum--;
    }
    
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        int bk = 173;// sqrt(30000)
        cin>>n;
        for ( int i = 1 ; i <= n ; i++) 
        {
            scanf("%d",&a[i]);
            pos[i] = (i-1)/bk;
        }
        cin>>Q;
        for ( int i = 1 ; i <= Q ; i++) scanf("%d %d",&q[i].l,&q[i].r),q[i].id = i ;
        sort(q+1,q+Q+1);
        int pl=1,pr=0,id,l,r;
        ms(cnt,0);
        sum = 0 ;
        for ( int i = 1 ; i <= Q ; i++)
        {
            id = q[i].id;
            l = q[i].l;
            r = q[i].r;
            if (pr<r)
            {
            for ( int j = pr+1 ; j <= r ; j++)
                update(j,1);
            }
            else 
            {
            for ( int j = r+1 ; j <= pr ; j++)
                update(j,-1);
            }
            pr = r;
            if (pl<l)
            {
            for ( int j = pl ; j <= l-1 ; j++)
                update(j,-1);
            }
            else
            {
            for ( int j = l ; j <= pl-1 ; j++)
                update(j,1);
            }
            pl = l;
            ans[id] = sum;
        }
        for ( int i = 1 ; i <= Q ; i++) printf("%d\n",ans[i]);
        
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





补一个在线的做法，可持久化线段树，其实思路和离线线段树几乎一样。


    
    /* ***********************************************
    Author :111qqz
    Created Time :Fri 16 Sep 2016 11:34:32 PM CST
    File Name :code/spoj/dquery.cpp
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
    const int N=3E4+7;
    const int M=2E5+7;
    int n,Q;
    int a[N],root[N];
    map<int,int>mp;
    int cnt;
    struct Ptree
    {
        int sum;
        int left,right;
    }tree[N*30];
    void build (int &rt,int l,int r)
    {
        rt =++cnt;
        tree[rt].sum = 0 ;
        if (l==r) return;
        int mid = (l+r)>>1;
        build (tree[rt].left,l,mid);
        build (tree[rt].right,mid+1,r);
    }
    inline int add_node(int _sum,int _left,int _right)
    {
        int idx = ++cnt;
        tree[idx].sum = _sum;
        tree[idx].left = _left;
        tree[idx].right = _right;
        return idx;
    }
    void Insert(int &root,int pre_rt,int pos,int val,int l,int r)
    {
    //    printf("l:%d r:%d\n",l,r);
        root = add_node(tree[pre_rt].sum + val,tree[pre_rt].left,tree[pre_rt].right);
       // root = ++cnt;
       // tree[root].sum = tree[pre_rt].sum+ val;
       // tree[root].left = tree[pre_rt].left;
       // tree[root].right = tree[pre_rt].right;
        if (l==r) return;
        int mid = (l+r)>>1;
        if (pos<=mid) Insert(tree[root].left,tree[pre_rt].left,pos,val,l,mid);
        else Insert(tree[root].right,tree[pre_rt].right,pos,val,mid+1,r);
    }
    int query(int pos,int l,int r,int rt)
    {
        if (l==r) return tree[rt].sum;
        int mid = (l+r)>>1;
        if (pos<=mid) return query(pos,l,mid,tree[rt].left);
        else return tree[tree[rt].left].sum + query(pos,mid+1,r,tree[rt].right);
    }
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        ms(tree,0);
        cnt = 0 ;
        cin>>n;
        for ( int i = 1 ; i <= n ; i++) scanf("%d",&a[i]);
        build (root[n+1],1,n);
        mp.clear();
        for ( int i = n ; i >= 1 ; i--)
        {
            if (mp.find(a[i])==mp.end())
            {
            Insert(root[i],root[i+1],i,1,1,n);
            }
            else
            {
            Insert(root[i],root[i+1],mp[a[i]],-1,1,n);
            Insert(root[i],root[i],i,1,1,n);
            }
            mp[a[i]] = i;
        }
        cin>>Q;
        while (Q--)
        {
            int l,r;
            scanf("%d %d",&l,&r);
           // printf("l:%d r:%d\n",l,r);
            int ans = query(r,1,n,root[l]);
            printf("%d\n",ans);
        }
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




