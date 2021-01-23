---
author: 111qqz
date: 2015-12-23 06:12:24+00:00
draft: false
title: 'codeforces #333 div 2 D. Lipshitz Sequence'
type: post
url: /2015/12/codeforces-333-div-2-d-lipshitz-sequence/
categories:
- ACM
tags:
- math
---

http://codeforces.com/contest/602/problem/D
题意：见题目描述。
思路：我们很容易发现，l[h]函数其实就是在求区间斜率的最大值。哦不对，是斜率的绝对值的最大值。而且一个显而易见的结论是，斜率最大值一定是由相邻的点得到。画图可以很容易看出。


<blockquote>具体的证明见这里：

In order to prove it properly, we'll consider three numbers _A__i_, _A__j_, _A__k_ (_i_ < _j_ < _k_) and show that one of the numbers _L_1(_i_, _j_),_L_1(_j_, _k_) is  ≥ _L_1(_i_, _k_). W.l.o.g., we may assume _A__i_ ≤ _A__k_. There are 3 cases depending on the position of _A__j_ relative to _A__i_, _A__k_:

> 
> 
	  * _A__j_ > _A__i_, _A__k_ — we can see that _L_1(_i_, _j_) > _L_1(_i_, _k_), since |_A__j_ - _A__i_| = _A__j_ - _A__i_ > _A__k_ - _A__i_ = |_A__k_ - _A__i_| and _j_ - _i_ < _k_ - _i_; we just need to divide those inequalities
	  * _A__j_ < _A__i_, _A__k_ — this is similar to the previous case, we can prove that _L_1(_j_, _k_) > _L_1(_i_, _k_) in the same way
	  * _A__i_ ≤ _A__j_ ≤ _A__k_ — this case requires more work:

	    * we'll denote _d_1_y_ = _A__j_ - _A__i_, _d_2_y_ = _A__k_ - _A__j_, _d_1_x_ = _j_ - _i_, _d_2_x_ = _k_ - _j_


	    * then, _L_1(_i_, _j_) = _d_1_y_ / _d_1_x_, _L_1(_j_, _k_) = _d_2_y_ / _d_2_x_, _L_1(_i_, _k_) = (_d_1_y_ + _d_2_y_) / (_d_1_x_ + _d_2_x_)


	    * let's prove it by contradiction: assume that _L_1(_i_, _j_), _L_1(_j_, _k_) < _L_1(_i_, _k_)


	    * _d_1_y_ + _d_2_y_ = _L_1(_i_, _j_)_d_1_x_ + _L_1(_j_, _k_)_d_2_x_ < _L_1(_i_, _k_)_d_1_x_ + _L_1(_i_, _k_)_d_2_x_ = _L_1(_i_, _k_)(_d_1_x_ + _d_2_x_) = _d_1_y_ + _d_2_y_, which is a contradiction



We've just proved that to any _L_1 computed for two elements _A_[_i_], _A_[_k_] with _k_ > _i_ + 1, we can replace one of _i_, _j_ by a point _j_between them without decreasing _L_1; a sufficient amount of such operations will give us _k_ = _i_ + 1. Therefore, the max. _L_1can be found by only considering differences between adjacent points.</blockquote>


这样子就好做了很多。由于斜率绝对值的最大值一定在由相邻的两个点得到。而相邻两个点的横坐标差1，所以斜率的绝对值就变成了相邻元素差的最大值。因此我们可以预处理一个数组b，表示相邻元素的差的绝对值。

接下来的问题就变成了如何求b的一段区间里的所有子区间的最大值的和。我们的思路是考虑这个区间里每个元素对答案的贡献。显然，对于b中越大的元素，它对答案的贡献会越多，因为会有更多包含它的区间以它为最大值。具体来讲，对于这个区间的每一个元素，我们可以分别向左和右边扩展，看最大能到哪里。

比如3 4 3 8 2 7 1，对于8，左边可以到达3，与8的距离为3，右边可以到达1，与8的距离为3，那么8对答案的贡献为(3+1)*(3+1)*8，也就是说一共有4*4个区间的最大值为8.对于7，左边可以到2，距离7为1，右边可以到1，距离7长度为1，那么7对答案的贡献就是（1+1）×（1+1）*7，也就是有4个区间的最大值为7.分别为{2}，{2,7}，{7,1}，{2,7,1}

由于q不算很大，可以直接搞...用两个数组right和left代表能到达的右边和左边的最远位置。







    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月22日 星期二 22时58分35秒
    File Name :code/cf/#333/D.cpp
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
    #define left lllllxy
    #define right rrrrrxy
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    const int N=1E5+7;
    int n ; 
    int q;
    LL a[N],b[N];
    int left[N];
    int right[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n;
    	cin>>q;
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    cin>>a[i];
     
    	}
    	for ( int i = 2 ;i  <= n ; i++)
    	{
    	    b[i] = abs(a[i]-a[i-1]);
    	}
    
    	while (q--)
    	{
    	    int l,r;
    	    scanf("%d %d",&l,&r);
    	    l++;
    
    	    for ( int i = l ; i <= r ; i++)        //以b[i]为最大值，最左能到达多远。
    	    {
    		left[i] = i ;
    		while (left[i]>l&&b[i]>b[left[i]-1])
    		    left[i] = left[left[i]-1];
    	    }
    	    for ( int i = r ; i >= l ; i--)         //最右能到达多远。
    	    {
    		right[i] = i;
    		while (right[i] < r &&b[i]>=b[right[i]+1])
    		    right[i] = right[right[i] + 1];
        	    }
    	    LL ans= 0 ;
    	    for ( int i = l ; i <= r ; i++)
    		ans +=(LL)(right[i]-i+1)*(LL)(i-left[i]+1)*b[i];
    	    cout<<ans<<endl;
    
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



