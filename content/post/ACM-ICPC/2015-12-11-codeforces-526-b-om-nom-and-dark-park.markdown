---
author: 111qqz
date: 2015-12-11 09:08:45+00:00
draft: false
title: codeforces 526 B Om Nom and Dark Park
type: post
url: /2015/12/codeforces-526-b-om-nom-and-dark-park/
categories:
- ACM
tags:
- greedy
- tree
---

http://codeforces.com/contest/526/problem/B
题意：有一棵完全二叉树。每条边上有一定数量的路灯。问最少需要添加多少个路灯。使得根节点道叶子节点的每一条路径上的路灯数量一样。
思路：同叶子节点网上更新即可。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月11日 星期五 16时57分27秒
    File Name :code/cf/problem/526B.cpp
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
    const int N=3E3+7;
    int n;
    int a[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n;
    	LL res = 0 ;
    	n = (2<<n)-2;
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    cin>>a[i];
    	}
    	for ( int i = n ; i >= 1 ; i-=2)
    	{
    	    res +=abs(a[i]-a[i-1]);
    	    if (i!=2) a[i/2-1] += max(a[i],a[i-1]);
    	}
    	cout<<res<<endl;
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




