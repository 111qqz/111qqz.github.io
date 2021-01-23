---
author: 111qqz
date: 2016-03-31 07:45:36+00:00
draft: false
title: 'codeforces #346 div 2 A. Round House'
type: post
url: /2016/03/codeforces-346-div-2-a-round-house/
categories:
- ACM
---

[题目链接](http://codeforces.com/contest/659/problem/A)

水题
乱搞。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年03月30日 星期三 23时59分47秒
    File Name :code/cf/#346/A.cpp
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
    int n,a,b;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n>>a>>b;
    	a = a + b;
    	while (a<=0) a+=n;
    	while (a>n) a-=n;
    	cout<<a<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



