---
author: 111qqz
date: 2017-04-13 07:14:03+00:00
draft: false
title: leetcode 47. Permutations II (生成全排列，有重复元素)
type: post
url: /2017/04/leetcode-47-permutations-ii/
categories:
- 面试
tags:
- 排列组合
- leetcode
---




Given a collection of numbers that might contain duplicates, return all possible unique permutations.__




思路：和[leet code 46](https://111qqz.com/wordpress/2017/04/leetcode-46-permutations-/) 类似，最后用set去个重即可。。






    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 15时00分48秒
    File Name :47.cpp
    ************************************************ */
    class Solution {
    
    public:
        void solve( vector<int>&nums)
        {
    	int n = nums.size();
    	if (n==0) return;
    	int k = -1;
    	for ( int i = n-2 ; i >= 0 ; i--)
    	{
    	    if (nums[i]<nums[i+1])
    	    {
    		k = i;
    		break;
    	    }
    	}
    	if (k==-1)
    	{
    	    reverse(nums.begin(),nums.end());
    	    return;
    	}
    	int l = -1;
    	for ( int i = n-1 ; i >k ; i--)
    	{
    	    if (nums[k]<nums[i])
    	    {
    		l =  i;
    		break;
    	    }
    	}
    	swap(nums[l],nums[k]);
    	reverse(nums.begin()+k+1,nums.end());
        }
        
        void pr (vector<int> &nums)
        {
    	int siz = nums.size();
    	for ( int i = 0 ; i < siz;  i++)
    	    printf("%d%c",nums[i],i==siz-1?'\n':' ');
        }
        vector<vector<int>> permuteUnique(vector<int>& nums) {
    	set<vector<int> >se;
    	vector<vector<int> >res;
    	int n = nums.size();
    	int total = 1 ;
    	for ( int i = 2 ; i <= n ; i++) total*=i;
    	
    	for ( int i = 1 ; i <= total ; i++)
    	{
    	    se.insert(nums);
    //	    pr(nums);
    	    solve(nums);
    	}
    	for ( auto &it :se)
    	{
    	    res.push_back(it);
    	}
    	return res;
        }
    
    };
    

















