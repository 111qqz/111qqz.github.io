---
author: 111qqz
date: 2015-09-22 02:39:00+00:00
draft: false
title: 'best coder #56 div 2 A　Clarke and minecraft（贪心）'
type: post
url: /2015/09/bestcoder56div2aclarkeandminecraft/
categories:
- ACM
tags:
- greedy
---

贪心．．尽量把一样的材料放在一起．．．
然后写蠢了．．妈蛋．．．
详情见代码




 

    
    /*************************************************************************
    	> File Name: code/bc/#56/1001.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月19日 星期六 18时55分49秒
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
    const int N=5E2+7;
    int a[N],b[N];
    int ans,cnt;
    int p[N];
    int n;
    int main()
    {
      #ifndef  ONLINE_JUDGE 
        freopen("in.txt","r",stdin);  
      #endif
        int T;
        cin>>T;
        while (T--)
        {
    	ans  = 0;
    	cnt  = 0;
    	ms(p,0);
    	scanf("%d",&n);
    	for ( int i = 0 ; i < n ; i++ )
    	{
    	    scanf("%d %d",&a[i],&b[i]);
    	    p[a[i]]+=b[i];
    	}
    	int kind =  0;
    	for ( int i = 1 ;i <= 500 ; i++)
    	{
    	    if (p[i]!=0)
    	    {
    	    //	cnt = cnt + (p[i]-1)/64 + 1;
    		cnt = cnt + (p[i]+63)/64;　　//这样写不知高到哪里去了．
    		p[i] = 0;
    	    }
    
    	}
    	//ans = ans + (cnt-1)/36+1;
    	ans = (cnt+35)/36; //不知高到哪里去了．．．
    	printf("%d\n",ans);
    
    
        }
      
      
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



