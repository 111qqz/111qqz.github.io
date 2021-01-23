---
author: 111qqz
date: 2017-02-22 12:14:36+00:00
draft: false
title: leetcode 226. Invert Binary Tree（反转二叉树）
type: post
url: /2017/02/leetcode-226-invert-binary-tree/
categories:
- 面试
---

[题目链接](https://leetcode.com/problems/invert-binary-tree/?tab=Description)

题意：反转一棵二叉树。。。字面意思理解即可。。就是把每一棵子树的左右孩子交换。。。

思路：直接照着题意做就好了。。。没有坑。。记录的原因是听说这题比较经典（虽然毫无难度...


    
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
        
            bool leaf(TreeNode* root)
            {
                if (root->left==NULL&&root->right==NULL) return true;
                return false;
            }
            void dfs(TreeNode* root)
            {
                if (leaf(root)) return;
                TreeNode* tmp = root->left;
                root->left = root->right;
                root->right = tmp;
                if (root->left!=NULL) dfs(root->left);
                if (root->right!=NULL) dfs(root->right);
            }
         TreeNode* invertTree(TreeNode* root) {
            if (root==NULL) return NULL;
            dfs(root);
            return root;
            
        }
    };




