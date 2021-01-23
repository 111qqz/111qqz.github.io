---
author: 111qqz
date: 2015-10-22 02:02:00+00:00
draft: false
title: zoj  3625 D - Geek's Collection(正项无穷级数，麦克劳林展开式，2015年10月AC)
type: post
url: /2015/10/zoj3625d-geekscollection201510ac/
categories:
- ACM
---




D - Geek's Collection


**Time Limit:**2000MS **Memory Limit:**65536KB **64bit IO Format:**%lld & %llu


Submit [Status](http://acm.hust.edu.cn/vjudge/contest/view.action?cid=95597#status//D/0)













Description







The word geek is a slang term, with different meanings ranging from "a computer expert or enthusiast" to "a carnival performer who performs sensationally morbid or disgusting acts", with a general pejorative meaning of "a peculiar or otherwise dislikable person, especially one who is perceived to be overly intellectual".




The definition of geek has changed considerably over time, and there is no longer a definitive meaning. The terms nerd, gimp, dweeb, dork, spod and gump have similar meanings as geek, but many choose to identify different connotations among these terms, although the differences are disputed. In a 2007 interview on The Colbert Report, Richard Clarke said the difference between nerds and geeks is "geeks get it done." Julie Smith defined a geek as "a bright young man turned inward, poorly socialized, who felt so little kinship with his own planet that he routinely traveled to the ones invented by his favorite authors, who thought of that secret, dreamy place his computer took him to as cyberspace somewhere exciting, a place more real than his own life, a land he could conquer, not a drab teenager's room in his parents' house."The definition of geek has changed considerably over time, and there is no longer a definitive meaning. The terms nerd, gimp, dweeb, dork, spod and gump have similar meanings as geek, but many choose to identify different connotations among these terms, although the differences are disputed. In a 2007 interview on The Colbert Report, Richard Clarke said the difference between nerds and geeks is "geeks get it done." Julie Smith defined a geek as "a bright young man turned inward, poorly socialized, who felt so little kinship with his own planet that he routinely traveled to the ones invented by his favorite authors, who thought of that secret, dreamy place his computer took him to as cyberspace somewhere exciting, a place more real than his own life, a land he could conquer, not a drab teenager's room in his parents' house."




The biggest geek in the world named Alice, she is major in many subject. One day she come to a new planet named wonderland and she find a way to entertain herself by copy herself again and again, she give the cloning the name as Alice1, Alice2, Alice3... Every Alice like collect things in wonderland, recently, the true Alice want to calculate how many collections did her cloning have.




The number of collections that each cloning have is (1+1/2+1/3+1/4+...+1/n-ln n)*her special number (n tends to infinity), the defination of special number is as follow, for Alice1, her special number is a, for Alice2, her special number is a(a-1)/(1*2), for Alice3, her special number is a(a-1)(a-2)/(1*2*3)... and there are endless cloning Alice. Your task is to help true Alice c啊alculate how many collections did her cloning have.













Input







This problem contains multiple test cases. Each case contains only one line with a float number a. (-1 < a < 0 or a > 0)













Output







Print exactly one line with the number of total collections, you should output it in scientific notation and retained thirteen significant figures. Because the wonderland is an amazing place so that the number of the collection can be negative number.













Sample Input






    
    -0.5
    100
    













Sample Output-1.690625540426e-01






    
    7.317077840736e+29<br></br><br></br>这题。。。<br></br>先是利用正项无穷级数的知识。。。那个数列的和当n趋近于无穷时趋近于欧拉常数r<br></br>再根据（1+x）<sup>y   的展开式。。。<br></br></sup>然后这道题的数据加强了。<br></br>网上能找到的那份AC代码以及适牛以前AC的代码现在都没办法通过了2333<br></br><img src="https://111qqz.com/wp-content/uploads/2015/11/690628-20151022100129942-451522011.png" alt=""></img><br></br><br></br>注意的地方一个是要用long double<br></br><span style="font-size: 16px;">而且要记得将得到long double变量的每一步计算结果强制转化成long double !!!<br></br><span style="font-size: 14px;"><br></br>大概类似如果变量是long long类型。。。int不强制转化的话有可能爆掉一样。<br></br>不会这个是爆精度。。<br></br>不过还有一个地方我不是很明白：<br></br><br></br></span></span>



    
    <span class="sh-comment">//printf("%.12en",ans);
    	cout<span class="sh-symbol"><<<span class="sh-function">setprecision<span class="sh-symbol">(<span class="sh-number">12<span class="sh-symbol">)<<<span class="sh-function">setiosflags<span class="sh-symbol">(ios<span class="sh-symbol">::scientific<span class="sh-symbol">)<<ans<span class="sh-symbol"><<endl<span class="sh-symbol">;</span></span></span></span></span></span></span></span></span></span></span></span><br></br><br></br>这两种写法有什么区别？注释掉的写法会WA 问了很多人也没有结果。如果有人知道麻烦指教以下，不胜感激。<br></br><br></br>



    
    <span style="font-size: 16px;"><span style="font-size: 14px;"> </span></span>




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock34.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart34.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/zoj/3625.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月21日 星期三 16时53分36秒
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
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span>  <span style="color: #0000ff;">double</span> r=  <span style="color: #800080;">0.57721566490153286060651209</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span>   <span style="color: #0000ff;">double</span><span style="color: #000000;"> a;
    </span><span style="color: #008080;">33</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">34</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">35</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE
    </span><span style="color: #008080;">36</span> <span style="color: #008000;">//</span><span style="color: #008000;">   freopen("in.txt","r",stdin);</span>
    <span style="color: #008080;">37</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">38</span> 
    <span style="color: #008080;">39</span> 
    <span style="color: #008080;">40</span>     <span style="color: #0000ff;">while</span> (scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%lf</span><span style="color: #800000;">"</span>,&a;)!=<span style="color: #000000;">EOF)
    </span><span style="color: #008080;">41</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">42</span>       <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">double</span> ans = (<span style="color: #0000ff;">long</span> <span style="color: #0000ff;">double</span> )pow(<span style="color: #800080;">2.0</span>,a) - (<span style="color: #0000ff;">long</span> <span style="color: #0000ff;">double</span>)<span style="color: #800080;">1.0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">43</span>       ans = ans *<span style="color: #000000;"> r;
    </span><span style="color: #008080;">44</span>     <span style="color: #008000;">//</span><span style="color: #008000;">printf("%.12en",ans);</span>
    <span style="color: #008080;">45</span>     cout<<setprecision(<span style="color: #800080;">12</span>)<<setiosflags(ios::scientific)<<ans<<<span style="color: #000000;">endl;
    </span><span style="color: #008080;">46</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">47</span> 
    <span style="color: #008080;">48</span> 
    <span style="color: #008080;">49</span> 
    <span style="color: #008080;">50</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE
    </span><span style="color: #008080;">51</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">52</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">53</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">54</span> }





View Code






    
     









