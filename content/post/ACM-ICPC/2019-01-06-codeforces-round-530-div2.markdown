---
author: 111qqz
date: 2019-01-06 06:43:12+00:00
draft: false
title: codeforces round 530 div2
type: post
url: /2019/01/codeforces-round-530-div2/
categories:
- ACM
---

A,B,C:都很简单，不说了。

D:一棵树，给出树的结构，以及从树根到某个深度为偶数的节点的路径和，问能否构造一种所有节点点权和最小的树，输出最小点权和。

思路：

容易知道，如果想要点权和最小，那么尽可能让靠近树根的点承担更多的点权。

具体做法是，bfs，对于每个节点u，取其儿子中最小的S值求节点u的信息。

比赛的时候wa16...最后发现是答案要用long long存...因为单个路径和是<=1E9的。。多个加起来会超过int...  长时间不打连这种常见的坑都不敏感了啊。。。

    
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
    const int N=1E5+7;
    int n;
    vector<int>edge[N];
    int s[N];
    int d[N];
    bool vis[N];
    int a[N];
    // void dfs(int u,int dep)
    // {
    //     int siz = edge[u].size();
    //     for (auto v: edge[u])
    //     {
    //         dfs(v,dep+1);
    //     }
    // }
    int bfs()
    {
        ms(d,-1);
        ms(vis,false);
        queue<int>Q;
        Q.push(1); //root
        vis[1] = true;
        d[1] = s[1];
        while (!Q.empty())
        {
            int u = Q.front();Q.pop();
            // cout<<"u:"<<u<<" "<<Q.size()<<endl;
            int min_sum_in_leaf = inf;
            bool even = false;
            // cout<<"v seq:";
            for ( auto v: edge[u])
            {
                // cout<<v<<" s[v]:"<<s[v]<<" ";
                if (s[v]==-1)
                {
                    Q.push(v);
                    d[v] = d[u];
                    even = true;
                }
                if (s[v]!=-1) min_sum_in_leaf = min(min_sum_in_leaf,s[v]);
            }
            cout<<endl;
            if (even) continue;
            // cout<<"min_sum_in_leaf:"<<min_sum_in_leaf<<endl;
            // cout<<"u:"<<u<<" d[u]:"<<d[u]<<endl;
            if (d[u]>min_sum_in_leaf) return -1; //不可能
            if (min_sum_in_leaf==inf)
            {
                // a[u] = 
                continue;
            }
            a[u] = min_sum_in_leaf - d[u];
            d[u] = min_sum_in_leaf;
            for ( auto v: edge[u])
            {
                a[v] = s[v] - d[u];
                d[v] = s[v];
                // cout<<"v:"<<v<<" a[v]:"<<a[v]<<" d[v]:"<<d[v]<<endl;
                Q.push(v);
            }
        }
        return 0;
    }
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
    
      cin>>n;
      for ( int i = 2  ; i <= n ; i++)
      {
          int x;
          cin>>x;
          edge[x].push_back(i);
      }
      for ( int i = 1 ; i <= n ; i++) cin>>s[i];
    //   for ( int i = 1 ;i <= n ; i++) cout<<"s[i]:"<<s[i]<<endl;
      ms(a,0);
      a[1] = s[1];
      LL ans = bfs();
      if (ans==-1)
      {
          puts("-1");
          
      }
      else
      {
          for ( int i = 1 ; i <= n ; i++)
          {
            //   cout<<i<<":"<<a[i]<<" d:"<<d[i]<<" s:"<<s[i]<<endl;
              ans = ans + a[i];
          } 
          cout<<ans<<endl;
      }
    
       
    
        
     
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





