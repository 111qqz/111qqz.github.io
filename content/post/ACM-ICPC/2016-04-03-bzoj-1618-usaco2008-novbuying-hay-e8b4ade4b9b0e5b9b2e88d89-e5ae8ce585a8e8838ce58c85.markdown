---
author: 111qqz
date: 2016-04-03 11:53:05+00:00
draft: false
title: 'BZOJ 1618: [Usaco2008 Nov]Buying Hay 购买干草 (完全背包)'
type: post
url: /2016/04/bzoj-1618-usaco2008-novbuying-hay--/
categories:
- ACM
tags:
- dp
- 完全背包
---




## 1618: [Usaco2008 Nov]Buying Hay 购买干草


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 906  Solved: 456
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1618)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1618)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1618)]


## Description







    约翰的干草库存已经告罄，他打算为奶牛们采购日(1≤日≤50000)磅干草．




    他知道N(1≤N≤100)个干草公司，现在用1到N给它们编号．第i个公司卖的干草包重量为Pi(1≤Pi≤5000)磅，需要的开销为Ci(l≤Ci≤5000)美元．每个干草公司的货源都十分充足，可以卖出无限多的干草包．    帮助约翰找到最小的开销来满足需要，即采购到至少H磅干草．







## Input







    第1行输入N和日，之后N行每行输入一个Pi和Ci．







## Output










    最小的开销．







## Sample Input




2 15
3 2
5 3






## Sample Output




9


FJ can buy three packages from the second supplier for a total cost of 9.











思路：完全背包。。。注意是买至少V,可以超过。我的做法是算了两倍，然后取最小值（V..2V)






 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月03日 星期日 19时40分29秒
    File Name :code/bzoj/1618.cpp
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
    const int N=105;
    int p[N],c[N];
    int n;
    int V;
    int dp[1000005];
    
    void solve (int val,int cost)
    {
        for ( int i = value ; i <= V ; i++)
    	dp[i] = min(dp[i],dp[i-value]+cost);
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n>>V;
    	V*=2;
    	for  ( int i = 1 ; i <= n ; i++) cin>>p[i]>>c[i];
    
    	ms(dp,0x3f);
    	dp[0]=0;
    	for ( int i = 1 ; i <= n ; i++) solve(p[i],c[i]);
    	int ans = inf;
    	for ( int i = 1 ; i <= n ; i++)  ans = min(ans,dp[i]);
    	cout<<ans<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



