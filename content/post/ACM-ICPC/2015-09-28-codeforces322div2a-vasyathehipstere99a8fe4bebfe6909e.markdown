---
author: 111qqz
date: 2015-09-28 17:05:00+00:00
draft: false
title: 'codeforces #322 div 2 A. Vasya the Hipster(纱布题)'
type: post
url: /2015/09/codeforces322div2a-vasyathehipster/
categories:
- ACM
tags:
- 水
---
















A. Vasya the Hipster







time limit per test


1 second









memory limit per test


256 megabytes









input


standard input









output


standard output











One day Vasya the Hipster decided to count how many socks he had. It turned out that he had _a_ red socks and _b_ blue socks.

According to the latest fashion, hipsters should wear the socks of different colors: a red one on the left foot, a blue one on the right foot.

Every day Vasya puts on new socks in the morning and throws them away before going to bed as he doesn't want to wash them.

Vasya wonders, what is the maximum number of days when he can dress fashionable and wear different socks, and after that, for how many days he can then wear the same socks until he either runs out of socks or cannot make a single pair from the socks he's got.

Can you help him?









Input


The single line of the input contains two positive integers _a_ and _b_ (1 ≤ _a_, _b_ ≤ 100) — the number of red and blue socks that Vasya's got.









Output


Print two space-separated integers — the maximum number of days when Vasya can wear different socks and the number of days when he can wear the same socks until he either runs out of socks or cannot make a single pair from the socks he's got.

Keep in mind that at the end of the day Vasya throws away the socks that he's been wearing on that day.









Sample test(s)










input



    
    3 1










output



    
    1 1










input



    
    2 3










output



    
    2 0










input



    
    7 3










output



    
    3 2
















Note


In the first sample Vasya can first put on one pair of different socks, after that he has two red socks left to wear on the second day.

实在没有可以解释的...
 

    
    /*************************************************************************
    	> File Name: code/cf/#322/A.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月29日 星期二 00时14分24秒
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
      // freopen("in.txt","r",stdin);
      #endif
        int a,b;
        cin>>a>>b;
        int tmp = min(a,b);
        cout<<tmp<<" ";
        if (a>b)
        {
    	cout<<(a-b)/2<<endl;
        }
        else
        {
    	cout<<(b-a)/2<<endl;
        }
    
       
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



