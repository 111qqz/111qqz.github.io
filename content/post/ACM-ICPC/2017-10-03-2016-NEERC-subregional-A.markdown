---
author: 111qqz
date: 2017-10-03 03:58:13+00:00
draft: false
title: 2016 NEERC  Northern Subregional Contest  A Anniversary Cake （水题）
type: post
url: /2017/10/2016-NEERC-subregional-A/
categories:
- ACM
---

# 题意：



W_H的方格纸，共有(w+1)_(H+1)个整点，现在将2个蜡烛放在2个不同的整点上。蜡烛不会被放在边界上。现在给出方格纸的尺寸和2个蜡烛的坐标，求一条线段将方格纸拆成2部分，而且这条线段不经过任何一个蜡烛且使得每一部分恰好有一个蜡烛。问线段的起点和终点。



# 思路：



为了方便讨论，我们将x坐标小的设为蜡烛1，另一个设为蜡烛2.

分两种情况讨论，即横坐标相同和不同2种情况。

需要注意的是...要交文件orz


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年10月02日 星期一 12时34分38秒
    File Name :A.cpp
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
    LL w,h,ax,ay,bx,by;
    int main()
    {
        freopen("anniversary.in","r",stdin);
        freopen("anniversary.out","w",stdout);
        cin>>w>>h>>ax>>ay>>bx>>by;
        if (ax>bx)
        {
            swap(ax,bx);
            swap(ay,by);
        }
        if (ax!=bx)
        {
            printf("%lld %lld %lld %lld\n",ax,0LL,ax+1,h);
        }
        else
        {
            LL my = min(ay,by);
            printf("%lld %lld %lld %lld\n",0LL,my,w,my+1);
        }
    
        return 0;
    }
    








