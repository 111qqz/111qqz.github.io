---
author: 111qqz
date: 2016-09-16 10:13:51+00:00
draft: false
title: codeforces 338 E. Optimize! (线段树维护最小前缀和）
type: post
url: /2016/09/codeforces-338-e-optimize/
categories:
- ACM
tags:
- 线段树
---

[题目链接](http://codeforces.com/contest/338/problem/E)

题意：题意是由伪代码给出的。。手算模拟了一下(noip初赛即视感），题意大概是说，给出两个数组a和b，a数组长度为n,b数组长度为len,然后从a中截取连续的len个元素，称为数组s，如果存在一种方法使得s中元素和b中的元素一一对应且每组和都大于等于h,则称这个s是合法的。现在问a中有多少个合法的s。
具体来说，对于样例
5 2 10
5 3
1 8 5 5 7

s={8,5}和s={5,7}是有解的。
因为对于前者8+3>=10并且5+5>=10,对于后者5+5>=10,7+3>=10,因此答案为2
思路：

**最重要的一部是，我们先将b排序，然后维护一个函数f[i],在排序后的b中找到一个最小的j，满足a[i]+b[j]>=h,然后让f[i]=j?**

f[i]直接二分就可以得到。。

因为f[i]的值是使得a[i]满足条件的最小的b值。

然后我们观察发现。

f[i]大于等于len的元素个数最多有1个，不然无解。

f[i]大于等于len-1的元素个数最多有2个，不然无解。

f[i]大于等于i的元素个数最多由len+1-i个，不然无解。

设g[i]=len+1-i-sum[i],sum[i]=y[i]+y[i+1]+...+y[len]。

如果某个s中，对于所有的i，都有g[i]>=0，那么这个s就是合法的。

实际上我们没有必要去查询每个g[i]，只要g[i]中最小的大于等于0，那么这个s就是合法的。

现在的问题就变成了动态维护一段长度为len的最小后缀和。

我的思路是整体覆盖，

当a数组的区间从[l,r]到[l+1,r+1]的时候，增加了a[r+1],假设f[r+1]=p,那么用线段树更新区间[1,p]，都增加1.
减少了a[l],假设f[l]=q,那么同样用线段树维护，使得区间[1,q]都减少1.

讲道理应该也可以做吧。。。

不过被羊神@sheep教育说其实单点更新就可以。。。

[![1862480807](https://111qqz.com/wordpress/wp-content/uploads/2016/09/1862480807.jpg)
](https://111qqz.com/wordpress/wp-content/uploads/2016/09/1862480807.jpg)

于是去学了下动态维护区间最大子段和的线段树做法：
[bzoj 1756解题报告](https://111qqz.com/wordpress/2016/09/bzoj-1756/)[hit oj 2687 解题报告](https://111qqz.com/wordpress/2016/09/hit-oj-2687-candy/)



然后单点更新维护最大后缀和就很容易了。

类似的做法，我们也维护一个最小前缀和。初始化的时候把1..len赋值成-1.

然后每次移动区间，从【l,r】移动到[l+1,r+1]的时候，将f[r+1]添加1，将f[l]减少1.

这样如果某个s中的任意前缀和都是等于0的，那么这个s就是合法的。

因此我们只需要维护最小前缀和。

代码是维护的最小前缀和



    
    /* ***********************************************
    Author :111qqz
    Created Time :Fri 16 Sep 2016 05:13:38 PM CST
    File Name :code/cf/problem/338E.cpp
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
    const int N=150005;
    int n,len,h;
    int a[N],b[N],f[N];
    struct Tree
    {
        int mn;//最小前缀和
        int sum;//区间和
    }tree[N<<2];
    void PushUp( int rt)
    {
        tree[rt].sum = tree[rt<<1].sum + tree[rt<<1|1].sum;
        tree[rt].mn = min(tree[rt<<1].mn,tree[rt<<1].sum+tree[rt<<1|1].mn);
    }
    void build( int l,int r,int rt)
    {
        if (l==r)
        {
    	if (l<=len)
    	tree[rt].sum = tree[rt].mn = -1;
    	return;
        }
        int m = (l+r)>>1;
        build(lson);
        build(rson);
        PushUp(rt);
    }
    void update( int p,int sc,int l,int r,int rt)
    {
        if (l==r)
        {
    	tree[rt].sum += sc;
    	tree[rt].mn +=sc;
    	return;
        }
        int m = (l+r)>>1;
        if (p<=m) update(p,sc,lson);
        else update(p,sc,rson);
        PushUp(rt);
    }
    int bin( int x)
    {
        int l = 1;
        int r = len;
        int res = len+1; //无穷。
        while (l<=r)
        {
    	int mid = (l+r)>>1;
    	if (b[mid]+x>=h)
    	{
    	    r = mid-1;
    	    res = mid;
    	}
    	else
    	{
    	    l = mid+1;
    	}
        }
        return res;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	ios::sync_with_stdio(false);
    	ms(tree,0);
    	cin>>n>>len>>h;
    	int siz = len+1;
    	for ( int i = 1 ;i  <= len ; i++) cin>>b[i];
    	sort(b+1,b+len+1);
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    int x;
    	    cin>>x;
    	    a[i] = bin(x);
    	}
    	build(1,siz,1);
    	for ( int i = 1 ; i < len ; i++) update(a[i],1,1,siz,1);
    	int ans = 0 ;
    	for ( int i = len ; i <= n ; i++)
    	{
    	    update(a[i],1,1,siz,1);
    	    if (tree[1].mn==0) ans++;
    	    update(a[i-len+1],-1,1,siz,1);
    	}
    	cout<<ans<<endl;
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



