---
author: 111qqz
date: 2017-04-12 16:00:57+00:00
draft: false
title: leetcode 495. Teemo Attacking
type: post
url: /2017/04/leetcode-495-teemo-attacking/
categories:
- 面试
tags:
- leetcode
---

In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking **ascending** time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

题意：若干长度相同的区间，升序给出区间左端点，以及区间长度。问区间被覆盖的长度总和。

思路：。。。。随便写。这题哪里有medium难度了啊。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月12日 星期三 23时42分25秒
    File Name :495.cpp
    ************************************************ */
    class Solution {
    
    public:
    
        int findPoisonedDuration(vector<int>& a, int t) {
    	int n = a.size();
    	int res = 0;
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    if (i==n-1)
    	    {
    		res+=t;
    		continue;
    	    }
    	    if (a[i]+t<=a[i+1]) res+=t;
    	    else res = res + a[i+1]-a[i];
    	}
    	return res;
            
    
        }
    
    };
    



