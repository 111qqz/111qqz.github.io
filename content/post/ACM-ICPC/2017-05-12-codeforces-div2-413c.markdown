---
author: 111qqz
date: 2017-05-12 13:27:36+00:00
draft: false
title: 'codeforces #413  C. Fountains （BIT维护前缀max）'
type: post
url: /2017/05/codeforces-div2-413c/
categories:
- ACM
tags:
- 树状数组
---

[题目链接](http://codeforces.com/contest/799/problem/C)

题意：有２种货币，分别为C和D.给出n种资源的代价和美丽度，每种资源只能用其中一种资源购买。现在拥有货币C的数量是c,拥有货币D的数量是d.然后恰好买２个资源，问最大美丽度，不能的话输出０．

思路：首先显然三种情况。。。CC，CD,DD.

CD直接扫一遍。。重点是CC和DD

一开始思路错掉了。。全程写two pointer wa4...一直调。。

最后恍然大悟。。发现two pointer非常错啊。。。

其实正解也很简单？

<del>先去跑步了orz</del>

只要想办法维护每个代价的最大美丽度就好了(更准确得说，是维护小于等于某代价的最大美丽度)

直接BIT搞。维护一个前缀max...好像很稳啊？

不过我竟然对于BIT能维护前缀max吃了一惊？

以往都是用线段树来做这个操作的...想想大概是。。我把BIT的函数起名叫"Sum"的锅。。。

看起来就只能求Sum。。。。233333

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年05月12日 星期五 20时20分57秒
    File Name :code/codeforces/413/CC.cpp
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
    #define PB push_back
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
    int n,c,d;
    int t[N] ; //for BIT
    vector<pair<int,int> >v[2]; 
    //总的思路是，维护每个代价(或者小于该代价）所对的美丽度的最大值
    //用bit维护一个前缀max
    //
    //
    
    int lowbit( int x)
    {
        return x&(-x);
    }
    void update( int x,int delta)
    {
        for ( int i = x ; i < N ; i+=lowbit(i))  t[i] = max(t[i],delta);
    }
    int query( int x)
    {
        int ret = 0 ;
        for ( int i = x ; i>=1 ; i-=lowbit(i))
    	ret = max(ret,t[i]);
        return ret;
    }
    
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("code/in.txt","r",stdin);
    #endif
        scanf("%d%d%d",&n,&c,&d);
        for ( int i = 1 ; i <= n ; i++)
        {
    	int bea,cost;
    	char opt[3];
    	scanf("%d%d",&bea,&cost);
    	scanf("%s",opt);
    	int id = opt[0]-'C';
    	v[id].PB(MP(cost,bea)); 
        }
    
        sort(v[0].begin(),v[0].end());
        sort(v[1].begin(),v[1].end()); //按照cost 排序
    
        //CD
        int ans1,ans2;
        ans1=ans2=0;
        int siz0 = v[0].size();
        for ( int i = 0 ; i < siz0 ; i++)
        {
    	if (v[0][i].fst>c) break;
    	ans1 = max(ans1,v[0][i].sec);
        }
        int siz1 = v[1].size();
        for ( int i = 0 ; i < siz1 ;  i++)
        {
    	if (v[1][i].fst>d) break;
    	ans2 = max(ans2,v[1][i].sec);
        }
        int ans = 0 ;
        if (ans1&&ans2) ans = ans1+ans2;
    
    
        //CC
        ms(t,0);
        for ( int i = 0 ; i  < siz0 ; i++)
        {
    	if (v[0][i].fst>c) break;
    	if (i)
    	{
    	    int tmp = query(c-v[0][i].fst); //我们不关心另一个取哪个，
    	    //只关心剩下的c-v[0][i].fst的coins能取到的最大美丽度。。bit维护一下。。。
    	    if (tmp) ans = max(ans,tmp+v[0][i].sec) ; //只有bit的返回值大于0时，才表示可以取。。
    	}
    	update(v[0][i].fst,v[0][i].sec);
        }
    
        //DD
        ms(t,0);
        for ( int i = 0 ; i < siz1 ; i++ )
        {
    	if (v[1][i].fst>d) break;
    	if (i)
    	{
    	    int tmp = query(d-v[1][i].fst);
    	    if (tmp) ans = max(ans,tmp+v[1][i].sec);
    	}
    	update(v[1][i].fst,v[1][i].sec);
        }
        printf("%d\n",ans);
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
    



