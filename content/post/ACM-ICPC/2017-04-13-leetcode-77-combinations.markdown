---
author: 111qqz
date: 2017-04-13 07:43:43+00:00
draft: false
title: leetcode 77. Combinations (枚举子集，限定集合大小)
type: post
url: /2017/04/leetcode-77-combinations/
categories:
- 面试
tags:
- 枚举子集
---

Given two integers _n_ and _k_, return all possible combinations of _k_ numbers out of 1 ... _n_.

思路：就是枚举子集，根据集合的大小剪枝。。。最后只要集合大小为k的集合

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 15时25分37秒
    File Name :77.cpp
    ************************************************ */
    class Solution {
    public:
        set<vector<int> >se;
        int B[1005];
        vector<vector<int> >res;
        void get_subset(int n,int *B,int cur,int cnt,int k)
        {
    	if (cur==n)
    	{
    	    vector<int>tmp;
    	    for ( int i = 0 ; i < n ; i++)
    		if (B[i]) tmp.push_back(i+1);
    	    if (tmp.size()==k)
    	    se.insert(tmp);
    	    return ;
    	}
    	if (cnt<k)
    	{
    	    B[cur] = 1;
    	    get_subset(n,B,cur+1,cnt+1,k);
    	}
    	B[cur] = 0 ;
    	get_subset(n,B,cur+1,cnt,k);
        }
        vector<vector<int>> combine(int n, int k) {
    	get_subset(n,B,0,0,k);
    	for (auto &it:se)
    	{
    	    res.push_back(it);
    	}
    	return res;
        }
    };
    



