---
author: 111qqz
date: 2015-11-20 19:32:00+00:00
draft: false
title: 'codeforces #332 div 2 B. Spongebob and Joke'
type: post
url: /2015/11/codeforces332div2b-spongebobandjoke/
categories:
- ACM
---




B. Spongebob and Joke







time limit per test


2 seconds







memory limit per test


256 megabytes







input


standard input







output


standard output










While Patrick was gone shopping, Spongebob decided to play a little trick on his friend. The naughty Sponge browsed through Patrick's personal stuff and found a sequence _a_1, _a_2, ..., _a__m_ of length _m_, consisting of integers from 1 to _n_, not necessarily distinct. Then he picked some sequence _f_1, _f_2, ..., _f__n_ of length _n_ and for each number _a__i_ got number _b__i_ = _f__a__i_. To finish the prank he erased the initial sequence _a__i_.




It's hard to express how sad Patrick was when he returned home from shopping! We will just say that Spongebob immediately got really sorry about what he has done and he is now trying to restore the original sequence. Help him do this or determine that this is impossible.










Input




The first line of the input contains two integers _n_ and _m_ (1 ≤ _n_, _m_ ≤ 100 000) -- the lengths of sequences _f__i_ and _b__i_ respectively.




The second line contains _n_ integers, determining sequence _f_1, _f_2, ..., _f__n_ (1 ≤ _f__i_ ≤ _n_).




The last line contains _m_ integers, determining sequence _b_1, _b_2, ..., _b__m_ (1 ≤ _b__i_ ≤ _n_).










Output




Print "Possible" if there is exactly one sequence _a__i_, such that _b__i_ = _f__a__i_ for all _i_ from 1 to _m_. Then print _m_ integers_a_1, _a_2, ..., _a__m_.




If there are multiple suitable sequences _a__i_, print "Ambiguity".




If Spongebob has made a mistake in his calculations and no suitable sequence _a__i_ exists, print "Impossible".










Sample test(s)










input



    
    3 3<br></br>3 2 1<br></br>1 2 3










output



    
    Possible<br></br>3 2 1 










input



    
    3 3<br></br>1 1 1<br></br>1 1 1










output



    
    Ambiguity










input



    
    3 3<br></br>1 2 1<br></br>3 3 3










output



    
    Impossible
















Note




In the first sample 3 is replaced by 1 and vice versa, while 2 never changes. The answer exists and is unique.




In the second sample all numbers are replaced by 1, so it is impossible to unambiguously restore the original sequence.




In the third sample _f__i_ ≠ 3 for all _i_, so no sequence _a__i_ transforms into such _b__i_ and we can say for sure that Spongebob has made a mistake.







理解题意。。




需要注意的是。。。只有当在f中重复出现的那个在b中也出现了。。答案才是任意。。不然五影响。。。







![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock2.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart2.gif)





    
    <span style="color: #008080;"> 1</span> #include <cstdio>
    <span style="color: #008080;"> 2</span> #include <iostream>
    <span style="color: #008080;"> 3</span> #include <cstring>
    <span style="color: #008080;"> 4</span> #include <algorithm>
    <span style="color: #008080;"> 5</span> 
    <span style="color: #008080;"> 6</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=1E5+<span style="color: #800080;">7</span><span style="color: #000000;">;
    </span><span style="color: #008080;"> 7</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n,m;
    </span><span style="color: #008080;"> 8</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> ans[N];
    </span><span style="color: #008080;"> 9</span> <span style="color: #0000ff;">bool</span><span style="color: #000000;"> v[N];
    </span><span style="color: #008080;">10</span> <span style="color: #0000ff;">bool</span><span style="color: #000000;"> v2[N];
    </span><span style="color: #008080;">11</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;">12</span> 
    <span style="color: #008080;">13</span> <span style="color: #0000ff;">struct</span><span style="color: #000000;"> node
    </span><span style="color: #008080;">14</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">15</span>     <span style="color: #0000ff;">int</span><span style="color: #000000;"> val;
    </span><span style="color: #008080;">16</span>     <span style="color: #0000ff;">int</span><span style="color: #000000;"> id;
    </span><span style="color: #008080;">17</span> <span style="color: #000000;">}f[N],b[N];
    </span><span style="color: #008080;">18</span> 
    <span style="color: #008080;">19</span> <span style="color: #0000ff;">bool</span><span style="color: #000000;"> cmp( node a,node b)
    </span><span style="color: #008080;">20</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">21</span>     <span style="color: #0000ff;">return</span> a.val<<span style="color: #000000;">b.val;
    </span><span style="color: #008080;">22</span> <span style="color: #000000;">}
    </span><span style="color: #008080;">23</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">24</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">25</span>     cin>>n>><span style="color: #000000;">m;
    </span><span style="color: #008080;">26</span>     memset(v2,<span style="color: #0000ff;">false</span>,<span style="color: #0000ff;">sizeof</span><span style="color: #000000;">(v2));
    </span><span style="color: #008080;">27</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++) scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&f;[i].val),f[i].id=<span style="color: #000000;">i;
    </span><span style="color: #008080;">28</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < m ; i++) scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&b;[i].val),b[i].id=<span style="color: #000000;">i;
    </span><span style="color: #008080;">29</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < m ; i++) v2[b[i].val] = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
    </span><span style="color: #008080;">30</span> 
    <span style="color: #008080;">31</span>     sort(f,f+<span style="color: #000000;">n,cmp);
    </span><span style="color: #008080;">32</span>     sort(b,b+<span style="color: #000000;">m,cmp);
    </span><span style="color: #008080;">33</span> 
    <span style="color: #008080;">34</span>     <span style="color: #0000ff;">bool</span> multi = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #008080;">35</span>     memset(v,<span style="color: #0000ff;">false</span>,<span style="color: #0000ff;">sizeof</span><span style="color: #000000;">(v));
    </span><span style="color: #008080;">36</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n-<span style="color: #800080;">1</span> ; i++) <span style="color: #0000ff;">if</span> (f[i].val==f[i+<span style="color: #800080;">1</span>].val&&v2;[f[i+<span style="color: #800080;">1</span>].val]) multi = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
    </span><span style="color: #008080;">37</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++) v[f[i].val] = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
    </span><span style="color: #008080;">38</span>     <span style="color: #0000ff;">bool</span> sad = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #008080;">39</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < m; i++) <span style="color: #0000ff;">if</span> (!v[b[i].val]) sad = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
    </span><span style="color: #008080;">40</span>     memset(ans,<span style="color: #800080;">0</span>,<span style="color: #0000ff;">sizeof</span><span style="color: #000000;">(ans));
    </span><span style="color: #008080;">41</span>     <span style="color: #0000ff;">int</span> j = <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">42</span>     <span style="color: #0000ff;">bool</span> flag = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #008080;">43</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">44</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">45</span>         <span style="color: #0000ff;">if</span> (j==m) <span style="color: #0000ff;">break</span><span style="color: #000000;">;
    </span><span style="color: #008080;">46</span>         <span style="color: #0000ff;">if</span> (f[i].val==b[j].val&&j;<<span style="color: #000000;">m)
    </span><span style="color: #008080;">47</span> <span style="color: #000000;">        {
    </span><span style="color: #008080;">48</span>             <span style="color: #0000ff;">while</span> (f[i].val==b[j].val&&j;<<span style="color: #000000;">m)
    </span><span style="color: #008080;">49</span> <span style="color: #000000;">            {
    </span><span style="color: #008080;">50</span>                 ans[b[j].id] =<span style="color: #000000;"> f[i].id;
    </span><span style="color: #008080;">51</span>                 j++<span style="color: #000000;">;
    </span><span style="color: #008080;">52</span> <span style="color: #000000;">            }
    </span><span style="color: #008080;">53</span> <span style="color: #000000;">        }
    </span><span style="color: #008080;">54</span> 
    <span style="color: #008080;">55</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">56</span>      <span style="color: #0000ff;">if</span><span style="color: #000000;"> (sad)
    </span><span style="color: #008080;">57</span> <span style="color: #000000;">     {
    </span><span style="color: #008080;">58</span>          puts(<span style="color: #800000;">"</span><span style="color: #800000;">Impossible</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">59</span> <span style="color: #000000;">     }
    </span><span style="color: #008080;">60</span>      <span style="color: #0000ff;">else</span>
    <span style="color: #008080;">61</span> <span style="color: #000000;">     {
    </span><span style="color: #008080;">62</span>          <span style="color: #0000ff;">if</span> (multi) puts(<span style="color: #800000;">"</span><span style="color: #800000;">Ambiguity</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">63</span>          <span style="color: #0000ff;">else</span>
    <span style="color: #008080;">64</span> <span style="color: #000000;">         {
    </span><span style="color: #008080;">65</span>              puts(<span style="color: #800000;">"</span><span style="color: #800000;">Possible</span><span style="color: #800000;">"</span><span style="color: #000000;">);
    </span><span style="color: #008080;">66</span>              <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < m-<span style="color: #800080;">1</span> ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">67</span>                 printf(<span style="color: #800000;">"</span><span style="color: #800000;">%d </span><span style="color: #800000;">"</span>,ans[i]+<span style="color: #800080;">1</span><span style="color: #000000;">);
    </span><span style="color: #008080;">68</span>                 printf(<span style="color: #800000;">"</span><span style="color: #800000;">%dn</span><span style="color: #800000;">"</span>,ans[m-<span style="color: #800080;">1</span>]+<span style="color: #800080;">1</span><span style="color: #000000;">);
    </span><span style="color: #008080;">69</span> <span style="color: #000000;">         }
    </span><span style="color: #008080;">70</span> 
    <span style="color: #008080;">71</span> <span style="color: #000000;">     }
    </span><span style="color: #008080;">72</span> 
    <span style="color: #008080;">73</span> 
    <span style="color: #008080;">74</span> 
    <span style="color: #008080;">75</span> 
    <span style="color: #008080;">76</span> }





View Code






