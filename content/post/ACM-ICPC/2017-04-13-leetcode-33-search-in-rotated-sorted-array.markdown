---
author: 111qqz
date: 2017-04-13 06:29:37+00:00
draft: false
title: leetcode 33. Search in Rotated Sorted Array (无重复数的旋转数组找定值)
type: post
url: /2017/04/leetcode-33-search-in-rotated-sorted-array/
categories:
- 面试
tags:
- binary search
- leetcode
---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

思路：找规律。。。二分。。。

    
    0 1 2 3 4 5 6
    1 2 3 4 5 6 0
    2 3 4 5 6 0 1
    3 4 5 6 0 1 2
    4 5 6 0 1 2 3
    5 6 0 1 2 3 4
    6 0 1 2 3 4 5


**观察发现。。。a[mid]<a[r]的时候，后半段有序;**

**a[mid]>a[r]的时候，前半段有序。。**

然后根据有序区间的端点值，确定tar是在该有序区间，还是在另一半区间。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 14时17分03秒
    File Name :33.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int bin(int n,int tar,vector<int>& nums)
        {
    	int l = 0 ;
    	int r = n-1;
    	while (l<=r)
    	{
    	    int mid = (l+r)>>1;
    	    if (nums[mid]==tar) return mid;
    	    if (nums[mid]<nums[r])
    	    {
    		if (nums[mid]<tar && tar<=nums[r]) l = mid + 1;
    		else r = mid -1;
    	    }
    	    else
    	    {
    		if (nums[l]<=tar && tar < nums[mid]) r = mid - 1;
    		else l = mid + 1;
    	    }
    	}
    	return -1;
        }
    
        int search(vector<int>& nums, int target) {
        int n = nums.size();
        int res = bin(n,target,nums);
        return res;
    
    
        }
    
    };
    





