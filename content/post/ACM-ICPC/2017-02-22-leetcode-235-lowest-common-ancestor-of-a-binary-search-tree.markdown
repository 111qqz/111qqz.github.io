---
author: 111qqz
date: 2017-02-22 13:22:08+00:00
draft: false
title: leetcode 235. Lowest Common Ancestor of a Binary Search Tree（求一个BST中某两个节点LCA）
type: post
url: /2017/02/leetcode-235-lowest-common-ancestor-of-a-binary-search-tree/
categories:
- 面试
tags:
- binary search
- LCA
---

[题目链接](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/?tab=Description)

题意：求一个BST中某两个节点LCA....

思路：卧槽。。。竟然求LCA...直接想到的显然是Tarjan的方法或者。。。RMQ+DFS。。。但是感觉。。。leetcode怎么可能考算法。。。。于是想到。。。可以从BST下手。。。

**两个节点的LCA的值一定在这两个节点之间。**

可以根据这个条件做二分。。。

这道题的收获是。。。不要被已知的东西限制住思路。。。tarjan或者RMQ+DFS显然也能做。。。但是那样的相当于没有用到BST的条件。。。


    
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
            TreeNode * Find(TreeNode* root,TreeNode* p,TreeNode *q)
            {
                if (root==NULL) return NULL; //实际上这应该不可能发生》。。。
                int rt = root->val;
                int a = p->val;
                int b = q->val;
                if (a<=rt&&rt<=b) return root;
                if (b<=rt&&rt<=a) return root;
                if (a<rt&&b<rt) return Find(root->left,p,q);
                if (a>rt&&b>rt) return Find(root->right,p,q);
            }
        TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
            if (root==NULL) return NULL;
            TreeNode* res = Find(root,p,q);  
            return res;    
        }
    };




