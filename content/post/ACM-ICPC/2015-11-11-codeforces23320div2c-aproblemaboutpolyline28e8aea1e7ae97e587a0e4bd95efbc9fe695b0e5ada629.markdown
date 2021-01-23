---
author: 111qqz
date: 2015-11-11 07:58:00+00:00
draft: false
title: 'codeforces #320 div 2 C. A Problem about Polyline(计算几何？数学)'
type: post
url: /2015/11/codeforces320div2c-aproblemaboutpolyline/
categories:
- ACM
---



















C. A Problem about Polyline







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










There is a polyline going through points (0, 0) - (_x_, _x_) - (2_x_, 0) - (3_x_, _x_) - (4_x_, 0) - ... - (2_kx_, 0) - (2_kx_ + _x_, _x_) - ....




We know that the polyline passes through the point (_a_, _b_). Find minimum positive value _x_ such that it is true or determine that there is no such _x_.










Input




Only one line containing two positive integers _a_ and _b_ (1 ≤ _a_, _b_ ≤ 109).










Output




Output the only line containing the answer. Your answer will be considered correct if its relative or absolute error doesn't exceed10 - 9. If there is no such _x_ then output  - 1 as the answer.










Sample test(s)










input



    
    3 1










output



    
    1.000000000000










input



    
    1 3










output



    
    -1










input



    
    4 1










output



    
    1.250000000000
















Note




You can see following graphs for sample 1 and sample 3.


![](https://111qqz.com/wp-content/uploads/2015/11/a8eacdc76b5041c0d011fcd24adf4c79a5a7c93a.png)
![](https://111qqz.com/wp-content/uploads/2015/11/4954a424c9cc12b22e10344f2653f2270edad1a5.png)


























题意：




　　有从原点开始，斜率分别为1和-1的折线周期下去，问是否存在x使得整点（a,b)在折线上，存在的话求最小的x，无解输出-1.







**思路：由于斜率为1，所以x>=y.那么x**




**对于x>=y的情况：我们发现（a,b）点如果是落在斜率为1的折线上，那么该折线与x轴的交点为（a-b,0）**




**如果(a,b)点落在落在斜率为-1的折线上，那么该折线与x轴的交点为（a+b,0） **




**分析可知，如果a+b为奇数，那么一定会落在斜率为-1的折线上，如果a-b为偶数，一定会落在斜率为1的折线上。**




**而（a+b）不为偶数和（a-b）补为偶数不可能同时成立。**




**因为碎玉x>=y的情况一定有解。**




**二分答案即可（其实还有一种比较偷懒（比较聪明？）的办法是...不去考虑是否一定有解。把二分的初始条件设置为-1就好)**




**不过证明无解也并不难想。**







**需要注意的是精度问题。。。eps要记得根据题目调整。。。比如这道题要求1E-9...**




**eps至少比要求的多两位才保险。。。。**




**因为忘记调整eps(因为一般题目要求都是1E-6。。。所以我eps写的是1E-8)而wa了好多次。。。。**










![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock5.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart5.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/cf/#320/C.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年11月10日 星期二 16时54分46秒
    </span><span style="color: #008080;"> 6</span> <span style="color: #008000;"> ***********************************************************************</span><span style="color: #008000;">*/</span>
    <span style="color: #008080;"> 7</span> 
    <span style="color: #008080;"> 8</span> #include<iostream>
    <span style="color: #008080;"> 9</span> #include<iomanip>
    <span style="color: #008080;">10</span> #include<cstdio>
    <span style="color: #008080;">11</span> #include<algorithm>
    <span style="color: #008080;">12</span> #include<cmath>
    <span style="color: #008080;">13</span> #include<cstring>
    <span style="color: #008080;">14</span> #include<<span style="color: #0000ff;">string</span>>
    <span style="color: #008080;">15</span> #include<map>
    <span style="color: #008080;">16</span> #include<<span style="color: #0000ff;">set</span>>
    <span style="color: #008080;">17</span> #include<queue>
    <span style="color: #008080;">18</span> #include<vector>
    <span style="color: #008080;">19</span> #include<stack>
    <span style="color: #008080;">20</span> #include<cctype>
    <span style="color: #008080;">21</span> <span style="color: #0000ff;">#define</span> fst first              
    <span style="color: #008080;">22</span> <span style="color: #0000ff;">#define</span> sec second      
    <span style="color: #008080;">23</span> <span style="color: #0000ff;">#define</span> lson l,m,rt<<1
    <span style="color: #008080;">24</span> <span style="color: #0000ff;">#define</span> rson m+1,r,rt<<1|1
    <span style="color: #008080;">25</span> <span style="color: #0000ff;">#define</span> ms(a,x) memset(a,x,sizeof(a))
    <span style="color: #008080;">26</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;">27</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">double</span> eps = 1E-<span style="color: #800080;">10</span><span style="color: #000000;">;
    </span><span style="color: #008080;">28</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dx4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span>,<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span><span style="color: #000000;">};
    </span><span style="color: #008080;">29</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dy4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span>,<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span><span style="color: #000000;">};
    </span><span style="color: #008080;">30</span> typedef <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x3f3f3f3f</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">const</span> LL linf =1LL<<<span style="color: #800080;">60</span><span style="color: #000000;">;
    </span><span style="color: #008080;">33</span> <span style="color: #000000;">LL a,b;
    </span><span style="color: #008080;">34</span> <span style="color: #0000ff;">int</span> dblcmp(<span style="color: #0000ff;">double</span><span style="color: #000000;"> d)
    </span><span style="color: #008080;">35</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">36</span>     <span style="color: #0000ff;">return</span> d<-eps?-<span style="color: #800080;">1</span>:d><span style="color: #000000;">eps;
    </span><span style="color: #008080;">37</span> <span style="color: #000000;">}
    </span><span style="color: #008080;">38</span> <span style="color: #000000;">LL bin(LL l,LL r)
    </span><span style="color: #008080;">39</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">40</span>     LL res = -<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">41</span>     <span style="color: #0000ff;">while</span> (l<=<span style="color: #000000;">r)
    </span><span style="color: #008080;">42</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">43</span>     LL mid = (l+r)>><span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">44</span>      <span style="color: #0000ff;">double</span> x=(a+b)*<span style="color: #800080;">1.0</span>/(<span style="color: #800080;">2</span>*<span style="color: #000000;">mid);
    </span><span style="color: #008080;">45</span>     <span style="color: #0000ff;">if</span> (dblcmp(x-b)>=<span style="color: #800080;">0</span><span style="color: #000000;">) 
    </span><span style="color: #008080;">46</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">47</span>         l = mid+<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">48</span>         res =<span style="color: #000000;"> mid;
    </span><span style="color: #008080;">49</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">50</span>     <span style="color: #0000ff;">else</span>
    <span style="color: #008080;">51</span>         r = mid -<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">52</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">53</span>     <span style="color: #0000ff;">return</span><span style="color: #000000;"> res;
    </span><span style="color: #008080;">54</span> <span style="color: #000000;">}
    </span><span style="color: #008080;">55</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">57</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">58</span> <span style="color: #008000;">//</span><span style="color: #008000;">   freopen("in.txt","r",stdin);</span>
    <span style="color: #008080;">59</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">60</span> 
    <span style="color: #008080;">61</span>    cin>>a>><span style="color: #000000;">b;
    </span><span style="color: #008080;">62</span>    LL k =<span style="color: #000000;"> bin(1LL,linf);
    </span><span style="color: #008080;">63</span>    <span style="color: #0000ff;">if</span> (a<<span style="color: #000000;">b)
    </span><span style="color: #008080;">64</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">65</span>     puts(<span style="color: #800000;">"</span><span style="color: #800000;">-1</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">66</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">67</span>    <span style="color: #0000ff;">else</span>
    <span style="color: #008080;">68</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">69</span> <span style="color: #008000;">//</span><span style="color: #008000;">    LL k = bin(1LL,linf);</span>
    <span style="color: #008080;">70</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%.12fn</span><span style="color: #800000;">"</span>,(a+b)*<span style="color: #800080;">1.0</span>/(<span style="color: #800080;">2.0</span>*<span style="color: #000000;">k));
    </span><span style="color: #008080;">71</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">72</span>   
    <span style="color: #008080;">73</span>    
    <span style="color: #008080;">74</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">75</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">76</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">77</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">78</span> }





View Code












