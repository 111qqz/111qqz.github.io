---
author: 111qqz
date: 2017-10-09 13:10:43+00:00
draft: false
title: 辛普森积分学习笔记
type: post
url: /2017/10/Simpsons-rule-notes/
categories:
- ACM
tags:
- 数值计算方法
- 计算几何
- 辛普森积分
---

16沈阳的阴影还在orz，来学习一下辛普森积分。

参考资料：[梯形多步法和辛普森积分](https://wenku.baidu.com/view/10653ac38bd63186bcebbca3.html)

[辛普森计算定积分](https://github.com/poluner/blog/blob/master/acm/computational-geometry/.md)

辛普森积分是一种数值积分方法（然后现在只记得教计算方法的是一个小姐姐，并不记得当时学了什么orz

大概就是用梯形近似计算曲边梯形面积，辛普森积分公式如下：
[![](https://camo.githubusercontent.com/9e31635a0068b1a145b52c3d0a9c932c6a0f123b/687474703a2f2f696d672e626c6f672e6373646e2e6e65742f3230313630383038313930313231343136)
](https://camo.githubusercontent.com/9e31635a0068b1a145b52c3d0a9c932c6a0f123b/687474703a2f2f696d672e626c6f672e6373646e2e6e65742f3230313630383038313930313231343136)

下面放代码：


    
    double f(double x){return sin(x)*x;}//这是被积函数
    double simpson(double l,double r){return (r-l)*(f(l)+f(r)+4*f((l+r)/2))/6;}
    double di(double l,double r){//越二分以得到更精确的结果
        double m=(l+r)/2;
        double ans=simpson(l,r);
        if(sgn(ans-simpson(l,m)-simpson(m,r))==0)return ans; //在误差之内
        return di(l,m)+di(m,r); //不再误差之内就继续将区间缩小
    }



切了个练手题，慢慢补充总结。

**需要注意的是，simpson对精度要求比较高。。。eps开到1E-10才过。。**

[hdu1724题目链接 ](http://acm.split.hdu.edu.cn/showproblem.php?pid=1724)

[hdu1724解题报告](https://111qqz.com/wordpress/2017/10/hdu1724/)

所以问题就在于写出积分公式（如果是多重积分要变成累次积分？orz)
















