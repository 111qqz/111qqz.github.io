---
author: 111qqz
date: 2015-09-14 12:22:00+00:00
draft: false
title: 'codeforces #519 A  A. Multiplication Table (暴力)'
type: post
url: /2015/09/codeforces519aa-multiplicationtable/
categories:
- ACM
---
















A. Multiplication Table







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Let's consider a table consisting of _n_ rows and _n_ columns. The cell located at the intersection of _i_-th row and _j_-th column contains number _i_ × _j_. The rows and columns are numbered starting from 1.




You are given a positive integer _x_. Your task is to count the number of cells in a table that contain number _x_.










Input




The single line contains numbers _n_ and _x_ (1 ≤ _n_ ≤ 105, 1 ≤ _x_ ≤ 109) -- the size of the table and the number that we are looking for in the table.










Output




Print a single number: the number of times _x_ occurs in the table.










Sample test(s)










input



    
    10 5










output



    
    2










input



    
    6 12










output



    
    4










input



    
    5 13










output



    
    0
















Note




A table for the second sample test is given below. The occurrences of number 12 are marked bold.


![](https://111qqz.com/wp-content/uploads/2015/11/7396f9adf8eaaf460e1588505b9c25ae438f0e8a.png)









我的内心是崩溃的。。。




20天没写代码。。。




然后这道谁题。。。竟然wa了两次。。。




其实思路是没有错的。。。




然后自作聪明得想优化。。。




把优化去掉就A了。。




慢慢恢复感觉==




哦，光扯了。




这道题很显然。。。x出现的话，在每一行只可能出现0次或1次。。




要同时满足 x%i==0 和 x/i<=n









    
    <span style="color: #008000;">/*</span><span style="color: #008000;">******************************************************************
    Author :111qqz
    ******************************************************************</span><span style="color: #008000;">*/</span><span style="color: #000000;">
    
    #include </span><algorithm><span style="color: #000000;">
    #include </span><cstdio><span style="color: #000000;">
    #include </span><iostream><span style="color: #000000;">
    #include </span><cstring><span style="color: #000000;">
    #include </span><<span style="color: #0000ff;">string</span>><span style="color: #000000;">
    #include </span><cmath><span style="color: #000000;">
    #include </span><map><span style="color: #000000;">
    #include </span><stack><span style="color: #000000;">
    #include </span><queue><span style="color: #000000;">
    #include </span><<span style="color: #0000ff;">set</span>>
    
    <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    typedef </span><span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> LL;
    typedef unsigned </span><span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> ULL;
    </span><span style="color: #0000ff;">const</span> <span style="color: #0000ff;">int</span> inf = <span style="color: #800080;">0x7fffffff</span><span style="color: #000000;">;
    </span><span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    {
        </span><span style="color: #0000ff;">int</span><span style="color: #000000;"> n,x;
        </span><span style="color: #0000ff;">int</span> ans=  <span style="color: #800080;">0</span><span style="color: #000000;">;
        cin</span>>>n>><span style="color: #000000;">x;
        </span><span style="color: #0000ff;">for</span> ( <span style="color: #0000ff;">int</span> i = <span style="color: #800080;">1</span> ; i <= n ; i++<span style="color: #000000;">)
        {
            </span><span style="color: #0000ff;">if</span> (x%i==<span style="color: #800080;">0</span> && x/i<=<span style="color: #000000;">n)
            {
                ans</span>++<span style="color: #000000;">;
            }
        }
        cout</span><<ans<<<span style="color: #000000;">endl;
    
        </span><span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    }</span>





















