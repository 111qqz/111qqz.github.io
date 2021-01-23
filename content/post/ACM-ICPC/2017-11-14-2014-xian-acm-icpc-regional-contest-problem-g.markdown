---
author: 111qqz
date: 2017-11-14 12:45:08+00:00
draft: false
title: 2014 Xi'An ACM-ICPC Regional Contest Problem G. The Problem to Slow Down You
  (回文自动机(模块化写法))
type: post
url: /2017/11/2014-xian-acm-icpc-regional-contest-problem-g/
categories:
- ACM
tags:
- 回文自动机
---

http://codeforces.com/gym/100548



# 题意：



切换面板：标签
标签
添加新标签
￼
回文自动机、 给2个字符串，问2个字符串中，相等并且都是回文串的对数。



# 思路：



构建2个PAM.然后奇偶起点分别跑dfs即可。

PAM写成了模块化的形式orz


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年11月14日 星期二 20时22分15秒
    File Name :G.cpp
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
    const int N=2E5+7;
    struct PAM
    {
        struct state
        {
        int fail,cnt,len;
        int nxt[26];
        }st[N];
        char S[N],RS[N];
        int n,now,sz;
        void init()
        {
        ms(st,0);
        st[0].fail = st[1].fail = 1;
        st[1].len = -1;
        sz = 1;
        }
        void extend(int c,int pos)  
        {
        int p = now;
        while (S[pos-st[p].len-1]!=S[pos]) p = st[p].fail;
        if (!st[p].nxt[c]){
            int np=++sz,q=st[p].fail;
            st[np].len=st[p].len+2;
            while (S[pos-st[q].len-1]!=S[pos]) q=st[q].fail;
            st[np].fail=st[q].nxt[c];
            st[p].nxt[c] = np;
        }
        now=st[p].nxt[c];
        st[now].cnt++;
        }
        void Cnt()
        {
        for ( int i = sz ; i >= 2;  i--) st[st[i].fail].cnt += st[i].cnt;
        }
        void build ()
        {
        init();
        int len = strlen(S+1);
        for ( int i = 1 ; i <= len ; i++) extend(S[i]-'a',i);
        }
    }A,B;
    
    LL ans;
    void dfs( int x,int y)
    {
      //  printf("x:%d y:%d\n",x,y);
        for ( int i = 0 ; i < 26 ; i++)
        {
        int u = A.st[x].nxt[i];
        int v = B.st[y].nxt[i];
        if (u&&v)
        {
            ans = ans + 1LL*A.st[u].cnt * B.st[v].cnt;
          //  printf("u:%d  v:%d ans:%lld\n",u,v,ans);
            dfs(u,v);
        }
        }
    }       
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
    #endif 
        int T,cas = 0 ;
        cin>>T;
        while (T--)
        {
        scanf("%s %s",A.S+1,B.S+1);
    //  cout<<A.S<<"  "<<B.S<<endl;
        A.build();
        B.build();
        A.Cnt();
        B.Cnt();
        ans = 0 ;
        dfs(0,0) ;
        dfs(1,1) ; //奇偶起点
        printf("Case #%d: %lld\n",++cas,ans);
        }
    
    
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
    
