---
author: 111qqz
date: 2018-08-06 11:54:35+00:00
draft: false
title: 使用python计算误差代码
type: post
url: /2018/08/calculate-error-with-python/
categories:
- 其他
tags:
- python
---

import os
    import math
    ave_err=0.0
    max_err=0.0
    max_err_rate=0.0
    length=0
    with open("cpu_result.txt","r") as fp1, open("cuda_ppl_result.txt","r") as fp2:
        for l1 in fp1:
            l2 = fp2.readline()
            l1=l1[:-2]
            l2=l2[:-2]
            lst = l1.split(' ')
            lst2 = l2.split(' ')
            #print lst
            lst = [float(x) for x in lst ]
            length = length + len(lst)
            lst2 = [float(x) for x in lst2]
            #print (lst)
            #print (lst2)
           
            for index,x in enumerate(lst):
                y = lst2[index]
                ave_err = ave_err + abs(x-y)
                max_err = max(max_err,abs(x-y))
                max_err_rate = max(max_err_rate,abs(x-y)/x)
    
        print("len=",length)
        print("max_err=",max_err)
        print("max_err_rate=",max_err_rate*100,"%")
        print("ave_err=",ave_err/length)


需要提供两个文件，并且两个文件的数据格式相同。


