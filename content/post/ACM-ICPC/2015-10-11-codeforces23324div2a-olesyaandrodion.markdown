---
author: 111qqz
date: 2015-10-11 15:53:00+00:00
draft: false
title: 'codeforces #324 div 2 A. Olesya and Rodion'
type: post
url: /2015/10/codeforces324div2a-olesyaandrodion/
categories:
- ACM
---
















A. Olesya and Rodion







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Olesya loves numbers consisting of _n_ digits, and Rodion only likes numbers that are divisible by _t_. Find some number that satisfies both of them.




Your task is: given the _n_ and _t_ print an integer strictly larger than zero consisting of _n_ digits that is divisible by _t_. If such number doesn't exist, print  - 1.










Input




The single line contains two numbers, _n_ and _t_ (1 ≤ _n_ ≤ 100, 2 ≤ _t_ ≤ 10) -- the length of the number and the number it should be divisible by.










Output




Print one such positive number without leading zeroes, -- the answer to the problem, or  - 1, if such number doesn't exist. If there are multiple possible answers, you are allowed to print any of them.










Sample test(s)










input



    
    3 2










output



    
    712







构造题．




让构造任意一个n位数满足整除t




由于t是个位数＝＝　




所以很水．




－１的话只有n为１t为１０的情况．




具体见代码．．．写得有点丑QAQ




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock43.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart43.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/cf/#324/A.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月11日 星期日 23时32分46秒
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
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n,t;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">33</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">34</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">35</span>  <span style="color: #008000;">//</span><span style="color: #008000;">  freopen("in.txt","r",stdin);</span>
    <span style="color: #008080;">36</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">37</span>    cin>>n>><span style="color: #000000;">t;
    </span><span style="color: #008080;">38</span>    <span style="color: #0000ff;">if</span> (n==<span style="color: #800080;">1</span>&&t;==<span style="color: #800080;">10</span><span style="color: #000000;">)
    </span><span style="color: #008080;">39</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">40</span>     puts(<span style="color: #800000;">"</span><span style="color: #800000;">-1</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">41</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">42</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">43</span>    <span style="color: #0000ff;">if</span> (n==<span style="color: #800080;">1</span><span style="color: #000000;">)
    </span><span style="color: #008080;">44</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">45</span>     cout<<t<<<span style="color: #000000;">endl;
    </span><span style="color: #008080;">46</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">47</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">48</span>    <span style="color: #0000ff;">if</span> (t==<span style="color: #800080;">10</span><span style="color: #000000;">)
    </span><span style="color: #008080;">49</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">50</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i <=n-<span style="color: #800080;">1</span> ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">51</span>         cout<<<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">52</span>     cout<<<span style="color: #800080;">0</span><<<span style="color: #000000;">endl;
    </span><span style="color: #008080;">53</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">54</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">55</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span>  ; i <= n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">56</span>        cout<<<span style="color: #000000;">t;
    </span><span style="color: #008080;">57</span>    cout<<<span style="color: #000000;">endl;
    </span><span style="color: #008080;">58</span>   
    <span style="color: #008080;">59</span>    
    <span style="color: #008080;">60</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">61</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">62</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">63</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">64</span> }





View Code
























