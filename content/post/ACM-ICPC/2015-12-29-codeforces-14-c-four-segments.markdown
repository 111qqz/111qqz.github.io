---
author: 111qqz
date: 2015-12-29 09:29:57+00:00
draft: false
title: codeforces 14 C. Four Segments
type: post
url: /2015/12/codeforces-14-c-four-segments/
categories:
- ACM
tags:
- 细节题
- 计算几何
---

http://codeforces.com/problemset/problem/14/C
题意：给出四条边的坐标，问能否形成一个边与坐标轴平行的矩形。边可能退化成点。
思路：首先第一步，检查有没有边退化成点以及是否有不平行的边。

第二步，检查两个方向的边是否各有两条。。

第三步，将所有点的坐标排序。。然后看8个点是否会因为重合而变成4个.。



    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月29日 星期二 16时28分28秒
    File Name :code/cf/problem/14C.cpp
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
    int a,b,c,d;
    int l[10];
    int cnt;
    
    
    
    struct point 
    {
        int x,y;
        
        bool operator <(point p)const
        {
    	if (x<p.x) return true;
    	if (x==p.x&&y<p.y) return true;
    	return false;
        }
        bool ok (point p)
        {
    	if (x!=p.x&&y!=p.y) return false; //不平行
    	if (x==p.x&&y==p.y) return false; //退化成一点
    	if (x==p.x) cnt++;
    	return true;
        }
    
        bool operator ==(point p)const
        {
    	return x==p.x&&y==p.y;
        }
        bool operator !=(point p)const
        {
    	if (x!=p.x||y!=p.y) return true;
    	return false;
        }
    }p[10];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	
    	bool ok=true;
    	cnt =  0 ;
    	for ( int i = 0 ; i < 4 ; i++)
    	{
    	    cin>>p[i].x>>p[i].y>>p[i+4].x>>p[i+4].y;
    	    if (!p[i].ok(p[i+4]))
    	    {
    		ok = false;
    	    }
    	}
    	if (!ok||cnt!=2)
    	{
    	    puts("NO");
    
    	}
    	else
    	{
    	    sort(p,p+8);
    	    if (p[0]==p[1]&&p[2]==p[3]&&p[4]==p[5]&&p[6]==p[7]&&p[0]!=p[2]&&p[2]!=p[4]&&p[4]!=p[6]) //两两重合后保证四个点
    	    {
    		puts("YES");
    	    }
    	    else
    	    {
    		puts("NO");
    	    }
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



