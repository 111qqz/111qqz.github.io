---
author: 111qqz
date: 2015-10-22 12:17:00+00:00
draft: false
title: 'codeforces #326 div 2 A. Duff and Meat(水）'
type: post
url: /2015/10/codeforces326div2a-duffandmeat/
categories:
- ACM
---
















A. Duff and Meat







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Duff is addicted to meat! Malek wants to keep her happy for _n_ days. In order to be happy in _i_-th day, she needs to eat exactly _a__i_ kilograms of meat.


![](https://111qqz.com/wp-content/uploads/2015/11/99fc691eaf57150b35c52b82b26f08446a71223c.png)



There is a big shop uptown and Malek wants to buy meat for her from there. In _i_-th day, they sell meat for _p__i_ dollars per kilogram. Malek knows all numbers _a_1, ..., _a__n_ and _p_1, ..., _p__n_. In each day, he can buy arbitrary amount of meat, also he can keep some meat he has for the future.




Malek is a little tired from cooking meat, so he asked for your help. Help him to minimize the total money he spends to keep Duff happy for_n_ days.










Input




The first line of input contains integer _n_ (1 ≤ _n_ ≤ 105), the number of days.




In the next _n_ lines, _i_-th line contains two integers _a__i_ and _p__i_ (1 ≤ _a__i_, _p__i_ ≤ 100), the amount of meat Duff needs and the cost of meat in that day.










Output




Print the minimum money needed to keep Duff happy for _n_ days, in one line.










Sample test(s)










input



    
    3<br></br>1 3<br></br>2 2<br></br>3 1










output



    
    10










input



    
    3<br></br>1 3<br></br>2 1<br></br>3 2










output



    
    8
















Note




In the first sample case: An optimal way would be to buy 1 kg on the first day, 2 kg on the second day and 3 kg on the third day.




In the second sample case: An optimal way would be to buy 1 kg on the first day and 5 kg (needed meat for the second and third day) on the second day.










做点水题换换脑子。。。




浙大月赛题已经做蒙了QAQ




这题很简单。。




扫的时候记得更新价钱的最小值就好了。




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock31.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart31.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/cf/#326/A.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月22日 星期四 20时00分33秒
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
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">33</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> a[N],p[N];
    </span><span style="color: #008080;">34</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">35</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">36</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">37</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">38</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">39</span> 
    <span style="color: #008080;">40</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">n);
    </span><span style="color: #008080;">41</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ;  i < n ; i++) scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d %d</span><span style="color: #800000;">"</span>,&a;[i],&<span style="color: #000000;">p[i]);
    </span><span style="color: #008080;">42</span>    <span style="color: #0000ff;">int</span> mi =<span style="color: #000000;"> inf;
    </span><span style="color: #008080;">43</span>    <span style="color: #0000ff;">int</span> ans = <span style="color: #800080;">0</span><span style="color: #000000;"> ;
    </span><span style="color: #008080;">44</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">45</span> <span style="color: #000000;">   {
    </span><span style="color: #008080;">46</span>        <span style="color: #0000ff;">if</span> (p[i]<<span style="color: #000000;">mi)
    </span><span style="color: #008080;">47</span>        mi =<span style="color: #000000;"> p[i];
    </span><span style="color: #008080;">48</span>        
    <span style="color: #008080;">49</span>        ans += mi*<span style="color: #000000;">a[i];
    </span><span style="color: #008080;">50</span> <span style="color: #000000;">   }
    </span><span style="color: #008080;">51</span>    cout<<ans<<<span style="color: #000000;">endl;
    </span><span style="color: #008080;">52</span>   
    <span style="color: #008080;">53</span>    
    <span style="color: #008080;">54</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">55</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">56</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">57</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">58</span> }





View Code





















