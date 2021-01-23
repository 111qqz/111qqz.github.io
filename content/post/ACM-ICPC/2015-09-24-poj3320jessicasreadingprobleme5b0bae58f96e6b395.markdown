---
author: 111qqz
date: 2015-09-24 13:37:00+00:00
draft: false
title: poj 3320 Jessica's Reading Problem (尺取法)
type: post
url: /2015/09/poj3320jessicasreadingproblem/
categories:
- ACM
tags:
- 尺取法
---

Jessica's Reading Problem





<table align="center" >
<tbody >
<tr >

<td >**Time Limit:** 1000MS
</td>

<td width="10px" >
</td>

<td >**Memory Limit:** 65536K
</td>
</tr>
<tr >

<td >**Total Submissions:** 8787
</td>

<td width="10px" >
</td>

<td >**Accepted:** 2824
</td>
</tr>
</tbody>
</table>





Description







Jessica's a very lovely girl wooed by lots of boys. Recently she has a problem. The final exam is coming, yet she has spent little time on it. If she wants to pass it, she has to master all ideas included in a very thick text book. The author of that text book, like other authors, is extremely fussy about the ideas, thus some ideas are covered more than once. Jessica think if she managed to read each idea at least once, she can pass the exam. She decides to read only one contiguous part of the book which contains all ideas covered by the entire book. And of course, the sub-book should be as thin as possible.




A very hard-working boy had manually indexed for her each page of Jessica's text-book with what idea each page is about and thus made a big progress for his courtship. Here you come in to save your skin: given the index, help Jessica decide which contiguous part she should read. For convenience, each idea has been coded with an ID, which is a non-negative integer.







Input







The first line of input is an integer _P_ (1 ≤ _P_ ≤ 1000000), which is the number of pages of Jessica's text-book. The second line contains _P_ non-negative integers describing what idea each page is about. The first integer is what the first page is about, the second integer is what the second page is about, and so on. You may assume all integers that appear can fit well in the signed 32-bit integer type.







Output







Output one line: the number of pages of the shortest contiguous part of the book which contains all ideals covered in the book.







Sample Input



    
    5
    1 8 8 8 1
    




Sample Output



    
    2




[今天开始学算法系列 -- 尺取法](http://blog.chinaunix.net/uid-24922718-id-4848418.html) 2015-02-28 09:54:49










分类： C/C++










转载一段讲解







<blockquote>

> 
> 我们先来介绍一下尺取法。尺取法，顾名思义，像尺子一样，一块一块的截取。是不是解释的有点让人纳闷～。。没关系，下面我们通过这个题目来体会尺取法的魅力。

> 
> 

> 
> 题目翻译：
> 
> 

> 
> 　　给定长度为n的数列整数a0,a1,a2,a3 ..... an-1以及整数S。求出综合不小于S的连续子序列的长度的最小值。如果解不存在，则输出0。
> 
> 

> 
> 

> 
> 　　限制条件：
> 
> 

> 
> 　　　　10
> 
> 

> 
> 　　　　0
> 
> 

> 
> 　　　　S<10^8
> 
> 

> 
> 

> 
> 这里我们拿第一组测试数据举例子，即 n=10, S = 15, a = {5,1,3,5,10,7,4,9,2,8}
> 
> 

> 
> ![](https://111qqz.com/wp-content/uploads/2015/11/291224259702079.jpg)

> 
> 

> 
> 

> 
> 　　 这幅图便是尺取法怎么"取"的过程了。
> 
> 

> 
> 　　整个过程分为4布：
> 
> 

> 
> 　　　　1.初始化左右端点
> 
> 

> 
> 　　　　2.不断扩大右端点，直到满足条件
> 
> 

> 
> 　　　　3.如果第二步中无法满足条件，则终止，否则更新结果
> 
> 

> 
> 　　　　4.将左端点扩大1，然后回到第二步
> 
> 

> 
> 

> 
> 用尺取法来优化，使复杂度降为了O(n)。
> 
> 

> 
> 最后，再给一个尺取法的定义以便更好理解：返回的推进区间开头和结尾，求满足条件的最小区间的方法称为尺取法。  
  
以上为网上关于尺取法的原理介绍，还是比较好理解的，邢如蚯蚓的爬动。  
  

> 
> 


> 
> 

> 
> 

</blockquote>







　　然后这道题可以先用set ，统计出不同的知识点有多少个，总是记为total




　　然后根据一段区间内的知识点数目sum是否达到total来移动两个pointer head 和tail




　　因为知识点的标号比较大，数组下表存不下，所以开个map来统计相应知识点出现的数量...




　　然后还有个．．．




　　误以为if (cnt[a[tail++]]++==0) sum++;和




　　if (cnt[a[tail]]==0)




　　{




　　　　sum++;




　　　　cnt[a[taill]]++;




　　　　tail++;




　　}




　　是等价的．．．




幸好没去队群里问．．．不然又要被嘲讽一番了．．




区别在于．前者无论cnt[a[tail]]是否为0，tail和cnt都会＋＋；




而后者．．只有在cnt[a[tail]]为０时，tail和cnt才会＋＋




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock67.gif)
/*************************************************************************
	> File Name: code/poj/3320.cpp
	> Author: 111qqz
	> Email: rkz2013@126.com 
	> Created Time: 2015年09月24日 星期四 19时33分20秒
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
#include<cctype>
#define y1 hust111qqz
#define yn hez111qqz
#define j1 cute111qqz
#define ms(a,x) memset(a,x,sizeof(a))
#define lr dying111qqz
using namespace std;
#define For(i, n) for (int i=0;i<int(n);++i)  
typedef long long LL;
typedef double DB;
const int inf = 0x3f3f3f3f;
const int N = 1E6+7;
int a[N];
int p;
void solve ()
{
    set<int>se;
    for ( int i = 1 ; i <= p ; i++)
    {
	scanf("%d",&a[i]);
	se.insert(a[i]);
    }
    int total = se.size();
    map<int,int> cnt;
    int ans = p ;
    int head = 1 ;
    int tail = 1 ;
    int sum = 0 ;
    while (1)
    {
	while (tail<=p&&sum<total) 
	{
	    // cout<<"ajhhh"<<endl;
	 //  if (cnt[a[tail++]]++ ==0) sum++;
	     if (cnt[a[tail]]==0)
	    {
		
		sum++;
	    }
 		cnt[a[tail]]++;
         	tail++;
		
	    
	     cout<<"total"<<total<<endl;
	}
	if (sum<total) break;
	ans = min (ans ,tail - head);
	if (--cnt[a[head++]]==0) sum--;
	
    }
    printf("%d\n",ans);
}
int main()
{
  #ifndef  ONLINE_JUDGE 
   freopen("in.txt","r",stdin);
  #endif
   while (scanf("%d",&p)!=EOF)
    {
	solve();
    }
  
   
 #ifndef ONLINE_JUDGE  
  fclose(stdin);
  #endif
	return 0;
}




