---
author: 111qqz
date: 2016-04-10 13:07:12+00:00
draft: false
title: 'BZOJ 1646: [Usaco2007 Open]Catch That Cow 抓住那只牛 (BFS)'
type: post
url: /2016/04/bzoj-1646-usaco2007-opencatch-that-cow--bfs/
categories:
- ACM
tags:
- bfs
---




## 1646: [Usaco2007 Open]Catch That Cow 抓住那只牛


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 915  Solved: 441
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1646)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1646)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1646)]


## Description






Farmer John has been informed of the location of a fugitive cow and wants to catch her immediately. He starts at a point N (0 <= N <= 100,000) on a number line and the cow is at a point K (0 <= K <= 100,000) on the same number line. Farmer John has two modes of transportation: walking and teleporting. * Walking: FJ can move from any point X to the points X-1 or X+1 in a single minute * Teleporting: FJ can move from any point X to the point 2*X in a single minute. If the cow, unaware of its pursuit, does not move at all, how long does it take for Farmer John to retrieve it?


    农夫约翰被通知，他的一只奶牛逃逸了！所以他决定，马上幽发，尽快把那只奶牛抓回来．




    他们都站在数轴上．约翰在N(O≤N≤100000)处，奶牛在K(O≤K≤100000)处．约翰有




两种办法移动，步行和瞬移：步行每秒种可以让约翰从z处走到x+l或x-l处；而瞬移则可让他在1秒内从x处消失，在2x处出现．然而那只逃逸的奶牛，悲剧地没有发现自己的处境多么糟糕，正站在那儿一动不动．




    那么，约翰需要多少时间抓住那只牛呢？







## Input






* Line 1: Two space-separated integers: N and K


    仅有两个整数N和K.







## Output






* Line 1: The least amount of time, in minutes, it takes for Farmer John to catch the fugitive cow.


    最短的时间．







## Sample Input




5 17
Farmer John starts at point 5 and the fugitive cow is at point 17.






## Sample Output




4

OUTPUT DETAILS:

The fastest way for Farmer John to reach the fugitive cow is to
move along the following path: 5-10-9-18-17, which takes 4 minutes.










大概是写得第一道bfs了。






 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月10日 星期日 21时00分01秒
    File Name :code/bzoj/1646.cpp
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
    const int N=1E5+7;
    int n,k;
    bool vis[N];
    int d[N];
    void bfs()
    {
        ms(d,-1);
        queue<int>q;
        q.push(n);
        vis[n] = true;
        d[n] = 0 ;
    
        while (!q.empty())
        {
    	int px = q.front () ; q.pop();
    	if (px==k)
    	{
    	    return ;
    	}
    	int nxt[3];
    	nxt[0] = px-1;
    	nxt[1] = px+1;
    	nxt[2] = 2*px;
    	for ( int i = 0 ; i < 3 ; i++)
    	{
    	    if (nxt[i]>=0&&nxt[i]<=100000&&!vis[nxt[i]])
    	    {
    		q.push(nxt[i]);
    		vis[nxt[i]] = true;
    		d[nxt[i]] = d[px] + 1;
    	    }
    	}
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	
    	scanf("%d %d",&n,&k);
    	bfs();
    	printf("%d\n",d[k]);
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



