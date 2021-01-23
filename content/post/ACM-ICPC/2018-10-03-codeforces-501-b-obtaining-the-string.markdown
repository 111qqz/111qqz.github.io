---
author: 111qqz
date: 2018-10-03 10:15:31+00:00
draft: false
title: codeforces 501 B. Obtaining the String
type: post
url: /2018/10/codeforces-501-b-obtaining-the-string/
categories:
- ACM
---

题目链接:http://codeforces.com/contest/1015/problem/B

题意: 给出字符串s和字符串t，问一个将s变为t的策略。 可以做的变换为，交换s中相邻的字符串，该操作最多不能超过4000次，字符串长度最大为50.

思路:

首先可以确定，当两个字符串的组成相同时（也就是有同样的字符组成，只是位置可能有所不同)一定有解。

考虑最坏情况，每个字符都要交换到最远的地方，总的操作数<50*50<4000,因此一定有解。

判断组成是否相同可以用multiset

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年10月03日 星期三 16时11分29秒
    File Name :b.cpp
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
    int n;
    string s,t;
    multiset<char>A,B;
    int main()
    {
            #ifndef  ONLINE_JUDGE 
            freopen("./in.txt","r",stdin);
      #endif
      cin>>n;
      cin>>s>>t;
      for ( auto x : s) A.insert(x);
      for (auto x: t) B.insert(x);
      if (A!=B)
      {
        puts("-1");
        return 0;
      }
      vector<int>ans;
      //可以保证处理过的一定相等
      for ( int i = 0 ; i < n ; i++)
      {
        if (s[i]==t[i]) continue;
        string sub_str = s.substr(i,50);
        // cout<<"sub_str:"<<sub_str<<endl;
        int pos = sub_str.find(t[i])+i;
        //  cout<<"pos:"<<pos<<endl;
        for ( int j = pos; j  >= i+1 ; j-- )
        {
          ans.push_back(j);
          swap(s[j-1],s[j]);
          //  cout<<s<<endl;
        }
      }
      cout<<ans.size()<<endl;
      for ( auto x : ans) cout<<x<<" ";
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





