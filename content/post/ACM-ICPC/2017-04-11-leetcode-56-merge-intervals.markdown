---
author: 111qqz
date: 2017-04-11 11:30:32+00:00
draft: false
title: leetcode 56. Merge Intervals (模拟，求相交区间)
type: post
url: /2017/04/leetcode-56-merge-intervals/
categories:
- 面试
tags:
- leetcode
---

Given a collection of intervals, merge all overlapping intervals.

For example,
Given `[1,3],[2,6],[8,10],[15,18]`,
return `[1,6],[8,10],[15,18]`.

思路：扫一遍即可。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月11日 星期二 19时15分30秒
    File Name :56.cpp
    ************************************************ */
    /**
    
     * Definition for an interval.
    
     * struct Interval {
    
     *     int start;
    
     *     int end;
    
     *     Interval() : start(0), end(0) {}
    
     *     Interval(int s, int e) : start(s), end(e) {}
    
     * };
    
     */
    
    class Solution {
    
    public:
        
        int n;
        static bool cmp(Interval A,Interval B)
        {
    	return A.start<B.start;
        }
        vector<Interval> merge(vector<Interval>& pi) {
    	vector<Interval>res;
    	n = pi.size();
    	if (n==0) return res;
    	sort(pi.begin(),pi.end(),cmp);
    	int l = -1,r = -1;
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    if (l==-1&&r==-1)
    	    {
    		l = pi[0].start;
    		r = pi[0].end;
    		continue;
    	    }
    	    if (pi[i].start<=r)
    	    {
    		r = max(r,pi[i].end);
    		continue;
    	    }
    	    if (pi[i].start>r)
    	    {
    		res.push_back(Interval(l,r));
    		l = pi[i].start;
    		r = pi[i].end;
    		continue;
    	    }
    	}
    	//最后一组不要忘记
    	res.push_back(Interval(l,r));
    	int siz = res.size();
    	for ( int i = 0 ; i  < siz ;i++) printf("%d ",res[i].start,res[i].end);
    
    
           return res;
    
        }
    
    };
    



