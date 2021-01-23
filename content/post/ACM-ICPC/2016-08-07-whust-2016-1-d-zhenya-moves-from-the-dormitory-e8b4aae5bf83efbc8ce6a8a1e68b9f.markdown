---
author: 111qqz
date: 2016-08-07 17:32:21+00:00
draft: false
title: 'whust 2016 #1 D Zhenya moves from the dormitory (贪心，模拟)'
type: post
url: /2016/08/whust-2016-1-d-zhenya-moves-from-the-dormitory-/
categories:
tags:
- greedy
- 模拟
---

[题目链接](http://acm.hust.edu.cn/vjudge/problem/179873/origin)
傻逼模拟。。读完题就ac了。。。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年08月07日 星期日 18时04分18秒
    File Name :code/whust2016/#1/D.cpp
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
    const int N=280;
    int n,m;
    int total,adva,advb;
    struct Friend
    {
        int money;
        int adv;
    }f[N];
    struct Room
    {
        int type;
        int cost;
        int adv;
    }r[N];
    struct Ans
    {
        int val;
        int rid;
        int fid;
        bool operator < (Ans b)const
        {
    	return val>b.val;
        }
    }ans[300*300];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>total>>adva>>advb;
    	cin>>n;
    	for ( int i = 1 ; i <= n ; i++)
    	    scanf("%d %d",&f[i].money,&f[i].adv);
    	scanf("%d",&m);
    	for ( int i = 1 ; i <= m ; i++)
    	    scanf("%d%d%d",&r[i].type,&r[i].cost,&r[i].adv);
    	int cnt = 0 ;
    	for ( int i = 1 ; i <= m ; i++)
    	{
    	    if (r[i].type==1)
    	    {
    		if (r[i].cost<=total)
    		{
    		    cnt++;
    		    ans[cnt].val = r[i].adv+adva;
    		    ans[cnt].rid = i;
    		    ans[cnt].fid = -1;
    		}
    		continue;
    	    }
    	    else
    	    {
    		for ( int j = 0 ; j <= n ; j++)
    		{
    		    if (j==0) //自己住双人间
    		    {
    			if (r[i].cost<=total)
    			{
    			    cnt++;
    			    ans[cnt].val = r[i].adv+advb;
    			    ans[cnt].rid = i ;
    			    ans[cnt].fid = -1;
    			}
    		    }
    		    else
    		    {
    			if (r[i].cost<=total*2&&r[i].cost<=f[j].money*2)
    			{
    			    cnt++;
    			    ans[cnt].val = r[i].adv+f[j].adv;
    			    ans[cnt].rid = i ;
    			    ans[cnt].fid =  j;
    			}
    		    }
    		}
    	    }
    	}
    //	for ( int i = 1 ; i <= cnt ; i++)
    //	{
    //	    printf("val:%d room: %d  friend : %d \n",ans[i].val,ans[i].rid,ans[i].fid);
    //	}
    	if (cnt==0)
    	{
    	    puts("Forget about apartments. Live in the dormitory.");
    	}else
    	{
    	    sort(ans+1,ans+cnt+1);
    	    if (r[ans[1].rid].type==1)
    	    {
    		printf("You should rent the apartment #%d alone.\n",ans[1].rid);
    	    }
    	    else
    	    {
    		if (ans[1].fid==-1)
    		{
    		    	printf("You should rent the apartment #%d alone.\n",ans[1].rid);
    		}
    		else
    		{
    		    
    		    printf("You should rent the apartment #%d with the friend #%d.\n",ans[1].rid,ans[1].fid);
    		    
    		}
    	    }
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }




