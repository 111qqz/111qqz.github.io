---
author: 111qqz
date: 2016-02-03 10:43:16+00:00
draft: false
title: codeforces 107 B. Basketball Team
type: post
url: /2016/02/codeforces-107-b-basketball-team/
categories:
- ACM
tags:
- math
- 概率
---

http://codeforces.com/problemset/problem/107/B


### 题意：有m个部门，每个部分s[i]个人，HW在第h部门，现在要从这m个部门中挑选包括HW在内的n个人去参加比赛，问被挑选的人中有HW的队友（同部门的人）的概率是多少。如果m个部分的人数不够组成n人的球队，输出-1.




### 思路：考虑一般情况。至少有一个队友的情况较多，应该从反面考虑，即没有一个队友的情况。选完HW以后面临的状态是：事件总数为从total(m个部门的人员之和)-1个人中选n-1个的方案数，包含的事件数目为从a(a=total-s[h])中选n-1个人包含的方案数。 可以看出分母相同，可以约掉。


然后对于边界情况，首先判断total是否比n小。然后，如果a<n-1,表示除去HW所在的h部分之外的人不可能组成n-1个人，也就是一定要选择HW的队友，概率为1.







    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年02月03日 星期三 17时56分30秒
    File Name :code/cf/problem/107B.cpp
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
    const int M=1E3+7;
    int n ,m,h;
    int s[M];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n>>m>>h;
    	for ( int i = 1 ; i <= m ; i++) cin>>s[i];
    
    	double total = 0;
    	for ( int i =1 ; i <= m ; i++)
    	{
    	    total+=s[i];
    	}
    	if (total<n)
    	{
    	    puts("-1");
    	    return 0;
    	}
    	total--;
    	n--;
    	s[h]--; //减去那个人。
    	double a = total - s[h];
    	double ans = 1.0;
    //	cout<<"total:"<<total<<" a:"<<a<<endl;
    	if (a<n) //s[h]队外的人无法满足剩余的要求。
    	{
    	    puts("1");
    	    return 0;
    	}
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    ans = ans *(a*1.0/total*1.0);
    //	    cout<<"ans:"<<ans<<endl;
    	    a--;
    	    total--;
    	}
    	printf("%.10f",1-ans);
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



