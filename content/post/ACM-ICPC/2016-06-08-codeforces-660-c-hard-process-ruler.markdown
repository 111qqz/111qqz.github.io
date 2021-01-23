---
author: 111qqz
date: 2016-06-08 16:17:00+00:00
draft: false
title: codeforces 660 C. Hard Process (ruler)
type: post
url: /2016/06/codeforces-660-c-hard-process-ruler/
categories:
- ACM
tags:
- 尺取法
---

[cf660C](http://codeforces.com/contest/660/problem/C)

solution:ruler.1A



    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年06月08日 星期三 23时43分18秒
    File Name :code/cf/problem/660C.cpp
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
    const int N=3E5+7;
    int n,k;
    int sum[N],a[N];
    
    void ruler()
    {
        int head = 1;
        int tail = 1;
        int l,r;
        int  res = -1;
        int cnt = 0 ;
    
        while (tail<=n)
        {
    	while (a[tail]==1) tail++;
    //	cout<<"head:"<<head<<" tail:"<<tail<<endl;
    	if (a[tail]==0&&tail<=n) cnt++;
    
    	while (sum[tail]-sum[head-1]<=k&&tail<=n) tail++;
    //	cout<<"head:"<<head<<"tail:"<<tail<<endl;
    	    if (tail-head>res)
    	    {
    		res = tail-head;
    	//	cout<<"res:"<<res<<endl;
    		l = head;
    		r = tail-1;
    	    }
    
    	while (head<=tail&&sum[tail]-sum[head-1]>k) head++;
    //	cout<<"head::"<<head<<" tail:"<<tail<<endl;
    	if (tail<=n&&tail-head+1>res)
    	{
    	    res = tail-head+1;
    	    l = head;
    	    r = tail;
    	}
    
    
        }
    
        
        for ( int i = l ; i <= r ; i++) a[i] = 1;
        
        cout<<res<<endl;
        for ( int i = 1 ; i <= n ; i++) cout<<a[i]<<" ";
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n>>k;
    
    	sum[0] = 0;
    	for ( int i = 1; i <= n ; i++)
    	{
    	    scanf("%d",&a[i]);
    	    sum[i] = sum[i-1] +(1-a[i]);
    	}
    
    	ruler();
    	
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



