---
author: 111qqz
date: 2017-04-07 06:59:26+00:00
draft: false
title: leetcode 79. Word Search (dfs)
type: post
url: /2017/04/leetcode-79-word-search-dfs/
categories:
- 面试
tags: 
- leetcode
- dfs
---

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

思路：dfs即可。记得要回溯一下...

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月07日 星期五 14时32分54秒
    File Name :79.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int n,m;
        const int dx4[4]={1,-1,0,0};
        const int dy4[4]={0,0,-1,1};
        bool vis[1005][1005];
        int len;
        
        bool yes( int x,int y)
        {
    	if (x>=0&&x<=n-1&&y>=0&&y<=m-1) return true;
    	return false;
        }
    
        bool dfs( int x,int y,int cur,vector<vector<char> > & maze,string & st)
        {
    //	printf("x:%d y:%d cur : %d\n",x,y,cur);
    	if (cur>=len) return true;
    	for ( int i = 0 ; i < 4 ; i++)
    	{
    	    int nx = x + dx4[i];
    	    int ny = y + dy4[i];
    	    if (!yes(nx,ny)) continue;
    	    if (vis[nx][ny]) continue;
    	    if (maze[nx][ny]!=st[cur]) continue;
    	    vis[nx][ny] = true;
    	    bool res = dfs(nx,ny,cur+1,maze,st);
    	    if (res) return true;
    	    vis[nx][ny] = false ;//好像还要回溯一下啊？
    	}
    	return false;
        }
    
        bool exist(vector<vector<char>>& board, string word) {
    	n = board.size();
    	if (n==0) return false;
    	m = board[0].size();
    	if (m==0) return false;
    	len = word.length();
    	cout<<"len:"<<len<<endl;
    	char beg = word[0];
    	for ( int i = 0 ; i < n ; i++)
    	    for ( int j = 0 ; j < m ; j++)
    		if (board[i][j]==beg)
    		{
    		    memset(vis,false,sizeof(vis));
    		    //起点忘记打标记了。。。智力-2.。。
    		    vis[i][j] = true;
    		    bool ok = dfs(i,j,1,board,word);
    		    cout<<"ok:"<<ok<<endl;
    		    if (ok) return true;
    		}
    	return false;
            
    
        }
    
    };
    



