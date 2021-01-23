---
author: 111qqz
date: 2015-07-29 06:28:00+00:00
draft: false
title: '(bc #45) A - Dylans loves numbers (hdu 5272)'
type: post
url: /2015/07/bc45a-dylanslovesnumbershdu5272/
categories:
- ACM
tags:
- brute force
---














快要炸了..




tle成狗




![](https://111qqz.com/wp-content/uploads/2015/11/291423556423808.png)








因为是tle,看了下自己没有写cin cout,估计就是算法的问题...




我是先存了二进制的每一位到数组,然后扫一遍...




嗯,这都tle...




那我不存不扫,直接记录当前二进制位和之前二进制位..




logn的复杂度总可以了吧啊?




还TLE..........




嗯,其实已经发现 n是小于等于1e18的,没开long long




但是一位没开long long 会是wa...就没理...




之后实在黔驴技穷,改了下,竟然过了...




然后想明白了.




因为存二进制的时候有一个while




没开long long 的话就炸了,不知道读进去的是什么,while就出不来,于是就tle了.T T




果然太年轻.







```c++
 

    
    /*************************************************************************
    	> File Name: code/bc/#45/1001.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年07月29日 星期三 13时25分01秒
     ************************************************************************/
    
    #include<iostream>
    #include<iomanip>
    #include<cstdio>
    #include<algorithm>
    #include<cmath>
    #include<cstring>
    #include<string>
    #include<map>
    #include<set>
    #include<queue>
    #include<vector>
    #include<stack>
    #define y0 abc111qqz
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define tm crazy111qqz
    #define lr dying111qqz
    using namespace std;
    #define REP(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef unsigned long long ULL;
    const int inf = 0x7fffffff;
    const int N=1E3+5;
    int a[N];
    LL n,nn;
    int main()
    {
        int T;
        cin>>T;
        while (T--)
        {
    	scanf("%lld",&n);
    	nn = n ;
    	int k = 0;
    	while (nn)
    	{
    	    k++;
    	    a[k]=nn&1;
    	    nn = nn >>1;
    	}
    	int ans = 0;
    //	for ( int i = 1 ; i <= k ; i++ )
    //	    cout<<a[i]<<endl;
    	for ( int i = 1 ; i <= k ; i++ )
    	{
    	    if (a[i]==1&&a[i-1]==0)
    		ans++;
    	}
    	printf("%d\n",ans);
        }
    	return 0;
    }
    


```
