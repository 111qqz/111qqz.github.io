---
author: 111qqz
date: 2017-04-13 09:45:45+00:00
draft: false
title: leetcode 16. 3Sum Closest (k-sum问题，two pointer)
type: post
url: /2017/04/leetcode-16-3sum-closest/
categories:
- 面试
tags:
- k-sum
- two pointer
- leetcode
---

Given an array _S_ of _n_ integers, find three integers in _S_ such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

思路： 排序，然后two pointer,复杂度 O(n^2)

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 16时24分28秒
    File Name :16.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int n;
        int threeSumClosest(vector<int>& nums, int target) {
    	n = nums.size();
    	sort(nums.begin(),nums.end());
    	int mn = 0x3f3f3f3f;
    	int x,y,z;
    	for ( int i = 0 ; i <=n-3 ; i++)
    	{
    	    int head = i+1;
    	    int tail = n-1;
    	    int tar = target - nums[i];
    	    while (head<tail)
    	    {
    		int cur = target-nums[i]-nums[head]-nums[tail];
    		if (abs(cur)<mn)
    		{
    		    mn = abs(cur);
    		    x = nums[i];
    		    y = nums[head];
    		    z = nums[tail];
    		}
    		if (nums[head]+nums[tail]==tar) return target;
    		if (nums[head]+nums[tail]<tar) head++;
    		else tail--;
    	    }
    	}
    	return x + y + z;
    
    
            
    
        }
    
    };
    
    



