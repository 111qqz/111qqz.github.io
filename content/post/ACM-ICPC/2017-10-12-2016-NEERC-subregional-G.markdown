---
author: 111qqz
date: 2017-10-12 13:44:29+00:00
draft: false
title: 2016-2017 ACM-ICPC, NEERC, Northern Subregional Contest  G Gangsters in Central
  City  (LCA)
type: post
url: /2017/10/2016-NEERC-subregional-G/
categories:
- ACM
tags:
- LCA
---

题意：

有一棵树，水源在根节点1，房子在叶子节点。有若干操作，操作可能是歹徒占领或者离开一个房子。我们不想给歹徒供水，可以通过切断边实现（如果某个叶子节点到根节点的路径上有一条边被切掉，那么就不能供水了。）对于每次操作后，问不给所有歹徒供水最少要切多少条边，并且问在切满足前面最小的情况下，最少使得多少个良民受影响。初始没有歹徒。

思路：



我们先考虑第一个问题。容易知道，假设与根相连的有k条边，那么最多只需要切k次，就切断了所有房子的水源。

也就是说，从最少切的次数角度的考虑，切与水源相连的边一定是最优的。

我们可以考虑把树根1去掉，这样得到k棵子树

然后可以预处理出，对于每个叶子节点，其非根的最远祖先是谁，也就是k棵子树的根节点都是谁。

那么对于每次出现歹徒，假设其非根的最远祖先是x,只需要切1-x这条边即可。



现在考虑第二个问题，在保证问题一最小的情况下，一个比较直观的想法是，我们尽量往低了切，也就是尽量往原理根的边上切，这样才能使收到影响的良民比较少。

**容易想到，一个子树上该切的点是，所有被歹徒占领的坏点的LCA**。这样可以使得受到影响的良民最少。

因为我们要得到受到影响的良民的数量，所以用siz[i]维护以i为根的子树的叶子数量，以及歹徒的数量。

**这道题的关键结论是，：树上多个点的LCA，就是DFS序最小的和DFS序最大的这两个点的LCA"**

**这道题的关键结论是，：树上多个点的LCA，就是DFS序最小的和DFS序最大的这两个点的LCA"**

**这道题的关键结论是，：树上多个点的LCA，就是DFS序最小的和DFS序最大的这两个点的LCA"**

因此这题就是写个LCA就可以了，切掉的坏点的dfs序可以用个set维护下。




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年10月12日 星期四 17时06分57秒
    File Name :G.cpp
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
    int n,q;
    int val[N];
    vector < int > edge[N];
    int in[N];
    int E[2*N],R[2*N],dis[N],depth[2*N];
    int p;
    int fa[N];
    int dp[2*N][20];
    int siz[N]; //siz[i]表示以i为根的子树的叶子数量。
    int FA[N]; //将树根去掉之后，每棵子树最上面能到达的顶点。
    set<int>T[N];//T[i]表示与根节点直接连接的节点i 切掉的点的dfs序 id
    int a[N];
    void dfs( int u,int dep,int d,int pre)
    {
        fa[u] = pre;
        p++;
        E[p] = u;
        depth[p] = dep;
        R[u] = p;
        dis[u] = d;
        int SIZ = edge[u].size();
        if (SIZ==0) siz[u] = 1;
        for ( int i = 0 ; i < SIZ ; i++)
        {
        int v = edge[u][i];
        if (v==pre) continue;
        if (u==1) FA[v] = v; //把树根去掉，原树分裂乘若干个子树
        else FA[v] = FA[u];
    
        dfs(v,dep+1,d+1,u);
        siz[u] += siz[v];
        p++;
        E[p] = u;
        depth[p] = dep;
        }
    }
    int _min( int l,int r)
    {
        if (depth[l] < depth[r]) return l;
        return r;
    }
    void rmq_init()
    {
        for ( int i = 1 ; i <= 2*n+2 ; i++) dp[i][0] = i;
        
        for ( int j = 1 ; (1<<j) <= 2*n+2 ; j++)
        for ( int i = 1 ; i + (1<<j)-1 <= 2*n+2 ; i++)
            dp[i][j] = _min(dp[i][j-1],dp[i+(1<<(j-1))][j-1]);
    }
    int rmq_min(int l,int r)
    {
        if (l>r) swap(l,r);
        int k = 0 ;
        while (1<<(k+1)<=r-l+1) k++;
        return _min(dp[l][k],dp[r-(1<<k)+1][k]);
    }
    int ans1=0,ans2=0;
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        //freopen("./in.txt","r",stdin);
        
      #endif
        freopen("gangsters.in","r",stdin);
        freopen("gangsters.out","w",stdout);
        ms(a,0);
        ms(siz,0);
        scanf("%d %d",&n,&q);
        for ( int i = 2 ; i <= n ; i++)
        {
            int x;
            scanf("%d",&x);
          //  cout<<"x:"<<x<<endl;
            edge[x].PB(i);
        }
        p = 0;
        dfs(1,0,0,-1);
        rmq_init();
        while (q--)
        {
            char opt[3];
            int x;
            scanf("%s%d",opt,&x);
           // cout<<opt<<" "<<x<<endl;
            if (opt[0]=='+')
            {
            int fx = FA[x];
            if (T[fx].size()==0) ++ans1;
            T[fx].insert(R[x]);
            ans2-=a[fx];//因为切掉了，先去掉之前的影响
            
            int fi = *T[fx].begin();
            int la = *T[fx].rbegin(); 
            int LCA = E[rmq_min(fi,la)]; //尽量往低了切，才可能影响小。
        //  printf( "(LCA(%d %d)=%d,siz[LCA]=%d \n",R[fi],R[la],LCA,siz[LCA]);
            a[fx] = siz[LCA] - T[fx].size();
            
            ans2 += a[fx];//再考虑新的影响
        //  cout<<"ans2:"<<ans2<<endl;
            }
            else
            {
            int fx = FA[x];
            if (T[fx].size()==1) ans1--;
            T[fx].erase(R[x]);
            ans2-=a[fx];
            if (T[fx].size()!=0)
            {
                int fi = *T[fx].begin();
                int la = *T[fx].rbegin();
                int LCA = E[rmq_min(fi,la)];
                a[fx] = siz[LCA] - T[fx].size();
        //      printf( "(LCA(%d %d)=%d\n",R[fi],R[la],LCA);
            }
            else a[fx] = 0;
    
            ans2 +=a[fx];
            }
            printf("%d %d\n",ans1,ans2);
        }
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    








