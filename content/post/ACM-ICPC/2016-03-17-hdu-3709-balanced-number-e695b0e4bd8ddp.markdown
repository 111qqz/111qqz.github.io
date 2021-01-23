---
author: 111qqz
date: 2016-03-17 11:46:31+00:00
draft: false
title: hdu 3709 Balanced Number (数位dp)
type: post
url: /2016/03/hdu-3709-balanced-number-dp/
categories:
- ACM
tags:
- dp
- 数位dp
---

[题目链接](http://acm.hdu.edu.cn/showproblem.php?pid=3709)
题意：找到某区间中平衡数的个数。所谓平衡数是指，存在某个位置，值得两边的力矩相等。举个例子。。比如14326，如果把4作为中间。。那么左边=1*1=1 右边=3*1+2*2+6*2=19。。。
思路：枚举中间的pivot。。。注意如果是个位数也是平衡数（就是认为两边的力矩都是0了。。。），所以每一个位置都可能是平衡位置。。枚举的时候从1到len...
一开始我是分别记录两边的值。。非常浪费空间。。。然而发现其实没必要。。**我们只关心左边是否相等。。而不关心左右的值到底是多少。。所以可以把两边的值带符号合并成一个值**（pivot左边为+，pivot右边为负）。。。如果最后为0。。说明左右相等。。。

以及。。这个值(设为sum)是递减的。。。**所以任何时刻如果sum<0。。那么狗带。。算一个剪枝。。而且避免了下标为负。。。**

以及，关于前导0的问题。。。有些题目不允许前导0.。。。**但是并不是所有不允许前导0的都需要特别处理。。。像这道。。前导0不会导致更新答案。。。所以不用管。。**。 但是要注意。。。由于0，00,000,0000都是合法的balanced数。。。然而其实他们是一个数。。多加了len-1次。。记得减去。







    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年03月17日 星期四 17时08分59秒
    File Name :code/hdu/3709.cpp
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
    LL l,r;
    int T;
    int digit[30];
    LL dp[20][2000][20];  //窝要判断左边和右边是否相等，并不需要分别统计两边，只要把数值带上符号，统计左右两边的和即可。
                            //如果相等，那么和为0.这样能节省很多空间。
    LL dfs( int pos,int sum ,int pivot,bool limit) 
    {			//不用考虑前导0，因为前导0的存在并不会对答案有任何贡献.
        if (pos==0) return sum==0;
        if (sum<0) return 0; //由于sum是递减的。。所以sum一旦小于0绝对药丸。。。肯定对答案没贡献。
    			//也算作一个剪枝..
        if (!limit&&dp[pos][sum][pivot]!=-1) return dp[pos][sum][pivot];
    
        int mx = limit?digit[pos]:9;
        LL res = 0LL ;
        for ( int i = 0 ; i <= mx ; i++)
        {
    	res+=dfs(pos-1,sum+(pos-pivot)*i,pivot,limit&&i==mx);
        }
    
       // cout<<"res:"<<res<<endl;  
        return limit?res:dp[pos][sum][pivot]=res;
    }
    LL solve (LL n)
    {
       // if (n<0) return 0;
        LL len = 0;
        ms ( digit , 0 );
        while (n)
        {
    	digit[++len] =  n % 10;
    	n /= 10;
        }
    
        LL res = 0LL ;
        for ( int piv = 1 ; piv <= len  ; piv++)  //pivot要从1开始枚举到len。因为个位数也是满足条件的数（两边都为0，相等）
        {
    	res += dfs (len,0,piv,true);
    //	cout<<"res:"<<res<<endl;
        }
    
        return res-(len-1); //0,00,000,0000都是满足条件的，然而其实他们是一个数，多算了len-1次。
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	ios::sync_with_stdio(false);
    	int T;
    	cin>>T;
    	ms(dp,-1);
    	while (T--)
    	{
    	    cin>>l>>r;
    	    LL ans = solve (r) - solve (l-1);
    	  //  cout<<"-1:"<<solve(-1)<<endl;
    	    cout<<ans<<endl;
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



