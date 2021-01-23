---
author: 111qqz
date: 2017-04-14 10:51:39+00:00
draft: false
title: leetcode 228. Summary Ranges
type: post
url: /2017/04/leetcode-228/
categories:
- 面试

tags:
- leetcode
---

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given `[0,1,2,4,5,7]`, return `["0->2","4->5","7"].`

题意：把连续的数连续表示

思路：模拟。注意有负数，注意有-2147483648这种数据。

本来还想着，可能是leetcode加数据的审核机制太松，导致被人加了奇怪的数据。。。

结果发现出题人和加数据的人是一个人啊？

不给数据范围，加这种奇怪的数据很有意思？ 分分钟卡掉你的标程啊？

感觉像吃了苍蝇一样恶心。。一句话，出题人傻逼

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月14日 星期五 16时26分01秒
    File Name :228.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        string int2st(long long x)
        {
    	if (x==0) return "0";
    	string ret = "";
    	int val;   //md还有负数
    	long long sign = 1;
    	if (x<0) sign = -1;
    	x*=sign;
    	while (x)
    	{
    	    val = x % 10;
    	    ret = ret + char(val+'0');
    	    x/=10;
    	}
    	if (sign==-1) ret +="-";
    	reverse(ret.begin(),ret.end());
    	return ret;
        }
        string solve(vector<int>& vec)
        {
    	string ret = "";
    	int siz = vec.size();
    	if (siz==1) ret = ret + int2st(vec[0]);
    	else ret = ret + int2st(vec[0]) + "->" + int2st(vec[siz-1]);
    	return ret;
        }
        vector<string> summaryRanges(vector<int>& nums) {
    	int siz = nums.size();
    	vector<string>res;
    	if (siz==0) return res;
    	vector<int>tmp;
    	for ( int i = 0 ; i < siz ; i++)
    	{
    	    if (tmp.size()==0)
    	    {
    		tmp.push_back(nums[i]);
    	    }else if (nums[i]==nums[i-1]+1)
    	    {
    		tmp.push_back(nums[i]);
    	    }else 
    	    {
    		res.push_back(solve(tmp));
    		tmp.clear();
    		tmp.push_back(nums[i]);
    	    }
    	}
    	res.push_back(solve(tmp));
    
    
    	    
            return res;
    
        }
    
    };
    





