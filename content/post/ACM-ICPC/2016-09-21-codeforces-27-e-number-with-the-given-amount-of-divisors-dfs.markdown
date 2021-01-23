---
author: 111qqz
date: 2016-09-21 09:02:26+00:00
draft: false
title: codeforces 27 E. Number With The Given Amount Of Divisors (dfs，反素数（假）)
type: post
url: /2016/09/codeforces-27-e-number-with-the-given-amount-of-divisors-dfs/
categories:
- ACM
tags:
- dfs
- number theory
- 反素数
---

[题目链接](http://codeforces.com/contest/27/problem/E)

题意：求约数个数**恰好**为n个的最小的x

思路：这道题是作为反素数的例题出现在acdreamer的博客里的。

但是实际上，这道题应该和反素数没有关系。

如果题目问的是最小的约数个数大于等于n的x，那么答案一定是反素数...打表就行了。。。

但是问的是**恰好，**比如如果n为5，那么最小的x是16，但是x不是反素数。

所以其实就是个dfs啦。

理论依据是：

一个数 A 可以分解成 p1k1 * p2k2 * …… * pnkn 其中p为素数。这样分解之后，A的因子个数

S = （k1+1） *（ k2+1） * …… *（ kn+1）



以及要找的是一个最小的x，满足约数个数等于n。

那么关于反素数的两个性质依然是满足的：


<blockquote>（1）一个反素数的所有质因子必然是从2开始的连续若干个质数，因为反素数是保证约数个数为![](http://img.blog.csdn.net/20140505150741093)
的这个数![](http://img.blog.csdn.net/20140505145329656)
尽量小

（2）同样的道理，如果![](http://img.blog.csdn.net/20140505151209203)
，那么必有![](http://img.blog.csdn.net/20140505151330421)
</blockquote>



    
    /* ***********************************************
    Author :111qqz
    Created Time :Wed 21 Sep 2016 04:48:42 PM CST
    File Name :code/cf/problem/27E.cpp
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
    int prime[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47};
    int n;
    LL ans = 1LL<<60;
    void dfs( int depth,LL val,int num)
    {
        if (num>n) return;
        if (num==n&&val<ans) ans = val;
        for ( int i = 1 ; i <=63 ; i++) //最多63个质数。。。因为2^64>1E18
        {
    	if (val*prime[depth]>ans) break;
    	dfs(depth+1,val*=prime[depth],num*(i+1));
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n;
    	dfs(0,1,1);
    	cout<<ans<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    













