---
author: 111qqz
date: 2015-10-27 06:54:00+00:00
draft: false
title: codeforces 589 B - Layer Cake
type: post
url: /2015/10/codeforces589b-layercake/
categories:
- ACM
---










B - Layer Cake


**Time Limit:**6000MS **Memory Limit:**524288KB **64bit IO Format:**%I64d & %I64u


Submit [Status](http://acm.hust.edu.cn/vjudge/contest/view.action?cid=96696#status//B/0) [Practice](http://acm.hust.edu.cn/vjudge/problem/viewProblem.action?id=261053) [CodeForces 589B](http://acm.hust.edu.cn/vjudge/problem/visitOriginUrl.action?id=261053)













Description







Dasha decided to bake a big and tasty layer cake. In order to do that she went shopping and bought _n_ rectangular cake layers. The length and the width of the _i_-th cake layer were _a__i_ and _b__i_ respectively, while the height of each cake layer was equal to one.




From a cooking book Dasha learned that a cake must have a form of a rectangular parallelepiped constructed from cake layers of the same sizes.




Dasha decided to bake the biggest possible cake from the bought cake layers (possibly, using only some of them). It means that she wants the volume of the cake to be as big as possible. To reach this goal, Dasha can cut rectangular pieces out of the bought cake layers. She always cuts cake layers in such a way that cutting lines are parallel to the edges of that cake layer. Dasha isn't very good at geometry, so after cutting out a piece from the original cake layer, she throws away the remaining part of it. Also she can rotate a cake layer in the horizontal plane (swap its width and length).




Dasha wants her cake to be constructed as a stack of cake layers of the same sizes. Each layer of the resulting cake should be made out of only one cake layer (the original one or cut out from the original cake layer).




Help Dasha to calculate the maximum possible volume of the cake she can bake using given cake layers.













Input







The first line contains an integer _n_(1 ≤ _n_ ≤ 4000) -- the number of cake layers that Dasha can use.




Each of the following _n_ lines contains two integer numbers _a__i_ and _b__i_(1 ≤ _a__i_, _b__i_ ≤ 106) -- the length and the width of _i_-th cake layer respectively.













Output







The first line of the output should contain the maximum volume of cake that can be baked using given layers.




The second line of the output should contain the length and the width of the resulting cake. If there are many solutions with maximum possible volume, print any of them.













Sample Input










Input



    
    5<br></br>5 12<br></br>1 1<br></br>4 6<br></br>6 4<br></br>4 6










Output



    
    96<br></br>6 4










Input



    
    2<br></br>100001 900000<br></br>900001 100000










Output



    
    180000000000<br></br>900000 100000
















Hint







In the first example Dasha doesn't use the second cake layer. She cuts 4 × 6 rectangle from the first cake layer and she uses other cake layers as is.




In the second example Dasha cuts off slightly from the both cake layers.







巧妙得利用了set....




注意因为可能有重复元素。。。所以要用multiset...




然后有点喜欢上用pair了hhh




队友是二维bit+熔池过掉的。。。。




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock23.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart23.gif)





    
    <span style="color: #008080;"> 1</span> <span style="color: #008000;">/*</span><span style="color: #008000;">************************************************************************
    </span><span style="color: #008080;"> 2</span> <span style="color: #008000;">    > File Name: code/hust/20151025/BB.cpp
    </span><span style="color: #008080;"> 3</span> <span style="color: #008000;">    > Author: 111qqz
    </span><span style="color: #008080;"> 4</span> <span style="color: #008000;">    > Email: rkz2013@126.com 
    </span><span style="color: #008080;"> 5</span> <span style="color: #008000;">    > Created Time: 2015年10月27日 星期二 14时34分16秒
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
    <span style="color: #008080;">25</span> <span style="color: #0000ff;">#define</span> sec second
    <span style="color: #008080;">26</span> <span style="color: #0000ff;">#define</span> fir first
    <span style="color: #008080;">27</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;">28</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dx4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span>,<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span><span style="color: #000000;">};
    </span><span style="color: #008080;">29</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> dy4[<span style="color: #800080;">4</span>]={<span style="color: #800080;">0</span>,-<span style="color: #800080;">1</span>,<span style="color: #800080;">1</span>,<span style="color: #800080;">0</span><span style="color: #000000;">};
    </span><span style="color: #008080;">30</span> typedef <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    </span><span style="color: #008080;">31</span> typedef <span style="color: #0000ff;">double</span><span style="color: #000000;"> DB;
    </span><span style="color: #008080;">32</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x3f3f3f3f</span><span style="color: #000000;">;
    </span><span style="color: #008080;">33</span> 
    <span style="color: #008080;">34</span> <span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> N=4E3+<span style="color: #800080;">7</span><span style="color: #000000;">;
    </span><span style="color: #008080;">35</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> n;
    </span><span style="color: #008080;">36</span> <span style="color: #000000;">LL mx,cura,curb;
    </span><span style="color: #008080;">37</span> pair<ll,ll><span style="color: #000000;"> a[N];
    </span><span style="color: #008080;">38</span> multiset<ll><span style="color: #000000;"> se;
    </span><span style="color: #008080;">39</span> multiset<ll><span style="color: #000000;"> ::iterator it;
    </span><span style="color: #008080;">40</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;">41</span> <span style="color: #000000;">{
    </span><span style="color: #008080;">42</span> <span style="color: #000000;">  #ifndef  ONLINE_JUDGE 
    </span><span style="color: #008080;">43</span>    freopen(<span style="color: #800000;">"</span><span style="color: #800000;">in.txt</span><span style="color: #800000;">"</span>,<span style="color: #800000;">"</span><span style="color: #800000;">r</span><span style="color: #800000;">"</span><span style="color: #000000;">,stdin);
    </span><span style="color: #008080;">44</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">45</span> 
    <span style="color: #008080;">46</span>    scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%d</span><span style="color: #800000;">"</span>,&<span style="color: #000000;">n);
    </span><span style="color: #008080;">47</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">0</span> ; i < n ; i++<span style="color: #000000;">)
    </span><span style="color: #008080;">48</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">49</span>     scanf(<span style="color: #800000;">"</span><span style="color: #800000;">%lld %lld</span><span style="color: #800000;">"</span>,&a;[i].fir,&<span style="color: #000000;">a[i].sec);
    </span><span style="color: #008080;">50</span>     <span style="color: #0000ff;">if</span> (a[i].fir><span style="color: #000000;">a[i].sec) swap(a[i].fir,a[i].sec);
    </span><span style="color: #008080;">51</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">52</span>    sort(a,a+<span style="color: #000000;">n);
    </span><span style="color: #008080;">53</span>    mx = -<span style="color: #800080;">1</span><span style="color: #000000;">;
    </span><span style="color: #008080;">54</span>    <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = n -<span style="color: #800080;">1</span> ; i >= <span style="color: #800080;">0</span> ; i--<span style="color: #000000;">)
    </span><span style="color: #008080;">55</span> <span style="color: #000000;">   {
    </span><span style="color: #008080;">56</span> <span style="color: #000000;">       se.insert(a[i].sec);
    </span><span style="color: #008080;">57</span>        it =<span style="color: #000000;">se.begin();
    </span><span style="color: #008080;">58</span>        <span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> j = i ; j < n ; j++<span style="color: #000000;">)
    </span><span style="color: #008080;">59</span> <span style="color: #000000;">    {
    </span><span style="color: #008080;">60</span>         LL tmp =a[i].fir*(*it)*(n-<span style="color: #000000;">j);
    </span><span style="color: #008080;">61</span>         <span style="color: #0000ff;">if</span> (tmp><span style="color: #000000;">mx)
    </span><span style="color: #008080;">62</span> <span style="color: #000000;">        {
    </span><span style="color: #008080;">63</span>         mx =<span style="color: #000000;"> tmp;
    </span><span style="color: #008080;">64</span>         cura =<span style="color: #000000;"> a[i].fir;
    </span><span style="color: #008080;">65</span>         curb = *<span style="color: #000000;">it;
    </span><span style="color: #008080;">66</span> <span style="color: #000000;">        }
    </span><span style="color: #008080;">67</span>         it++<span style="color: #000000;">;
    </span><span style="color: #008080;">68</span> <span style="color: #000000;">    }
    </span><span style="color: #008080;">69</span> <span style="color: #000000;">   }
    </span><span style="color: #008080;">70</span>    printf(<span style="color: #800000;">"</span><span style="color: #800000;">%lldn%lld %lldn</span><span style="color: #800000;">"</span><span style="color: #000000;">,mx,curb,cura);
    </span><span style="color: #008080;">71</span>   
    <span style="color: #008080;">72</span>    
    <span style="color: #008080;">73</span> <span style="color: #000000;"> #ifndef ONLINE_JUDGE  
    </span><span style="color: #008080;">74</span> <span style="color: #000000;">  fclose(stdin);
    </span><span style="color: #008080;">75</span>   <span style="color: #0000ff;">#endif</span>
    <span style="color: #008080;">76</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">77</span> }





View Code
























