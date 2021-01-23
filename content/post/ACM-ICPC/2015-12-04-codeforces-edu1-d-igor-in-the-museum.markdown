---
author: 111qqz
date: 2015-12-04 08:29:50+00:00
draft: false
title: codeforces edu1 D. Igor In the Museum
type: post
url: /2015/12/codeforces-edu1-d-igor-in-the-museum/
categories:
- ACM
tags:
- dfs
- 记忆化搜索
---

http://codeforces.com/contest/598/problem/D

题意：给第一个地图。 ‘.’是能走的，‘*’是不能走的。**每个‘.’和'*'之间有一幅画，**给出k个起点，问对于每组起点，最多能观察到多少副画。

思路：dfs.要注意即使只有一个‘*’，从不同方向访问仍然算不同的画。这样就不用标记画是否访问过了。一开始直接暴力dfs..TLE 10

然后发现，如果是在同一个联通快内，能看到的画的最大值是确定的。。如果之前有同一个联通快内的其他点dfs过得到过答案，那么下次就不用再dfs了。。。记得把之前的记过保存下来。。

我具体的写法是把某一次dfs进过的点的恒纵坐标都存起来。。。然后dfs结束后把更新这些沿途中经过的点的答案。。结果还是TLE 10

果然是记忆化写残了。。也不是写残了。。看了几个别人的代码。。。记忆化存的时候是按照某一次来存答案。。而我是按照某个点的坐标。。来存答案。果然还是要提高姿势水平啊。。。SAD





    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月04日 星期五 15时08分22秒
    File Name :code/cf/edu1/D.cpp
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
    
    
    
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    const int N=1E3+3;
    int n,m,k;
    char maze[N][N];
    bool pic[N][N];
    int v[N][N];
    int ans[N*N];
    int res;
    int cnt = 0 ;
    
    bool ok ( int x,int y)
    {
        if (x>=0&&x<n&&y>=0&&y<m&&v[x][y]==-1)
    	return true;
        return false;
    }
    int dfs ( int x,int y,int kk)
    {
        if (!ok(x,y)) return 0;
    
        if (maze[x][y]=='*') return 1;
        v[x][y] = kk;
    
        return  dfs(x+1,y,kk)+dfs(x-1,y,kk)+dfs(x,y-1,kk)+dfs(x,y+1,kk);
    
    
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
    	 #endif
    
        scanf("%d%d%d",&n,&m,&k);
        for ( int i = 0  ; i < n ; i++) scanf("%s",maze[i]);
        
        ms(ans,-1);
        ms(v,-1);
        while (k--)
        {
    	int x,y;
    	scanf("%d %d",&x,&y);
    
    	x--;
    	y--;
    	if (v[x][y]==-1)
    	    ans[k] = dfs(x,y,k);
    	else ans[k] = ans[v[x][y]];
    
    	printf("%d\n",ans[k]);
    	
        
    	
        }
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



