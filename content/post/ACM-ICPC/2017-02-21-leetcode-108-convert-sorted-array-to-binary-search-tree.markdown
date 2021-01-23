---
author: 111qqz
date: 2017-02-21 11:14:48+00:00
draft: false
title: leetcode 108. Convert Sorted Array to Binary Search Tree（有序数组转化成bst）
type: post
url: /2017/02/leetcode-108-convert-sorted-array-to-binary-search-tree/
categories:
- 面试
tags:
- binary search tree
---

[leetcode108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/?tab=Description)

题意：把有一个有序的数组转化成一课高度尽量小的bst(二叉搜索树)

思路：我竟然忘记了什么是bst........我好傻啊...不过想想可能是因为...最朴素的二叉搜索树几乎用不到...所以很容易忘记吧2333

bst是 binary search tree的缩写..

具体见  [维基百科_二叉搜索树](https://zh.wikipedia.org/zh-hans/)

想起来概念就好搞了...直接递归建树即可...类似线段树的build的过程




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年02月21日 星期二 13时08分04秒
    File Name :108.cpp
    ************************************************ */
    /**
    
     * Definition for a binary tree node.
    
     * struct TreeNode {
    
     *     int val;
    
     *     TreeNode *left;
    
     *     TreeNode *right;
    
     *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    
     * };
    
     */
    
    class Solution {
    
    public:
    
        TreeNode* dfs( int l,int r,vector<int>&nums)
        {
            
            int  n = r-l+1;
            if (n<=0) return NULL;
            int  m = n/2;
            cout<<"l:"<<l<<" r:"<<r<<endl;
            TreeNode* rt = new TreeNode(nums[l+m]);
            rt->left = dfs(l,l+m-1,nums);
            rt->right = dfs(l+m+1,r,nums);
            return rt;
        }
            
        
        TreeNode* sortedArrayToBST(vector<int>& nums) {
    
            int siz = nums.size();
            if (siz==0) return NULL;
             return dfs(0,siz-1,nums);
        }
    
    };






