---
author: 111qqz
date: 2017-04-11 12:07:54+00:00
draft: false
title: leetcode 54. Spiral Matrix (矩阵蛇形取数)
type: post
url: /2017/04/leetcode-54-spiral-matrix/
categories:
- 面试
tags:
- leetcode
---

Given a matrix of _m_ x _n_ elements (_m_ rows, _n_ columns), return all elements of the matrix in spiral order.

思路：。。。再次让我回想起高一的暑假。。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月11日 星期二 19时42分05秒
    File Name :54.cpp
    ************************************************ */
    class Solution {
    public:
        int n,m; //0右，1下，2左，3上
        int cal( int &x,int &y,int dir,vector<vector<bool> > & vis)
        {
    	if (dir==0)
    	{
    	    if (y<=n-2&&!vis[x][y+1]) y++;
    	    else
    	    {
    		dir++;
    		x++;
    	    }
    	    return dir;
    	}
    	if (dir==1)
    	{
    	    if (x<=m-2&&!vis[x+1][y]) x++;
    	    else
    	    {
    		dir++;
    		y--;
    	    }
    	    return dir;
    	}
    	if (dir==2)
    	{
    	    if (y>=1&&!vis[x][y-1]) y--;
    	    else
    	    {
    		dir++;
    		x--;
    	    }
    	    return dir;
    	}
    	if (dir==3)
    	{
    	    if (x>=1&&!vis[x-1][y]) x--;
    	    else
    	    {
    		dir = 0 ;
    		y++;
    	    }
    	    return dir;
    	}
        }
        vector<int> spiralOrder(vector<vector<int>>& matrix) {
    	vector<int>res;
    	m = matrix.size();
    	if (m==0) return res;
    	n = matrix[0].size();
    	if (n==0) return res;
    	vector<vector<bool> >vis(m,vector<bool>(n,false));
    	int x,y,dir;
    	x = y = dir = 0 ;
    	for ( int i = 0 ; i < n*m ;  i++)
    	{
    	    printf("x:%d y:%d\n",x,y);
    	    res.push_back(matrix[x][y]);
    	    vis[x][y] = true;
    	    dir = cal(x,y,dir,vis);
    	}
    	return res;
        }
    };
    



