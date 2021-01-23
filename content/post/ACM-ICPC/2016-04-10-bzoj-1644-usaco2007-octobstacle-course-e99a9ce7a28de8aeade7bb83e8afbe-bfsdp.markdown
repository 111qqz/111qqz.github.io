---
author: 111qqz
date: 2016-04-10 12:41:46+00:00
draft: false
title: 'BZOJ 1644: [Usaco2007 Oct]Obstacle Course 障碍训练课 (BFS,DP)'
type: post
url: /2016/04/bzoj-1644-usaco2007-octobstacle-course--bfsdp/
categories:
- ACM
tags:
- bfs
- dp
---




## 1644: [Usaco2007 Oct]Obstacle Course 障碍训练课


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 451  Solved: 226
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1644)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1644)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1644)]


## Description






考虑一个 N x N (1 <= N <= 100)的有1个个方格组成的正方形牧场。有些方格是奶牛们不能踏上的，它们被标记为了'x'。例如下图：

. . B x .
. x x A .
. . . x .
. x . . .
. . x . .

贝茜发现自己恰好在点A处，她想去B处的盐块舔盐。缓慢而且笨拙的动物，比如奶牛，十分讨厌转弯。尽管如此，当然在必要的时候她们还是会转弯的。对于一个给定的牧场，请你计算从A到B最少的转弯次数。开始的时候，贝茜可以使面对任意一个方向。贝茜知道她一定可以到达。






## Input






第 1行: 一个整数 N 行

2..N + 1: 行 i+1 有 N 个字符 ('.', 'x', 'A', 'B')，表示每个点的状态。






## Output






行 1: 一个整数，最少的转弯次数。






## Sample Input




3
.xA
...
Bx.





## Sample Output




2










思路：bfs.我一开始的错误做法是用优先队列，以转弯数为关键字。




但是实际上错的，因为到达同一个点可能之后到达的方法有更少的转弯数，但是在做bfs的时候，之前访问的节点已经被标记了，所以无法更新成更优的值。




正解是类似dp的做法。需要注意不需要vis数组标记。




用dir[x][y][i]表示从i方向到达x,y的需要转弯数。




初始dir[s.x][s.y][0..3]为0,其余为inf






然后更新的时候如果dir[fx][fy][i]=min(dir[x][y][j]+1) 当i!=j

dir[fx][fy][i]=min(dir[x][y][j]) 当i=j








 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月10日 星期日 17时00分22秒
    File Name :code/bzoj/1644.cpp
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
    const int N=105;
    char maze[N][N];
    int n;
    bool vis[N][N];
    int dir[N][N][5];
    struct node
    {
        int x,y;
    
    
        bool ok ()
        {
    	if (x>=0&&x<n&&y>=0&&y<n&&maze[x][y]!='x') return true;
    	return false;
        }
    
        void look()
        {
    	cout<<"x:"<<x<<" y:"<<y<<endl;
        }
    
    }s,e;
    
    void bfs()
    {
        queue<node>q;
        q.push(s);
    
        while (!q.empty())
        {
    	node pre = q.front(); q.pop();
    //	pre.look();
    	for ( int i = 0 ; i < 4 ; i++)
    	{
    	    node nxt;
    	    nxt.x = pre.x + dx4[i];
    	    nxt.y = pre.y + dy4[i];
        	    if (!nxt.ok()) continue; 
    	    for ( int j = 0 ; j < 4 ; j++)
    	    {
    		bool flag = false;
    		if (i==j&&dir[nxt.x][nxt.y][i]>dir[pre.x][pre.y][j])
    		{
    		    dir[nxt.x][nxt.y][i] = dir[pre.x][pre.y][j];
    		    flag = true;
    		}
    		if (i!=j&&dir[nxt.x][nxt.y][i]>dir[pre.x][pre.y][j]+1)
    		{
    		    dir[nxt.x][nxt.y][i] = dir[pre.x][pre.y][j] + 1;
    		    flag = true;
    		}
    		if (flag)
    		{
    		    q.push(nxt);
    		}
    
    	    }
    	}
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	scanf("%d",&n);
    	for ( int i = 0 ; i < n ; i++) scanf("%s",maze[i]);
    
    	for ( int i = 0 ; i < n ; i ++)
    	    for ( int j = 0 ; j < n ; j++)
    		{
    		    if (maze[i][j]=='A')
    		    {
    			s.x = i ;
    			s.y = j;
    		    }
    		    if (maze[i][j]=='B')
    		    {
    			e.x = i ;
    			e.y = j ;
    		    }
    		}
    
    	ms(dir,0x3f);
    	for ( int i = 0 ; i < 4 ; i++) dir[s.x][s.y][i] = 0;
    	bfs();
    //	for ( int i = 0 ; i < 4 ; i++) cout<<dir[e.x][e.y][i]<<endl;
    	int ans = inf;
    	for ( int i = 0 ; i < 4 ; i++) ans = min(ans,dir[e.x][e.y][i]);
    	printf("%d\n",ans);
    
        return 0;
    }
    	
    



