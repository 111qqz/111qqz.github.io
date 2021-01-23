---
author: 111qqz
date: 2015-12-02 08:54:38+00:00
draft: false
title: 'codeforces #334 div 2 C. Alternative Thinking'
type: post
url: /2015/12/codeforces-334-div-2-c-alternative-thinking/
categories:
- 其他
---

题意：给定一个01串。要进行一次变换：选一段连续的非空的字串，将这段串的0和1反转（0变成1,1变成0）
然后问能得到的最长的0,1交替的序列的长度是多少（不一定连续）

  比赛的时候想出来两种会将答案增加的可能情况。一种是10000001 中间有大于等于3个的连续字符，这样可以把中间反转一下，答案会+2  另外一种是 1001001 这样。。有至少两段的连续两个以上的相同字符被另一个字符隔开的情况。只要将1001001变成1010101。答案还是会+2。。。然后发现这两种情况实际上可以统一起来。即：有至少两段的连续相同字符。
注意000 也算有两段。 如果有两段或者以上，那么答案+2.

 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月02日 星期三 00时36分47秒
    File Name :code/cf/#334/C.cpp
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
    const int N=1E5+7;
    char a[N];
    int n;
    
    char tow(char ch)
    {
        if (ch=='0') return '1';
        if (ch=='1') return '0';
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	
    	scanf("%d",&n);
    	scanf("%s",a);
    	int cnt =  0;
    	for ( int i = 0  ; i < n-1 ; i++) 
    	    if (a[i]==a[i+1])
    		cnt++;
    
        if (cnt>=2) cnt = 2;
        
        char tar = a[0];
    	tar = tow(tar);
    	int ans = 1;
    	for ( int i = 1 ; i < n ; i++ )
    	{
    //	    printf("%d %c\n",i,tar);
    	    if (a[i]==tar)
    	    {
    		ans++;
    		tar = tow(tar);
    	    }
    	}
    	
    	printf("%d\n",ans+cnt);
        
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    






