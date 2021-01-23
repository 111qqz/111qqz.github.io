---
author: 111qqz
date: 2017-02-24 00:20:19+00:00
draft: false
title: leetcode 110. Balanced Binary Tree
type: post
url: /2017/02/leetcode-110-balanced-binary-tree/
categories:
- 面试
---

[题目链接](https://leetcode.com/submissions/detail/94039403/)

题意：判断一颗二叉树是否平衡....

思路：直接搞就好了。。。神TM又忘记dfs的时候忘记返回子调用的值。。。。我这是药丸啊。。。

    
     /**
     * Definition for a binary tree node.
     * struct TreeNode {
     *     int val;
     *     TreeNode *left;
     *     TreeNode *right;
     *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
     * };
     */
    class Solution {  //错误原因：左右子树都平衡的树未必平衡！！！！
    public:
    		bool leaf(TreeNode* root)
    		{
    			if (root->left==NULL&&root->right==NULL) return true;
    			return false;
    		}
    		int dep(TreeNode* root)
    		{
    			if (root==NULL) return 0;
    			return max(dep(root->left),dep(root->right))+1;
    		}
    		bool dfs(TreeNode* root)
    		{
    				bool res = true;
    				if (abs(dep(root->left)-dep(root->right))>1) return false;
    				if (root->left!=NULL) res = dfs(root->left);
    				if (!res) return false;
    				if  (root->right!=NULL) res = dfs(root->right);
    				if (!res) return false;
    				return true;		
    		}
        bool isBalanced(TreeNode* root) {
    		if (root==NULL) return true;
    		bool res = dfs(root);
    		return res;
        }
    };
    



