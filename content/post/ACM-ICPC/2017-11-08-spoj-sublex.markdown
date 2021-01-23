---
author: 111qqz
date: 2017-11-08 13:15:20+00:00
draft: false
title: SPOJ  SUBLEX   Lexicographical Substring Search （ 后缀自动机）
type: post
url: /2017/11/spoj-sublex/
categories:
- ACM
tags:
- 后缀自动机
---

http://www.spoj.com/problems/SUBLEX/en/



# 题意：



给一个字符串，每次询问字典序第k大的不重复子串。



# 思路：



先做个拓扑dp，求出SAM上，一个状态到种态的路径数。

拓扑dp其实就是按照拓扑序的dp啦...

然后从SAM的初始态开始，每次字典序从小到大得贪心寻找。思想类似可持久化线段树求区间第k大。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年11月08日 星期三 18时50分18秒
    File Name :sublex.cpp
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
    #define MAXALP 26
    
    struct state
    {
        int len, link, nxt[MAXALP];
    };
    const int N =3E5+7;
    state st[N*2];
    int sz, last,rt;
    char s[N];
    int cnt[2*N],a[2*N];//for radix sort
    int sum[2*N]; //表示状态i到终态的路径数
    void sa_init()
    {
        sz = 0;
        last = rt = ++sz;
        st[1].len = 0;
        st[1].link=-1;
        ms(st[1].nxt,-1);
        ms(cnt,0);
    }
    
    void sa_extend(int c)
    {
        int cur = ++sz;
        st[cur].len = st[last].len + 1;
        memset(st[cur].nxt, -1, sizeof(st[cur].nxt));
        int p;
        for (p = last; p != -1 && st[p].nxt[c] == -1; p = st[p].link)
            st[p].nxt[c] = cur;
        if (p == -1) {
            st[cur].link = rt;
        } else {
            int q = st[p].nxt[c];
            if (st[p].len + 1 == st[q].len) {
                st[cur].link = q;
            } else {
                int clone = ++sz ;
                st[clone].len = st[p].len + 1;
                st[clone].link = st[q].link;
                memcpy(st[clone].nxt, st[q].nxt, sizeof(st[q].nxt));
                for (; p != -1 && st[p].nxt[c] == q; p = st[p].link)
                    st[p].nxt[c] = clone;
                st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
    }
    void query( int k) //思想类似可持久化线段树找第k大
    //因为我们注意到，对于某个状态的所有转移，转移是j后得到的状态的所有子串的字典序一定比转移是(j+1)后得到的状态的所有子串的字典序小。
    {
        int now = rt;
        while (k)
        {
        for ( int i = 0 ; i < 26 ; i++)//字典序从小到大寻找，找到的一定是字典序最小的。
            if (st[now].nxt[i]!=-1)
            {
            if (sum[st[now].nxt[i]]>=k)
            {
                putchar(('a'+i));
                k--;
                now = st[now].nxt[i];
                break;
            }
            else k-=sum[st[now].nxt[i]]; //类似权值线段树找第k大
            }
        }
        putchar('\n');
    }
    
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        sa_init();
        ms(sum,0);
        scanf("%s",s+1);
        int len = strlen(s+1);
        for ( int i = 1 ; i <= len ; i++)
        {
            sa_extend(s[i]-'a');
        }
        //  a simple radix sort
        for (int i = 1 ; i <= sz ; i++) cnt[st[i].len]++;
        for ( int i = 1 ; i <= len ; i++) cnt[i]+=cnt[i-1];
        for (int i = 1 ; i <= sz  ;i++) a[cnt[st[i].len]--] = i;
    //  for ( int i = 1 ; i <= sz ; i++) printf("a:%d\n",a[i]);
        //将len按照从大到小的顺序存入临时数组a，a[1]表示len最短的状态的标号
        //
        //
        //从len最长的更新，就是按照拓扑序更新。
        //正确性在于len越大的越靠近SAM上的终止态
        for ( int i = sz ; i >=1 ; i--)
        {
            int num = 0 ;
            for ( int j = 0 ; j < 26 ; j++) if (st[a[i]].nxt[j]!=-1)
            num+=sum[st[a[i]].nxt[j]];
            
            sum[a[i]] = num + 1; //到终态的路径数，等于其能到达的状态到终态的路径数之和sum+该状态到终态的路径数1.
        }
    //  for ( int i = 1 ; i <= sz ; i++) printf("sum:%d\n",sum[i]);
        int q;
        cin>>q;
        while (q--)
        {
            int x;
            scanf("%d",&x);
            query(x);
        }
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




