---
author: 111qqz
date: 2017-02-24 02:57:19+00:00
draft: false
title: leetcode 101. Symmetric Tree Add to List（二叉树，判断镜像）
type: post
url: /2017/02/leetcode-101-symmetric-tree-add-to-list/
categories:
- 面试
---

[题目链接](https://leetcode.com/problems/symmetric-tree/?tab=Description)

题意：判断一棵二叉树是否是自己的镜像。做法是做个copy，相当于两棵树做比较。注意逻辑不要漏掉就好


    
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
        bool mirror(TreeNode* rt1,TreeNode* rt2)
        {
        
            if (rt1==NULL&&rt2==NULL) return true;
            if (rt1==NULL||rt2==NULL) return false;
                 printf("%d %d\n",rt1->val,rt2->val);
            if (leaf(rt1)&&leaf(rt2)&&rt1->val==rt2->val) return true;
            if (leaf(rt1)||leaf(rt2)) return false; //包含了其中一个是叶子，或者两个都是叶子但是值不相等的情况。
            if (rt1->val!=rt2->val) return false; //不是叶子，但是值不相等，没必要继续了。
            bool res = true;        
             res = mirror(rt1->left,rt2->right);
            if (!res) return false;
              res = mirror(rt2->left,rt1->right);
            if (!res) return false;
            return true;
        }
        bool isSymmetric(TreeNode* root) {
            if (root==NULL) return true;
            return mirror(root,root);
            
        }
    };






