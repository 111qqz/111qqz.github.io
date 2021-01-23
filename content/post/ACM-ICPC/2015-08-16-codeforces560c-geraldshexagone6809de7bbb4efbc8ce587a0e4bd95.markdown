---
author: 111qqz
date: 2015-08-16 23:28:00+00:00
draft: false
title: codeforces 560 C. Gerald's Hexagon (思维，几何)
type: post
url: /2015/08/codeforces560c-geraldshexagon/
categories:
- ACM
tags:
- 思维题
- 计算几何
---


题意：给定一个六边形的六条边的长，问能分割成多少个单位正三角形．



分割不好办，那我们就反着来，先补成一个包含这个六边形的正三角形．

对于边长为a的正三角形，显然我们可以分割成a*a个单位正三角形

大正三角形的边长为连续的三条边的和

而要减掉的三个小三角形的边长为与之前连续的三条边的起始边的序号的奇偶性相同的三条边．

就是说如果求和的时候求的是前三条边，那么三个要减掉的小三角形的边长就是第一，三，五条边．

如果求和的时候求的是后三条边，那么三个要减掉的小三角形的边长就是第二，第四，第六条边．
 

    
    /*************************************************************************
    	> File Name: code/#313/C.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月17日 星期一 07时13分54秒
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
    int main()
    {
        int a[10];
        int b[5];
        for ( int i = 1 ; i <= 6 ; i++)
        {
    	cin>>a[i];
        }
        memset(b,0,sizeof(b));
        for ( int i = 1 ; i <= 6 ; i++)
        {
    	if (i<=3)
    	{
    	    b[0] = b[0] + a[i] ;
    	}
    	if (i%2==1)
    	{
    	    b[i/2+1] = a[i];
    	}
        }
        int ans;
        ans = b[0]*b[0]-b[1]*b[1]-b[2]*b[2]-b[3]*b[3];
        cout<<ans<<endl;
      
    	return 0;
    }
    



