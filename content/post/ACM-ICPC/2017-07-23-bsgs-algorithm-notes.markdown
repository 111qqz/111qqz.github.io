---
author: 111qqz
date: 2017-07-23 12:41:46+00:00
draft: false
title: BSGS（Baby steps giant steps）算法学习笔记
type: post
url: /2017/07/bsgs-algorithm-notes/
categories:
- ACM
tags:
- BSGS
- 分块
---

**离散对数**（Discrete Logarithm）问题是这样一个问题，它是对于模方程

a^x=b(mod prime)，求满足条件的X，或者得出不存在这样的X

最暴力的思路，那么就是枚举x? 根据[费马小定理](https://zh.wikipedia.org/zh-cn/)，只需要枚举[0,p-1)

但是还是很大...我们不禁想到把x写成x=A*m+B的形式，m=ceil(sqrt(p))

因此有![ a^{A\lceil \sqrt{p} \rceil + B} \equiv b \pmod p ](http://blog.miskcoo.com/wp-content/plugins/latex/cache/tex_e074c544474c0974ac48e4130a8a298a.gif)
，变形得到![ a^{A\lceil \sqrt{p} \rceil} \equiv b\cdot a^{-B} \pmod p ](http://blog.miskcoo.com/wp-content/plugins/latex/cache/tex_b5b97e06b3a3e9d53d25bb32966b7887.gif)


然后预处理一边存到map中，从小到大枚举另一边看是否存在...



我们可以设 ![x = A \lceil \sqrt{p} \rceil - B](http://blog.miskcoo.com/wp-content/plugins/latex/cache/tex_6a327ff427047a52f12ae62db2c62a17.gif)
，其中 ![0 \leq B < \lceil \sqrt{p} \rceil](http://blog.miskcoo.com/wp-content/plugins/latex/cache/tex_5eae323ac137bfcd344156a9fcd2ae4e.gif)
,  ![0 < A \leq \lceil \sqrt{p} \rceil + 1](http://blog.miskcoo.com/wp-content/plugins/latex/cache/tex_9bc1e7994d1dffbd9d826801ce759781.gif)
，这样的话化简后的方程就是

![ a^{A\lceil \sqrt{p} \rceil} \equiv b\cdot a^B \pmod p ](http://blog.miskcoo.com/wp-content/plugins/latex/cache/tex_6034086ebf3222f45c410883f4f2c6ae.gif)


**就可以不用求出逆元，要注意只是不用求出逆元，而不是没有用到逆元的存在**

**就可以不用求出逆元，要注意只是不用求出逆元，而不是没有用到逆元的存在**

**就可以不用求出逆元，要注意只是不用求出逆元，而不是没有用到逆元的存在**



其实在m=sqrt(p)的时候你可能就有预感了...

BSGS算法的本质，就是个分块啊，而分块的本质就是暴力乱搞...所以BSGS看起来很高大上的算法不过是**暴力乱搞**2333

而BSGS的名字也很贴切...A的变化是giant step？B的变化是baby step? (纯属yy...但是我感觉这样想很好理解啊？

需要注意的是，这里介绍的是常规的BSGS算法，

**前提条件是a和P互质**

**前提条件是a和P互质**

**前提条件是a和P互质**

放一个板子好了，poj 2417

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年07月23日 星期日 11时11分00秒
    File Name :2417.cpp
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
    LL p,b,n;
    map<LL,LL>Hash;
    map<LL,LL>::iterator it;
    inline LL ksm(LL a,LL b,LL MOD)
    {
        LL res = 1LL;
        while (b)
        {
    	if (b&1) res = (res*a)%MOD;
    	b = b >> 1;
    	a = (a*a)%MOD;
        }
        return res;
    }
    LL BSGS(LL a,LL b ,LL p) // a^x = b (mod p),求x 
    {
        a%=p;
        b%=p;
        if (!a&&!b) return 1;
        if (!a) return -1;
        Hash.clear();
        LL m = ceil(sqrt(double(p)));
        LL tmp = b;
        for (LL j = 0 ; j <= m ; j++)
        {
    	Hash[tmp]=j;
    	tmp = (tmp*a)%p;
        }
        tmp = ksm(a,m,p);
        LL ret = 1;
    
        for (LL i = 1  ; i <= m+1 ; i++)
        {
    	ret = ret*tmp%p;
    	if (Hash[ret]) return i*m-Hash[ret]; //注意处理下%....虽然其实不处理也没关系...
        }
        return -1;
    
    }
    int main()
    {
            #ifndef  ONLINE_JUDGE 
           // freopen("./in.txt","r",stdin);
      #endif
    	while (~scanf("%lld%lld%lld",&p,&b,&n))   // B^L = n(mod p)
    	{
    	    LL ans = BSGS(b,n,p);
    	    if (ans==-1) printf("no solution\n");
    	    else printf("%lld\n",(ans%p+p)%p);
    	}
    	    
        
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




参考资料：

[ 一个很多BSGS算法初学者的误区](http://kzoacn.is-programmer.com/posts/97193.html)

[扩展大步小步法解决离散对数问题](http://blog.miskcoo.com/2015/05/discrete-logarithm-problem)

[大步小步算法与扩展大步小步算法](http://qpswwww.logdown.com/posts/333090-BSGS-extBSGS)

[BSGS算法学习小记（大步小步算法）](http://blog.csdn.net/doyouseeman/article/details/52084773)






