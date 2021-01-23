---
author: 111qqz
date: 2016-04-18 08:46:54+00:00
draft: false
title: poj 3974 Palindrome (最长回文字串，manacher裸题)
type: post
url: /2016/04/poj-3974-palindrome-manacher/
categories:
- ACM
tags:
- manacher
---

[poj3974](http://poj.org/problem?id=3974)
题意：求最大长度的回文字串。
思路：manacher裸题，用来练习算法。 
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月18日 星期一 16时32分25秒
    File Name :code/poj/3974.cpp
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
    const int N=2E6+7;
    char st[2*N];
    int p[2*N];
    
    int manacher(char *s)
    {
        int len = strlen(s);
        for ( int i = len ; i >= 0 ; i-- )
        {
    	s[i+i+2]=s[i];
    	s[i+i+1]='#';
        }
        s[0]='$';
    
        int id = 0 ;
        int maxlen = 0 ;
    
        for ( int i = 2 ; i < 2*len+1 ; i++)
        {
    	if (id+p[id]>i) p[i] = min(p[2*id-i],id+p[id]-i);
    	else p[i] = 1;
    	
    	while (s[i+p[i]]==s[i-p[i]]) p[i]++;
    	if (id+p[id]<i+p[i]) id =  i;
    	if (p[i]>maxlen) maxlen = p[i];
        }
        return maxlen-1;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int cas = 0 ;
    	while (scanf("%s",st)!=EOF)
    	{
    	    if (st[0]=='E'&&st[1]=='N'&&st[2]=='D') break;
    	    printf("Case %d: %d\n",++cas,manacher(st));
    
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




