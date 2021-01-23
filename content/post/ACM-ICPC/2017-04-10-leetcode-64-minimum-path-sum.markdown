---
author: 111qqz
date: 2017-04-10 02:35:20+00:00
draft: false
title: leetcode 64. Minimum Path Sum (二维dp)
type: post
url: /2017/04/leetcode-64-minimum-path-sum/
categories:
- 面试
tags:
- dp
- leetcode
---












Given a _m_ x _n_ grid filled with non-negative numbers, find a path from top left to bottom right which _minimizes_ the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

数字三角形。。。。从坐上到右下问最短路径。。每次只能向下或者向右。。。

wa了一次。。。是因为边界值赋值成了0.。。求最短路径显然因为赋值成inf才对orz..果然傻了。。

简单的dp我们简单的A.

顺便吐槽一下。。(100,100)的答案会溢出int...然而答案就是负的。。。就没人check一下吗，，，

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月10日 星期一 10时11分26秒
    File Name :64.cpp
    ************************************************ */
    class Solution {
    public:
        int minPathSum(vector<vector<int>>& grid) {
    	int n = grid.size();
    	int m = grid[0].size();
    	vector<vector<int> > dp(n+1,vector<int>(m+1,0x3f3f3f3f)); //求最小路径，初始化为最大值。
    
    	dp[n-1][m-1] = grid[n-1][m-1];
    	for ( int i = n-1 ;  i >= 0 ; i--)
    	{
    	    for ( int j = m-1 ; j >= 0 ; j--)
    	    {
    		if (i==n-1&&j==m-1) continue;
    		dp[i][j] = min(dp[i+1][j],dp[i][j+1]) + grid[i][j];
    	    }
    	}
    
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    for ( int j = 0 ; j < m ; j++)
    		printf("%d ",dp[i][j]);
    	    printf("\n");
    	}
    	int res = dp[0][0];
    	cout<<"res:"<<res<<endl;
    	return res;
        }
    };
    





