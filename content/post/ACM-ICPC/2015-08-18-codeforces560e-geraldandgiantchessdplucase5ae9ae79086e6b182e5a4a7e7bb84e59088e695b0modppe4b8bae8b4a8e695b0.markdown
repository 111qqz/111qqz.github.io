---
author: 111qqz
date: 2015-08-18 11:36:00+00:00
draft: false
title: codeforces 560 E. Gerald and Giant Chess (dp+lucas定理,求大组合数 mod p,p为质数)
type: post
url: /2015/08/codeforces560e-geraldandgiantchessdplucasmodpp/
categories:
- ACM
tags:
- dp
- lucas定理
- 计数问题
---

dp方程想错了.果然还是欠练啊.

如果我们不考虑坏点,那么从 (0,0)到(x,y)的方案数是c(x+y,x)或者c(x+y,y)

因为有坏点的存在,我们可以逆向思维,先求出总数,然后减去那些由于坏点的影响不能走的方案数.

由于存在黑点i(x,y)，从左上到该黑点的方案数sum[i] = C(x+y,x)，其中如果在黑点i的左上还有黑点j(u,v)，那么应该减去sum[j]*C(x-u+y-v)(y-u)

然后可以把坏点按照x为第一关键字,y为第二关键字排序.

从左上出发,往右下扫黑点.

还有一个考点是大组合数的求法

因为太大,递推也不行.

可以用欧拉公式求逆元的方法求解.

或者是lucas定理.

记得拿到骑士(1,1)到(n,m)的题和这道题很像.

也是从坐上到右下,中间有些坏点,不过骑士的走法并不是向下或者想有1步,而是向右p步,向下q步,或者向又q步,向下p步.

而且那道题的n和m是 10^9的数量级...

那道题的话就只能用lucas定理了貌似

这道题算是那道题的弱化版本,在此orz zhangk,果然厉害

所以我还是决定写lucas定理的解法

lucas定理适用于 求C(n,m)%p,p为素数 且n,m很大的情况.

引用一段题解:


<blockquote>

>     
>     题意，给一个n * m 的网格，其只有一些点是坏的不能走，要求从0，0点起到n,m的总方案数。
> 
> 
</blockquote>



    
    设dp[i] 表示到达第i个坏点且不经过其他坏点的总方案数。增加一个点(n-1,m-1),则dp[k]即为答案。




<blockquote>

>     
>     壮态转移方程 dp[i] = C[x[i]+y[i],x[i]) - sum(dp[j] * C(x[i] - x[j] + y[i] - y[j],x[i] - x[j]),j表示，所有在i之前的坏点，由于这里的dp[i]都是不经过别的坏点，不会有重复的路径，所以减去以前的坏点到达i的路径就是答案。
> 
> 

>     
>     先排序，就可以得到每个点的先后顺序，这样在更新状态的时候，可以从小到大枚举。总的复杂度为 o(k * k);
> 
> 

>     
>     现在剩下的问题 就是要求c(n,m),由于n,m很大，一般求组合数的方法是n * m，这样复杂度太高，即使用递推o(n)的复杂度，也是太高的。这里引入了 定理Lucas，这个就是专门求大组合数的一种方法。
> 
> 

>     
>     Lucas(n,m,p)=c(n%p,m%p)*Lucas(n/p,m/p,p) 设 aa = n % p,bb = m % p;这里可以看出来把n,m很大的数转化了相对比较小的aa,bb,
> 
> 

>     
>     这个公式把n - n/p m - m/p,这样可以递归解决。求c(aa,bb)就可以直接用组合公式aa!/(bb! * (aa - bb)! ),由于这里有除法，所以要求bb! * (aa - bb)!的逆。
>     由欧拉公式
>     p为素数a的逆为pow_mod(a,p-2,p);即a^(p-2) % p;
>     
> 
> 

>     
>     所以整个公式转化成ret=(ret*fac[a]*pow_mod(fac[b]*fac[a-b]%p,p-2,p))%p; 这样就可以递归求解了。
> 
> 

>     
>      
> 
> 

> 
> 

>     
>     总的说一下，虽然这题，由于n,m很小只有10^5，所以不用lucas定理也可以解决，但有可能会出现一种情况n,m很大，达到10^9,而MoD很小，只有10^5,这样，这个lucas定理，就可以有真正的用场了,而且要求MOD是质数才可以的，因为是质数，那个欧拉定理才适用的。
> 
> 

>     
>      
> 
> 
</blockquote>


 

    
    /*************************************************************************
    	> File Name: code/cf/#313/EE.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月18日 星期二 18时43分18秒
     ************************************************************************/
    
    #include<iostream>
    #include<iomanip>
    #include<cstdio>
    #include<algorithm>
    #include<cmath>
    #include<cstring>
    #include<string>
    #include<map>
    #include<set>
    #include<queue>
    #include<vector>
    #include<stack>
    #define y0 abc111qqz
    #define y1 hust111qqz
    #define yn hez111qqz
    #define j1 cute111qqz
    #define tm crazy111qqz
    #define lr dying111qqz
    using namespace std;
    #define REP(i, n) for (int i=0;i<int(n);++i)  
    typedef long long LL;
    typedef unsigned long long ULL;
    const int inf = 0x7fffffff;
    const int N=2E3+7;
    const int mod = 1E9 + 7;
    const int M = 1E5+7;
    int h,w,n;
    typedef long long ll;
    ll fac[2*M];
    ll dp[N];
    pair<int,int> p[N];
    LL quickpow(LL a,LL b)
    {
    	LL res=1;
    	while(b)
    	{
    	    if(b&1) res=res*a%mod;
    	    a=(a*a)%mod;
    	    b>>=1;
    	}
    	return res;
    }
    LL C(LL a,LL b)
    {
    	if(b>a) return 0;
    	return fac[a]*quickpow(fac[b]*fac[a-b]%mod,mod-2)%mod;
    }
    LL lucas(LL a,LL b)
    {
    	if(b==0) return 1;
    	return (C(a%mod,b%mod)*lucas(a/mod,b/mod))%mod;
    }
    void init()
    {
    	fac[0]=1,fac[1]=1;
    	for(int i=1;i<2*M;i++)
    	{
    		fac[i]=(fac[i-1]*i)%mod;
    	}
    }
    int main()
    {
    	init();
    	cin>>h>>w>>n;
    	for(int i=1;i<=n;i++){
    //		int x,y;  cin>>x>>y;
    //		p[i].first=x; p[i].second=y;
    	    cin>>p[i].first;
    	    cin>>p[i].second;
    	}
    	p[n+1].first=h,p[n+1].second=w;
    	sort(p+1,p+n+2);
    	
    	for(int i=1;i<=n+1;i++)
    	{
    		dp[i]=lucas(p[i].first+p[i].second-2,p[i].first-1);
    		for(int j=1;j<i;j++)
    		{
    	 		if(p[j].second<=p[i].second) 
    			{
    				dp[i]-=dp[j]*lucas(p[i].first-p[j].first+p[i].second-p[j].second,p[i].first-p[j].first)%mod;
    				dp[i] = (dp[i]+ mod ) % mod;
    			}
     		}
    	}
    	cout<<dp[n+1]<<endl;
    
    	return 0;
    }
    



