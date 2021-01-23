---
author: 111qqz
date: 2017-02-24 03:45:38+00:00
draft: false
title: leetcode 437. Path Sum III
type: post
url: /2017/02/leetcode-437-path-sum-iii/
categories:
- 面试
tags:
- brute force
---

[题目链接](https://leetcode.com/problems/path-sum-iii/?tab=Description)

题意：求一棵二叉树中，所有一段连续路径之和等于给定值的路径数目。

思路：想了半天就只能想到暴力。。。复杂度大概O(n^2)。。。也不是不可以接受。。。但是感觉这也太暴力了。。就去看了题解。。。发现题解就还真是暴力orz。。。

    
    /**
     * Definition for a binary tree node.
     * struct TreeNode {
     *     int val;
     *     TreeNode *left;
     *     TreeNode *right;
     *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
     * };
     */
    class Solution {  //思路：枚举每个起点？？？好暴力啊。。。卧槽。。正解就是这样。。。
    public:
    	 int dfs(TreeNode* root,int sum)
    	{
    		int res = 0 ;
    		if (root==NULL) return res;
    		if (root->val==sum) res++;
    		res += dfs(root->left,sum-root->val)+dfs(root->right,sum-root->val);
    		return res;
    	}
        int pathSum(TreeNode* root, int sum) {
    		if (root==NULL) return 0;
    		return dfs(root,sum)+pathSum(root->left,sum)+pathSum(root->right,sum);
        }
    };



