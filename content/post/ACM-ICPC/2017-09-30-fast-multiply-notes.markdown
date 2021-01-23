---
author: 111qqz
date: 2017-09-30 12:50:42+00:00
draft: false
title: 快速乘
type: post
url: /2017/09/fast-multiply-notes/
categories:
- ACM
tags:
- 快速乘
---

16年北京网络赛遇到了这个技巧...但是竟然忘记记了下来？

快速乘是为了解决 计算a_b % mod 时a_b溢出LL 的问题

比如a=1E16,b=1E16,mod=1E18，虽然最后的结果没有溢出，但是中间溢出了。

原理和快速幂很类似，具体可以参考 [晴川大爷的专栏](https://zhuanlan.zhihu.com/p/24831082)


    
    ll fastMultiplication(ll a,ll b,ll mod){
        ll ans = 0;
        while(b){
            if(b%2==1){
                b--; 
                ans = ans + a;
                            ans %= mod;
            }else{
                            b /= 2;
                a = a + a;
                            a %= mod;
            }
        }
        return ans;
    }



完全就是把快速幂中的乘法变成加法了嘛（从记忆角度考虑orz




    
    inline long long multi(long long x,long long y,long long mod)  
    {  
    long long tmp=(x*y-(long long)((long double)x/mod*y+1.0e-8)*mod);  
    return tmp<0 ? tmp+mod : tmp;  
    }






