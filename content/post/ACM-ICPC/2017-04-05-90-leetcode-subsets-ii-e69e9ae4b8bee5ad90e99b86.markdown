---
author: 111qqz
date: 2017-04-05 10:45:02+00:00
draft: false
title: leetcode 90. Subsets II (枚举子集)
type: post
url: /2017/04/leetcode 90-subsets-ii/
categories:
- 面试
tags:
- 枚举子集
- leetcode
---

Given a collection of integers that might contain duplicates, **_nums_**, return all possible subsets.

**Note:** The solution set must not contain duplicate subsets.

For example,
If **_nums_** = `[1,2,2]`, a solution is:

    
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]




思路：

复习（？）一下 [枚举子集的三种写法](http://blog.csdn.net/tczxw/article/details/47394903)

（还有种更飘逸的...先不写了orz

这道题我用位向量法A的。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月05日 星期三 17时15分34秒
    File Name :90.cpp
    ************************************************ */
    class Solution {
    public:
        set<vector<int> >se;
        int B[1005];
        vector <vector<int> >res;
        void get_subset(int n,int *B,int cur,vector<int>& nums)
        {
    //	cout<<"cur:"<<cur<<endl;
    	if (cur==n) //from 0
    	{
    	    vector<int>tmp;
    	    for ( int i = 0 ; i < n ; i++)
    		if (B[i]) tmp.push_back(nums[i]);
    
    	    sort(tmp.begin(),tmp.end());
    	    int siz = tmp.size();
    //	    for ( int i = 0 ; i < siz ; i++) printf("%d ",tmp[i]);printf("\n");
    	    se.insert(tmp);
    	    return;
    	}
    	B[cur] = 1;
    	get_subset(n,B,cur+1,nums);
    	B[cur] = 0;
    	get_subset(n,B,cur+1,nums);
        }
        vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    	int siz = nums.size();
    	if (siz==0) return res;
    	get_subset(siz,B,0,nums);
    	for ( auto &it : se)
    	{
    	    res.push_back(it);
    	}
    	return res;
        }
    };
    



