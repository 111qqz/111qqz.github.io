---
author: 111qqz
date: 2017-04-11 11:39:15+00:00
draft: false
title: leetcode  55. Jump Game (dp)
type: post
url: /2017/04/leetcode-55-jump-game-dp/
categories:
- 面试
tags:
- leetcode
---

Given a collection of intervals, merge all overlapping intervals.

For example,
Given `[1,3],[2,6],[8,10],[15,18]`,
return `[1,6],[8,10],[15,18]`.



思路:dp[i]表示能否到达位置i...无脑dp即可。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月11日 星期二 19时33分51秒
    File Name :55.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        bool canJump(vector<int>& nums) {
    	int n = nums.size();
    	if (n==0) return false;
    	vector<int>dp(n,false);
    	dp[0] = true;
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    if (dp[i])
    	    {
    		int r = min(i+nums[i],n-1);
    		for ( int j = i+1 ; j <=r ; j++)
    		    dp[j] = true;
    	    }
    	}
    	return dp[n-1];
            
    
        }
    
    };
    



