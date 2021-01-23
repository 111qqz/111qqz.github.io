---
author: 111qqz
date: 2015-08-14 20:33:00+00:00
draft: false
title: codeforces 570 E. Pig and Palindromes (dp)
type: post
url: /2015/08/codeforces570e-pigandpalindromesdp/
categories:
- ACM
tags:
- dp
---






比赛的时候想到了是dp搞...

不过dp废.....

可能更多的是心理上...

这道题并不怎么难想,但是以觉得是dp,就给了自己一种暗示...这题我搞不出来...

实际上,我把cA掉的时候应该还有一个小时十分钟左右的样子...

d题没啥思路,所以我有大概一个小时的时间可以搞e...未必就搞不出来.



还有因为答案很大要取模,感觉一般取模的题,要么是数学,要么是像dp这种有递推式子的.

这道题的思路是:

因为要形成回文串,我们可以从两边往中间走,保证每一步都相同.

dp[i][x1][x2] 表示路径长度为i,左上角出发到达x坐标为x1,又下角出发到达x坐标为x2,且两条路径上对应的字母都相同的方案数.

然后判断当前格子的字母是否一样,如果一样,则考虑转移.

由于从左上角出发可以往下往右,从右下角出发可以往上往左,排列组合,所以当前状态和之前的四种状态有关.

由因为这步的状态只和上以步的四种状态有关,所以路径长度那以维要滚动掉不然会MLE

dp方程为 dp[cur][x1][x2]=(dp[cur^1][x1][x2],dp[cur^1][x1-1][x2],dp[cur^1][x1][x2+1],dp[cur^1][x1-1][x2+1])%MOD;

然后注意由于(m+n) 的奇偶性,答案会有所不同.

根据奇偶性判断从两端出发是到两个相邻的格子还是到同一个格子.

初始化的话如果(1,1)和{n,m}点的字母一样那么 dp[0][1][n] 为1,否则为0.

其他点显然都为0
 

    
    /*************************************************************************
    	> File Name: code/cf/#316/EE.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月15日 星期六 04时10分13秒
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
    const int MOD=1E9+7;
    const int N=5E2+7;
    int n,m;
    char st[N][N];
    
    int dp[2][N][N];
    int main()
    {
        scanf("%d %d",&n,&m);
        for ( int i = 1 ; i <= n ; i++)
        {
    	scanf("%s",&st[i][1]);
        }
      //  dp[0][1][n]= st[1][1]==st[n][m];
        if (st[1][1]==st[n][m])
        {
    	dp[0][1][n]=1;
        }
        else
        {
    	dp[0][1][n]=0;
        }
        int cur = 0;
        int mx = (m+n-2)/2;
        for ( int step = 1 ; step <= mx ; step++)
        {
    	cur = cur ^ 1;
    	for (int i = 1 ; i<= n ; i++)
    	{
    	    for ( int j = 1 ; j <= n ; j++ )
    	    {
    		dp[cur][i][j]  =0 ;
    	    }
    	}
        
    	 for ( int x1 = 1 ; x1 <= n&&x1-1<=step ;x1++)
    	 {
    		for ( int x2 = n ; x2>=1 &&n-x2<=step ;x2--)
    		{
    		    int y1 = 1+step-(x1-1);         
    		    int y2 = m-step+(n-x2);         //由x1,x2 可以计算出y1,y2
    		    if (st[x1][y1]==st[x2][y2])
    		    {
    			dp[cur][x1][x2] = (dp[cur][x1][x2] + dp[cur^1][x1][x2])%MOD;
    			dp[cur][x1][x2] = (dp[cur][x1][x2] + dp[cur^1][x1][x2+1])%MOD;
    			dp[cur][x1][x2] = (dp[cur][x1][x2] + dp[cur^1][x1-1][x2])%MOD;
    			dp[cur][x1][x2] = (dp[cur][x1][x2] + dp[cur^1][x1-1][x2+1])%MOD;
    		    }//只有当前pic 相同的时候才转移
    		}   
    	 }
        }
    	 int ans = 0;
    	 for ( int i = 1 ; i<= n ; i++ )
    	 {
    	     ans = (ans + dp[cur][i][i]) % MOD;
    	 }
    	 if ((m+n)%2)
    	 {
    	    for ( int i = 1 ; i<= n-1 ; i++)
    	    {
    		ans = (ans + dp[cur][i][i+1])%MOD;
    	    }
    	 }
    	 cout<<ans<<endl;
      
    	return 0;
    }
    



