---
author: 111qqz
date: 2015-12-04 06:54:38+00:00
draft: false
title: codeforces edu1 B Queries on a String
type: post
url: /2015/12/codeforces-edu1-b-queries-on-a-string/
categories:
- ACM
tags:
- 字符串
---

题意：给一个字符串（1E4），然后给m次操作（m<=300），每次操作是给定一个区间l,r，然后进行k次（k<=1E6）cyclic shift (rotation) 变换。


<blockquote>One operation of a cyclic shift (rotation) is equivalent to moving the last character to the position of the first character and shifting all other characters one position to the right.</blockquote>


For example, if the string _s_ is abacaba and the query is _l_1 = 3, _r_1 = 6, _k_1 = 1 then the answer is abbacaa. If after that we would process the query _l_2 = 1, _r_2 = 4, _k_2 = 2 then we would get the string baabcaa.



简单的说。。就是把最后一位移动到第一位，其他位依次往后。

很容易想到，对于一个长度为len的字符串。进行i次变换和进行（i+len）次变换是等价的。

然后直接暴力搞。

offset为偏移量。对于位置i的偏移量为（i-l+len-k）%len,len为每次操作区间的长度。





    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月04日 星期五 14时24分56秒
    File Name :code/cf/edu/B.cpp
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
    const int N=1E4+7;
    
    char st[N];
    int len;
    int m;
    int l,r,k;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	scanf("%s",st);
    	scanf("%d",&m);
    	while (m--)
    	{
    	    scanf("%d %d %d",&l,&r,&k);
    	    l--;
    	    r--; //强行让下标从0开始。。。处理起来方便
    	    int len = r-l+1;
    	    k = k % len;
    	    char tmp[N];
    
    	    for ( int i = l ; i <= r ; i++)
    	    {
    		int offset = (i-l+len-k)%len;
    		tmp[i] = st[offset+l];
    	    }
    	    for ( int i = l; i <= r ; i++) st[i] = tmp[i];
    
    //	    printf("%s\n",st);
    	}
    	printf("%s\n",st);
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



