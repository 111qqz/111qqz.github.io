---
author: 111qqz
date: 2017-04-13 06:47:55+00:00
draft: false
title: leetcode 31. Next Permutation (in-place 生成下一个全排列)
type: post
url: /2017/04/leetcode-31-next-permutation-in-place/
categories:
- 面试
tags:
- 排列组合
- leetcode
---

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
`1,2,3` → `1,3,2`
`3,2,1` → `1,2,3`
`1,1,5` → `1,5,1`



思路： 参考了[wiki_Permutation](https://en.wikipedia.org/wiki/Permutation)

有一个算法完美解决了这个问题，空间复杂度O(1),时间复杂度O(n)


<blockquote>The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

> 
> 
 	  1. Find the largest index _k_ such that _a_[_k_] < _a_[_k_ + 1]. If no such index exists, the permutation is the last permutation.
 	  2. Find the largest index _l_ greater than k such that _a_[_k_] < _a_[_l_].
 	  3. Swap the value of _a_[_k_] with that of _a_[_l_].
 	  4. Reverse the sequence from _a_[_k_ + 1] up to and including the final element _a_[_n_].

</blockquote>



    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 14时39分33秒
    File Name :31.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        void nextPermutation(vector<int>& nums) {
    
    	int n = nums.size();
    	if (n==0) return;
    	int k = -1;
    	for (int i = n-2 ;  i>= 0 ; i--) 
    	    if (nums[i]<nums[i+1])
    	    {
    		k = i;
    		break;
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
    		l = i;
    		break;
    	    }
    	}
    	swap(nums[l],nums[k]);
    	reverse(nums.begin()+k+1,nums.end());
    
        }
    
    };
    



