---
author: 111qqz
date: 2016-08-15 13:09:28+00:00
draft: false
title: hdu 4828 Xor Sum (trie 树模板题，经典应用)
type: post
url: /2016/08/hdu-4828-xor-sum-trie-/
categories:
- ACM

tags:
- trie
---

[hdu 4825 题目链接](http://acm.hdu.edu.cn/showproblem.php?pid=4825)

题意：给定n个数，然后给出m个询问，每组询问一个数x，问n中的数y使得x和y的异或和最大。

思路：字典树。。把每个数转化成二进制，注意补全前导0，使得所有数都有相同的位数。

如果想要异或和最大，那么每一位尽可能都是1.

所以做法是，先构建字典树，然后每次find的时候，尽可能按照和当前寻找的数的位相反的位的方向走（如果有的话）

比如当前位是1，那我就往0的方向走。

**需要注意的是，多组数据，每次要重新初始化一遍。**

做法是 在struct 中重新 root = new Node() 一下。。这样就重新调用了Node中初始化用的构造函数。



    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年08月15日 星期一 20时03分05秒
    File Name :code/hdu/4825.cpp
    ************************************************ */
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <stack>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <deque>
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
    const int LEN = 32;
    int n,m;
    char str[35];
    struct Trie
    {
        struct Node
        {
    	Node *nxt[2];
    	int val;
    	Node()
    	{
    	    for ( int i = 0 ; i < 2 ; i++) nxt[i]=NULL;
    	    val = 0 ;
    	}
        };
        Node *root;
        void init()
        {
    	root = new Node();
        }
        Trie()
        {
    	root = new Node();
        }
        void Insert(char *s,int num)
        {
    	Node *u =root;
    	int len = strlen(s);
    //	cout<<" len :"<<len<<endl;
    	for ( int i = 0 ; i < len ; i++)
    	{
    	    int v = s[i]-'0';
    	    if (u->nxt[v]==NULL) u->nxt[v] = new Node();
    	    u = u->nxt[v];
    	}
    	u->val = num;
        }
        int Find(char *s)
        {
    	Node *u = root;
    	int len = strlen(s);
    	for ( int i = 0 ; i < len ; i++)
    	{
    	    int x = s[i]-'0';
    	    int y = !x;
    	    if (u->nxt[y]==NULL)  //相反的方向有路就走相反的，没路就只能走一样的。
    		u = u->nxt[x];
    	    else u = u->nxt[y];
    	}
    	return u->val;
        }
    }trie;
    void bianshen( int x)
    {
        for ( int i = LEN-1,j=0 ; i>=0 ; i--,j++) //高位补0，以及str[0]是最高位，str[LEN-1]是最低位
    	str[i] =((x>>j)&1)+'0';
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int T;
    	cin>>T;
    	int cas = 0 ;
    	while (T--)
    	{
    	    trie.init();
    	    printf("Case #%d:\n",++cas);
    	    scanf("%d%d",&n,&m);
    	    for ( int i = 1 ; i <= n ; i++)
    	    {
    		int x;
    		scanf("%d",&x);
    		bianshen(x);
    		trie.Insert(str,x);		
    	    }
    	    while (m--)
    	    {
    		int x;
    		scanf("%d",&x);
    		bianshen(x);
    		printf("%d\n",trie.Find(str));
    	    }
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    







