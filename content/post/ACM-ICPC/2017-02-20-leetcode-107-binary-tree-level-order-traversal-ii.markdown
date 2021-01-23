---
author: 111qqz
date: 2017-02-20 12:36:21+00:00
draft: false
title: leetcode 107 Binary Tree Level Order Traversal II(最底层往上依次输出二叉树每一个node的val)
type: post
url: /2017/02/leetcode-107-binary-tree-level-order-traversal-ii/
categories:
- 面试
---

最近要准备面试...虽然leetcode的题目难度比较水..不过白板写代码还是要练下的。。。我所理解的白板写代码。。。大概就是。。。用记事本。。一遍写对代码的能力吧。。。所以我来记录一下。。思路想错的或者没有秒的题目。

（**因为题目描述傻逼/数据范围故意坑人/leetcode抽风 / 我自己犯傻逼 等原因 没有一次通过的题目不在记录之列）**

[leetcode107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/?tab=Description)

题意：给一棵二叉树，从最底层往上依次输出每一个node的val..

思路：一开始以为同一层的一定会在相邻时间内访问。。。后来发现的确是蠢了。。。

因此dfs的时候加了一个level域。。。每次dfs的时候先左后右就好了。。。

注意记得判断root为空的情况。。。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年02月20日 星期一 19时21分51秒
    File Name :107.cpp
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
    
        vector<vector<int>>res;
        vector<int>tmp[1500];
        int mx_level = 0 ;
        void dfs( TreeNode* root,int level)
        {
    //  cout<<"level:"<<level<<endl;
        mx_level = max(mx_level,level);
        if (root->left!=NULL)
        {
            tmp[level].push_back(root->left->val);
            dfs(root->left,level+1);
        }
        if (root->right!=NULL)
        {
            tmp[level].push_back(root->right->val);
            dfs(root->right,level+1);
        }
        }
        vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (root==NULL) return res; 
            tmp[0].push_back(root->val);
            dfs(root,1);
            for ( int i = mx_level;  i>= 0 ; i--)if (!tmp[i].empty()) res.push_back(tmp[i]);
        return res;
        }
    
    };
    






