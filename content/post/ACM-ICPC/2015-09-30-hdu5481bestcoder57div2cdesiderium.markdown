---
author: 111qqz
date: 2015-09-30 03:37:00+00:00
draft: false
title: 'hdu 5481||bestcoder #57 div 2 C Desiderium (概率)'
type: post
url: /2015/09/hdu5481bestcoder57div2cdesiderium/
categories:
- ACM
tags:
- 概率
---

# Desiderium


**Time Limit: 4000/2000 MS (Java/Others)    Memory Limit: 65536/65536 K (Java/Others)
Total Submission(s): 427    Accepted Submission(s): 167
**


Problem Description






There is a set of intervals, the size of this set is n.

If we select a subset of this set with equal probability, how many the expected length of intervals' union of this subset is?

We assume that the length of empty set's union is 0, and we want the answer multiply 2n modulo 109+7.










Input






The first line of the input is a integer T, meaning that there are T test cases.

Every test cases begin with a integer n ,which is size of set.

Then n lines follow, each contain two integers l,r describing a interval of [l,r].

1≤n≤100,000.

−1,000,000,000≤l≤r≤1,000,000,000.











Output




For every test case output the answer multiply 2n modulo 109+7.









Sample Input







2
1
0 1
2
0 2
1 3











Sample Output









1 7





_Hint_


For the second sample, the excepted length is $frac{0+2+2+3}{4}=frac{7}{4}$.









比赛的时候并没有做出来...sad．．




因为b题调了太久...这题基本就没时间了．．．果然还是太弱了QAQ




然后发现有时间也做不出...




题意真是好难懂．．．




转载一段题解：




<blockquote>

> 
> 

一个含有n个区间的集合，从该集合中等概率地选取子集，求所有子集中的所有区间的构成的并集长度的和。

第二个样例解释：

集合中含有2个区间：一个是[0,2],编号为1，一个是[1,3]，编号为2。

集合的子集有4个：

1、空集，集合中区间的并的长度为0

2、{区间1}，集合中区间的并的长度为2

3、{区间2}，集合中区间的并的长度为2

4、{区间1、区间2}，集合中区间的并为[0,3]，长度为3

考虑某一个区间对于答案的贡献：

若某个区间没有被其它区间覆盖，则该区间在子集中出现的总次数为：2^(n-1)次（总子集数-去掉该区间的子集总数)

若某个区间被覆盖了1次，即有2个区间重叠，那么该区间在子集中出现总次数为：2^(n-1)+2^(n-2)次（第1个区间在子集中出现的次数+第2个区间在子集中出现且第1个区间不出现的总次数）

…………

可以得到

若该区间被覆盖了k(k>=0)次，即有k+1个区间重叠，得到该区间在所有子集中出现的总次数：2^(n-1)+2^(n-2)+……+2^(n-k-1)

如何统计每一个区间的重叠次数？

对于输入的每一个区间的两个端点，给一个权值，左端点为1，右端点为-1。然后把所有端点按照位置从小到大排序。从左往右扫一遍，累加端点的权值，得到的当前的权值和就是当前所在区间的重叠次数。

累加每个区间的重叠次数*区间长度，即为所求。


> 
> </blockquote>






    
    /*************************************************************************
    	> File Name: code/bc/#57/C.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月30日 星期三 11时08分35秒
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
    #include<cctype>
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define ms(a,x) memset(a,x,sizeof(a))
    #define lr dying111qqz
    using namespace std;
    #define For(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef double DB;
    const int inf = 0x3f3f3f3f;
    const int N=1E5+7;
    const int mod = 1E9+7; 
    struct P
    {
        int x,y;
    }a[N<<1];
    LL ans;
    int n;
    LL sum[N],p[N];
    bool cmp(P a,P b) {return a.x<b.x;}
    
    void init() { p[0] = 1;for (int i = 1 ; i < N  ; i ++) p[i] = p[i-1]*2 %mod;}
    int main()
    {
      #ifndef  ONLINE_JUDGE 
       freopen("in.txt","r",stdin);
      #endif
    
        init();
        int T;
        scanf("%d",&T);
        while(T--)
        {
            scanf("%d",&n);
            for(int i = 1 ; i <= 2*n ; i+=2)
    	{
                scanf("%d %d",&a[i].x,&a[i+1].x);
                a[i].y=1;
    	    a[i+1].y=-1;
            }
    
            sum[1]=p[n-1];
            for(int i = 2 ; i <= n ; i++ ) sum[i]=(sum[i-1]+p[n-i])%mod;
            sort(a+1,a+2*n+1,cmp);
            int ans=0;
    	int cnt=0;
            for(int i = 1 ; i < 2*n ;i++)
    	{
                cnt = cnt + a[i].y;
                ans=(ans+sum[cnt]*(a[i+1].x-a[i].x)%mod)%mod;
            }
            printf("%d\n",ans);
        }
      
       
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    









