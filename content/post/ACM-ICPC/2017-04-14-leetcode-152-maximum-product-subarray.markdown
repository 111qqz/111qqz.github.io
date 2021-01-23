---
author: 111qqz
date: 2017-04-14 11:33:30+00:00
draft: false
title: leetcode 152. Maximum Product Subarray (最大连续子序列乘积，dp)
type: post
url: /2017/04/leetcode-152-maximum-product-subarray/
categories:
- 面试
tags:
- dp
- leetcode
---












Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array `[2,3,-2,4]`,
the contiguous subarray `[2,3]` has the largest product = `6`.

思路：由于有正，有负，还有0.。。所以比最大子串之和要复杂一些。。。

**dp[i].max表示到当前位置的最大乘积。**

**dp[i].min表示到当前位置的最小乘积。**

**dp[i].max = max{dp[i-1].max*a[i],dp[i-1].min*a[i],a[i]};**

**dp[i].min同理**

**边界dp[i].max = dp[i].min = a[0]**

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月14日 星期五 18时57分13秒
    File Name :152.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        //dp
        //dp[i]表示当前的最大乘积。
        //用了滚动数组优化空间/
        int maxProduct(vector<int>& nums) {
    	int siz = nums.size();
    	int mnpre,mncur,mxpre,mxcur;
    	int ret;
    	ret = mnpre = mncur = mxpre = mxcur = nums[0];
    	for ( int i = 1 ; i < siz ; i++ )
    	{
    	    mncur = min(nums[i],min(nums[i]*mnpre,nums[i]*mxpre));
    	    mxcur = max(nums[i],max(nums[i]*mnpre,nums[i]*mxpre));
    	    ret = max(ret,mxcur);
    	    mnpre = mncur;
    	    mxpre = mxcur;
    	}
    	return ret;
    	
        }
    
    };
    







