---
author: 111qqz
date: 2017-04-05 13:36:44+00:00
draft: false
title: leetcode 80 Remove Duplicates from Sorted Array II  （有序数组去除重复元素）
type: post
url: /2017/04/leetcode-80-remove-duplicates-from-sorted-array-ii/
categories:
- 面试
tags:
- leetcode
---

Follow up for "Remove Duplicates":
What if duplicates are allowed at most _twice_?

For example,
Given sorted array _nums_ = `[1,1,1,2,2,3]`,

Your function should return length = `5`, with the first five elements of _nums_ being `1`, `1`, `2`, `2` and `3`. It doesn't matter what you leave beyond the new length.





[Subscribe](https://leetcode.com/subscribe/) to see which companies asked this question.

题意：一个有序数组，每个元素最多出现两次，如果大于两次，把多的去掉，返回去掉后的数组长度len，以及要求数组前len是去掉那些元素之后的元素。//语死早。。看原题好了。。

思路：排序了还不是随便搞？ 没要求空间再开一个标记空间。。。O(1)空间的话。。就乱搞一下？

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 21时25分48秒
    File Name :80.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int removeDuplicates(vector<int>& nums) {
        int siz = nums.size();
        if (siz==0) return 0;
        int p = 0;
        int magic = -324784312;
        for ( int i = 0 ; i < siz-1 ; i++)
        {
            if (nums[i]==nums[i+1]) p++;
            else p = 0;
            if (p>=2) nums[i-1] = magic;
        }
        int cur = 0;
        for ( int i = 0 ; i < siz ; i++)
        {
            if (nums[i]!=magic) nums[cur++] = nums[i];
        }
        return cur;
    
        }
    
    };
    







