---
author: 111qqz
date: 2017-04-09 11:50:05+00:00
draft: false
title: leetcode 238. Product of Array Except Self (乱搞)
type: post
url: /2017/04/leetcode-238-product-of-array-except-self/
categories:
- 面试
tags:
- leetcode
---

Given an array of _n_ integers where _n_ > 1, `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Solve it **without division** and in O(_n_).

For example, given `[1,2,3,4]`, return `[24,12,8,6]`.

**Follow up:**
Could you solve it with constant space complexity? (Note: The output array **does not** count as extra space for the purpose of space complexity analysis.)


 先来个O(n)空间的无脑解法。。。一个前缀积一个后缀积就好了。。。






    
    class Solution {
    public:
        vector<int> productExceptSelf(vector<int>& nums) {
            vector<int>res;
            vector<int>pre,suf;
            int siz = nums.size();
            if (siz==0) return res;
            for ( int i = 0 ; i < siz ; i++)
            {
                int tmp;
                if (i==0) tmp = nums[0];
                else tmp = pre[i-1]*nums[i];
                pre.push_back(tmp);
            }
            int cnt = 0 ;
            for ( int i = siz -1 ; i>= 0 ; i--)
            {
                int tmp;
                if (i==siz-1) tmp = nums[siz-1];
                else tmp = suf[cnt++]*nums[i];
                suf.push_back(tmp);
            }
          //  for ( int i = 0 ; i < siz ; i++) printf("%d ",pre[i]); puts("");
        //    for ( int i = 0 ; i < siz ; i++) printf("%d ",suf[i]);puts("");
            reverse(suf.begin(),suf.end());
            for ( int i = 0 ; i < siz;  i++)
            {
                int l = i-1;
                int r = i+1;
                int x,y;
                if (l<0) x = 1;
                else x = pre[l];
                if (r>=siz) y = 1;
                else y = suf[r];
          //      cout<<"x:"<<x<<" y:"<<y<<endl;
                res.push_back(x*y);
            }
            return res;
            
        }
    };


常数空间的做法。。。想了半天没有想法。。。

看了solution...发现就是借用res数组搞事情。。。。每个位置的答案扫完两遍得到。。。

感觉。。。非常的。。。无聊啊。。。。真心没意思吧，还以为是什么巧妙的做法呢。。。




