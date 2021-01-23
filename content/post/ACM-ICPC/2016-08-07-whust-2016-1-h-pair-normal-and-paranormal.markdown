---
author: 111qqz
date: 2016-08-07 17:29:31+00:00
draft: false
title: 'whust 2016 #1  H - Pair: normal and paranormal'
type: post
url: /2016/08/whust-2016-1-h-pair-normal-and-paranormal/
categories:
tags:
- 括号匹配
- 栈
---

[题目链接](http://codeforces.com/gym/100507/attachments)



其实就是括号匹配的模型。。用栈即可。。被我写挂好几发。。该死该死。。。


 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年08月07日 星期日 17时34分13秒
    File Name :code/whust2016/#1/HH.cpp
    ************************************************ */
    
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <stack>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <deque>
    #include <ctime>
    #include <cctype>
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
    const int N=1E4+7;
    char st[N];
    int s[N];
    int n;
    int plow[N];
    int pup[N];
    int ans[N];
    stack<int>stk;
    
    
    bool ok(int  x, int y)
    {
      //  cout<<"x:"<<x<<" y:"<<y<<endl;
        if (plow[x]>0&&pup[y]>0)
        {
    	ans[pup[y]] = plow[x];
    	 return true;
        }
        if (plow[y]>0&&pup[x]>0)
        {
    	ans[pup[x]] = plow[y];
    	return true;
        }
        return false;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n>>st;
    	n*=2;
    	int cntA = 0 ;
    	int cnta = 0 ;
    	ms(pup,0);
    	ms(plow,0);
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    if (st[i]>='a'&&st[i]<='z')
    	    {
    		cnta++;
    		plow[i] = cnta;
    	    }
    	    else
    	    {
    		cntA++;
    		pup[i] = cntA;
    	    }
    	}
    //	for ( int i = 0 ; i < n ; i++) cout<<"plow[i]:"<<plow[i]<<" pup[i]:"<<pup[i]<<endl;
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    st[i] = toupper(st[i]);
    	}
    //	cout<<"st:"<<st<<endl;
    	ms(ans,-1);
    	while (!stk.empty()) stk.pop();
    	stk.push(0);
    	for ( int i =  1 ; i < n ; i++)
    	{
    	    while (!stk.empty()&&st[stk.top()]==st[i]&&ok(stk.top(),i)&&i<n) 
    	    {
    		stk.pop();
    		i++;	
    	    }
    	    stk.push(i);    
    	}
    	for ( int i = 1 ; i <= n/2 ; i++) 
    	{
    	    if (ans[i]==-1)
    	    {
    		puts("Impossible");
    		return 0;
    	    }
    	}
    	for ( int i = 1 ; i < n/2 ; i++) printf("%d ",ans[i]);
    	printf("%d\n",ans[n/2]);
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }



