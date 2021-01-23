---
author: 111qqz
date: 2016-02-22 09:13:55+00:00
draft: false
title: nthu 10925 - Advanced Heap Sort
type: post
url: /2016/02/nthu-10925-advanced-heap-sort/
categories:
- ACM
tags:
- greedy
---

http://140.114.86.238/problem/10925/
Description
有兩個序列S1和S2，各有N個元素。當我們在S1,S2各取一個數字時，總共會有N*N這麼多可能的”和”(sum)。請找出這N*N這麼多和裡最小的N個值，並將它們加總後輸出。

Input
只有一筆測資。

    測試資料第一行為一個正整數N。

    第二行有N個數字，以空白隔開，代表序列S1。

    第二行有N個數字，以空白隔開，代表序列S2。

 數字範圍：

0 < N < 10000

Output
輸出一行，N個最小的可能的和的加總。

Sample Input
5
1 3 5 7 9
2 4 6 8 10

EOF
Sample Output
27 
EOF


思路：贪心。先分别升序排列，枚举第一个数组，当枚举到第i个的时候，第二个数组的int(n*1.0/i+0.5)显然都没用。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年02月22日 星期一 16时26分18秒
    File Name :yzy.cpp
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
    #define pi pair < int ,int >
    #define MP make_pair
    
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    const int N=1E4+7;
    int n;
    int a[N];
    int b[N];
    int ans[N];
    multiset<int>se;
    multiset<int>::iterator it;
    int main()
    {//	#ifndef  ONLINE_JUDGE 
    //	freopen("code/in.txt","r",stdin);
    //  #endif
    
    	scanf("%d",&n);
    	for  ( int i = 1 ; i <= n ; i++)
    	{
    	    scanf("%d",&a[i]);
    	}
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    scanf("%d",&b[i]);
    	}
    	sort(a+1,a+n+1);
    	sort(b+1,b+n+1);
    
    //	for ( int i = 1 ; i <= n ; i++) cout<<a[i]<<" "<<b[i]<<endl;
    
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    for ( int j = 1 ; j <= ceil(n*1.0/i) ; j++)
    		se.insert(a[i]+b[j]);
    	}
    
    	LL sum = 0 ;
    	int cnt = 0 ;
    	for ( it = se.begin() ; it !=se.end() ;it++)
    	{
    	    sum += *it;
    	 //   cout<<"*it:"<<*it<<endl;
    	    cnt++;
    	    if (cnt>=n) break;
    	}
    	cout<<sum<<endl;
    	
    
    
    		
    
    
    
        return 0;
    }
    



