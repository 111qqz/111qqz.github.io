---
author: 111qqz
date: 2015-11-06 06:41:00+00:00
draft: false
title: hdu 1086  A - You can Solve a Geometry Problem too （线段的规范相交&&非规范相交）
type: post
url: /2015/11/hdu1086a-youcansolveageometryproblemtoo/
categories:
- ACM
---










A - You can Solve a Geometry Problem too


**Time Limit:**1000MS **Memory Limit:**32768KB **64bit IO Format:**%I64d & %I64u


Submit [Status](http://acm.hust.edu.cn/vjudge/contest/view.action?cid=98500#status//A/0)













Description







Many geometry（几何）problems were designed in the ACM/ICPC. And now, I also prepare a geometry problem for this final exam. According to the experience of many ACMers, geometry problems are always much trouble, but this problem is very easy, after all we are now attending an exam, not a contest :)   
Give you N (1<=N<=100) segments（线段）, please output the number of all intersections（交点）. You should count repeatedly if M (M>2) segments intersect at the same point.   
  
Note:   
You can assume that two segments would not intersect at more than one point.




















Input







Input contains multiple test cases. Each test case contains a integer N (1=N<=100) in a line first, and then N lines follow. Each line describes one segment with four float values x1, y1, x2, y2 which are coordinates of the segment's ending.   
A test case starting with 0 terminates the input and this test case is not to be processed.




















Output







For each case, print the number of intersections, and one line one case.




















Sample Input










2
0.00 0.00 1.00 1.00
0.00 1.00 1.00 0.00
3
0.00 0.00 1.00 1.00
0.00 1.00 1.00 0.000
0.00 0.00 1.00 0.00
0 

























Sample Output










1
3















给N个线段。问交点总数。




多条线段相交于同一个点算多次。




规范相交和非规范相交都算。




规范相交就是，交点不能是线段的端点。




而非规范相交可以。







![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock15.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart15.gif)





    
    <span style="color: #008080;">  1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;">  2</span> <span style="color: #008000;">    > File Name: code/hdu/1086.cpp
    </span><span style="color: #008080;">  3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;">  4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;">  5</span> <span style="color: #008000;">    > Created Time: 2015年11月06日 星期五 13时41分46秒
    </span><span style="color: #008080;">  6</span> <span style="color: #008000;">***********************************************************************</span><span style="color: #008000;">*/</span>
    <span style="color: #008080;">  7</span> 
    <span style="color: #008080;">  8</span> #include<iostream>
    <span style="color: #008080;">  9</span> #include<iomanip>
    <span style="color: #008080;"> 10</span> #include<cstdio>
    <span style="color: #008080;"> 11</span> #include<algorithm>
    <span style="color: #008080;"> 12</span> #include<cmath>
    <span style="color: #008080;"> 13</span> #include<cstring>
    <span style="color: #008080;"> 14</span> #include<<span style="color: #0000ff;">string</span>>
    <span style="color: #008080;"> 15</span> #include<map>
    <span style="color: #008080;"> 16</span> #include<<span style="color: #0000ff;">set</span>>
    <span style="color: #008080;"> 17</span> #include<queue>
    <span style="color: #008080;"> 18</span> #include<vector>
    <span style="color: #008080;"> 19</span> #include<stack>
    <span style="color: #008080;"> 20</span> #include<cctype>
    <span style="color: #008080;"> 21</span> <span style="color: #0000ff;">#define</span> fst first              
    <span style="color: #008080;"> 22</span> <span style="color: #0000ff;">#define</span> lson l,m,rt<<1
    <span style="color: #008080;"> 23</span> <span style="color: #0000ff;">#define</span> rson m+1,r,rt<<1|1
    <span style="color: #008080;"> 24</span> <span style="color: #0000ff;">#define</span> ms(a,x) memset(a,x,sizeof(a))
    <span style="color: #008080;"> 25</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;"> 26</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dx4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span>,<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span><span style="color: #000000;">};
    </span><span style="color: #008080;"> 27</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dy4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span>,<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span><span style="color: #000000;">};
    </span><span style="color: #008080;"> 28</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">double</span> eps = 1E-<span style="color: #800080;">8</span><span style="color: #000000;">;
    </span><span style="color: #008080;"> 29</span> typedef <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    </span><span style="color: #008080;"> 30</span> <span style="color: #0000ff;">#define</span> sec second
    <span style="color: #008080;"> 31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x3f3f3f3f</span><span style="color: #000000;">;
    </span><span style="color: #008080;"> 32</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=<span style="color: #800080;">105</span><span style="color: #000000;">;
    </span><span style="color: #008080;"> 33</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;"> 34</span> <span style="color: #0000ff;">int</span> dblcmp(<span style="color: #0000ff;">double</span><span style="color: #000000;"> d)
    </span><span style="color: #008080;"> 35</span> <span style="color: #000000;">{
    </span><span style="color: #008080;"> 36</span>     <span style="color: #0000ff;">return</span> d<-eps?-<span style="color: #800080;">1</span>:d><span style="color: #000000;">eps;
    </span><span style="color: #008080;"> 37</span> <span style="color: #000000;">}
    </span><span style="color: #008080;"> 38</span> 
    <span style="color: #008080;"> 39</span> <span style="color: #0000ff;">struct</span><span style="color: #000000;"> point
    </span><span style="color: #008080;"> 40</span> <span style="color: #000000;">{
    </span><span style="color: #008080;"> 41</span>     <span style="color: #0000ff;">double</span><span style="color: #000000;"> x,y;
    </span><span style="color: #008080;"> 42</span> <span style="color: #000000;">    point(){}
    </span><span style="color: #008080;"> 43</span>     point (<span style="color: #0000ff;">double</span> _x,<span style="color: #0000ff;">double</span><span style="color: #000000;"> _y):
    </span><span style="color: #008080;"> 44</span> <span style="color: #000000;">    x(_x),y(_y){};
    </span><span style="color: #008080;"> 45</span>     <span style="color: #0000ff;">void</span><span style="color: #000000;"> input()
    </span><span style="color: #008080;"> 46</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 47</span>     scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%lf%lf</span><span style="color: #800000;">"</span>,&x;,&<span style="color: #000000;">y);
    </span><span style="color: #008080;"> 48</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;"> 49</span> <span style="color: #000000;">    point sub(point p)
    </span><span style="color: #008080;"> 50</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 51</span>     <span style="color: #0000ff;">return</span> point(x-p.x,y-<span style="color: #000000;">p.y);
    </span><span style="color: #008080;"> 52</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;"> 53</span>     <span style="color: #0000ff;">double</span><span style="color: #000000;"> det(point p)
    </span><span style="color: #008080;"> 54</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 55</span>     <span style="color: #0000ff;">return</span> x*p.y-y*<span style="color: #000000;">p.x;
    </span><span style="color: #008080;"> 56</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;"> 57</span>     <span style="color: #0000ff;">double</span><span style="color: #000000;"> dot(point p)
    </span><span style="color: #008080;"> 58</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 59</span>     <span style="color: #0000ff;">return</span> x*p.x+y*<span style="color: #000000;">p.y;
    </span><span style="color: #008080;"> 60</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;"> 61</span> <span style="color: #000000;">};
    </span><span style="color: #008080;"> 62</span> 
    <span style="color: #008080;"> 63</span> <span style="color: #0000ff;">struct</span><span style="color: #000000;"> line
    </span><span style="color: #008080;"> 64</span> <span style="color: #000000;">{
    </span><span style="color: #008080;"> 65</span> <span style="color: #000000;">    point a,b;
    </span><span style="color: #008080;"> 66</span>     <span style="color: #0000ff;">void</span><span style="color: #000000;"> input()
    </span><span style="color: #008080;"> 67</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 68</span> <span style="color: #000000;">    a.input();
    </span><span style="color: #008080;"> 69</span> <span style="color: #000000;">    b.input();
    </span><span style="color: #008080;"> 70</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;"> 71</span>     <span style="color: #0000ff;">int</span><span style="color: #000000;"> segcrossseg(line v)
    </span><span style="color: #008080;"> 72</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 73</span>     <span style="color: #0000ff;">int</span> d1=<span style="color: #000000;">dblcmp(b.sub(a).det(v.a.sub(a)));
    </span><span style="color: #008080;"> 74</span>     <span style="color: #0000ff;">int</span> d2=<span style="color: #000000;">dblcmp(b.sub(a).det(v.b.sub(a)));
    </span><span style="color: #008080;"> 75</span>     <span style="color: #0000ff;">int</span> d3=<span style="color: #000000;">dblcmp(v.b.sub(v.a).det(a.sub(v.a)));
    </span><span style="color: #008080;"> 76</span>     <span style="color: #0000ff;">int</span> d4=<span style="color: #000000;">dblcmp(v.b.sub(v.a).det(b.sub(v.a)));
    </span><span style="color: #008080;"> 77</span>     <span style="color: #0000ff;">if</span> ((d1^d2)==-<span style="color: #800080;">2</span>&&(d3^d4)==-<span style="color: #800080;">2</span>) <span style="color: #0000ff;">return</span> <span style="color: #800080;">2</span><span style="color: #000000;">;
    </span><span style="color: #008080;"> 78</span>     <span style="color: #0000ff;">return</span> (d1==<span style="color: #800080;">0</span>&&dblcmp;(v.a.sub(a).dot(v.a.sub(b)))<=<span style="color: #800080;">0</span>||
    <span style="color: #008080;"> 79</span>         d2==<span style="color: #800080;">0</span>&&dblcmp;(v.b.sub(a).dot(v.b.sub(b)))<=<span style="color: #800080;">0</span>||
    <span style="color: #008080;"> 80</span>         d3==<span style="color: #800080;">0</span>&&dblcmp;(a.sub(v.a).dot(a.sub(v.b)))<=<span style="color: #800080;">0</span>||
    <span style="color: #008080;"> 81</span>         d4==<span style="color: #800080;">0</span>&&dblcmp;(b.sub(v.a).dot(b.sub(v.b)))<=<span style="color: #800080;">0</span><span style="color: #000000;">);
    </span><span style="color: #008080;"> 82</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;"> 83</span> <span style="color: #000000;">}li[N];
    </span><span style="color: #008080;"> 84</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;"> 85</span> <span style="color: #000000;">{
    </span><span style="color: #008080;"> 86</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;"> 87</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;"> 88</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;"> 89</span>    
    <span style="color: #008080;"> 90</span>    <span style="color: #0000ff;">while</span> (~scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&n;)!=EOF&&<span style="color: #000000;">n)
    </span><span style="color: #008080;"> 91</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;"> 92</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i <= n ; i++<span style="color: #000000;">) li[i].input();
    </span><span style="color: #008080;"> 93</span>     <span style="color: #0000ff;">int</span> cnt = <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;"> 94</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;"> 95</span>         <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> j = i+<span style="color: #800080;">1</span> ; j <= n ; j++<span style="color: #000000;">)
    </span><span style="color: #008080;"> 96</span> <span style="color: #000000;">        {
    </span><span style="color: #008080;"> 97</span> 
    <span style="color: #008080;"> 98</span>         <span style="color: #0000ff;">if</span><span style="color: #000000;"> (li[i].segcrossseg(li[j]))
    </span><span style="color: #008080;"> 99</span>             cnt++<span style="color: #000000;">;
    </span><span style="color: #008080;">100</span> <span style="color: #000000;">        }
    </span><span style="color: #008080;">101</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%dn</span><span style="color: #800000;">"</span><span style="color: #000000;">,cnt);
    </span><span style="color: #008080;">102</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">103</span> 
    <span style="color: #008080;">104</span>   
    <span style="color: #008080;">105</span>    
    <span style="color: #008080;">106</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">107</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">108</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">109</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">110</span> }





View Code



























