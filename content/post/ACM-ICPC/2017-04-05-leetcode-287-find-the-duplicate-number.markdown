---
author: 111qqz
date: 2017-04-05 07:31:49+00:00
draft: false
title: leetcode 287. Find the Duplicate Number (floyd判圈算法找重复元素)
type: post
url: /2017/04/leetcode-287-find-the-duplicate-number-floyd/
categories:
- 面试
tags:
- floyd 判圈
- leetcode
---

Given an array _nums_ containing _n_ + 1 integers where each integer is between 1 and _n_ (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

**Note:**




      1. You **must not** modify the array (assume the array is read only).
      2. You must use only constant, _O_(1) extra space.
      3. Your runtime complexity should be less than `O(n2)`.
      4. There is only one duplicate number in the array, but it could be repeated more than once.


思路：O(n^2)的复杂度暴力即可，说个O(n)复杂度的解法。

需要注意元素范围1..n是个很重要的条件。

使得我们可以把位置和元素映射起来。

可以看成一个迭代函数

由于存在重复重复元素，因此一定存在一个环。

因此可以用floyd判圈算法。

[floyd判圈算法_维基百科](https://zh.wikipedia.org/wiki/Floyd)

这算法以前遇到过[sgu455 解题报告](https://111qqz.com/wordpress/2015/07/sgu455/)，所以不算很陌生...

但是从有重复元素没有联想到会有环orz，我好菜啊...


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 15时16分11秒
    File Name :287.cpp
    ************************************************ */
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 14时58分11秒
    File Name :287.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int findDuplicate(vector<int>& nums) {
        int slow = nums[0];
        int fast = nums[nums[0]];
        while (slow!=fast)
        {
            slow = nums[slow];
            fast = nums[nums[fast]];
    
            printf("slow:%d fast:%d\n",slow,fast);
        }
        fast = 0 ;
        while (fast != slow)
        {
            fast = nums[fast];
            slow = nums[slow];
        }
        return slow;
    
        }
    
    };
    
    




