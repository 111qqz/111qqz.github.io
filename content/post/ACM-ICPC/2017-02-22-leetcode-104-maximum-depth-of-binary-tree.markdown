---
author: 111qqz
date: 2017-02-22 12:41:34+00:00
draft: false
title: leetcode 104. Maximum Depth of Binary Tree（求一棵树的深度）
type: post
url: /2017/02/leetcode-104-maximum-depth-of-binary-tree/
categories:
- ACM
---

[题目链接](https://leetcode.com/problems/maximum-depth-of-binary-tree/?tab=Description)

题意：求一棵树的深度。。。。

思路：。。。定义搞即可。。按照左右子树中大的算。。。因为据说是经典题（虽然并不觉得2333。。。所以记录下。。。


    
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
            
            int dfs(TreeNode* root)
            {
                if (root==NULL) return 0;
                return max(dfs(root->left),dfs(root->right))+1;
            }
                
        int maxDepth(TreeNode* root){
            if (root==NULL) return 0;
            int res = dfs(root);
            return res;
        
            
        }
    };






