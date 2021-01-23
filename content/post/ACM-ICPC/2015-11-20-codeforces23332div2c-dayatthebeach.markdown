---
author: 111qqz
date: 2015-11-20 19:33:00+00:00
draft: false
title: 'codeforces #332 div 2 C. Day at the Beach'
type: post
url: /2015/11/codeforces332div2c-dayatthebeach/
categories:
- ACM
---




C. Day at the Beach







time limit per test


2 seconds







memory limit per test


256 megabytes







input


standard input







output


standard output










One day Squidward, Spongebob and Patrick decided to go to the beach. Unfortunately, the weather was bad, so the friends were unable to ride waves. However, they decided to spent their time building sand castles.




At the end of the day there were _n_ castles built by friends. Castles are numbered from 1 to _n_, and the height of the _i_-th castle is equal to _h__i_. When friends were about to leave, Squidward noticed, that castles are not ordered by their height, and this looks ugly. Now friends are going to reorder the castles in a way to obtain that condition _h__i_ ≤ _h__i_ + 1 holds for all _i_ from 1 to _n_ - 1.




Squidward suggested the following process of sorting castles:





  * Castles are split into blocks -- groups of consecutive castles. Therefore the block from _i_ to _j_ will include castles_i_, _i_ + 1, ..., _j_. A block may consist of a single castle.
  * The partitioning is chosen in such a way that every castle is a part of exactly one block.
  * Each block is sorted independently from other blocks, that is the sequence _h__i_, _h__i_ + 1, ..., _h__j_ becomes sorted.
  * The partitioning should satisfy the condition that after each block is sorted, the sequence _h__i_ becomes sorted too. This may always be achieved by saying that the whole sequence is a single block.



Even Patrick understands that increasing the number of blocks in partitioning will ease the sorting process. Now friends ask you to count the maximum possible number of blocks in a partitioning that satisfies all the above requirements.










Input




The first line of the input contains a single integer _n_ (1 ≤ _n_ ≤ 100 000) -- the number of castles Spongebob, Patrick and Squidward made from sand during the day.




The next line contains _n_ integers _h__i_ (1 ≤ _h__i_ ≤ 109). The _i_-th of these integers corresponds to the height of the _i_-th castle.










Output




Print the maximum possible number of blocks in a valid partitioning.










Sample test(s)










input



    
    3<br></br>1 2 3










output



    
    3










input



    
    4<br></br>2 1 3 2










output



    
    2
















Note




In










![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock1.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart1.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/cf/#332/C.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年11月21日 星期六 03时14分55秒
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
    </span><span style="color: #008080;">27</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">double</span> eps = 1E-<span style="color: #800080;">8</span><span style="color: #000000;">;
    </span><span style="color: #008080;">28</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dx4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span>,<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span><span style="color: #000000;">};
    </span><span style="color: #008080;">29</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dy4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span>,<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span><span style="color: #000000;">};
    </span><span style="color: #008080;">30</span> typedef <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x3f3f3f3f</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=1E5+<span style="color: #800080;">7</span><span style="color: #000000;">;
    </span><span style="color: #008080;">33</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">34</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> a[N];
    </span><span style="color: #008080;">35</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> l[N],r[N];
    </span><span style="color: #008080;">36</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">37</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">38</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">39</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">40</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">41</span>    cin>><span style="color: #000000;">n;
    </span><span style="color: #008080;">42</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i <= n ; i++) scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">a[i]);
    </span><span style="color: #008080;">43</span>    r[n+<span style="color: #800080;">1</span>] =<span style="color: #000000;"> inf;
    </span><span style="color: #008080;">44</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = n ; i >= <span style="color: #800080;">0</span> ; i --) r[i] = min(r[i+<span style="color: #800080;">1</span><span style="color: #000000;">],a[i]);
    </span><span style="color: #008080;">45</span>    <span style="color: #0000ff;">int</span> mx = -<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">46</span>    <span style="color: #0000ff;">int</span> cnt = <span style="color: #800080;">0</span><span style="color: #000000;"> ;
    </span><span style="color: #008080;">47</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i <= n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">48</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">49</span>     mx =<span style="color: #000000;"> max(mx,a[i]);
    </span><span style="color: #008080;">50</span>     <span style="color: #0000ff;">if</span> (mx<=r[i+<span style="color: #800080;">1</span><span style="color: #000000;">])
    </span><span style="color: #008080;">51</span>         cnt++,mx = -<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">52</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">53</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%dn</span><span style="color: #800000;">"</span><span style="color: #000000;">,cnt);
    </span><span style="color: #008080;">54</span>   
    <span style="color: #008080;">55</span>    
    <span style="color: #008080;">56</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">57</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">58</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">59</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">60</span> }





View Code










