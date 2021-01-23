---
author: 111qqz
date: 2017-04-13 06:59:43+00:00
draft: false
title: leetcode 46. Permutations (生成全排列，无重复元素)
type: post
url: /2017/04/leetcode-46-permutations/
categories:
- 面试
tags:
- 排列组合
- leetcode
---

Given a collection of **distinct** numbers, return all possible permutations.

思路：调用n-1次 [leetcode 31 解题报告](https://111qqz.com/wordpress/2017/04/leetcode-31-next-permutation-in-place-/) 中提到的算法即可。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 14时49分34秒
    File Name :46.cpp
     ************************************************ */
    class Solution {
    
        public:
    
    	void solve(vector<int> &nums)
    	{
    	    int n = nums.size();
    	    if (n==0) return;
    	    int k = -1;
    	    for ( int i = n-2 ; i >= 0 ; i--)
    	    {
    		if (nums[i]<nums[i+1])
    		{
    		    k = i ;
    		    break;
    		}
    	    }
    	    if (k==-1)
    	    {
    		reverse(nums.begin(),nums.end());
    		return;
    	    }
    	    int l = -1;
    	    for ( int i = n-1 ; i > k ; i-- )
    	    {
    		if (nums[k]<nums[i])
    		{
    		    l = i ;
    		    break;
    		}
    	    }
    	    swap(nums[l],nums[k]);
    	    reverse(nums.begin()+k+1,nums.end());
    	}
    	vector<vector<int>> permute(vector<int>& nums) {
    	    vector<vector<int> >res;
    	    int n = nums.size();
    	    int total = 1;
    	    for ( int i = 2 ; i <= n ; i++) total*=i;
    	    for ( int i = 1 ; i <= total; i++)
    	    {
    		res.push_back(nums);
    		solve(nums);
    	    }
    
    	    return res;
    	}
    
    };
    



