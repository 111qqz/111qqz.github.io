---
author: 111qqz
date: 2017-04-05 06:19:06+00:00
draft: false
title: leetcode 448. Find All Numbers Disappeared in an Array(寻找所有消失的元素）
type: post
url: /2017/04/leetcode-448-find-all-numbers-disappeared-in-an-array/
categories:
- 面试
tags:
- leetcode
---

Given an array of integers where 1 ≤ a[i] ≤ _n_ (_n_ = size of array), some elements appear twice and others appear once.

Find all the elements of [1, _n_] inclusive that do not appear in this array.

Could you do it without extra space and in O(_n_) runtime? You may assume the returned list does not count as extra space.

**Example:**

    
    Input:
    [4,3,2,7,8,2,3,1]
    
    Output:
    [5,6]


思路：由于元素大小有限制，是在1..n之间。

这个信息有两个作用。一个是元素都是正数，一个是元素大小（绝对值意义上的）有限。

因此我们可以把元素本身和一个位置关联起来。

由于都是正数，我们可以用变成其相反数的方法进行标记（如果已经为负数，就不做处理）

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 14时07分53秒
    File Name :448.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        vector<int> findDisappearedNumbers(vector<int>& nums) {
    
    	int siz = nums.size(); //由于出现的元素大小在1..之间，因此可以用位置i的正负来表示元素i+1是否出现了。
    	for ( int i = 0 ; i < siz ; i++)
    	{
    	    int id = abs(nums[i]);
    	    if (nums[id-1]>0) nums[id-1]*=-1;
    	}
    	vector<int>res;
    	for ( int i = 0 ; i < siz ; i++)
    	{
    	    if (nums[i]>0) res.push_back(i+1);
    	}
    	return res;
    
        }
    
    };
    





