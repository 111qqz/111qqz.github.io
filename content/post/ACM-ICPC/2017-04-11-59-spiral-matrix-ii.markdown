---
author: 111qqz
date: 2017-04-11 11:07:52+00:00
draft: false
title: leetocde 59. Spiral Matrix II (模拟)
type: post
url: /2017/04/59-spiral-matrix-ii/
categories:
- 面试
tags:
- leetcode
---

Given an integer _n_, generate a square matrix filled with elements from 1 to _n_2 in spiral order.

思路：仿佛回到高一的那个暑假。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月11日 星期二 18时52分15秒
    File Name :59.cpp
    ************************************************ */
    class Solution {
    
    public:
    
    
        int ok (int dir, int &x,int &y,int n,vector<vector<int> >&res)  // 0右，1下，2左，3上
        {
    	if (dir==0)
    	{
    	    if (y<=n-2&&res[x][y+1]==0) y++;
    	    else
    	    {
    		dir++;
    		x++;
    	    }
    	    return dir;
    	}
    	if (dir==1)
    	{
    	    if (x<=n-2&&res[x+1][y]==0) x++;
    	    else
    	    {
    		dir++;
    		y--;
    	    }
    	    return dir;
    	}
    	if (dir==2)
    	{
    	    if (y>=1&&res[x][y-1]==0) y--;
    	    else
    	    {
    		dir++;
    		x--;
    	    }
    	    return dir;
    	}
    	if (dir==3)
    	{
    	    if (x>=1&&res[x-1][y]==0) x--;
    	    else
    	    {
    		dir = 0 ;
    		y++;
    	    }
    	    return dir;
    	}
        }
    
    		
    	    
    
        vector<vector<int>> generateMatrix(int n) {
    
    	vector<vector<int> >res(n,vector<int>(n,0));
    	int dir = 0;
    	int x,y;
    	x = y = 0 ;
    	for ( int i = 0 ; i < n*n ; i++)
    	{
    	    res[x][y] = i+1;
    //	    printf(" x:%d y: %d\n",x,y);
    	    dir = ok (dir,x,y,n,res);
    	}
    	return res;
    
    
        }
    
    };
    



