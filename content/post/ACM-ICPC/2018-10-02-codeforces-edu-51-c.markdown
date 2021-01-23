---
author: 111qqz
date: 2018-10-02 10:49:29+00:00
draft: false
title: 'codeforces edu #51 C. Vasya and Multisets (思维题)'
type: post
url: /2018/10/codeforces-edu-51-c/
categories:
- ACM
tags:
- 思维题
---

[题目链接](http://codeforces.com/contest/1051/problem/C)

题意:有n个数，现在要分成2个集合，使得2个集合中，仅出现1次的数的个数相同，问是否有解，以及具体的分法。

思路:

一开始考虑出现多个的数的思路麻烦了，比如对于出现2次的某个数x，**与其一个集合中分得一个，使得两个结合中，仅出现1次的数的个数各+1，还不如都放在同一个集合中，使得仅出现1次的数的个数不增加。**

因此思路是这样的:

先考虑出现1次的数的个数，如果为偶数，那么均分，然后把其他出现多次的数全都放在第一个集合；

如果出现1次的数的个数为奇数，我们还是尽可能均分，然后不妨假设第一个集合中的只出现1次的数的个数比第二个集合中多1个。

我们现在需要让第二个集合中，仅出现一次的数增加一个。

什么样的数可以满足这个条件呢？ 出现2次的数是不行的，因为这会使得两个集合中的数字各自+1

因此需要至少有一个出现3次或者以上的数。

具体见代码:

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年10月02日 星期二 15时28分39秒
    File Name :c.cpp
    ************************************************ */
    #include <bits/stdc++.h>
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
    int n;
    int cnt[N];
    int a[N];
    string ans="";
    int main()
    {
            #ifndef  ONLINE_JUDGE 
        //    freopen("./in.txt","r",stdin);
      #endif
    		cin>>n;
    		ms(cnt,0);
    		for ( int i = 1; i <= n ; i++)
    		{
    			cin>>a[i];
    			cnt[a[i]]++;
    		}
    		int cnt_1 = 0;
    		for ( int i = 1 ; i <= 100 ; i++)
    		{
    			if (cnt[i]==1) cnt_1++;
    		}
    		int cur_1 = 0 ;
    		for ( int i = 1 ;i  <= n ; i++)
    		{
    			if (cnt[a[i]]>=2)
    			{
    				ans+='A';
    			}
    			if (cnt[a[i]]==1)
    			{
    				cur_1++;
    				if (cur_1<=(cnt_1+1)/2)
    				{
    					ans+='A';
    				}
    				else
    				{
    					ans+='B';
    				}
    			}
    		}
    
    		if (cnt_1%2==0)
    		{
    			puts("YES");
    			cout<<ans<<endl;
    		}
    		else
    		{
    			bool triple = false;
    			for ( int i = 1; i <= n ; i++)
    			{
    				if (cnt[a[i]]>=3&&!triple)
    				{
    					triple = true;
    					ans[i-1] = 'B';
    				}
    			}
    			if (triple)
    			{
    				puts("YES");
    				cout<<ans<<endl;
    			}
    			else
    			{
    				puts("NO");
    			}
    		}
    			
    
    
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }



