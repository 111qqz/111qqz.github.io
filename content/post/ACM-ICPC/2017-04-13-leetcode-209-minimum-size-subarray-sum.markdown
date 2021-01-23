---
author: 111qqz
date: 2017-04-13 13:50:02+00:00
draft: false
title: leetcode 209. Minimum Size Subarray Sum (尺取法)
type: post
url: /2017/04/leetcode-209-minimum-size-subarray-sum/
categories:
- 面试
tags:
- 尺取法
- leetcode
---

Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.

For example, given the array `[2,3,1,2,4,3]` and `s = 7`,
the subarray `[4,3]` has the minimal length under the problem constraint



思路：尺取即可。。好久没写，竟然调了半天。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 20时48分00秒
    File Name :209.cpp
    ************************************************ */
    class Solution {
    
    public:
    
    	int ruler(vector<int>nums,int tar,int n)
    	{
    	    int head = 0;
    	    int tail = 0;
    	    int sum = 0 ;
    	    int res = 0x3f3f3f3f;
    	    while (tail<n&&head<=tail)
    	    {
    		sum = sum + nums[tail];
    		if (sum>=tar)
    		{
    		    res = min(res,tail-head+1);
    		    while (sum>=tar&&head<tail)
    		    {
    			sum-=nums[head];
    			head++;
    		    }
    		    if (sum>=tar) 
    		    {
    			res = min(res,tail-head+1);
    		    }
    		    else
    		    {
    			head--;
    			sum+=nums[head];
    			res = min(res,tail-head+1);
    		    }
    		}
    
    
    
    		tail++;
    	    }
    	    return res==0x3f3f3f3f?0:res;
    	}
    
    
        int minSubArrayLen(int s, vector<int>& nums) {
    	int n = nums.size();
    	int res = ruler(nums,s,n);
    	return res;
            
    
        }
    
    };
    



