---
author: 111qqz
date: 2015-09-25 14:46:00+00:00
draft: false
title: 'codeforces #321 div 2 B. Kefa and Company(尺取法)'
type: post
url: /2015/09/codeforces321div2b-kefaandcompany/
categories:
- ACM
tags:
- 尺取法
---
















B. Kefa and Company







time limit per test


2 seconds









memory limit per test


256 megabytes









input


standard input









output


standard output











Kefa wants to celebrate his first big salary by going to restaurant. However, he needs company.

Kefa has _n_ friends, each friend will agree to go to the restaurant if Kefa asks. Each friend is characterized by the amount of money he has and the friendship factor in respect to Kefa. The parrot doesn't want any friend to feel poor compared to somebody else in the company (Kefa doesn't count). A friend feels poor if in the company there is someone who has at least _d_ units of money more than he does. Also, Kefa wants the total friendship factor of the members of the company to be maximum. Help him invite an optimal company!









Input


The first line of the input contains two space-separated integers, _n_ and _d_ (1 ≤ _n_ ≤ 105, ![](http://codeforces.com/predownloaded/1a/e4/1ae48a19254167100a31cc359b7286e5912c0617.png)
) — the number of Kefa's friends and the minimum difference between the amount of money in order to feel poor, respectively.

Next _n_ lines contain the descriptions of Kefa's friends, the (_i_ + 1)-th line contains the description of the _i_-th friend of type _m__i_, _s__i_(0 ≤ _m__i_, _s__i_ ≤ 109) — the amount of money and the friendship factor, respectively.









Output


Print the maximum total friendship factir that can be reached.









Sample test(s)










input



    
    4 5
    75 5
    0 100
    150 20
    75 1










output



    
    100










input



    
    5 100
    0 7
    11 32
    99 10
    46 8
    87 54










output



    
    111
















Note


In the first sample test the most profitable strategy is to form a company from only the second friend. At all other variants the total degree of friendship will be worse.

In the second sample test we can take all the friends.



尺取直接搞...

然后因为没开longlong wa了一发...

因为看错条件,money差值等于d也会被鄙视．．．所以不能取等号...

都是傻逼错误...药丸，药丸啊...




 

    
    /*************************************************************************
    	> File Name: code/cf/#321/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月25日 星期五 17时21分55秒
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
    LL n,d;
    struct Q
    {
        LL m,f;
    }q[N];
    
    bool cmp(Q a,Q b)
    {
        if (a.m<b.m) return true;
        return false;
    }
    
    void solve()
    {
    
        LL head = 0 ;
        LL tail = 0 ;
        LL sum  = 0 ;
        LL  ans = -1 ;
        while (head<n)
        {
    	while (q[tail].m-q[head].m<d&&tail<n)
    	{
    	    sum += q[tail].f;
    //	    cout<<"sum:"<<sum<<endl;
    	    tail++;
    	}
    //	cout<<"sum:"<<sum<<endl;
    	ans = max (ans,sum);
    	sum -= q[head].f;
    	head++;
    
        }
        cout<<ans<<endl;
    }
    int main()
    {
      #ifndef  ONLINE_JUDGE 
       freopen("in.txt","r",stdin);
      #endif
        while(scanf("%lld %lld",&n,&d)!=EOF)
        {
    	 for ( int i =  0; i  < n ; i++) cin>>q[i].m>>q[i].f;
    	 sort(q,q+n,cmp);
    //	 for ( int i = 0 ; i < n ; i++) cout<<q[i].m<<" "<<q[i].f<<endl;
    	 solve();
        }
       
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



