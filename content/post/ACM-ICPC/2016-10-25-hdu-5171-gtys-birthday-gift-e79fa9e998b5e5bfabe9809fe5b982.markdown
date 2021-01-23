---
author: 111qqz
date: 2016-10-25 10:56:10+00:00
draft: false
title: hdu 5171 GTY's birthday gift (矩阵快速幂)
type: post
url: /2016/10/hdu-5171-gtys-birthday-gift-/
categories:
- ACM
tags:
- 快速幂
- 斐波那契
- 矩阵
---

[题目链接](http://acm.hdu.edu.cn/showproblem.php?pid=5171)

题意：给出n,k，以及n个正数，把n个数放在一个集合里，进行k次操作，每次操作取最大的数和次大的数放进集合。问k次操作结束后，集合中所有数的和。

思路：假设初始时刻，次大和最大分别为a0,a1，那么得到的就是一个类斐波那契数列。初始为a0,a1,fn = fn-1 + fn

最后求和。



[![screenshot-from-2016-10-25-18-48-09](https://111qqz.com/wordpress/wp-content/uploads/2016/10/Screenshot-from-2016-10-25-18-48-09.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/10/Screenshot-from-2016-10-25-18-48-09.png)

利用这个性质。。。

我们直接构造完矩阵。。。求出F(n+2)即可。。

需要注意。。。矩阵中每一项是小于1E7+7的。。。矩乘的时候会爆int...

所以mat要用LL存。。我好傻啊。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :Thu 20 Oct 2016 10:40:39 AM CST
    File Name :code/hdu/5171.cpp
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
    const int N =1E5+7;
    const LL mod = 1E7+7;
    int n;
    LL k;
    LL a[N];
    LL sum;
    LL a0,a1;
    struct Mat
    {
        LL mat[3][3];
        void clear()
        {
    	ms(mat,0);
        }
        Mat operator*(const Mat &b)const
        {
    	Mat ans;
    	ans.clear();
    	for ( int i = 0 ; i < 2 ; i++)
    	    for ( int j = 0 ; j < 2 ; j++)
    		for ( int k = 0 ; k < 2 ; k++)
    		    ans.mat[i][j] = ( ans.mat[i][j] + mat[i][k] * b.mat[k][j] ) % mod;
    	return ans;
        }
        void pr()
        {
    	cout << mat[0][0] << ' ' <<  mat[0][1] << endl << mat[1][0] << ' ' << mat[1][1] << endl;
        }
        Mat operator ^ ( LL b)
        {
    	Mat res;
    	res.clear();
    	for ( int i = 0 ; i < 2 ; i++) res.mat[i][i] = 1;
    	Mat a = *this;
    	while (b>0)
    	{
    	    if (b&1) res = res * a;
    	    b = b >> 1LL;
    	    a = a * a;
    	}
    	return res;
        }
        void out()
        {
    	for ( int i = 0 ; i < 2 ; i++)
    	{
    	    for ( int j = 0 ; j < 2 ; j++)
    	    {
    		printf("%d ",mat[i][j]);
    	    }
    		printf("\n");
    	}
        }
    }M,M1;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	while (~scanf("%d%lld",&n,&k))
    	{
    	    sum = 0 ;
    	    for ( int i = 1 ; i <= n ; i++)
    	    {
    		scanf("%lld\n",&a[i]);
    		sum = (sum + a[i])%mod;
    	    }
    	    sort(a+1,a+n+1);
    	    a0 = a[n-1];
    	    a1 = a[n];
    	  //  cout<<"a0:"<<a0<<" a1:"<<a1<<endl;
    	    M1.clear();
    	    M1.mat[0][0] = a0;
    	    M1.mat[1][0] = a1;
    	    M.clear();
    	    M.mat[0][1] = 1;
    	    M.mat[1][0] = 1;
    	    M.mat[1][1] = 1;
    	    Mat ans;
    	    ans.clear();
    	    ans = (M^(k+2))*M1;
    	    sum = sum-a0-a1;
    	    printf("%lld\n",(sum + ans.mat[1][0]-a1+mod) % mod);
        	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





