---
author: 111qqz
date: 2017-04-13 12:02:02+00:00
draft: false
title: leetcode 75. Sort Colors
type: post
url: /2017/04/leetcode-75-sort-colors/
categories:
- 面试
tags:
- two pointer
- leetcode
---

Given an array with _n_ objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

题意：一个数组，由0,1,2组成，现在要求升序排列

思路：无脑做法就是计数排序，扫两遍，时间复杂度O(n)，空间复杂度O(1)

如果只扫一遍呢？

一个容易想到的思路是两个指针：

需要注意 的是，交换2后要再次遍历到当前位置，或者说，只有当不交换2的时候，才执行cur++

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 18时24分25秒
    File Name :75.cpp
    ************************************************ */
    class Solution {
    
    public:
        
        //思路：把0往前仍，把2往后仍
        void pr(vector<int>& nums)
        {
    	int siz = nums.size();
    	for ( int i = 0 ; i < siz;  i++) printf("%d%c",nums[i],i==siz-1?'\n':' ');
        }
        void sortColors(vector<int>& nums) {
    	int n = nums.size();
    	int l=0,r=n-1;
    	int cur = 0;
    	while (cur<r+1)
    	{
    	    if (nums[cur]==0)
    	    {
    		swap(nums[cur],nums[l]);
    		l++;
    		cur++;
    		continue;
    	    }
    	    if (nums[cur]==2)
    	    {
    		swap(nums[cur],nums[r]);
    		r--;
    		continue;
    	    }
    	    cur++; //只有不交换的时候才cur++
    	    pr(nums);
    	}
    
        }
    
    };
    








还有一个神奇的思路：r,w,b分别表示下一个对应颜色要放的位置。

如果当前是0,那么0,1,2都要后移一个。

如果当前是1,那么1,2的位置需要后移。

如果当前是2,那么2的位置需要后移。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 18时24分25秒
    File Name :75.cpp
    ************************************************ */
    class Solution {
    
    public:
        
        //思路：把0往前仍，把2往后仍
        void pr(vector<int>& nums)
        {
    	int siz = nums.size();
    	for ( int i = 0 ; i < siz;  i++) printf("%d%c",nums[i],i==siz-1?'\n':' ');
        }
        void sortColors(vector<int>& nums) {
    	int n = nums.size();
    	int r,w,b;
    	r=w=b=0; //r,w,b,分别表示，当前如果要放一个相应颜色，应该放在第几个。
    	for ( auto x :nums)
    	{
    	    if (x==0)nums[b++]=2,nums[w++]=1,nums[r++]=0;
    	    else if (x==1) nums[b++]=2,nums[w++]=1;
    	    else nums[b++]=2;  //因为b,r,w前进的速度是不一样的，取决于当前的值
    	   // printf("r:%d  w:%d b:%d ",r,w,b);pr(nums);
    	}
    
        }
    
    };
    



