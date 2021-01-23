---
author: 111qqz
date: 2015-08-05 19:00:00+00:00
draft: false
title: 'cf #314  B. Berland National Library (模拟)'
type: post
url: /2015/08/cf314b-berlandnationallibrary/
categories:
- ACM
tags:
- 模拟
---

给出一个图书馆人员进出情况，问图书馆满足题意的最小容量是多少。

注意在初始之前图书馆里面可能就有人了，也就是说不是所有进入图书馆的人都会被给出。

我的做法是先统计出图书馆里面初始的人数，开一个布尔数组，初始全为false,如果一个人标记为 false  而且从 图书馆里出来了，就说明这个人初始是在图书馆里的。

然后就正常模拟，图书馆的人数由初始的和后来的两部分组成。

    
    /*************************************************************************
    	> File Name: code/cf/#314/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月06日 星期四 00时23分26秒
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
    #define y0 abc111qqz
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define tm crazy111qqz
    #define lr dying111qqz
    using namespace std;
    #define REP(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef unsigned long long ULL;
    const int inf = 0x7fffffff;
    const int N=1E2+5;moni
    int n;
    int r[N];
    bool vis[1000060];
    char ch[N];
    int main()
    {
        cin>>n;
        char cmd;
        int mx = -1;
        int cur = 0;
        int beforein = 0;
        memset(vis,false,sizeof(vis));
        for ( int i = 0 ; i < n ; i++)
        {
    	
    	cin>>ch[i]>>r[i];
    	if (ch[i]=='+')
    	{
    	    vis[r[i]] = true;
    	}
    	if (ch[i]=='-')
    	{
    	    if (!vis[r[i]])
    	    {
    		beforein++;
    	    }
    	    vis[r[i]] = false;
    	}
        }
        mx = beforein;
        memset(vis,false,sizeof(vis));
       // cout<<"beforein:"<<beforein<<endl;
        for ( int i = 0 ; i <n ; i++ )
        {
    	if (ch[i]=='+')
    	{
    	    cur++;
    	    vis [r[i]] =true;
    	}
    	else
    	{
    	    if (vis[r[i]])
    	    {
    //	    if (vis[1]) cout<<"fuffffffffff"<<endl;
    		cur--;
    //		cout<<"r[i]:"<<r[i]<<endl;
    		vis[r[i]] = false;
    	    }
    	    else
    	    {
    		beforein--;
    	    }
    	}
    //	cout<<"cur:"<<cur<<" beforein:"<<beforein<<endl;   
    	if (cur+beforein>mx)
    	{
    	    mx = cur + beforein;
    	}
    
        }
        cout<<mx<<endl;
    	return 0;
    }
    
