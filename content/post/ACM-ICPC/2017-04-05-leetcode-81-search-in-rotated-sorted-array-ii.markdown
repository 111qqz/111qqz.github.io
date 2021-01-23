---
author: 111qqz
date: 2017-04-05 13:17:51+00:00
draft: false
title: leetcode  81. Search in Rotated Sorted Array II (有重复元素的旋转数组找给定值)
type: post
url: /2017/04/leetcode-81-search-in-rotated-sorted-array-ii/
categories:
- 面试
tags:
- binary search
- leetcode
---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

好像阿里一面的时候问过。。。

思路：肯定是二分。。。不过由于有重复元素。。。所以很恶心。。。

总的思路是。。。当发现重复元素。。并且该重复元素不是target的时候。。。缩小范围。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 20时26分25秒
    File Name :81.cpp
    ************************************************ */
    
    
    
    class Solution {
    
    public:
    
        bool search(vector<int>& nums, int target) {
    	int siz = nums.size();
    	if (siz==0) return false;
    	int l = 0 ;
    	int r = siz-1;
    	while (l<=r)
    	{
    	    int mid = (l+r)>>1;
    	    if (nums[mid]==target)  return true;
    	    if (nums[l]<nums[mid])
    	    {
    		if (nums[l]<=target&&target<nums[mid])
    		    r = mid - 1;
    		else 
    		    l = mid + 1;
    	    }
    	    else if (nums[mid]<nums[r])
    	    {
    		if (nums[mid]<target&&target<=nums[r]) l = mid + 1;
    		else r = mid -1;
    	    }
    	    else if (nums[l]==nums[mid]) l++;
    	    else if (nums[mid]==nums[r]) r--;   //nums[l]或nunms[r] is not the target,so remove it..重复元素最烦人了。。。
    	}
    
    	return false;
    
        }
    
    };
    



