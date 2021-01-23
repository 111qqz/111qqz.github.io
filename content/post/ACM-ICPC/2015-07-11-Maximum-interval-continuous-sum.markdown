---
author: 111qqz
date: 2015-07-11 21:17:00+00:00
draft: false
title: 最大连续区间和的算法总结
type: post
url: /2015/07/Maximum-interval-continuous-sum/
categories:
  - ACM
---

最大连续区间和是一个经典的问题。给定一个长度为 n 的序列 a[1],a[2]...a[n-1],a[n]，求一个连续的子序列 a[i],a[i+1]...a[j-1],a[j]，使得 a[i]+a[i+1]...a[j-1]+a[j]最大。

① 最简单最容易想到的就是根据定义来枚举。  
枚举上下界{i,j | 0<=i<=j<=n}，维护一个 max 值即可。  
其中枚举上下界的时间复杂度为 O(n^2)，求区间和的复杂度为 O(n)，所以总时间复杂度为 O(n^3)。

```c++
for ( i = 1 ; i <= n ; i++ )
for ( j = i ; j <= n ; j++ )
ans = max(ans,accumulate(a+i,a+j+1,0));
```

② 其实就是第一种方法的优化。  
这里有个很容易想到的优化，即预处理出前缀和 sum[i]=a[0]+a[1]+...+a[i-1]+a[i]，算区间和的时候即可将求区间和的复杂度降到 O(1)，枚举上下界的复杂度不变，所以总时间复杂度为 O(n^2)。

```c++
for ( i = 1 ; i <= n ; i++ )
sum[i]=sum[i-1]+a[i];
for ( i = 1 ; i <= n ; i++ )
for ( j = i ; j <= n ; j++ )
ans = max(ans,sum[j]-sum[i-1]);

```

③ 可以利用动态规划的思维来继续优化，得到一个线性的算法，也是最大连续区间和的标准算法  
定义 maxn[i]为以 i 为结尾的最大连续和，则很容易找到递推关系：maxn[i]=max{0,maxn[i-1]}+a[i]。  
所以只需要扫描一遍即可，总时间复杂度为 O(n)。

```c++
for ( i = 1 ; i <= n ; i++ )
{
last = max(0,last)+a[i];
ans = max(ans,last);
}
```

④ 同样用到类似的思维。  
首先也需要预处理出前缀和 sum[i]，可以推出 ans=max{sum[i]-min{sum[j] } | 0<=j 而最小前缀和可以动态维护，所以总时间复杂度为 O(n)。

```c++
for
( i = 1 ; i <= n ; i++ )
sum[i]=sum[i-1]+a[i];
for ( i = 1 ; i <= n ; i++ )
{
ans = max(ans,sum[i]-minn);
minn = min(minn,sum[i]);
}
```




总结：虽然朴素的O(n^3)和前缀和优化的O(n^2)算法很容易想到，但代码实现却反而比方法三麻烦，第四个方法虽然有和方法三相同的复杂度，但需要一个预处理和多出的O(n)的空间，所以，方法三很好很强大。
```
