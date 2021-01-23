---
author: 111qqz
date: 2017-11-08 12:16:05+00:00
draft: false
title: spoj nsubstr Substrings (后缀自动机 模板题)
type: post
url: /2017/11/spoj-nsubstr/
categories:
- ACM
tags:
- 后缀自动机
---

http://www.spoj.com/problems/NSUBSTR/en/



# 题意：



f[i]指长度为i的串出现次数的最大值。这里的不同出现指，可以有重复串，只要起始位置不同就视为不同的出现。

求f[1]..f[lenth]。



# 思路：



我们知道，SAM上的节点是right集合的等价类。

一个子串的right集合是指在一个母串中，某个子串所有出现位置的右端点的集合。

如果两个子串的right集合完全相同，那么就可以归结为同一个节点，也就是说这两个子串对于SAM是等价的。

因为在SAM上，这两个子串后，添加若干字符得到的后缀都是一样的。

所以一个SAM节点的个数，就是right集合等价类的个数（如果不考虑初始状态）

对于SAM某一个节点，其能表示的子串有一个范围，设为[MIN,MAX]

SAM的一个节点能表示的子串的含义是说，这些子串的right集合相同。

而一个子串出现的次数就是其right集合的大小。

考虑SAM上的某个节点，其表示的长度区间在[MIN,MAX]的子串都出现了|right|次

如果我们直接从MIN更新到MAX有点太暴力了，实际上这里我们可以只更新f[MAX]

由于长度i-1的子串出现的次数一定大于等于长度为i的子串出现的次数，所以最后长度从大到小更新f即可。

现在的问题就变成了如何求right集合。

实际上我们不需要知道right集合的具体组成，只需要知道right集合的大小。

考虑一棵parent树，树上某个节点的right集合就是该节点的所有儿子节点的right集合的并集

因此我们只需要在parent上自低向上更新right集合的大小就可以了。

如何保证在parent树上是自底向上更新呢？

我们只需要按照len,也就是SAM中所有节点能表示的子串的MAX值从大到小的顺序更新right集合。

原因是parent树上，儿子的len一定比父亲的len长。

注意到，对于parent树上的叶子节点，其right集合是1，这也是我们的初始状态。

部分实现细节见代码注释。

关于SAM的详细学习笔记日后补

20171109Update:

**注释写错了一处，a[1]应该是len最短的状态的标号，之前写成了最长的。**


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年11月08日 星期三 18时50分18秒
    File Name :nsubstr.cpp
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
    int Right[2*N]; //right[i]表示第i个状态的right集合大小
    int sz, last,rt;
    char s[N];
    int cnt[2*N],a[2*N];//for radix sort
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
    int f[N]; //答案
    int main()
    {
        #ifndef  ONLINE_JUDGE 
    //  freopen("./in.txt","r",stdin);
      #endif
        sa_init();
        ms(f,0);
        ms(Right,0);
        scanf("%s",s+1);
        int len = strlen(s+1);
        for ( int i = 1 ; i <= len ; i++)
        {
            Right[sz+1] = 1; //初始化right集合的大小
            sa_extend(s[i]-'a');
        }
        //  a simple radix sort
        for (int i = 1 ; i <= sz ; i++) cnt[st[i].len]++;
        for ( int i = 1 ; i <= len ; i++) cnt[i]+=cnt[i-1];
        for (int i = 1 ; i <= sz  ;i++) a[cnt[st[i].len]--] = i;
        //将len按照从大到小的顺序存入临时数组a，a[1]表示len最*短*的状态的标号。
    
        for ( int i = sz ; i >= 1 ; i--) Right[st[a[i]].link]+=Right[a[i]]; 
        //按照len从大到小的顺序更新right集合。
        //考虑一棵parent树，某个状态的right集合就是其就是其所有儿子节点的并集。
        //我们对parent树自底向上更新，由于儿子的len一定比父亲的len长，所以自底向上更新也就是按照len从大到小更新
        //
        //
        for ( int i = rt ; i <= sz ; i++) f[st[i].len] = max(f[st[i].len],Right[i]) ; 
        //长度为st[i].len的字符串出现了right[i]次
        
        for ( int i = len ; i >= 1 ; i--) f[i] = max(f[i],f[i+1]);
        //由于我们之前对于一个状态，只是更新了其表示的子串中长度最长的那个(也就是st[i].len)
        //但实际上每个状态表示的子串的长度是在区间[st[st[i].link]+1,st[i].len]
        //这个状态表示的每一个长度在该区间中的子串实际上都出现了right[i]次
        //我们只更新了最大，所以最后要倒序更新一下。
        //这样做的正确性在于，长度i-1的子串出现的次数一定大于等于长度为i的子串出现的次数。
        for ( int i = 1 ; i <= len ; i++) printf("%d\n",f[i]);
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    










