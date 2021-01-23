---
author: 111qqz
date: 2017-04-12 16:23:29+00:00
draft: false
title: leetcode 40. Combination Sum II (枚举子集，和为定值)
type: post
url: /2017/04/leetcode-40-combination-sum-ii/
categories:
- 面试
tags:
- leetcode
- 枚举子集
---





 	  * Total Accepted: **106670**
 	  * Total Submissions: **329718**
 	  * Difficulty: **Medium**
 	  * Contributor: **LeetCode**








Given a collection of candidate numbers (**_C_**) and a target number (**_T_**), find all unique combinations in **_C_** where the candidate numbers sums to **_T_**.

Each number in **_C_** may only be used **once** in the combination.

**Note:**



 	  * All numbers (including target) will be positive integers.
 	  * The solution set must not contain duplicate combinations.

题意：若干正数，求所有和为target的组合。

思路：枚举子集，用和剪枝。




