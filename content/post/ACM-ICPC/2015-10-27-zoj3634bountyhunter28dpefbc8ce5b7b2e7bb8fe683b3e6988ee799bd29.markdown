---
author: 111qqz
date: 2015-10-27 06:02:00+00:00
draft: false
title: zoj 3634 Bounty hunter(dp，已经想明白)
type: post
url: /2015/10/zoj3634bountyhunterdp/
categories:
- ACM
---




M - Bounty hunter


**Time Limit:**5000MS **Memory Limit:**65536KB **64bit IO Format:**%lld & %llu


Submit [Status](http://acm.hust.edu.cn/vjudge/contest/view.action?cid=95597#status//M/0)













Description







Bounty hunter is a hero who always moves along cities to earn money by his power. One day he decides to N cities one by one




At the beginning ,Bounty hunter has X money and Y points of Attack force. At day 1, he will goes to city 1, then city 2 at day 2, city 3 at day 3, ... At last ,he goes to city N at day N and leaves it at day N+1. In each city, he can increase his attack force by money and earn some money by accepting a task. In the city i, it costs him ai money to increase one point of attack force. And he can gets bi*yi money after finishing the task in city i while yi is his attack force after his increasing at city i.




As it's known to all that money is the life of Bounty hunter, he wants to own as much money as he can after leaving city N. Please find out the maximal moeny he can get.




PS1: when Bounty hunter leaves a city he won't come back.




PS2: Bounty hunter can increases his attack force by any real numbers he wants, if the money is enough. For example, if he has 7 money and the unit price of attack force at the city he stays now is 2, he can spend 3 money to increase attack force by 1.5.




PS3: After Bounty hunter finishes the task he will leave the city at once. It means he can and only can increase his attack force before he finishes the task and gets the money at the same city.













Input







The first line of the input is three integers N,X,Y, (0≤N,X,Y≤100000) following is N lines. In the i-th line has two real number ai and bi.(0≤bi≤1,0<ai≤100000)













Output







Output the maximal money he can get.Two decimal places reserved. We promise that the answer is less than 1e15













Sample Input






    
    1 10 0
    1.0 1.0
    
    3 13 5
    7.0 1.0
    1.1 0.6
    1.0 0.6
    













Sample Output






    
    10.00
    25.64<br></br><br></br>dp苦手。。。。<br></br>看了很多题解。。。然而都是一个样。。。<br></br>抄别人题解也不加个出处。。。<br></br>好像是自己写的似的。。。真是无聊。。。<br></br>转移方程有一个地方没想明白。。。<br></br>就是dp_m[i+1]*b[i]这个式子。。。。表示啥。。。<br></br>妈蛋。。。。改天再想。<br></br>update_2015_10_27晚上：<br></br>傻逼了。。。dpa[i]和dp[m]表示的都是能赚到的最多钱数。。。dpa[i]表示的不是攻击力！！！<br></br>上午看怎么dp_m[i+1]*b[i]表示的应该是第i天能赚到的钱数（的一部分）。。怎么加给攻击力了orz....脑袋真是补清醒的可以。。。。。<br></br>想清楚就没问题了。




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock26.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart26.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/zoj/3634.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月27日 星期二 13时46分35秒
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
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=1E5+<span style="color: #800080;">7</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">double</span><span style="color: #000000;"> a[N],b[N],dp_a[N],dp_m[N];
    </span><span style="color: #008080;">33</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">34</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> x,y;
    </span><span style="color: #008080;">35</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">36</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">37</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">38</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">39</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">40</span> 
    <span style="color: #008080;">41</span>    <span style="color: #0000ff;">while</span> (scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d %d %d</span><span style="color: #800000;">"</span>,&n;,&x;,&y;)!=<span style="color: #000000;">EOF)
    </span><span style="color: #008080;">42</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">43</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i <= n ; i++) scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%lf %lf</span><span style="color: #800000;">"</span>,&a;[i],&<span style="color: #000000;">b[i]);
    </span><span style="color: #008080;">44</span>     
    <span style="color: #008080;">45</span>     ms(dp_a,<span style="color: #800080;">0</span><span style="color: #000000;">);
    </span><span style="color: #008080;">46</span>     ms(dp_m,<span style="color: #800080;">0</span><span style="color: #000000;">);
    </span><span style="color: #008080;">47</span>     dp_a[n] =<span style="color: #000000;"> b[n];
    </span><span style="color: #008080;">48</span>     dp_m[n] =max(<span style="color: #800080;">1.0</span>,<span style="color: #800080;">1.0</span>/a[n]*<span style="color: #000000;">b[n]); 
    </span><span style="color: #008080;">49</span> 
    <span style="color: #008080;">50</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span>  i = n-<span style="color: #800080;">1</span> ; i >=<span style="color: #800080;">1</span> ; i--<span style="color: #000000;">)
    </span><span style="color: #008080;">51</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">52</span>         dp_a[i] = dp_m[i+<span style="color: #800080;">1</span>]*b[i]+dp_a[i+<span style="color: #800080;">1</span>];        <span style="color: #008000;">//</span><span style="color: #008000;">转移方程还是没太想清楚TAT  主要是dp_m[i+1]*b[i]这部分。。。再想一下</span>
    <span style="color: #008080;">53</span>         dp_m[i] = max(dp_m[i+<span style="color: #800080;">1</span>],<span style="color: #800080;">1.0</span>/a[i]*<span style="color: #000000;">dp_a[i]);
    </span><span style="color: #008080;">54</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">55</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%.2fn</span><span style="color: #800000;">"</span>,x*dp_m[<span style="color: #800080;">1</span>]+y*dp_a[<span style="color: #800080;">1</span><span style="color: #000000;">]);
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">57</span>   
    <span style="color: #008080;">58</span>    
    <span style="color: #008080;">59</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">60</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">61</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">62</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">63</span> }





View Code












