---
author: 111qqz
date: 2016-08-02 10:50:52+00:00
draft: false
title: spoj SUBST1 - New Distinct Substrings(后缀数组)
type: post
url: /2016/08/spoj-subst1-new-distinct-substrings/
categories:
- ACM
tags:
- 后缀数组
---

[题目连接](http://www.spoj.com/problems/SUBST1/en/)

题意：求所有不同的子串个数。

思路：后缀数组。和上一道题一样，就是数据范围变成了 5E4...1A

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年08月02日 星期二 18时32分28秒
    File Name :code/spoj/subst1.cpp
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
    const int  N=5E4+7; 
    char s[N];
    int sa[N],rk[N],t[N],t2[N],cnt[N],height[N];
    int cmp (int *r,int a,int b,int l){ return r[a]==r[b]&&r[a+l]==r[b+l];}
    void getSa(int n,int m)
    {
        int *x=t,*y=t2;
        ms(cnt,0);
        for ( int i = 0 ; i < n ; i++) cnt[x[i]=s[i]]++;
        for ( int i = 0 ; i < m ; i++) cnt[i]+=cnt[i-1];
        for ( int i = n-1 ; i >= 0 ; i--) sa[--cnt[x[i]]] = i;
        for ( int k = 1 ; k <= n ; k<<=1)
        {
    	int p = 0;
    	for ( int i = n-k ; i < n ; i++) y[p++] = i;
    	for ( int i = 0 ; i < n;  i++) if (sa[i]>=k) y[p++] = sa[i]-k;
    	ms(cnt,0);
    	for ( int i = 0 ; i <n ; i++) cnt[x[y[i]]]++;
    	for ( int i = 0 ;i < m ; i++) cnt[i]+=cnt[i-1];
    	for ( int i = n-1 ; i >= 0 ; i--) sa[--cnt[x[y[i]]]] = y[i];
    	swap(x,y);
    	p = 1;
    	x[sa[0]] = 0;
    	for ( int i = 1 ; i < n ; i++ )
    	    x[sa[i]] = cmp(y,sa[i-1],sa[i],k)?p-1:p++;
    	if (p>=n) break;
    	m = p;
        }
    }
    void getHeight( int n)
    {
        int k = 0 ;
        for ( int i = 0 ; i <n ; i ++) rk[sa[i]] = i ;
        height[0] = 0 ;
        for ( int i = 0 ; i < n ; i++)
        {
    	if (rk[i]==0) continue;
    	if (k) k--;
    	int j = sa[rk[i]-1];
    	while (s[i+k]==s[j+k]) k++;
    	height[rk[i]] = k;
        }
    }
    int getSuffix(char s[])
    {
        int len = strlen(s);
        int up = 0 ;
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
    int solve ( int n)
    {
        ms(cnt,0);
        int up  =  0;
        for ( int i = 0 ;i <n ; i ++) cnt[height[i]]++, up = max(up,height[i]);
        for ( int i = up-1 ; i >= 1;  i--) cnt[i]+=cnt[i+1];
        int res = 0 ;
        for ( int i = 1 ; i <=up ; i++)
    	res+=cnt[i];
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
    	    LL ans = 1LL*len*(len-1)/2;
    	    ans-=1LL*solve(len);
    	    printf("%lld\n",ans);
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    









