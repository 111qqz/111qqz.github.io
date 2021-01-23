---
author: 111qqz
date: 2015-11-05 10:54:00+00:00
draft: false
title: 'codeforces #329 div 2 B. Anton and Lines(几何）'
type: post
url: /2015/11/codeforces329div2b-antonandlines/
categories:
- ACM
---




B. Anton and Lines







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










The teacher gave Anton a large geometry homework, but he didn't do it (as usual) as he participated in a regular round on Codeforces. In the task he was given a set of _n_ lines defined by the equations _y_ = _k__i_*_x_ + _b__i_. It was necessary to determine whether there is at least one point of intersection of two of these lines, that lays strictly inside the strip between _x_1 < _x_2. In other words, is it true that there are1 ≤ _i_ < _j_ ≤ _n_ and _x_', _y_', such that:





  * _y_' = _k__i_ * _x_' + _b__i_, that is, point (_x_', _y_') belongs to the line number _i_;
  * _y_' = _k__j_ * _x_' + _b__j_, that is, point (_x_', _y_') belongs to the line number _j_;
  * _x_1 < _x_' < _x_2, that is, point (_x_', _y_') lies inside the strip bounded by _x_1 < _x_2.



You can't leave Anton in trouble, can you? Write a program that solves the given task.










Input




The first line of the input contains an integer _n_ (2 ≤ _n_ ≤ 100 000) -- the number of lines in the task given to Anton. The second line contains integers _x_1 and _x_2 ( - 1 000 000 ≤ _x_1 < _x_2 ≤ 1 000 000) defining the strip inside which you need to find a point of intersection of at least two lines.




The following _n_ lines contain integers _k__i_, _b__i_ ( - 1 000 000 ≤ _k__i_, _b__i_ ≤ 1 000 000) -- the descriptions of the lines. It is guaranteed that all lines are pairwise distinct, that is, for any two _i_ ≠ _j_ it is true that either _k__i_ ≠ _k__j_, or _b__i_ ≠ _b__j_.










Output




Print "Yes" (without quotes), if there is at least one intersection of two distinct lines, located strictly inside the strip. Otherwise print "No" (without quotes).










Sample test(s)










input



    
    4<br></br>1 2<br></br>1 2<br></br>1 0<br></br>0 1<br></br>0 2










output



    
    NO










input



    
    2<br></br>1 3<br></br>1 0<br></br>-1 3










output



    
    YES










input



    
    2<br></br>1 3<br></br>1 0<br></br>0 2










output



    
    YES










input



    
    2<br></br>1 3<br></br>1 0<br></br>0 3










output



    
    NO
















Note




In the first sample there are intersections located on the border of the strip, but there are no intersections located strictly inside it.




好吧。。。人蠢。。所以没想出来。。




其实画个图就能明白。。。如果两条直线相交在x1,x2之间。。




那么两条直线，分别于x1,x2的交点。。一定是一对逆序对。。。




我们可以得到每条直线在x1,x2的交点的纵坐标。。




然后按照与x1交点的纵坐标降序排。




另外一个比较重要的的是，判断是否有逆序对，只需要判断相邻的就行了。




可以用如下证明（不知道有什么更容易想的办法？）




假设直线i与直线i+k(k>=2)相交，那么直线i与直线i+j(1=


那么li[i].secli[i+k].sec




所以li[i+j].sec>li[i].sec>li[i+k].sec




那么直线i+j一定与i+k相交




当j=k-1时，i+j与i+k相邻。




也就是说...如果任意直线i与j相交...我们总可以转化成一对相邻的直线相交。




因此只判断相邻直线的相交就可以。




画图也能看出来。




**最后一点是，要开long long 。**




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock18.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart18.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/cf/#329/B.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年11月05日 星期四 15时34分05秒
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
    <span style="color: #008080;">21</span>                  
    <span style="color: #008080;">22</span> <span style="color: #0000ff;">#define</span> lson l,m,rt<<1
    <span style="color: #008080;">23</span> <span style="color: #0000ff;">#define</span> rson m+1,r,rt<<1|1
    <span style="color: #008080;">24</span> <span style="color: #0000ff;">#define</span> ms(a,x) memset(a,x,sizeof(a))
    <span style="color: #008080;">25</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;">26</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dx4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span>,<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span><span style="color: #000000;">};
    </span><span style="color: #008080;">27</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dy4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span>,<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span><span style="color: #000000;">};
    </span><span style="color: #008080;">28</span> typedef <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    </span><span style="color: #008080;">29</span> typedef <span style="color: #0000ff;">double</span><span style="color: #000000;"> DB;
    </span><span style="color: #008080;">30</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x3f3f3f3f</span><span style="color: #000000;">;
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=1E5+<span style="color: #800080;">7</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">33</span> <span style="color: #000000;">LL x1,x2;
    </span><span style="color: #008080;">34</span> pair<ll,ll><span style="color: #000000;">li[N];
    </span><span style="color: #008080;">35</span> 
    <span style="color: #008080;">36</span> 
    <span style="color: #008080;">37</span> 
    <span style="color: #008080;">38</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">39</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">40</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">41</span> <span style="color: #008000;">//</span><span style="color: #008000;">   freopen("in.txt","r",stdin);</span>
    <span style="color: #008080;">42</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">43</span> 
    <span style="color: #008080;">44</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">n);
    </span><span style="color: #008080;">45</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%I64d %I64d</span><span style="color: #800000;">"</span>,&x1;,&<span style="color: #000000;">x2);
    </span><span style="color: #008080;">46</span> <span style="color: #000000;">   LL b,k;
    </span><span style="color: #008080;">47</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">48</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">49</span>     scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%I64d %I64d</span><span style="color: #800000;">"</span>,&k;,&<span style="color: #000000;">b);
    </span><span style="color: #008080;">50</span>     li[i]=make_pair(k*x1+b,k*x2+<span style="color: #000000;">b);
    </span><span style="color: #008080;">51</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">52</span>    sort(li,li+<span style="color: #000000;">n);
    </span><span style="color: #008080;">53</span>    <span style="color: #0000ff;">bool</span> ok = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #008080;">54</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">55</span>        <span style="color: #0000ff;">if</span> (li[i-<span style="color: #800080;">1</span>].second><span style="color: #000000;">li[i].second)
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">57</span>         ok = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
    </span><span style="color: #008080;">58</span>         <span style="color: #0000ff;">break</span><span style="color: #000000;">;
    </span><span style="color: #008080;">59</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">60</span> 
    <span style="color: #008080;">61</span>    <span style="color: #0000ff;">if</span> (!ok) puts(<span style="color: #800000;">"</span><span style="color: #800000;">NO</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">62</span>    <span style="color: #0000ff;">else</span> puts(<span style="color: #800000;">"</span><span style="color: #800000;">YES</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">63</span> 
    <span style="color: #008080;">64</span>   
    <span style="color: #008080;">65</span>    
    <span style="color: #008080;">66</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">67</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">68</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">69</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">70</span> }





View Code










