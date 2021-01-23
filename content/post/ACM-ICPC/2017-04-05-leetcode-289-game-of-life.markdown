---
author: 111qqz
date: 2017-04-05 12:03:28+00:00
draft: false
title: leetcode  289. Game of Life (模拟)
type: post
url: /2017/04/leetcode-289-game-of-life/
categories:
- 面试
tags:
- leetcode
---

According to the [Wikipedia's article](https://en.wikipedia.org/wiki/Conways_Game_of_Life): "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a _board_ with _m_ by _n_ cells, each cell has an initial state _live_ (1) or _dead_ (0). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):



 	  1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
 	  2. Any live cell with two or three live neighbors lives on to the next generation.
 	  3. Any live cell with more than three live neighbors dies, as if by over-population..
 	  4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

**Follow up**:



 	  1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
 	  2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?



题意：生命游戏。。。看到follow up本以为是提高篇。。不是题目要求。。。可是第一个又说 board要同时更新。。。这是要求吧。。。于是我就按照棋盘是二维环来写的。。。最后发现。。。棋盘是有限的。。。

也就是两个follow up...要看1（同时变换）,不要看2（实际上棋盘是有限的。。）。。。这不是有毒吗。。。

<del>所以做leetcode最大的挑战是如何保持心平气和，不要被傻逼题目以及傻逼题目描述影响心情（</del>

我直接写了棋盘是二维环的版本。。。注意的就是，八个方向遍历后记得去重，以及不能和起点相同。

同时更新再加两个标记就好了。。。

1代表活的，0代表死了

-1代表刚才活的，现在死了

-2代表刚才死的，现在活了。

最后记得再变回来。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 18时52分29秒
    File Name :289.cpp
    ************************************************ */
    class Solution {
    
    public:
        const int dx[8]={1,1,1,0,0,-1,-1,-1};
        const int dy[8]={-1,0,1,-1,1,-1,0,1};
        const int N=1E3+3;
        int n,m;
        int checkX( int x)
        {
    	if (x>=0&&x<=n-1) return x;
    	if (x==n) return 0;
    	if (x==-1) return n-1;
        }
        int checkY( int y) 
        {
    	if (y>=0&&y<=m-1) return y;
    	if (y==m) return 0;
    	if (y==-1) return m-1;
        }
        bool check ( int x,int y) //follow up 里的不是题意啊。。。有毒。。。
        {
    	if (x>=0&&x<=n-1&&y>=0&&y<=m-1) return true;
    	return false;
        }
    
        int live( int x,int y,vector<vector<int> >& maze)
        {
    	int cnt = 0 ;
    	set < pair < int ,int > > se;
    
    	for ( int i = 0 ; i < 8 ;  i++) //八个方向经过check以后可能有相同的orz...
    	{				//还可能遇到自己orz...
    	    int nx = x + dx[i];
    	    int ny = y + dy[i];
    	   // nx = checkX(nx);
    	   // ny = checkY(ny);
    	    if (!check(nx,ny)) continue;
    	    if (nx==x&&ny==y) continue;
    //	    cout<<"nx:"<<nx<<" ny:"<<ny<<" maze:"<<maze[nx][ny]<<endl;
    	    if (maze[nx][ny]==1||maze[nx][ny]==-1) se.insert(make_pair(nx,ny));
    	}
    	cnt = se.size();
    	//cout<<"x:"<<x<<" y:"<<y<<" cnt:"<<cnt<<endl;
    	if (cnt<2||cnt>3) return -1;
    	else
    	return 1;
    
        }						    //1 -> live ,0->dead
        int dead( int x,int y,vector<vector<int> >& maze) //-1>刚才活的，现在死了， -2->刚才死的，现在活了
        {
    	int cnt = 0 ;
    	set< pair <int,int > >se;
    	for ( int i = 0 ; i < 8  ; i++)
    	{
    	    int nx = x + dx[i];
    	    int ny = y + dy[i];
    	    //nx = checkX(nx);
    	    //ny = checkY(ny);
    	    if (!check(nx,ny)) continue;
    	    if (nx==x&&ny==y) continue;
    //	    printf("nx:%d ny:%d\n",nx,ny);
    	    if (maze[nx][ny]==1||maze[nx][ny]==-1) se.insert(make_pair(nx,ny));
    	}
    	cnt = se.size();
    	if (cnt==3) return -2; //死的变活了
    	return 0;
    
        }
        void gameOfLife(vector<vector<int>>& board) {
    	n = board.size();
    	if (n==0) return;
    	m = board[0].size();
    	if (m==0) return;
    	for ( int i  = 0 ; i < n ; i++)
    	{
    	    for ( int j = 0 ;j < m ; j++)
    	    {
    		int tmp = board[i][j];
    //		cout<<"val:"<<tmp<<endl;
    		if (tmp==1||tmp==-1)
    		{
    		    board[i][j] = live(i,j,board);
    		}
    		else if (tmp==0||tmp==-2)
    		     {
    			 board[i][j] = dead(i,j,board);
    		     }
    	    }
    	 }
    	for ( int i = 0 ;i < n ; i++)
    	    for ( int j = 0 ; j < m ; j++)
    		if (board[i][j]==-2) board[i][j] = 1;
    		else if (board[i][j]==-1) board[i][j] = 0;
    
        }
    
    };
    









