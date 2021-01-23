---
author: 111qqz
date: 2015-10-26 14:56:00+00:00
draft: false
title: codeforces 589 I - Lottery(水）
type: post
url: /2015/10/codeforces589i-lottery/
categories:
- ACM
---




I - Lottery


**Time Limit:**2000MS **Memory Limit:**524288KB **64bit IO Format:**%I64d & %I64u


Submit [Status](http://acm.hust.edu.cn/vjudge/contest/view.action?cid=96696#status//I/0) [Practice](http://acm.hust.edu.cn/vjudge/problem/viewProblem.action?id=261061) [CodeForces 589I](http://acm.hust.edu.cn/vjudge/problem/visitOriginUrl.action?id=261061)













Description







Today Berland holds a lottery with a prize -- a huge sum of money! There are _k_ persons, who attend the lottery. Each of them will receive a unique integer from 1 to _k_.




The organizers bought _n_ balls to organize the lottery, each of them is painted some color, the colors are numbered from 1 to _k_. A ball of color _c_ corresponds to the participant with the same number. The organizers will randomly choose one ball -- and the winner will be the person whose color will be chosen!




Five hours before the start of the lottery the organizers realized that for the lottery to be fair there must be an equal number of balls of each of _k_ colors. This will ensure that the chances of winning are equal for all the participants.




You have to find the minimum number of balls that you need to repaint to make the lottery fair. A ball can be repainted to any of the _k_colors.













Input







The first line of the input contains two integers _n_ and _k_(1 ≤ _k_ ≤ _n_ ≤ 100) -- the number of balls and the number of participants. It is guaranteed that _n_ is evenly divisible by _k_.




The second line of the input contains space-separated sequence of _n_ positive integers _c__i_(1 ≤ _c__i_ ≤ _k_), where _c__i_ means the original color of the _i_-th ball.













Output







In the single line of the output print a single integer -- the minimum number of balls to repaint to make number of balls of each color equal.













Sample Input










Input



    
    4 2<br></br>2 1 2 2










Output



    
    1










Input



    
    8 4<br></br>1 2 1 1 1 4 1 4










Output



    
    3
















Hint







In the first example the organizers need to repaint any ball of color 2 to the color 1.




In the second example the organizers need to repaint one ball of color 1 to the color 2 and two balls of the color 1 to the color 3.







![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock28.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart28.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/hust/20151025/I.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月25日 星期日 13时09分42秒
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
    <span style="color: #008080;">22</span> <span style="color: #0000ff;">#define</span> yn hez111qqz
    <span style="color: #008080;">23</span> <span style="color: #0000ff;">#define</span> j1 cute111qqz
    <span style="color: #008080;">24</span> <span style="color: #0000ff;">#define</span> ms(a,x) memset(a,x,sizeof(a))
    <span style="color: #008080;">25</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;">26</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dx4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span>,<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span><span style="color: #000000;">};
    </span><span style="color: #008080;">27</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dy4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span>,<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span><span style="color: #000000;">};
    </span><span style="color: #008080;">28</span> typedef <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    </span><span style="color: #008080;">29</span> typedef <span style="color: #0000ff;">double</span><span style="color: #000000;"> DB;
    </span><span style="color: #008080;">30</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x3f3f3f3f</span><span style="color: #000000;">;
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n,k;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">int</span> cnt[<span style="color: #800080;">111</span><span style="color: #000000;">];
    </span><span style="color: #008080;">33</span> 
    <span style="color: #008080;">34</span> <span style="color: #0000ff;">bool</span> cmp( <span style="color: #0000ff;">int</span> a,<span style="color: #0000ff;">int</span><span style="color: #000000;"> b)
    </span><span style="color: #008080;">35</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">36</span>     <span style="color: #0000ff;">return</span> a><span style="color: #000000;">b;
    </span><span style="color: #008080;">37</span> <span style="color: #000000;">}
    </span><span style="color: #008080;">38</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">39</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">40</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">41</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">42</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">43</span> 
    <span style="color: #008080;">44</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d %d</span><span style="color: #800000;">"</span>,&n;,&<span style="color: #000000;">k);
    </span><span style="color: #008080;">45</span>    ms(cnt,<span style="color: #800080;">0</span><span style="color: #000000;">);
    </span><span style="color: #008080;">46</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">47</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">48</span>     <span style="color: #0000ff;">int</span><span style="color: #000000;"> x;
    </span><span style="color: #008080;">49</span>     scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">x);
    </span><span style="color: #008080;">50</span>     cnt[x]++<span style="color: #000000;">;
    </span><span style="color: #008080;">51</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">52</span>     sort(cnt,cnt+<span style="color: #800080;">105</span><span style="color: #000000;">,cmp);
    </span><span style="color: #008080;">53</span>     <span style="color: #0000ff;">int</span> ans = <span style="color: #800080;">0</span><span style="color: #000000;"> ;
    </span><span style="color: #008080;">54</span>     <span style="color: #0000ff;">int</span> ave = n/<span style="color: #000000;">k;
    </span><span style="color: #008080;">55</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i  = <span style="color: #800080;">0</span> ;  i < <span style="color: #800080;">105</span> ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">57</span>     <span style="color: #0000ff;">if</span> (cnt[i]<=ave) <span style="color: #0000ff;">break</span><span style="color: #000000;">;
    </span><span style="color: #008080;">58</span>     <span style="color: #0000ff;">else</span> ans+=cnt[i]-<span style="color: #000000;">ave;
    </span><span style="color: #008080;">59</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">60</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%dn</span><span style="color: #800000;">"</span><span style="color: #000000;">,ans);
    </span><span style="color: #008080;">61</span>   
    <span style="color: #008080;">62</span>    
    <span style="color: #008080;">63</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">64</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">65</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">66</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">67</span> }





View Code












