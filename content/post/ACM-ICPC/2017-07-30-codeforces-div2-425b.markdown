---
author: 111qqz
date: 2017-07-30 06:46:23+00:00
draft: false
title: 'codeforces #425 B. Petya and Exam (暴力)'
type: post
url: /2017/07/codeforces-div2-425b/
categories:
- ACM
tags:
- brute force
---

[题目链接](http://codeforces.com/contest/832/problem/B)


## 题意：


给出由小写字母，'?'和'*'组成的字符串s，仅由小写字母组成的字符串t,问按照规则s能否变成t.

规则如下：首先给出定义的[好字母]的字符串，[好字母]之外的都是[坏字母],对于s中每个‘?’，规定其必须替换为一个[好字母]

对于s中的每个‘*’，规定其必须替换为0个或者多个坏字母。


## 思路：


显然带*的会比较难搞。所以只说带*的情况

我WA了好多次，原因是一开始读错题（或者题意不太清楚？），认为*只能最多替换一个[坏字母]

后来在这个思路上改，越改越复杂orz

仔细想一下，关键点有两个，一个是当前位置有三种情况{没有经过*,经过*且仍在*的作用域内，经过*且已经出了*的作用域}

如何知道*的作用域呢？由于*的替换是连续的，因此只要对比s和t的长度差就可以了。

对于不同的作用域，普通字母的判断位置是不同的，在经过*的作用域之后，普通字母（**包括‘？’**）记得加一个offset

所以第二个关键点就是，对于*的替换，一次判断完多个。

除此之外，注意下*可能为空的特殊情况，特判一下比较保险。

    
    /* ***********************************************
    Author :111qqz
    Created Time :Mon 24 Jul 2017 10:32:44 PM CST
    File Name :B.cpp
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
    #define PB push_back
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
    string good;
    int len,len2;
    vector<char>go;
    string st;
    int n;
    string tmp;
    vector<int>zimu; //字母的位置
    vector<int>fuhao; //符号的位置
    bool star;
    bool vis[26];
    bool solve()
    {
        len2 = tmp.length();
        if (!star)
        {
    	if (len2!=len) return false;
    	for ( int i = 0 ; i < len2 ; i++)
    	{
    	    if (st[i]=='?')
    	    {
    		if (!vis[tmp[i]-'a']) return false;
    	    }else 
    	    {
    		if (st[i]!=tmp[i]) return false;
    	    }
    	}
    	return true;
        }
        if (star)
        {
    
    	int stat =  0; //0表示没有经过*,1表示在*的作用域内，-1表示经过了*的作用域
    	if (len2>=len)
    	{
    	    int num = len2-len+1; //*匹配的字母个数
    	    int offset = num;
        	   // cout<<"num:"<<num<<endl;
    	    for ( int i = 0 ; i < len ; i++)
    	    {
    		if (st[i]=='*')
    		{
    		    stat = 1;
    		}
    		if (1==stat) //遇*一次判断完
    		{
    		    for ( int j = i ; j < i+num ; j++)
    			if (vis[tmp[j]-'a']) return false;
    		    stat = -1;
    		}
    
    		if(st[i]=='?')
    		{
    		    if (0 == stat)
    		    {
    			if (!vis[tmp[i]-'a']) return false;
    		    }
    		    if (-1 == stat)
    		    {
    			if (!vis[tmp[i+offset-1]-'a']) return false;
    		    }
    		}
    		if (st[i]!='?'&&st[i]!='*')
    		{
    		    if (0==stat)
    		    {
    			if (st[i]!=tmp[i]) return false;
    		    }
    		    if (-1==stat)
    		    {
    			if (st[i]!=tmp[i+offset-1]) return false;  //记得*造成的偏移，却只考虑了*表示一个字母时的偏移...orz
    		    }
    		}
    	    }
    	    //区分*经过前和后的两种状态
    	    return true;
    	}
    	else  if (len2==len-1) //*替换为空
    	{
    	    bool flag = false;
    	    for ( int i = 0 ; i < len2 ; i++)
    	    {
    		int cur = i;
    		if (st[cur]=='*') flag = true;
    		if (flag) cur = i+1;
    		if (st[cur]=='?')
    		{
    		    if (!vis[tmp[i]-'a']) return false;
    		}else
    		{
    		    if (st[cur]!=tmp[i]) return false;
    		}
    	    }
    	}else return false;
    
        }
        return true;
    }
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
    #endif
    
        ms(vis,false);
        cin>>good;
        len = good.length();
        for ( int i = 0 ; i < len ; i++) vis[good[i]-'a'] = true;
    
        cin>>st;
        len = st.length();
        star = false;
        for ( int i = 0 ; i < len ; i++) if (st[i]=='*') star = true;
        cin>>n;
        for ( int i = 1 ; i <= n ; i++)
        {
    	cin>>tmp;
    	bool ok = solve();
    	if (ok) puts("YES");
    	else puts("NO");
        }
    
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
    









