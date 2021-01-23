---
author: 111qqz
date: 2017-04-13 12:41:33+00:00
draft: false
title: leetcode 229. Majority Element II （O(1)空间找出现次数大于n/3的元素）
type: post
url: /2017/04/leetcode-229-majority-element-ii/
categories:
- 面试
  
tags:
- leetcode
---

Given an integer array of size _n_, find all elements that appear more than `⌊ n/3 ⌋` times. The algorithm should run in linear time and in O(1) space.

题意：给你n个数，要求找出出现此处大于n/3的。。。

思路：之前做过一个找出n个数出现此处大于n/2的题目，思想是“非吾族类，其心必异”。。

这道题类似。。。容易知道题目要求的数最多有2个，最少有0个。。。

由于最多两个“族类”，在更新的时候，要判断是不是友军的人...毕竟朋友妻不可欺嘛（什么鬼

最后记得扫一遍，check一下，检查出现此处是否满足题意。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月13日 星期四 20时05分53秒
    File Name :229.cpp
    ************************************************ */
    class Solution {
    
    public:
        //出现次数大于int(n/3)的元素，最少有0个，最多有两个
        vector<int> majorityElement(vector<int>& nums) {
    	vector<int>res;
    	int n = nums.size();
    	if (n==0) return res; 
    	int cnt1,cnt2,v1,v2;
    	cnt1 = cnt2 = 0;
    	v1 = v2 = -1;
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    int x = nums[i];
    //	    printf("i:%d nums[i]:%d v1:%d cnt1:%d v2:%d cnt2:%d\n",i,nums[i],v1,cnt1,v2,cnt2);
    	    if (cnt1==0&&v2!=x) //兄弟的女人不要抢(误
    	    {
    		cnt1++;
    		v1 = x;
    		continue;
    	    }else if ( cnt2==0&&v1!=x) //朋友妻不可欺（？？？
    	    {
    		cnt2++;
    		v2 = x;
    		continue;
    	    }
    	    if (x==v1) cnt1++;
    	    else if (x==v2) cnt2++;
    	    else 
    	    {
    		cnt1--;
    		cnt2--;
    	    }
    	}
    	int n3 = n/3;
    	int check1=0,check2=0; //未必出现此处大于int(n/3),再检查一次。
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    if (nums[i]==v1) check1++;
    	    else
    	    if (nums[i]==v2) check2++;
    	}
    //	cout<<"v1:"<<v1<<" v2:"<<v2<<"c1:"<<check1<<" c2:"<<check2<<endl;
    	if (v1==v2)
    	{
    	    if (check1>n3) res.push_back(v1);
    	    return res;
    	}
    //	cout<<"check1:"<<check1<<" n3:"<<n3<<endl;
    	if (check1>n3)
    	res.push_back(v1);
    	if (check2>n3)
    	res.push_back(v2);
    	return res;
    
    
        }
    
    };
    





