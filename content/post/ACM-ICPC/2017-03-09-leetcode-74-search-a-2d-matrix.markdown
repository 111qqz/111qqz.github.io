---
author: 111qqz
date: 2017-03-09 11:14:05+00:00
draft: false
title: leetcode 74. Search a 2D Matrix
type: post
url: /2017/03/leetcode-74-search-a-2d-matrix/
categories:
- 面试
tags:
- binary search
---

[题目链接](https://leetcode.com/problems/search-a-2d-matrix/?tab=Description)

题意：给一个二维数组。。。每一行每一列都分别递增。。问某个value是否出现过。。。

思路：单调。。显然二分。。。唯一的技巧是从右上角开始搜。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年03月09日 星期四 19时03分07秒
    File Name :74.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        bool searchMatrix(vector<vector<int>>& matrix, int target) {
    
    	int n = matrix.size();
    	if (n==0) return false;
    	int m = matrix[0].size();
    	if (m==0) return false;
    	int row = 0 ;
    	int col = m-1;
    	while (col>=0&&row<n)
    	{
    	    if (matrix[row][col]==target) return true;
    	    else
    	    if (matrix[row][col]>target) col--;
    	    else  row++; 
    	}
    	return false;
    
        }
    
    };





