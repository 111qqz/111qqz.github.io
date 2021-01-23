---
author: 111qqz
date: 2017-04-11 10:50:57+00:00
draft: false
title: leetocde 63. Unique Paths II
type: post
url: /2017/04/63-unique-paths-ii/
categories:
- 面试
tags:
- dp
- leetcode 
---

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

    
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    


The total number of unique paths is `2`.



题意：从左上到右下的方案数，有些点不能走。

思路：简单dp...1A

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月11日 星期二 18时37分47秒
    File Name :63.cpp
    ************************************************ */
    class Solution {
    public:
        int n,m;
        void pr(vector<vector<int> > & a)
        {
    	for ( int i = 0 ; i < n ; i++)
    	    for ( int j = 0 ;j < m ; j++) 
    		printf("%d%c",a[i][j],j==m-1?'\n':' ');
        }
        int uniquePathsWithObstacles(vector<vector<int>>& maze) {
    	n = maze.size();
    	m = maze[0].size();
    	vector<vector<int> >dp(n,vector<int>(m,0));
    	bool sad = false;
    	for ( int i = 0 ;  i < n ; i++)
    	{
    	    if (maze[i][0]==1) sad = true;
    	    if (sad) dp[i][0] = 0 ;
    	    else dp[i][0] = 1;
    	}
    	sad = false;
    	for ( int j = 0 ; j < m ; j++)
    	{
    	    if (maze[0][j]==1) sad = true;
    	    if (sad) dp[0][j] = 0 ;
    	    else dp[0][j] = 1;
    	}
    //	pr(dp);
    	for ( int i = 1 ; i < n ;  i++)
    	{
    	    for (  int j = 1 ; j < m ; j++)
    	    {
    		if (maze[i][j]==1) dp[i][j]=0;
    		else dp[i][j] = dp[i-1][j] + dp[i][j-1];
    	    }
    	}
    //	pr(dp);
    	return dp[n-1][m-1];
        }
    };
    



