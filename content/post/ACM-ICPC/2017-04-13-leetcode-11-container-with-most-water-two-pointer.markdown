---
author: 111qqz
date: 2017-04-13 10:13:01+00:00
draft: false
title: leetcode 11. Container With Most Water (two pointer)
type: post
url: /2017/04/leetcode-11-container-with-most-water-two-pointer/
categories:
- 面试
tags:
- two pointer
- leetcode
---

Given _n_ non-negative integers _a1_, _a2_, ..., _an_, where each represents a point at coordinate (_i_, _ai_). _n_ vertical lines are drawn such that the two endpoints of line _i_ is at (_i_, _ai_) and (_i_, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and _n_ is at least 2.

题意：n条竖直的线段 (i,0)->(i,a[i]),从中选2条，和x轴共同组成一个开口的容器，问容器的最大面积。

思路：一开始想错了，以为是最大连续矩形面积...还在想leetcode竟然考单调栈？？？

然而实际上只取两个线段，中间的线段有没有，长度，都是无所谓的。

因此two pointer就好了。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 18时06分42秒
    File Name :11.cpp
     ************************************************ */
    class Solution {
    
        public:
    
    	int maxArea(vector<int>& height) {
    	    int res = 0 ;
    	    int n = height.size();
    	    int head = 0 ;
    	    int tail = n-1;
    	    while (head<tail)
    	    {
    		int h = min(height[head],height[tail]);
    		res = max(res,(tail-head)*h);
    		while (head<tail&&height[head]<=h) head++;
    		while (head<tail&&height[tail]<=h) tail--;
    	    }
    	    return res;
    
    
    	}
    
    };
    



