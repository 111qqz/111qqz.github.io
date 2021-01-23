---
author: 111qqz
date: 2017-10-31 16:31:10+00:00
draft: false
title: hdu 6043 | 2017 Multi-University Training Contest - Team 1 K KazaQ's Socks  （循环节）
type: post
url: /2017/11/hdu-6043/
categories:
- ACM
tags:
- 循环节
---

http://acm.hdu.edu.cn/showproblem.php?pid=6043



# 题意：



n双袜子标号1到n，初始在抽屉里，每天早晨**穿一双标号最小的袜子**，晚上把脏袜子放到盆里，如果放完之后喷子里已经有了n-1双脏袜子，那么就要洗，然后在第二天晚上放回抽屉里。问第k天穿的是标号为几的袜子。



# 思路：



手写了几个发现对于n双袜子,标号出现的情况是:

1,2,3...n,1,2,3...n-2,n-1,1,2,3...n-2,n

所以特判k<=n的情况然后算循环的次数即可。




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年11月01日 星期三 00时14分38秒
    File Name :6043.cpp
    ************************************************ */
    
    #include <bits/stdc++.h>
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
    LL n,k;
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        //freopen("./in.txt","r",stdin);
      #endif
        int cas = 0 ;
        while (~scanf("%lld %lld",&n,&k))
        {
            printf("Case #%d: ",++cas);
            if (k<=n)
            {
            printf("%lld\n",k);
            continue;
            }
            k-=n;
            LL num = (k-1)/(n-1)+1;
            LL yu = k%(n-1);
            if (yu==0) yu+=n-1;
            if (num%2==1)
            {
            printf("%lld\n",yu);
            }
            else
            {
            if (yu<=n-2) printf("%lld\n",yu);
            else printf("%lld\n",n);
            }
        }
    
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




