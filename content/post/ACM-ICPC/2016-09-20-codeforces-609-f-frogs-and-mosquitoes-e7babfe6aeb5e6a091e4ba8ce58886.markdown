---
author: 111qqz
date: 2016-09-20 17:48:18+00:00
draft: false
title: 'codeforces #609 F. Frogs and mosquitoes (线段树+二分)'
type: post
url: /2016/09/codeforces-609-f-frogs-and-mosquitoes-/
categories:
- ACM
tags:
- binary search
- 线段树
---

[题目链接](http://codeforces.com/problemset/problem/609/F)

题意：n只青蛙，第i只位于x[i],舌头长度为t[i]。m只蚊子，第i只蚊子所在位置为p[i],蚊子的大小为b[i]。

蚊子按照出现顺序输入。

一只青蛙能吃到蚊子当且仅当蚊子和青蛙在同一个位置，或者蚊子在青蛙右边并且与青蛙的距离小于等于该青蛙舌头的长度。

当多只青蛙可以吃到同一只蚊子的时候，最左边的那只青蛙来吃。

当一只青蛙吃掉一只蚊子以后，青蛙的舌头增加蚊子的大小。

当一只青蛙吃掉一只蚊子后，因为舌头边长而又能吃到其他蚊子的时候，这只青蛙会继续吃，只到当前没有蚊子可以被任何一只青蛙吃到，在这个过程之后才会飞来下一只蚊子。



思路：问题的关键在于，对于某只蚊子，我们如何找到能吃到该蚊子的青蛙中最左边的那只。

可以抽象成寻找区间[1,r]中，最左边的那个>=x的元素。

联想到一个类似的问题：对于区间[1,n]，找到最左边的>=x的元素。做法是线段树维护最大值，只需要每次先query左子树，就可以保证找到额是最左边的。

但是如果是区间[1,r]呢。。。

我们发现。。。区间[1..k] (k<=r)的最大值是随着k的增大而不减的。。。。（最大值。。。肯定不减呀）

**也就是说是单调的。。。因此我们可以考虑二分。。。这很重要。。。**

**寻找区间[1，r]中第一个大于等于x的元素，利用单调性来二分做是一个很经典的做法，复杂度(lgn)^2,注意体会。**



因此具体做法是：

建树，存的是区间中x[i]+t[i]的最大值。

对于每一只飞来的蚊子，寻找能吃到它的最左边的青蛙的编号（具体做法是，先找到最后一个位置小于等于蚊子位置的青蛙的下标，作为青蛙的下标的上界，然后二分，每次query区间最大值，不断缩小区间。）

当蚊子被吃的时候记录答案，更新青蛙的各种信息（线段树要update)

并且由于青蛙的舌头变长了，可能吃到之前没有青蛙能吃到的蚊子，因此要把之前的没有能被青蛙吃到的蚊子存进一个multiset(因为蚊子可能落在同一个位置） 然后让当前的青蛙尽可能吃这些没有被吃到的蚊子，同时更新青蛙的各种信息，并在multiset中删除这只蚊子/

没被吃的时候就扔进multiset里。

需要注意multiset erase的时候要erase一个迭代器。。。不然会把所有相同的都删掉。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :Wed 21 Sep 2016 12:30:16 AM CST
    File Name :code/cf/problem/609F.cpp
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
    #define pi pair < LL ,LL >
    #define MP make_pair
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    const int N=2E5+7;
    struct node
    {
        LL x,t;
        LL sum;
        int id;
        bool operator < (node b)const
        {
    	return x<b.x;
        }
    }frog[N];
    pi mos[N];
    int n,m;
    int cnt;
    LL X[N];
    LL tree[N<<2];
    void PushUp(int rt)
    {
        tree[rt] = max(tree[rt<<1],tree[rt<<1|1]);
    }
    void build( int l,int r,int rt)
    {
        if (l==r)
        {
    	tree[rt] = frog[l].sum;
    	return ;
        }
        int m = (l+r)>>1;
        build(lson);
        build(rson);
        PushUp(rt);
    }
    void update( int p,LL sc,int l,int r,int rt)
    {
        if (l==r)
        {
    	tree[rt] += sc;
    	return;
        }
        int m = (l+r)>>1;
        if (p<=m) update(p,sc,lson);
        else update(p,sc,rson);
        PushUp(rt);
    }
    LL query(int L,int R,int l,int r,int rt)
    {
        if (L<=l&&r<=R) return tree[rt];
        int m = (l+r)>>1;
        LL ret = -1;
        if (L<=m) ret = max(ret,query(L,R,lson));
        if (R>=m+1) ret = max(ret,query(L,R,rson));
        return ret;
    }
    int bin( int k)
    {
        int l = 1;
        int r = upper_bound(X+1,X+cnt+1,k)-X;//r为X中第一个大于k的下标。
        r--;//此时r为最后一个小于等于k的下标。
        if (r==0||query(1,r,1,n,1)<k) return -1; //因为1..x的最大值是在x递增的意义夏单调的，所以可以二分。
        int res = -1;
        while (l<=r)
        {
    	int mid = (l+r)/2;
    	if (query(1,mid,1,n,1)>=k) r = mid-1,res = mid;
    	else l = mid+1;
        }
        return res;
    }
    pi ans[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	scanf("%d%d",&n,&m);
    	cnt = 0 ;
    	for ( int i = 1 ;i  <= n ; i++)
    	{
    	    scanf("%lld%lld",&frog[i].x,&frog[i].t);
    	    frog[i].id = i ;
    	}
    	sort(frog+1,frog+n+1);
    	for ( int i = 1 ; i <= n ; i++) frog[i].sum = frog[i].x + frog[i].t,X[++cnt] = frog[i].x;
    	build(1,n,1);
    	multiset<pi>mse;
    	for ( int i = 1 ; i <= m ; i++) scanf("%lld%lld",&mos[i].fst,&mos[i].sec);
    	for ( int i = 1 ; i <= m ; i++)
    	{
    	    int pos = bin(mos[i].fst); //找到一个最左边的i，满足X[i]<=mos[i].fst并且x[i]+t[i]>=mos[i].fst
    	    if (pos!=-1)
    	    {
    		ans[frog[pos].id].fst++;
    		frog[pos].t+=mos[i].sec;
    		update(pos,mos[i].sec,1,n,1);
    		frog[pos].sum = frog[pos].t + frog[pos].x;
    		while (!mse.empty())
    		{
    		    auto it = mse.lower_bound(make_pair(frog[pos].x,0)); //返回第一个大于等于当前青蛙位置的蚊子
    		    if (it==mse.end()||frog[pos].sum< it->fst) break; //没有这样的蚊子或者当前青蛙没办法吃到所有没被吃的蚊子中最左边（最容易被吃到）的
    		    //不然就一直吃。。。把之前没被吃的尽量吃。。。直到某个吃不到。。。
    		    frog[pos].t += it->sec;
    		    frog[pos].sum += it->sec;
    		    ans[frog[pos].id].fst++;
    		    update(pos,it->sec,1,n,1);
    		    mse.erase(it);//论multiset的正确erase方法
    		}
    	    }else mse.insert(mos[i]);
    	}
    	for ( int i = 1 ; i <= n ; i++) ans[frog[i].id].sec = frog[i].t;
    	for ( int i = 1; i <= n ; i++) printf("%lld %lld\n",ans[i].fst,ans[i].sec);
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





