---
author: 111qqz
date: 2015-12-04 13:25:05+00:00
draft: false
title: 'codeforces #327 B Rebranding'
type: post
url: /2015/12/codeforces-327-b-rebranding/
categories:
- ACM
tags:
- 字符串
---

http://codeforces.com/contest/591/problem/B

题意：给定一个字符串。给出m组替换。对于某一组替换，给出x,y。将字符串中所有的字符x换成y，所有的字符y换成x.
字符串仅包含英文小写字母。

思路： 可以用一个char 到 char 的map 初始映射本身。。 然后进行m次修改。。**需要注意的是，每一次修改要修改全部。。因为当进行完i次修改而要进行i+1次修改的时候。。value值为x的可能不止一个。。所以要从a到z都扫一遍。。**





    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月04日 星期五 19时13分12秒
    File Name :code/cf/#327/B.cpp
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
    const int N=2E5+7;
    char st[N];
    
    int n,m;
    char x,y;
    map<char,char>mp;
    
    
    int main()
    {
        freopen("code/in.txt","r",stdin);
        mp.clear();
        for ( int i = 0 ; i < 26 ; i++)
        {
    	char tmp = char(i+97);
    	mp[tmp] = tmp;
        }
    
        scanf("%d %d",&n,&m);
        scanf("%s",st);
        getchar();
        while (m--)
        {
    	char x,y;
    	scanf("%c %c",&x,&y);
    	getchar();
    	for ( int i = 0 ; i < 26 ; i ++)
    	{
    	    char tmp = char(i+97);
    	    if (mp[tmp]==x) mp[tmp]=y;
    	    else if (mp[tmp]==y) mp[tmp] = x;
    	}
        }
        for ( int i = 0 ; i < n ;i++)
        {
    	printf("%c",mp[st[i]]);
        }
        return 0;
    }
    



