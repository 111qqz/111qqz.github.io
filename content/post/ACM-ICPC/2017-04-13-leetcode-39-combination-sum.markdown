---
author: 111qqz
date: 2017-04-13 02:47:49+00:00
draft: false
title: leetcode 39. Combination Sum (dfs，求所有的组合，和为定值，每个数可以重复用)
type: post
url: /2017/04/leetcode-39-combination-sum/
categories:
- 面试
tags:
- dfs
- leetcode
---

Given a **set** of candidate numbers (**_C_**) **(without duplicates)** and a target number (**_T_**), find all unique combinations in **_C_** where the candidate numbers sums to **_T_**.

The **same** repeated number may be chosen from **_C_** unlimited number of times.

**Note:**



 	  * All numbers (including target) will be positive integers.
 	  * The solution set must not contain duplicate combinations.



题意：给n个数，求所有的组合，和为定值，每个数可以重复用)

思路：。。。。一开始用顺着枚举子集的思路。。。发现。。并不好搞。。。？还不如直接dfs...

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 00时06分12秒
    File Name :39.cpp
    ************************************************ */
    class Solution {
    public:
    
        vector<vector<int> >res;
        vector<int>tmp;
        int n;
        //思路：dfs
        void dfs( int start,int cur,vector<int> &nums)
        {
    	if (cur==0)
    	{
    	    res.push_back(tmp);
    	    return ;
    	}
    	else if (cur<0) return;
    	else
    	{
    	    for ( int i = start ; i < n ; i++)
    	    {
    		tmp.push_back(nums[i]);
    		dfs(i,cur-nums[i],nums);
    		tmp.erase(tmp.begin()+tmp.size()-1);
    	    }
    	}
        }
    	
        vector<vector<int>> combinationSum(vector<int>& nums, int target) {
    	n = nums.size();
    	if (n==0) return res;
    	dfs(0,target,nums);
    	return res;
        }
    };
    
    
    



