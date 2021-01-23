---
author: 111qqz
date: 2015-09-28 17:07:00+00:00
draft: false
title: 'codeforces #322 div 2 B. Luxurious Houses (思路)'
type: post
url: /2015/09/codeforces322div2b-luxurioushouses/
categories:
- ACM
---



















B. Luxurious Houses







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










The capital of Berland has _n_ multifloor buildings. The architect who built up the capital was very creative, so all the houses were built in one row.




Let's enumerate all the houses from left to right, starting with one. A house is considered to be luxurious if the number of floors in it is strictly greater than in all the houses with larger numbers. In other words, a house is luxurious if the number of floors in it is strictly greater than in all the houses, which are located to the right from it. In this task it is assumed that the heights of floors in the houses are the same.




The new architect is interested in _n_ questions, _i_-th of them is about the following: "how many floors should be added to the _i_-th house to make it luxurious?" (for all _i_ from 1 to _n_, inclusive). You need to help him cope with this task.




Note that all these questions are independent from each other -- the answer to the question for house _i_ does not affect other answers (i.e., the floors to the houses are not actually added).










Input




The first line of the input contains a single number _n_ (1 ≤ _n_ ≤ 105) -- the number of houses in the capital of Berland.




The second line contains _n_ space-separated positive integers _h__i_ (1 ≤ _h__i_ ≤ 109), where _h__i_ equals the number of floors in the _i_-th house.










Output




Print _n_ integers _a_1, _a_2, ..., _a__n_, where number _a__i_ is the number of floors that need to be added to the house number _i_ to make it luxurious. If the house is already luxurious and nothing needs to be added to it, then _a__i_ should be equal to zero.




All houses are numbered from left to right, starting from one.










Sample test(s)










input



    
    5<br></br>1 2 3 1 2










output



    
    3 2 0 2 0 










input



    
    4<br></br>3 2 1 4










output



    
    2 3 4 0<br></br><br></br>从后往前扫．．<br></br>更新最大值．




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock58.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart58.gif)

 

    
    /*************************************************************************
    	> File Name: code/cf/#322/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月29日 星期二 00时27分25秒
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
    int a[N];
    int ans[N];
    int n;
    int main()
    {
      #ifndef  ONLINE_JUDGE 
    //   freopen("in.txt","r",stdin);
      #endif
       cin>>n;
       for ( int i = 1 ; i <= n ; i++)
           scanf("%d",&a[i]);
       int mx ;
       ms(ans,0);
       mx = a[n];
       for ( int i = n-1 ; i >= 1 ; i--)
        {
    	if (a[i]>mx)
    	{
    	    mx = a[i];
    	    continue;
    	}
    	else
    	{
    	    ans[i] = mx-a[i]+1;
    	}
        }
       for ( int i = 1 ; i < n ; i++)
           printf("%d ",ans[i]);
       printf("%d",0);
       
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



