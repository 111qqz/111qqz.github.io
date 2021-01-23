---
author: 111qqz
date: 2015-09-18 15:28:00+00:00
draft: false
title: 'codeforces #320 div 2A - Raising Bacteria (位运算）'
type: post
url: /2015/09/codeforces320div2a-raisingbacteria/
categories:
- ACM
tags:
- 位运算
---




x的二进制表示中1的个数即为答案．




原因是，每天晚上糖果数量翻倍，相当于左移１位,这时候二进制表示中1的数量不变




也就是说，二进制表示中的所有的1，一定都是添加进去的




而且也只有二进制表示中的1是添加进去的




所以二进制表示中1的数量，就是添加的糖果数．


 

    
    /*************************************************************************
    	> File Name: code/cf/#320/A.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月18日 星期五 23时18分34秒
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
    int main()
    {
      #ifndef  ONLINE_JUDGE 
      
      #endif
        int x;
        cin>>x;
        int ans = 0 ;
        while (x)
        {
    	if (x%2==1) ans++;
    	x = x / 2;
        }
        cout<<ans<<endl;
      
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



