---
author: 111qqz
date: 2015-10-04 08:16:00+00:00
draft: false
title: 'codeforces #323 div 2 C. GCD Table (暴力？)'
type: post
url: /2015/10/codeforces323div2c-gcdtable/
categories:
- ACM
---




C. GCD Table







time limit per test


2 seconds







memory limit per test


256 megabytes







input


standard input







output


standard output










The GCD table _G_ of size _n_ × _n_ for an array of positive integers _a_ of length _n_ is defined by formula


![](https://111qqz.com/wp-content/uploads/2015/11/c41174b207b1e8f3f5b51c6c0b2a1a479f9fd5ac.png)



Let us remind you that the greatest common divisor (GCD) of two positive integers _x_ and _y_ is the greatest integer that is divisor of both _x_ and _y_, it is denoted as ![](http://codeforces.com/predownloaded/78/72/78721f5f6c09f3f26ba8570df31de2cac8da3df1.png)
. For example, for array _a_ = {4, 3, 6, 2} of length 4 the GCD table will look as follows:


![](https://111qqz.com/wp-content/uploads/2015/11/306134769278f09384ca40efc6a5d981b18f3bb9.png)



Given all the numbers of the GCD table _G_, restore array _a_.










Input




The first line contains number _n_ (1 ≤ _n_ ≤ 500) -- the length of array _a_. The second line contains _n_2 space-separated numbers -- the elements of the GCD table of _G_ for array _a_.




All the numbers in the table are positive integers, not exceeding 109. Note that the elements are given in an arbitrary order. It is guaranteed that the set of the input data corresponds to some array _a_.










Output




In the single line print _n_ positive integers -- the elements of array _a_. If there are multiple possible solutions, you are allowed to print any of them.










Sample test(s)










input



    
    4<br></br>2 1 2 3 4 3 2 6 1 1 2 2 1 2 3 2










output



    
    4 3 6 2










input



    
    1<br></br>42










output



    
    42 










input



    
    2<br></br>1 1 1 1










output



    
    1 1 <br></br><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">被hack了．．sad．</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">首先可以发现一些结论</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">１：对角线上的数就是原序列</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">２：table关于对角线对称</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">３：出现奇数次数一定是原序列中的数（这个结论并没有用到，不过这是首先能想到的，用到用不到再说）</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">４：gcd(a,b)<=min(a,b)；</span><br></br><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">然后我之前的做法是用一个map统计出现的次数</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">然后遍历map，先把出现奇数的挑出来.算作一个答案．并把次数-1</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">这样所有的都是出现１</span>




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock50.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart50.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/#323/CC.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月04日 星期日 14时51分08秒
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
    </span><span style="color: #008080;">31</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=5E2+<span style="color: #800080;">7</span><span style="color: #000000;">;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">int</span> a[N*<span style="color: #000000;">N];
    </span><span style="color: #008080;">33</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">34</span> map<<span style="color: #0000ff;">int</span>,<span style="color: #0000ff;">int</span>><span style="color: #000000;">mp;
    </span><span style="color: #008080;">35</span> vector<<span style="color: #0000ff;">int</span>><span style="color: #000000;"> ans;
    </span><span style="color: #008080;">36</span> <span style="color: #0000ff;">int</span> gcd(<span style="color: #0000ff;">int</span> a,<span style="color: #0000ff;">int</span> b) { <span style="color: #0000ff;">return</span> b==<span style="color: #800080;">0</span>?a:gcd(b,a%<span style="color: #000000;">b);}
    </span><span style="color: #008080;">37</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">38</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">39</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">40</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">41</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">42</span> <span style="color: #000000;">   mp.clear();
    </span><span style="color: #008080;">43</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">n);
    </span><span style="color: #008080;">44</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n*n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">45</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">46</span>     scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">a[i]);
    </span><span style="color: #008080;">47</span>     mp[a[i]]++<span style="color: #000000;">;
    </span><span style="color: #008080;">48</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">49</span>     sort(a,a+n*<span style="color: #000000;">n);
    </span><span style="color: #008080;">50</span> 
    <span style="color: #008080;">51</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = n*n-<span style="color: #800080;">1</span> ;i>=<span style="color: #800080;">0</span> ; i--<span style="color: #000000;">)
    </span><span style="color: #008080;">52</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">53</span>     <span style="color: #0000ff;">if</span> (!mp[a[i]]) <span style="color: #0000ff;">continue</span><span style="color: #000000;">;
    </span><span style="color: #008080;">54</span>     mp[a[i]]--<span style="color: #000000;">;
    </span><span style="color: #008080;">55</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> j = <span style="color: #800080;">0</span> ; j< ans.size() ; j++<span style="color: #000000;">)
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">57</span>         <span style="color: #0000ff;">int</span> tmp =<span style="color: #000000;"> gcd(a[i],ans[j]);
    </span><span style="color: #008080;">58</span>         mp[tmp]--<span style="color: #000000;">;
    </span><span style="color: #008080;">59</span>         mp[tmp]--<span style="color: #000000;">;
    </span><span style="color: #008080;">60</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">61</span> <span style="color: #000000;">    ans.push_back(a[i]);
    </span><span style="color: #008080;">62</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">63</span>     <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n-<span style="color: #800080;">1</span> ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">64</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%d </span><span style="color: #800000;">"</span><span style="color: #000000;">,ans[i]);
    </span><span style="color: #008080;">65</span>     printf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,ans[n-<span style="color: #800080;">1</span><span style="color: #000000;">]);
    </span><span style="color: #008080;">66</span> 
    <span style="color: #008080;">67</span>   
    <span style="color: #008080;">68</span>    
    <span style="color: #008080;">69</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">70</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">71</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">72</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">73</span> }





View Code









    
    <span style="font-family: 'Microsoft YaHei'; font-size: 16px;">偶数次</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">然后我从大往小加，直到有n个为止（算上之前的奇数次的）</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">错了是因为我想当然得以为...n个数的gcd table 中...对于任意一对gcd(a,b)（a!=b）一定小于等于所有的原始数列的数．．．</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">这显然不对...因为第四点的小于等于关系只是针对某对数的局部结论，而没办法推到整体...想当然了．好傻逼啊．．．</span><br></br><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">正确的做法其实很接近了...</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">由于第四个可以知道...最大的数一定是原始数列中的数...</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">我们可以从已经确定为原始数列的数来排除掉答案．</span><br></br><span style="font-family: 'Microsoft YaHei'; font-size: 16px;">由于对称性...将a[i]排序后从大到小枚举...每个新出现的数和已经确定为原始数列的数为产生一对相等的gcd．．．减掉就可以了．</span><br></br>具体见代码：<br></br><br></br>









