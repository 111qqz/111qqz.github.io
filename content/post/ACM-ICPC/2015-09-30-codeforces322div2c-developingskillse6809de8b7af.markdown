---
author: 111qqz
date: 2015-09-30 02:38:00+00:00
draft: false
title: 'codeforces #322 div 2 C. Developing Skills(乱搞)'
type: post
url: /2015/09/codeforces322div2c-developingskills/
categories:
- ACM
tags:
- 乱搞
---







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Petya loves computer games. Finally a game that he's been waiting for so long came out!




The main character of this game has _n_ different skills, each of which is characterized by an integer _a__i_ from 0 to 100. The higher the number_a__i_ is, the higher is the _i_-th skill of the character. The total rating of the character is calculated as the sum of the values ​​of ![](https://111qqz.com/wp-content/uploads/2015/11/d57eb2f9c5cdd47117a3d4c38f8d70b49461a957.png)
for all _i_ from 1 to _n_. The expression ⌊ _x_⌋ denotes the result of rounding the number _x_ down to the nearest integer.




At the beginning of the game Petya got _k_ improvement units as a bonus that he can use to increase the skills of his character and his total rating. One improvement unit can increase any skill of Petya's character by exactly one. For example, if _a_4 = 46, after using one imporvement unit to this skill, it becomes equal to 47. A hero's skill cannot rise higher more than 100. Thus, it is permissible that some of the units will remain unused.




Your task is to determine the optimal way of using the improvement units so as to maximize the overall rating of the character. It is not necessary to use all the improvement units.










Input




The first line of the input contains two positive integers _n_ and _k_ (1 ≤ _n_ ≤ 105, 0 ≤ _k_ ≤ 107) -- the number of skills of the character and the number of units of improvements at Petya's disposal.




The second line of the input contains a sequence of _n_ integers _a__i_ (0 ≤ _a__i_ ≤ 100), where _a__i_ characterizes the level of the _i_-th skill of the character.










Output




The first line of the output should contain a single non-negative integer -- the maximum total rating of the character that Petya can get using _k_ or less improvement units.










Sample test(s)










input



    
    2 4<br></br>7 9










output



    
    2










input



    
    3 8<br></br>17 15 19










output



    
    5










input



    
    2 2<br></br>99 100










output



    
    20
















Note




In the first test case the optimal strategy is as follows. Petya has to improve the first skill to 10 by spending 3 improvement units, and the second skill to 10, by spending one improvement unit. Thus, Petya spends all his improvement units and the total rating of the character becomes equal to _lfloor_ _frac_{100}{10} _rfloor_ +  _lfloor_ _frac_{100}{10} _rfloor_ = 10 + 10 =  20.




In the second test the optimal strategy for Petya is to improve the first skill to 20 (by spending 3 improvement units) and to improve the third skill to 20 (in this case by spending 1 improvement units). Thus, Petya is left with 4 improvement units and he will be able to increase the second skill to 19 (which does not change the overall rating, so Petya does not necessarily have to do it). Therefore, the highest possible total rating in this example is ![](https://111qqz.com/wp-content/uploads/2015/11/474d3c832d2017b4a4e816c764fedc91f3282a8c.png)
.




In the third test case the optimal strategy for Petya is to increase the first skill to 100 by spending 1 improvement unit. Thereafter, both skills of the character will be equal to 100, so Petya will not be able to spend the remaining improvement unit. So the answer is equal to ![](http://codeforces.com/predownloaded/05/f8/05f8611f710c0ca7c188f9020a10e40475030c69.png)
.







不能超过１００没看到...




贡献若干次wa...蠢哭了．




然后写蠢了...




最后觉得这样写比较好：




开一个结构体数组... a,b




a用来记录原始值，b用来记录mod10的余数与１０的差..




整个填充过程分两步骤




第一步是把余数不为0的填充到１０..




这部分要先填充...显然比先填充余数为0的更优．而且先填充余数大的..也就是b小的...




以b为关键字...从小到达排序..




然后填充的时候记得更新　a的值到整十　　




同时用一个sum累加更新后的a[i] 到100的距离...




sum/10是一个限制条件




而k/10是第二个限制条件




所以答案最后加上　min(k,sum)/10;



 

    
    /*************************************************************************
    	> File Name: code/cf/#322/C.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月29日 星期二 00时40分26秒
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
    const int N=1E5+7;
    int n;
    int k,ans;
    
    struct Q
    {
        int a,b;
    }q[N];
    
    bool cmp(Q x, Q y)
    {
        if (x.b<y.b) return true;
        return false;
    }
    int main()
    {
      #ifndef  ONLINE_JUDGE 
     //    freopen("in.txt","r",stdin);
      #endif
       
        ans = 0 ;
        scanf("%d %d",&n,&k);
        for ( int i = 0 ; i < n ; i++)
        {
    	scanf("%d",&q[i].a);
    	ans = ans + q[i].a / 10;
    	q[i].b = q[i].a % 10 ; 
    	q[i].b = 10 - q[i].b;
        }
        sort(q,q+n,cmp);
        int sum = 0 ;
        int i = 0;
        for ( int i = 0 ; i  < n ; i++)
        {
    //	if (q[i].b==10) break;
    	if (k-q[i].b>=0)
    	{
    	    k = k - q[i].b;
    	    q[i].a = 100-(q[i].a/10+1)*10;
    	    sum = sum + q[i].a;
    	    ans++;
    	}
    	if (k<=0) break;
        }
        ans = ans + min(k,sum)/10 ;
        
      //  cout<<"ans:"<<ans<<endl;
    
        printf("%d",ans);
    
       
     #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
    	return 0;
    }
    



