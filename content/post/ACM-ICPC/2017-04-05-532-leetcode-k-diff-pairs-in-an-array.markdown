---
author: 111qqz
date: 2017-04-05 06:53:02+00:00
draft: false
title: leetcode 532. K-diff Pairs in an Array （找差为k的数对）
type: post
url: /2017/04/leetcode-532-k-diff-pairs-in-an-array/
categories:
- 面试
tags:
- leetcode
---

Given an array of integers and an integer **k**, you need to find the number of **unique** k-diff pairs in the array. Here a **k-diff** pair is defined as an integer pair (i, j), where **i** and **j** are both numbers in the array and their [absolute difference](https://en.wikipedia.org/wiki/Absolute_difference) is **k**.

**Example 1:**


    
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
    



**Example 2:**


    
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    



**Example 3:**


    
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).
    



**Note:**




      1. The pairs (i, j) and (j, i) count as the same pair.
      2. The length of the array won't exceed 10,000.
      3. All the integers in the given input belong to the range: [-1e7, 1e7].




思路：由于重复的只算一次，所以存两个set,分别为nums[i]和nums[i]+k.复杂度O(nlgn)

对于k=0的情况特殊处理，因为可能自己和自己组成一对...所以k=0可以排序然后找出现次数大于一次的元素,也是O(nlgn)

总体复杂度O(nlgn)

另外需要注意的是，两个数的绝对值可能是负数.....k<0返回0。。。

脑回路真是不一样。。。都绝对值了。。还负数。。。？出题人觉得没考虑到负数是考虑不周到？

然而我只觉得出题人傻逼。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 14时25分00秒
    File Name :532.cpp
     ************************************************ */
    class Solution {
        public:
        int findPairs(vector<int>& nums, int k) {
            int siz = nums.size();
            int res = 0 ;
            if (k<0) return 0;
            if (k==0)
            {
            sort(nums.begin(),nums.end());
            nums.push_back(1E8);
            for ( int i = 1 ; i < siz ; i++)
            {
                if (nums[i]==nums[i-1]&&nums[i]!=nums[i+1]) res++;
            }
            return res;
            }
            set<int>a;
            set<int>b;
            for ( int i = 0 ; i < siz;  i++)
            {
            a.insert(nums[i]+k);
            b.insert(nums[i]);
            }
            for ( auto &it:a)
            {
            if (b.count(it)) res++;
            }
            return res;
        }
    };
    






