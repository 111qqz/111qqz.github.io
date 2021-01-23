---
author: 111qqz
date: 2015-08-23 08:06:00+00:00
draft: false
title: 'codeforces #317 div2 A. Arrays (水)'
type: post
url: /2015/08/codeforces317div2a-arrays/
categories:
- ACM
tags:
- 水题
---




应该３分钟过的题。。。




结果花了８分钟。。。ssssad


 

    
    /*************************************************************************
    	> File Name: code/cf/#317/A.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月23日 星期日 00时29分47秒
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
    int na,nb,k,m;
    int a[N],b[N];
    int main()
    {
      #ifndef  ONLINE_JUDGE 
        freopen("in.txt","r",stdin); 
      #endif
        cin>>na>>nb;
        cin>>k>>m;
        for ( int i = 1 ; i <= na ; i++){
    	scanf("%d",&a[i]);
        }
        for ( int i  = 1 ; i<= nb ; i++){
    	scanf("%d",&b[i]);
        }
        if (a[k]<b[nb-m+1]){
    	puts("YES");
        }
        else
        {
    	puts("NO");
        }
      
      
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



