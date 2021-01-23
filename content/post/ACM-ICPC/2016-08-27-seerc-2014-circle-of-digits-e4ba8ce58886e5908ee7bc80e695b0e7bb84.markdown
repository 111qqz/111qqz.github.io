---
author: 111qqz
date: 2016-08-27 07:37:23+00:00
draft: false
title: seerc 2014 Circle of digits (二分+后缀数组)
type: post
url: /2016/08/seerc-2014-circle-of-digits-/
categories:
tags:
- binary search
- 后缀数组
---

[题目链接](http://acm.hust.edu.cn/vjudge/contest/130303#problem/B)

题意：把一个长度为n的只由数字构成的串分成k个不为空的字串，使得最大的串最小（大小是说串所对应的十进制数的大小）

思路：由于长度为x的串肯定大于长度为x-1的串，因此很容易想到，我们要尽可能使得k组串的长度尽可能平均（避免出现某一个串的长度非常大的情况）

我们可以知道，最大值的串的长度一定为 LEN=(n+k-1)/k;

而每一组的长度，只可能是LEN或者LEN-1。

然后build_sa

注意循环串的几个地方记得%n

接下来二分sa数组的下标。

二分check的时候，先枚举断点，断环为链。

由于每部分最长的长度为LEN，所以0..LEN-1中一定存在一个断点。

然后贪心，尽可能取LEN

根据rk值来决定某一段的长度是LEN还是LEN-1（如果rk值比当前的大，那么就只能取LEN-1，否则取LEN）

如果此时k段的长度之和超过了n，说明此时的最大值还可能更小。

于是继续二分区间的前一半。

    
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
    char s[N];
    int sa[N],t[N],t2[N],c[N];
    int rk[N],height[N];
    int L;
    int n,k;
    int cmp(int *r,int a,int b,int l){return r[a]==r[b]&&r[(a+l)%n]==r[(b+l)%n];}
    void build_sa(int n,int m)
    {
        int *x = t;
        int *y = t2;
        //ms(cnt,0);
        ms(c,0);
        for ( int i = 0 ; i < n ; i++) c[x[i]=s[i]]++;
        for ( int i = 1 ; i < m ; i++) c[i]+=c[i-1];
        for ( int i = n-1 ; i >= 0 ; i--) sa[--c[x[i]]] = i;
        for ( int k = 1 ; k <= n ; k <<=1)
        {
            int p = 0;
            for ( int i = 0 ; i < n ; i++) if (sa[i]>=k) y[p++] = sa[i]-k;
                                            else y[p++] = n+(sa[i]-k)%n;
            ms(c,0);
            for ( int i = 0 ; i < n ; i++) c[x[y[i]]]++;
            for ( int i = 0 ; i < m ; i++) c[i]+=c[i-1];
            for ( int i = n-1 ; i >=0 ; i--) sa[--c[x[y[i]]]] = y[i];
            swap(x,y);
            p = 1;
            x[sa[0]] = 0 ;
            for ( int i = 1 ; i < n ; i++)
                x[sa[i]] = cmp(y,sa[i-1],sa[i],k)?p-1:p++;
            if (p>=n) break;
            m =  p;
        }
    }
    void getHeight(int n)
    {
        int k = 0;
        for ( int i = 0 ; i < n ; i++) rk[sa[i]] = i ;
        height[0] = 0 ;
        for ( int i = 0 ; i < n ; i++)
        {
            if (rk[i]==0) continue;
            if (k) k--;
            int j = sa[rk[i]-1];
            while (s[i+k]==s[j+k]) k++;
            height[rk[i]] = k;
         }
     }
     int getSuffix(char s[])
     {
         int len = strlen(s);
         int up = 0;
         for ( int i = 0 ; i < len ; i++)
         {
             int val = s[i];
             up = max(up,val);
         }
         build_sa(len,up+1);
         getHeight(len);
         return len;
     }
    bool check( int p)
    {
        cout<<"p:"<<p<<endl;
        p = sa[p];
        for ( int i = 0 ; i < L ; i++)
        {
            int st = i ;
            int ed = st+n-1;
            for ( int j = 0 ; j < k ; j++)
            {
                int tmp = st%n;
                if (rk[tmp]>rk[p])
                    st+=L-1;
                else st+=L;
    //	    cout<<"tmp:"<<tmp<<" rk[tmp]:"<<rk[tmp]<<" st:"<<st<<endl;
                if (st>ed) return true;
            }
        }
        return false;
    }
    void bin()
    {
        int l = 0 ;
        int r = n-1;
        while (l<r)
        {
            int mid = (l+r)/2;
            if (check(mid)) r= mid;
            else l = mid+1;
        }
        int ans = sa[l];
     //   cout<<"L:"<<L<<endl;
        for ( int i = 0 ; i < L ;  i++)
        {
            int v = (ans+i)%n;
            printf("%c",s[v]);
        }
        printf("\n");
    }
    int main()
    {
      freopen("code/in.txt","r",stdin);
      while (scanf("%d%d",&n,&k)!=EOF)
      {
          L = (n+k-1)/k;
        //  cout<<"L:"<<L<<endl;
          scanf("%s",s);
          getSuffix(s);
          bin();
      //   for ( int i = 0 ; i < n ; i++) cout<<"sa[i]:"<<sa[i]<<" rk[i]:"<<rk[i]<<endl;
      }
    return 0;
    }
    





