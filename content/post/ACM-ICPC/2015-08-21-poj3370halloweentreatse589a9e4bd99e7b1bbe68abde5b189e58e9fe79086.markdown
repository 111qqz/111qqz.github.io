---
author: 111qqz
date: 2015-08-21 05:36:00+00:00
draft: false
title: poj 3370 Halloween treats (剩余类,抽屉原理)
type: post
url: /2015/08/poj3370halloweentreats/
categories:
- ACM
tags:
- number theory
- 剩余系
- 抽屉原理
---







昨天那道签到的数学题没搞出来不开心.




是时候刷一波数学了







这题题意是说,从n个数中任选m个,使得m个的和为c的倍数.




如果有解,输出选的数的下标,否则输出无解字符串.







抽屉原理的原始描述是,如果有n+1个物品,有n个抽屉,那么至少有一个抽屉有2个物品.




由**抽屉原理我们可以退出一个结论,对于任意 n个自然数,一定有连续的一段和为n的倍数.**




证明如下:




　　设这n个自然数分别为a1,a2,a3,a4....an




　　处理一个前缀和sum[i] = (sum[i-1] + a[i])%n




　　因为n的剩余类有n种,分别为0,1,2...n-1




　　所以sum[1],sum[2],sum[3]..sum[n]




　　那么sum[1],sum[2],sum[3]...sum[n]最多也有n种.




　　我们分情况讨论:




　　　　(1)sum[1],sum[2],sum[3]...sum[n]互不相同,那么一定存在sum[i]=0,也就是前i个数的和为n的倍数.




　　　　(2)情况(1)的反面,也就是存在sum[i]==sum[j]  (i<j),那么 从a[i+1] 到 a[j]的和就是n的倍数.










因为题目中的数据 c<=n ,所以解一定存在.




具体做法就是处理出来一个前缀和%c




然后如果有0,则为解,输出.




否则记录sum[i]%d出现的位置,存在一个数组里




如果sum[i]%d第二次出现,就输出这段下标.







嘛,大括号换风格了....




都写开代码太长了==






    
    /*************************************************************************
    	> File Name: code/poj/3370.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月21日 星期五 13时06分34秒
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
    const int inf = 0x3f3f3f3f;
    const int N=1E5+7;
    int a[N];
    LL sum[N];
    int p[N];
    int n,c;
    int main()
    {
        while (~scanf("%d %d",&c,&n)){
    	if (c==0&&n==0) break;
    	sum[0]  = 0;
    	for ( int i  = 1 ; i <= n ;i++){
    		scanf("%d",&a[i]);
    	    a[i] = a[i] % c;
    	    sum[i] = (sum[i-1] + a[i])%c;
    	}
    	memset(p,0,sizeof(p));
    	for ( int i = 1 ; i <= n ; i++ ){
    	    if (sum[i]==0){
    		for ( int  j = 1 ;  j <= i ; j++){
    		    cout<<j<<" ";
    		   // cout<<"wang wang wang !"<<endl;
    		}
    		cout<<endl;
    		break;
    	    }
    	    if (p[sum[i]]){
    		for ( int  j = p[sum[i]]+1 ; j <= i ; j++){
    		    cout<<j<<" ";
    	//	    cout<<"111qqz"<<endl;
    		}
    		cout<<endl;
    		break;
    	    }
    	    p[sum[i]] = i ;
    	}
        }
      
    	return 0;
    }
    



