---
author: 111qqz
date: 2017-05-12 13:18:06+00:00
draft: false
title: 'codeforces #413 B T-shirt buying (贪心)'
type: post
url: /2017/05/codeforces-div2-413b/
categories:
- ACM
tags:
- greedy
---

[题目链接](http://codeforces.com/contest/799/problem/B)

题意：有n个Ｔ恤，每个价格都不同，有三种颜色，分别用1,2,3表示，每件Ｔ恤给出前xiong和后背的颜色。现在有m个顾客排成一队，对于每个顾客，给出他喜欢的颜色，只要一个Ｔ恤的前xiong或者后背的颜色之一满足该颜色即可。顾客总希望买符合他喜欢颜色的Ｔ恤中价格最低的。现在问每个顾客买到的Ｔ恤的价格，如果某个顾客没有买Ｔ恤，输出-1

思路：贪一下？

对于每个颜色，找到价格最低的。记录的时候顺便记录id，以标记某件有２个颜色的衣服是否卖出去了。

１A美滋滋

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年05月11日 星期四 15时29分58秒
    File Name :B.cpp
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
    const int N=2E5+7;
    int n,m;
    bool vis[N]; //表示某个id的是否被卖出。
    vector< pair<int,int>>v[4]; //pair<price,id>,id是为了标记是否卖出去了，卖出去就继续找下一个。
    				    //虽然价格本身唯一，但是太大不适合做标记？
    struct node
    {
        int p,a,b;
        int id;
    }A[N];
    
    bool cmp(node x,node y)
    {
        return x.p<y.p;
    }
    vector<int>ans;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	ms(vis,false);
    	scanf("%d",&n);
    	for ( int i = 1 ; i <= n ; i++) scanf("%d",&A[i].p);
    	for ( int i = 1 ; i <= n ; i++) scanf("%d",&A[i].a);
    	for ( int i = 1 ; i <= n ; i++) scanf("%d",&A[i].b);
    	for ( int i = 1 ; i <= n ; i++) A[i].id = i;
    	//sort(A+1,A+n+1,cmp); //价格升序 没有必要吧。。。
    	
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    int a = A[i].a;
    	    int b = A[i].b;
    	    int p = A[i].p;
    	    int id = A[i].id;
    	    if (a==b)
    	    {
    		v[a].push_back(make_pair(p,id));
    	    }else
    	    {
    		v[a].push_back(make_pair(p,id));
    		v[b].push_back(make_pair(p,id));
    	    }
    	}
    
    
    
    	sort(v[1].begin(),v[1].end());
    	sort(v[2].begin(),v[2].end());
    	sort(v[3].begin(),v[3].end());
    	scanf("%d",&m);
    	//cout<<"m:"<<m<<endl;
    	int p[4]={0};
    	int mm = m;
    	while (m--)
    	{
    	    int x;
    	    scanf("%d",&x);
    	    while (p[x]<v[x].size()&&vis[v[x][p[x]].second]) p[x]++;
    	    if (p[x]==v[x].size())
    	    {
    		ans.push_back(-1);
    	    }
    	    else
    	    if (!vis[v[x][p[x]].second])
    	    {
    		vis[v[x][p[x]].second] = true;
    		ans.push_back(v[x][p[x]].first);
    	    }
    	}
    	m = mm;
    	for ( int i = 0 ; i < m ; i++)
    	    printf("%d%c",ans[i],i==m-1?'\n':' ');
    	
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



