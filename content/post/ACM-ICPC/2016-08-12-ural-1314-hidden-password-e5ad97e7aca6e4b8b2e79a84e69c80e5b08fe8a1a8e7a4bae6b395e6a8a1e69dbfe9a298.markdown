---
author: 111qqz
date: 2016-08-12 17:14:46+00:00
draft: false
title: ural 1314 Hidden Password (字符串的最小表示法模板题)
type: post
url: /2016/08/ural-1314-hidden-password-/
categories:
- ACM

tags:
- 最小表示法
---

[uva 1314 题目链接](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4060)

题意：给定一个循环字符串，问字典序最小的串的开始位置。最小表示法裸题。


 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年08月12日 星期五 18时48分29秒
    File Name :code/uva/1314.cpp
    ************************************************ */
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <stack>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <deque>
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
    const int N=1E5+7;
    int n ;
    char s[N];
    int minRep(char *s)
    {
        int n = strlen(s);
        int i = 0;
        int j = 1;
        int k = 0;
        while (i<n&&j<n&&k<n)
        {
    	int t = s[(i+k)%n]-s[(j+k)%n];
    	if (t==0) k++;
    	else 
    	{
    	    if (t>0)
    		i+=k+1;
    	    else j+=k+1;
    	    if (i==j) j++;
    	    k = 0 ;
    	}
        }
        return i<j?i:j;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int T;
    	cin>>T;
    	while (T--)
    	{
    	    scanf("%d\n%s",&n,s);
    	    printf("%d\n",minRep(s));
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



