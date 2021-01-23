---
author: 111qqz
date: 2015-08-14 19:50:00+00:00
draft: false
title: codeforces 570 D. Tree Requests (dfs序)
type: post
url: /2015/08/codeforces570d-treerequestsdfs/
categories:
- ACM
tags:
- dfs序
---




因为字母的排列顺序是任意的,所以判断能否形成回文串的条件就成了出现次数为奇数的字母的个数是否大于1个,如果是,那么一定不能形成回文串,否则一定可以.




为了找到以节点v为根的 subtree 中深度为h的后代,需要求出dfs序列,并且记录每个节点初次访问的时间戳和离开它的时间戳,然后二分.




貌似也可以用树状数组做?


 

    
    /*************************************************************************
    	> File Name: code/cf/#316/D.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月15日 星期六 02时55分55秒
     ************************************************************************/
    #include <bits/stdc++.h>
    
    
    using namespace std;
    const int N=5E5+7;
    int n,m;
    vector<int> adj[N];
    char S[N];
    vector<int> occ[N][26];
    int in[N], out[N], now;
    
    void dfs(int u, int depth)
    {
        occ[depth][S[u]-'a'].push_back(++now);
        in[u]=now;
        vector<int>::iterator it;
        for (it=adj[u].begin();it!=adj[u].end();it++)
        {
    	dfs(*it,depth+1);
        }
        out[u]=now;
    }
    
    int main()
    {
        scanf("%d %d",&n,&m);
        for(int i=2; i<=n; i++)
        {
            int a;
            scanf("%d",&a);
            adj[a].push_back(i);
        }
        scanf("%s", S+1);
        dfs(1, 1);
        while(m--)
        {
            int v, h;
            scanf("%d %d",&v,&h);
            int odd=0;
            for(int i=0; i<26; i++)
            {
                int cnt=upper_bound(occ[h][i].begin(), occ[h][i].end(), out[v])-
                        lower_bound(occ[h][i].begin(), occ[h][i].end(), in[v]);
                if(cnt%2==1)
                {
                    odd++;
                    if(odd>1)
                        break;
                }
            }
            if(odd>1)
                printf("No\n");
            else
                printf("Yes\n");
        }
        return 0;
    }
    



