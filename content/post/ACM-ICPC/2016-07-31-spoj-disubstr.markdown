---
author: 111qqz
date: 2016-07-31 19:31:42+00:00
draft: false
title: spoj DISUBSTR - Distinct Substrings (统计字串个数，后缀数组)
type: post
url: /2016/08/spoj-disubstr/
categories:
- ACM
tags:
- 后缀数组
---

[题目链接](http://www.spoj.com/problems/DISUBSTR/en/)

题意：给出一个字符串，问所有不同的字串的个数。

思路：直接求比较困难。我们考虑，假如组成字符串的所有字符都不相同，那么就没有相同的字串，假设字符串的长度为n，那么长度为1的子串有n个，为2的有n-1个。。。为n的有1个，一共就是n*(n+1)/2个。。但是实际上会有重复的。。。

我们再次考虑这张图。[![Selection_004](https://111qqz.com/wordpress/wp-content/uploads/2016/08/Selection_004.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/08/Selection_004.png)

先找一个字符重复的个数，对应height[i]数组就是找height[i]大于等于1个的个数（**因为x个height代表了x+1个后缀，保留1个，重复了x个，所以重复的个数恰好和符合条件的height数组对应**）

接着找大于等于2的个数，大于等于3的个数...

最后再把所有答案累加起来，就是总共重复的次数。

然后按照我推出的这个结论，试着写了一发。。。1A蛤蛤蛤。。。

能想到这里大概是因为之前的题目让我得出了，“height数组是个小妖精”的结论,所以入手就先观察了一下height数组。。。

具体的实现呢，就是先统计height[i]中每个值出现的次数，然后做一个后缀和，最后累加。

 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年08月01日 星期一 02时43分19秒
    File Name :code/spoj/disubstr.cpp
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
    const int N=1E3+7;
    int n;
    char s[N];
    int sa[N],rk[N],t[N],t2[N],cnt[N];
    int height[N];
    int cmp(int *r,int a,int b,int l){return r[a]==r[b]&&r[a+l]==r[b+l];}
    
    void getSa(int n,int m)
    {
        int *x = t,*y = t2;
        ms(cnt,0);
        for ( int i = 0 ; i < n ; i++) cnt[x[i]=s[i]]++;
        for ( int i = 1 ; i < m ; i++) cnt[i] += cnt[i-1];
        for ( int i = n-1 ; i >= 0 ; i--) sa[--cnt[x[i]]] = i ;
        for ( int k = 1 ; k <=  n;  k <<=1 )
        {
    	int p = 0 ;
    	for ( int i = n-k ; i < n; i ++) y[p++] = i;
    	for (  int i = 0 ; i < n ; i++) if (sa[i]>=k) y[p++] = sa[i]-k;
    	ms(cnt,0);
    	for ( int i = 0 ; i < n ; i++) cnt[x[y[i]]]++;
    	for ( int i = 0 ; i < m ; i++) cnt[i]+=cnt[i-1];
    	for ( int i = n-1 ; i >= 0 ; i--) sa[--cnt[x[y[i]]]] = y[i];
    	swap(x,y);
    	p = 1;
    	x[sa[0]] = 0;
    	for ( int i = 1 ; i < n ; i++)
    	    x[sa[i]] = cmp(y,sa[i-1],sa[i],k)?p-1:p++;
    	if (p>=n) break;
    	m = p;
        }
    }
    
    void getHeight( int n)
    {
        int k = 0 ;
        for ( int i = 0 ; i < n ;i ++) rk[sa[i]] = i ;
        height[0] = 0 ;
        for ( int i = 0 ; i < n;  i++)
        {
    	if (rk[i]==0) continue;
    	if (k) k--;
    	int j = sa[rk[i]-1];
    	while (s[i+k]==s[j+k]) k++;
    	height[rk[i]] = k ;
        }
    }
    
    int getSuffix( char s[])
    {
        int len = strlen(s);
        int up = 0;
        for ( int i = 0 ; i < len ; i++)
        {
    	int val = s[i];
    	up = max(up,val);
        }
        s[len++]='$';
        getSa(len,up+1);
        getHeight(len);
        return len;
    }
    
    int solve( int n)
    {
      //  for ( int i = 0 ; i < n ; i++) cout<<"i:"<<i<<" height[i]:"<<height[i]<<endl;
        
        ms(cnt,0); //cnt在求完sa之后就没用了，所以拿来用一下，嘿嘿嘿
        int up = 0 ;
        for ( int i = 0 ; i < n; i++) cnt[height[i]]++,up=max(up,height[i]);
    
        for ( int i = up-1 ; i >=1 ; i--) cnt[i] = cnt[i]+cnt[i+1];
        int res = 0 ;
        //for ( int i = 1 ; i <= up; i++) cout<<"cnt[i]:"<<cnt[i]<<endl;
        for ( int i = 1 ; i <= up ; i++ )
    	res += cnt[i];
        return res;
    }
    
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	int T;
    	scanf("%d",&T);
    	while (T--)
    	{
    	    scanf("%s",s);
    	   int len = getSuffix(s);
    	   int ans = len*(len-1)/2;
    	    ans-=solve(len);
    	    printf("%d\n",ans);
    
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    









