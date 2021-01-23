---
author: 111qqz
date: 2015-12-04 06:11:13+00:00
draft: false
title: 'codeforces #edu 1 A tricky sum'
type: post
url: /2015/12/codeforces-edu-1-a-tricky-sum/
categories:
- ACM
---

题意：求1+2+..+n的和。。但是对于是2的整数幂的项数。。符号是-。。

思路：可以先当做正数。(n+1)*n/2; 然后减去二倍的2的整数次幂的项的和。

坑点： 妈蛋第三次了。。。我想求小于等于n的最大是2的几次幂。。。取整的时候用int又会迷之错误。。。为什么说是迷之错误。。因为我WA的点的数据拿下来在本地跑是没有问题的。。。一交上去就错。。。不明觉厉。。。下次遇到double类型是数一点要小心小心再小心。。。第一次遇到是pow的返回类型是double，然后答案莫名奇妙的差1.第二次是#334 div2 的A题。。一道傻逼算分数的题我WA了一个小时。。。第三次是这个。。向下取整不要用（int）的强制转换。。而用floor吧。。233

 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月03日 星期四 16时46分46秒
    File Name :code/cf/edu/A.cpp
    ************************************************ */
    
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #define fst first
    #define sec second
    #define lson l,m,rt<<1
    #define rson m+1,r,rt<<1|1
    #define ms(a,x) memset(a,x,sizeof(a))
    typedef long long LL;
    
    
    
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    LL n;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	int T;
    	scanf("%d",&T);
    	while (T--)
    	{
    	    LL sum = 0 ;
    	    cin>>n;
    	    LL k = LL(floor(log(n)/log(2)));
    	   // cout<<"k:"<<k<<endl;
    	    k =(1<<(k+1))-1;
    	 //   cout<<"kk:"<<k<<endl;
    	    sum = sum-2*k;
    	  //  cout<<"sum:"<<sum<<endl;
    	    s`um = sum + (n+1)*n/2;
    	    cout<<sum<<endl;
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



