---
author: 111qqz
date: 2017-04-13 05:34:45+00:00
draft: false
title: leetcode 34. Search for a Range (二分，找到一段值为tar的区间)
type: post
url: /2017/04/leetcode-34-search-for-a-range/
categories:
- 面试
tags:
- binary search
- leetcode
---

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of _O_(log _n_).

If the target is not found in the array, return `[-1, -1]`.

For example,
Given `[5, 7, 7, 8, 8, 10]` and target value 8,
return `[3, 4]`.



思路：二分。。。

我好像根本不会二分啊？？？

[二分查找](http://www.voidcn.com/blog/LaoJiu_/article/p-6513405.html)



    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 10时49分02秒
    File Name :34.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int n;
        vector<int>res;
        int bin(int l,int r,vector<int>& nums,int tar) //
        {
    	while (l<=r)
    	{
    	    int mid = (l+r)>>1;
    	    if (nums[mid]>=tar) r = mid - 1;
    	    else l = mid + 1;
    	}
    	return nums[r+1]==tar?r+1:-1;//找到第一个等于tar的下标
        }
        int bin2(int l,int r,vector<int>& nums,int tar)
        {
    	while (l<=r)
    	{
    	    int mid = (l+r)>>1;
    	    if (nums[mid]>tar) r = mid-1;
    	    else l = mid + 1;
    	}
    	return nums[l-1]==tar?l-1:-1; //找到最后一个等于tar的下标
        }
        vector<int> searchRange(vector<int>& nums, int target) {
            n = nums.size();
    	if (n==0) return vector<int>(2,-1);
    	int L = bin(0,n-1,nums,target);
    	int R = bin2(0,n-1,nums,target);
    	if (L>=n) L = -1; //对于只有一个数的情况，需要维护一下。
    	if (R>=n) R = -1;
    	res.push_back(L);
    	res.push_back(R);
    	return res;
        }
    
    };
    
    






