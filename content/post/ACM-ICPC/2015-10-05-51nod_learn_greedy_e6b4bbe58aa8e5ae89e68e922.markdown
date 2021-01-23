---
author: 111qqz
date: 2015-10-05 11:35:00+00:00
draft: false
title: 51nod_learn_greedy_活动安排2
type: post
url: /2015/10/51nod_learn_greedy_2/
categories:
- ACM
---

有若干个活动，第i个开始时间和结束时间是[Si,fi)，同一个教室安排的活动之间不能交叠，求要安排所有活动，最少需要几个教室？






    
    第一行一个正整数n (n <= 10000)代表活动的个数。
    第二行到第(n + 1)行包含n个开始时间和结束时间。
    开始时间严格小于结束时间，并且时间都是非负整数，小于1000000000







**输出**









    
    一行包含一个整数表示最少教室的个数。










**输入示例**




  


    
    3
    1 2
    3 4
    2 9







  
**输出示例**




  


    
    2<br></br><br></br><br></br>其实就是求某个时间点的最大厚度...<br></br>一开始傻逼了...<br></br>想着什么从１开始推过去...必然tle．．就没写＝＝<br></br>然后今天再开...我只要把开始时间和结束时间放在一起排序...从小到大<br></br>然后用一个boolean做好标记就好...<br></br>有点像海洋兄的收费站的比喻？




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock45.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart45.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/51nod/learn/greedy/2.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月05日 星期一 19时24分32秒
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
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=1E4+<span style="color: #800080;">5</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">33</span> <span style="color: #0000ff;">struct</span><span style="color: #000000;"> Q
    </span><span style="color: #008080;">34</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">35</span>     <span style="color: #0000ff;">int</span><span style="color: #000000;"> t;
    </span><span style="color: #008080;">36</span>     <span style="color: #0000ff;">bool</span><span style="color: #000000;"> sta;
    </span><span style="color: #008080;">37</span> }q[<span style="color: #800080;">2</span>*<span style="color: #000000;">N];
    </span><span style="color: #008080;">38</span> 
    <span style="color: #008080;">39</span> <span style="color: #0000ff;">bool</span><span style="color: #000000;"> cmp(Q a,Q b)
    </span><span style="color: #008080;">40</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">41</span>     <span style="color: #0000ff;">return</span> a.t<<span style="color: #000000;">b.t;
    </span><span style="color: #008080;">42</span> <span style="color: #000000;">}
    </span><span style="color: #008080;">43</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">44</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">45</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">46</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">47</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">48</span> 
    <span style="color: #008080;">49</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">n);
    </span><span style="color: #008080;">50</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < <span style="color: #800080;">2</span>*n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">51</span> <span style="color: #000000;">   {
    </span><span style="color: #008080;">52</span>        scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">q[i].t);
    </span><span style="color: #008080;">53</span>        <span style="color: #0000ff;">if</span> (i%<span style="color: #800080;">2</span>==<span style="color: #800080;">0</span><span style="color: #000000;">)
    </span><span style="color: #008080;">54</span> <span style="color: #000000;">       {
    </span><span style="color: #008080;">55</span>        q[i].sta = <span style="color: #0000ff;">true</span><span style="color: #000000;">;
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">       }
    </span><span style="color: #008080;">57</span>        <span style="color: #0000ff;">else</span>
    <span style="color: #008080;">58</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">59</span>        q[i].sta = <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #008080;">60</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">61</span> <span style="color: #000000;">   }
    </span><span style="color: #008080;">62</span>    sort(q,q+<span style="color: #800080;">2</span>*<span style="color: #000000;">n,cmp);
    </span><span style="color: #008080;">63</span>    <span style="color: #0000ff;">int</span> ans = -<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">64</span>    <span style="color: #0000ff;">int</span> cnt = <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">65</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < <span style="color: #800080;">2</span>*n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">66</span> <span style="color: #000000;">   {
    </span><span style="color: #008080;">67</span>        <span style="color: #0000ff;">if</span><span style="color: #000000;"> (q[i].sta)
    </span><span style="color: #008080;">68</span> <span style="color: #000000;">       {
    </span><span style="color: #008080;">69</span>         cnt++<span style="color: #000000;">;
    </span><span style="color: #008080;">70</span> <span style="color: #000000;">       }
    </span><span style="color: #008080;">71</span>        <span style="color: #0000ff;">else</span>
    <span style="color: #008080;">72</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">73</span>         cnt--<span style="color: #000000;">;
    </span><span style="color: #008080;">74</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">75</span>        ans =<span style="color: #000000;"> max(ans,cnt);
    </span><span style="color: #008080;">76</span> <span style="color: #000000;">   }
    </span><span style="color: #008080;">77</span>    printf(<span style="color: #800000;">"</span><span style="color: #800000;">%dn</span><span style="color: #800000;">"</span><span style="color: #000000;">,ans);
    </span><span style="color: #008080;">78</span>   
    <span style="color: #008080;">79</span>    
    <span style="color: #008080;">80</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">81</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">82</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">83</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">84</span> }





View Code






    
    <br></br> 



