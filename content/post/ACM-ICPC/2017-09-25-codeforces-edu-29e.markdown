---
author: 111qqz
date: 2017-09-25 10:55:57+00:00
draft: false
title: 'codeforces edu #29 E. Turn Off The TV (思维，乱搞)'
type: post
url: /2017/09/codeforces-edu-29e/
categories:
- ACM
tags:
- 乱搞
---

[题目链接](http://codeforces.com/contest/863/problem/E)

题意：有若干线段，给出起点和终点，问是否有一个线段是冗余的。冗余的意思是说，对于该线段所覆盖的所有整数点，没有该线段，也能被其他一个或者多个线段覆盖到。如果有，输出任意**一个**冗余线段即可。

思路：画画图？ 显然可以按照第一关键字左端点升序，第二关键字右端点降序（降序是为了处理 n=2,[1,2],[1,3] 这样的case容易一些），先考虑2种最简单的情况。

第一种是a[i+1]完全被a[i]包裹在里面，准确得说不一定是a[i]，而是之前所有线段的最大右端点的那条线段，此时a[i+1]就是冗余的线段。

第二种是a[i+1]的左端点在之前所有线段的最大右端点右边，此时没有冗余，继续进行。

接下来考虑比较复杂的相交情况，我们画图发现，当前线段是否冗余，只与a[i-1]和a[i+1]有关。

如果第i条线段的左端点，不超过第i-2条线段的右端点的右边一个位置，此时第i-1条线段就是冗余的。

wa了2次。。原因是没认真看题，l,r的范围的最小值是从0开始而不是1。所以总体来说是道水题（调教场的题这么水了么。。。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年09月25日 星期一 02时57分03秒
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
    const int N=2E5+7;
    struct Node
    {
        int l,r;
        int id;
    }a[N];
    int n;
    int ans;
    vector<int>ret;
    bool cmp( Node x, Node y)
    {
        if (x.l==y.l) return x.r>y.r;
        return x.l<y.l;
    }
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        cin>>n;
        for ( int i =  1 ; i <= n ; i++) 
        {
            scanf("%d %d",&a[i].l,&a[i].r);
            a[i].id = i;
        }
        sort(a+1,a+n+1,cmp);
        ans = 0 ;
        int mxR=-1;
        int lsR=-1;
        for ( int i = 1 ; i <= n ; i++)
        {
            //puts("miao");
            if (i>=3) lsR=a[i-2].r;
            if (a[i].r<=mxR)
            {
            ans++;
            ret.push_back(a[i].id);
            }
            else if (a[i].l>=mxR+1) //先考虑最easy的2个情况.
            {
            mxR=max(mxR,a[i].r);
            }else if (lsR!=-1&&a[i].l<=lsR+1&&a[i].r)
            {
            ans++;
            ret.push_back(a[i-1].id);
            }
    
            mxR = max(mxR,a[i].r);
        }
        if (ans==0) ans=-1;
        else ans = ret[0];
        printf("%d\n",ans);
    
    
            
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    










