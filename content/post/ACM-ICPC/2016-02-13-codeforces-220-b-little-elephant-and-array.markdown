---
author: 111qqz
date: 2016-02-13 17:27:22+00:00
draft: false
title: codeforces 220 B. Little Elephant and Array
type: post
url: /2016/02/codeforces-220-b-little-elephant-and-array/
categories:
- ACM
tags:
- 分块
- 莫队算法
---

http://codeforces.com/contest/220/problem/B


## 题意：n个数，m个查询区间，对于每一个区间[l,r]输出区间中cnt[x]==x的数的个数。


思路：首先，a[i]很大。。。但是n最大才1e5...每个a[i]最多出现1E5次。。所以对于大于1E5的a[i]对答案没有贡献。其次，上莫队算法。



    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年02月14日 星期日 00时47分18秒
    File Name :code/cf/problem/220B.cpp
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
    const int N=1E5+7;
    
    int n,m;
    int a[N];
    int pos[N];
    int sum;
    int ans[N];
    int cnt[N];
    
    struct node
    {
        int l,r;
        int id;
    
        bool operator<(node b)const
        {
    	if (pos[l]==pos[b.l]) return r<b.r;
    	return pos[l]<pos[b.l];
        }
    }q[N];
    
    
    void update( int x,int d)
    {
        
        if (a[x]>100000) return;  
        if (cnt[a[x]]==a[x]) sum--;
        cnt[a[x]]+=d;
        if (cnt[a[x]]==a[x]) sum++;
    
      //  cout<<"x:"<<x<<" d:"<<d<<" sum:"<<sum<<endl;
    
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n>>m;
    	ms(pos,-1);
    	ms(cnt,0);
    	int siz = int(sqrt(n));
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    scanf("%d",&a[i]);
    	    pos[i] = (i-1)/siz;
    	}
    
    	for ( int i = 1 ;i  <= m ; i++)
    	{
    	    scanf("%d %d",&q[i].l,&q[i].r);
    	    q[i].id = i ;
    	}
    	sort(q+1,q+m+1);
    
    //	for ( int i = 1 ;i  <= m ; i++) cout<<q[i].l<<" "<<q[i].r<<endl;
    	int pl = 1;
    	int pr = 0;
    	int id,l,r;
    	 sum = 0 ; //不小心又定义了个局部变量2333
    	for ( int i = 1 ; i <= m ; i++)
    	{
    	    id = q[i].id;
    	    l = q[i].l;
    	    r = q[i].r;
    
    	    if (r<pr)
    	    {
    		for ( int j = r+1 ; j <= pr ; j++) update(j,-1);
    	    }
    	    else
    	    {
    		for ( int j = pr +1 ; j <= r ; j++) update(j,1);
    	    }
    
    	    pr = r;
    
    	//   cout<<"sum1:"<<sum<<endl;
    
    	    if (l<pl)
    	    {
    		for ( int j = l ; j <= pl-1 ; j++) update(j,1);
    	    }
    	    else
    	    {
    		for ( int j = pl ; j <= l-1 ; j++) update(j,-1);
    	    }
    
    	    pl = l;
    //	    cout<<"sum2:"<<sum<<endl;
    	    ans[id] = sum;
    
    	//    cout<<endl;
    	}
    
    	for ( int i = 1 ; i <= m ;i ++) printf("%d\n",ans[i]);
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



