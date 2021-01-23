---
author: 111qqz
date: 2015-08-23 08:13:00+00:00
draft: false
title: 'codeforces # 317 div 2 B. Order Book（模拟）'
type: post
url: /2015/08/codeforces317div2b-orderbook/
categories:
- ACM
tags:
- 模拟
---




B. Order Book







time limit per test


2 seconds







memory limit per test


256 megabytes







input


standard input







output


standard output










In this task you need to process a set of stock exchange orders and use them to create order book.




An order is an instruction of some participant to buy or sell stocks on stock exchange. The order number _i_ has price _p__i_, direction _d__i_ -- buy or sell, and integer _q__i_. This means that the participant is ready to buy or sell _q__i_ stocks at price _p__i_ for one stock. A value _q__i_ is also known as a volume of an order.




All orders with the same price _p_ and direction _d_ are merged into one aggregated order with price _p_ and direction _d_. The volume of such order is a sum of volumes of the initial orders.




An order book is a list of aggregated orders, the first part of which contains sell orders sorted by price in descending order, the second contains buy orders also sorted by price in descending order.




An order book of depth _s_ contains _s_ best aggregated orders for each direction. A buy order is better if it has higher price and a sell order is better if it has lower price. If there are less than _s_ aggregated orders for some direction then all of them will be in the final order book.




You are given _n_ stock exhange orders. Your task is to print order book of depth _s_ for these orders.










Input




The input starts with two positive integers _n_ and _s_ (1 ≤ _n_ ≤ 1000, 1 ≤ _s_ ≤ 50), the number of orders and the book depth.




Next _n_ lines contains a letter _d__i_ (either 'B' or 'S'), an integer _p__i_ (0 ≤ _p__i_ ≤ 105) and an integer _q__i_ (1 ≤ _q__i_ ≤ 104) -- direction, price and volume respectively. The letter 'B' means buy, 'S' means sell. The price of any sell order is higher than the price of any buy order.










Output




Print no more than 2_s_ lines with aggregated orders from order book of depth _s_. The output format for orders should be the same as in input.










Sample test(s)










input



    
    6 2<br></br>B 10 3<br></br>S 50 2<br></br>S 40 1<br></br>S 50 6<br></br>B 20 4<br></br>B 25 10










output



    
    S 50 8<br></br>S 40 1<br></br>B 25 10<br></br>B 20 4
















Note




Denote (x, y) an order with price _x_ and volume _y_. There are 3 aggregated buy orders (10, 3), (20, 4), (25, 10) and two sell orders (50, 8), (40, 1) in the sample.




You need to print no more than two best orders for each direction, so you shouldn't print the order (10 3) having the worst price among buy orders.







昨天头疼。。然后觉得要掉。。就用小号打的。。。




结果涨了２００＋rating。。。。




这题就是纯模拟啊。。。




一遍ac。。。




需要注意的地方，如果说有。。。




大概就是，sell的是取最小的s个，要先从小到大排序。。。但是输出的时候又是从大到小排序。。。




昨天４０分钟做完前2道题。。然后c题不会搞。。。就水群（求不鄙视> <），好像一堆人wa　b　wa得特别惨的样子。。。


 

    
    /*************************************************************************
    	> File Name: code/cf/#317/B.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月23日 星期日 00时30分51秒
     ************************************************************************/
    #include<iostream>
    #include<iomanip>
    #include<cstdio>
    #include<algorithm>
    #include<cmath>
    #include<cstring>
    #include<string>
    #include<map>
    #include<set>
    #include<queue>
    #include<vector>
    #include<stack>
    #include<cctype>
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define ms(a,x) memset(a,x,sizeof(a))
    #define lr dying111qqz
    using namespace std;
    #define For(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef double DB;
    const int inf = 0x3f3f3f3f;
    const int N=1E5+7;
    struct Q
    {
        int val;
        int num;
        int id;
    }b[N],s[N],ans[N];
    int id[N];
    int id2[N];
    int n,ss;
    bool cmp(Q a,Q b)
    {
        if (a.val<b.val)
    	return true;
        return false;
    }
    bool cmp2(Q a,Q b)
    {
        if (a.val>b.val) return true;
        return false;
    }
    int main()
    {
      #ifndef  ONLINE_JUDGE 
        freopen("in.txt","r",stdin); 
      #endif
        cin>>n>>ss;
        int x,y;
        char order;
        ms(b,0);
        ms(s,0);
        ms(id,0);
        ms(id2,0);
        int cntA=0,cntB= 0 ;
        for ( int i  = 0  ; i < n ; i++){
    	cin>>order>>x>>y;
    	if (order=='B'){
    	    if (id[x]==0)
    	    {
    		cntA++;
    		id[x] = cntA;
    	    }
    	    b[id[x]].num = b[id[x]].num + y;
    	    b[id[x]].val = x;
    	    b[id[x]].id = id[x];
    	}
    	else
    	{
    	    if (id2[x]==0)
    	    {
    		cntB++;
    		id2[x] = cntB;
    	    }
    	    s[id2[x]].num = s[id2[x]].num+y;
    	    s[id2[x]].val = x;
    	    s[id2[x]].id = id2[x];
    	}
        }
        sort(s+1,s+cntB+1,cmp);
        sort(b+1,b+cntA+1,cmp2);
        cntA = min(cntA,ss);
        cntB = min(cntB,ss);
        ms(ans,0);
        for ( int i = 1 ; i <= cntB ; i++){
    	ans [i].val = s[i].val;
    	ans[i].num = s[i].num;
        }
        sort(ans+1,ans+cntB+1,cmp2);
        for ( int i = 1; i <= cntB ; i++){
    	cout<<"S "<<ans[i].val<<" "<<ans[i].num<<endl;
        }
        ms(ans,0);
        for ( int i =  1 ; i <= cntA ; i++){
    	ans[i].val = b[i].val;
    	ans[i].num = b[i].num;
        }
        sort(ans+1,ans+cntA+1,cmp2);
        for ( int i = 1 ; i <= cntA ; i++){
    	cout<<"B "<<ans[i].val<<" "<<ans[i].num<<endl;
        }
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



