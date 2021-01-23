---
author: 111qqz
date: 2016-09-14 07:05:21+00:00
draft: false
title: codeforces 501 D Misha and Permutations Summation (康托展开+康托逆展开+factorial_number_system+线段树×2)
type: post
url: /2016/09/codeforces-501-d-misha-and-permutations-summation-factorial_number_systemx2/
categories:
- ACM
tags:
- Factorial number system
- 康托展开/逆展开
- 线段树
---

[题目链接](http://codeforces.com/problemset/problem/501/D)

题意：给出两个排列，定义ord(p)为排列p的顺序（字典顺从小到大），定义perm(x)为顺序为x的排列，现在要求![](http://codeforces.com/predownloaded/46/04/46046198f19147fb9f021abaacf5458998990830.png)
 1 ≤ _n_ ≤ 200 000



思路：首先去学了一下康托展开和逆展开。。。其实就是对于这种排列之类的问题。。。的一个比较省空间的hash函数。。。？

[康托展开资料](http://blog.csdn.net/acdreamers/article/details/7982067)

然后由于n非常大。。康托展开中要查找当前位置后面有多少个比当前位置小的。。。

[![screenshot-from-2016-09-14-14-48-25](https://111qqz.com/wordpress/wp-content/uploads/2016/09/Screenshot-from-2016-09-14-14-48-25.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/09/Screenshot-from-2016-09-14-14-48-25.png)

然而这复杂是n2。。。肯定gg。。。

因此里面那层我们用一课线段树维护。。。复杂度nlgn

在康托逆展开的过程中。。。我们要查询之前没有出现过的第k个元素。。。。

因为n很大这里也需要线段树来维护。。。

所以再建一棵线段树。。。某位置表示初始时刻是否为空，初始都为1，表示都没有出现。思想类似于poj 2828
[poj 2828解题报告](https://111qqz.com/wordpress/2016/09/poj-2828/)



然后还是由于n很大。。。在康托展开中的阶乘部分。。。完全存不下。。。

直接用高精度应该也能做？

不过比较推荐的做法是：
[The Factorial Number System](http://www.mathpages.com/home/kmath165.htm)
[wiki_Factorial number system](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwigydSPpI7PAhUCKpQKHTsyCEUQFggcMAA&url=httpsenwikipediaorgwikiFactorial_number_system&usg=AFQjCNGrAkOqwwIVzFQBMNUvJ4rV3OWkKA&sig2=QHYbhZCXxsHDLxHGhqpe8Q&bvm=bv.132479545,d.dGo)

是一种和阶乘相关的进制表示法。

大概就是不同位置上的权值，不像一般的k进制数，是k^0,k^1,k^2....

而是0!,1!,2!。。。

这种表示合法的正确性基于：

    
    1*1! + 2*2! + 3*3! + ... + k*k!  =  (k+1)! - 1


具体参见上面两个链接。



因为我们可以把所有康托展开都用 Factorial number system来表示。





    
    /* ***********************************************
    Author :111qqz
    Created Time :Tue 13 Sep 2016 04:33:55 PM CST
    File Name :code/cf/problem/501D.cpp
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
    const int N=2E5+7;
    int n ;
    int tree[N<<2];
    int fac[N];
    int A[N],B[N];
    int ans[N];
    void PushUp(int rt)
    {
        tree[rt] = tree[rt<<1] + tree[rt<<1|1];
    }
    void update(int p,int l,int r,int rt)
    {
        if (l==r)
        {
    	tree[rt]++;
    	return;
        }
        int m = (l+r)>>1;
        if (p<=m) update(p,lson);
        else update(p,rson);
        PushUp(rt);
    }
    int query(int L,int R,int l,int r,int rt)
    {
        if (L<=l&&r<=R) return tree[rt];
        int m = (l+r)>>1;
        int ret = 0 ;
        if (L<=m)
        {
    	int res = query(L,R,lson);
    	ret +=res;
        }
        if (R>=m+1)
        {
    	int res = query(L,R,rson);
    	ret +=res;
        }
        return ret;
    }
    void Contor(int A[])//https://en.wikipedia.org/wiki/Factorial_number_system 
    {
        ms(tree,0);
        for ( int i = 0 ; i < n ; i++)
        {
    	int x;
    	scanf("%d",&x);
    	x++;
    	A[n-i-1] = x-query(1,x,1,n,1)-1; //A[i]位置是factorial_number_system所表示的高精度，整个A数组表示contor展开的答案（也就是字典序第几大），具体参考上面的链接。
    	update(x,1,n,1);
        }
    }
    void print(int *a,int n)
    {
        for ( int i =  0; i <  n ; i++ ) printf("%d ",a[i]);
        printf("\n");
    }
    void build( int l,int r,int rt)
    {
        if (l==r)
        {
    	tree[rt]  = 1; //第二棵线段树。。。表示的是空位置的个数。。。初始每个节点都为空，所以都为1.
    	return;
        }
        int m = (l+r)>>1;
        build(lson);
        build(rson);
        PushUp(rt);
    }
    int update2( int x,int l,int r,int rt)
    {
        if (l==r)
        {
    	tree[rt]--;
    	return l;
        }
        int m = (l+r)/2;
        int ret ; //又犯了。。。递归多层只由最后一层返回结果的错误2333，
        if (x<=tree[rt<<1]) ret = update2(x,lson);
        else ret =update2(x-tree[rt<<1],rson);
        PushUp(rt);
        return ret;
    }
    
    void ni_Contor()
    {
        build(1,n,1);
        A[0] = 0 ;
        for ( int i = n -1 ; i>= 0 ; i--)
        {
    	int x  =update2(A[i]+1,1,n,1)-1;
    	printf("%d%c",x,i==0?'\n':' ');
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n;
    	Contor(A); //读入排列p并且将其康托展开，然后按照factorial_number_system存入A数组。
    	Contor(B);
    //	print(A,n);
    //	print(B,n);
    	int tmp = 0 ;
    	for ( int i = 1 ; i < n ; i++) //
    	{
    	    A[i]+=B[i]+tmp;   //这部分就是在factorial_number_system下求A和B两个数的和%n!...只不过是每一步分别算了。。。
    	    tmp = A[i]/(i+1);
    	    A[i]-=tmp*(i+1);  //处理了高精度的进位和%运算。
    	}
    //	print(A,n);
    	ni_Contor();
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    











