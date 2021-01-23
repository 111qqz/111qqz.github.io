---
author: 111qqz
date: 2017-04-13 07:24:41+00:00
draft: false
title: leetcode 60. Permutation Sequence (求第k个排列)
type: post
url: /2017/04/leetcode-60-permutation-sequence/
categories:
- 面试
tags:
- 排列组合
- leetcode
---

The set `[1,2,3,…,_n_]` contains a total of _n_! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for _n_ = 3):



 	  1. `"123"`
 	  2. `"132"`
 	  3. `"213"`
 	  4. `"231"`
 	  5. `"312"`
 	  6. `"321"`

Given _n_ and _k_, return the _k_th permutation sequence.

**Note:** Given _n_ will be between 1 and 9 inclusive.



思路：还是根据[leetcode 31 解题报告](https://111qqz.com/wordpress/2017/04/leetcode-31-next-permutation-in-place-/) 中的算法搞一下就好了。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 15时17分19秒
    File Name :60.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        void solve(vector<int>&nums)
        {
    	int n = nums.size();
    	if (n==0) return;
    	int k = -1;
    	for ( int i = n-2 ; i>= 0 ; i--)
    	{
    	    if (nums[i]<nums[i+1])
    	    {
    		k =  i;
    		break;
    	    }
    	}
    	if (k==-1)
    	{
    	    reverse(nums.begin(),nums.end());
    	    return;
    	}
    	int l = -1;
    	for ( int i = n-1 ; i > k ; i--)
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
        string getPermutation(int n, int k) {
    	vector<int>nums;
    	
    	for ( int i = 1 ; i <= n ; i++) nums.push_back(i);
    	for ( int i = 2 ; i <= k ; i++) solve(nums);
    	
    	string res = "";
    	int siz = nums.size();
    	for ( int i = 0 ; i < siz ; i++) res = res + char(nums[i]+'0');
    	return res;
    
        }
    
    };
    



