---
author: 111qqz
date: 2017-04-12 15:21:23+00:00
draft: false
title: leetcode 442. Find All Duplicates in an Array（找出出现两次的元素）
type: post
url: /2017/04/leetcode-442-find-all-duplicates-in-an-array/
categories:
- 面试
tags:
- leetcode
---







Given an array of integers, 1 ≤ a[i] ≤ _n_ (_n_ = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in O(_n_) runtime?





思路：还是一个映射，如果某个位置要映射的时候已经为负了，就说明之前映射过该位置，那么该位置对应的元素就是出现了两个的元素。

和leetcode 448是一对题目。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月12日 星期三 21时49分11秒
    File Name :442.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        vector<int> findDuplicates(vector<int>& nums) {
        vector<int>res;
        int n = nums.size();
        if (n==0) return res;
        for ( int i = 0 ; i < n ; i++)
        {
            int id = abs(nums[i])-1;
    //      printf("%d%c",id,i==n-1?'\n':' ');
            if (nums[id]>0)nums[id] *=-1;
            else res.push_back(id+1);
        }
    //  for ( int i = 0 ; i< n ;i++) printf("%d%c",nums[i],i==n-1?'\n':' ');
        return res;        
    
        }
    
    };
    




