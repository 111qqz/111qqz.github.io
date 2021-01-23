---
author: 111qqz
date: 2015-09-30 17:41:00+00:00
draft: false
title: 'codeforces #322 div 2　D. Three Logos (枚举)'
type: post
url: /2015/09/codeforces322div2d-threelogos/
categories:
- ACM
tags:
- brute force
---




D. Three Logos







time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Three companies decided to order a billboard with pictures of their logos. A billboard is a big square board. A logo of each company is a rectangle of a non-zero area.




Advertisers will put up the ad only if it is possible to place all three logos on the billboard so that they do not overlap and the billboard has no empty space left. When you put a logo on the billboard, you should rotate it so that the sides were parallel to the sides of the billboard.




Your task is to determine if it is possible to put the logos of all the three companies on some square billboard without breaking any of the described rules.










Input




The first line of the input contains six positive integers _x_1, _y_1, _x_2, _y_2, _x_3, _y_3 (1 ≤ _x_1, _y_1, _x_2, _y_2, _x_3, _y_3 ≤ 100), where _x__i_ and _y__i_ determine the length and width of the logo of the _i_-th company respectively.










Output




If it is impossible to place all the three logos on a square shield, print a single integer "-1" (without the quotes).




If it is possible, print in the first line the length of a side of square _n_, where you can place all the three logos. Each of the next _n_ lines should contain _n_ uppercase English letters "A", "B" or "C". The sets of the same letters should form solid rectangles, provided that:





  * the sizes of the rectangle composed from letters "A" should be equal to the sizes of the logo of the first company,
  * the sizes of the rectangle composed from letters "B" should be equal to the sizes of the logo of the second company,
  * the sizes of the rectangle composed from letters "C" should be equal to the sizes of the logo of the third company,



Note that the logos of the companies can be rotated for printing on the billboard. The billboard mustn't have any empty space. If a square billboard can be filled with the logos in multiple ways, you are allowed to print any of them.




See the samples to better understand the statement.










Sample test(s)










input



    
    5 1 2 5 5 2










output



    
    5<br></br>AAAAA<br></br>BBBBB<br></br>BBBBB<br></br>CCCCC<br></br>CCCCC










input



    
    4 4 2 6 4 2










output



    
    6<br></br>BBBBBB<br></br>BBBBBB<br></br>AAAACC<br></br>AAAACC<br></br>AAAACC<br></br>AAAACC<br></br><br></br>题意很清楚．<br></br>给三个矩形，问能否拼成一个正方形．<br></br>我们先把矩形都躺着放（保证x<=y）<br></br>然后容易知道，一共有两种可能的方法<br></br>一种是三个矩形罗在一起<br></br>另外一种是一个矩形在上面，下面两个矩形竖着放．<br></br>后一种方法又因为上面的矩形的不同以及下面两个矩形的横竖放置不同（00 01 10 11）＊３<br></br>所以一共有１２种要枚举...<br></br>直接写会累死...<br></br>想了个简单点的办法，具体见代码．<br></br>一遍AC,好爽！！！




![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock55.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart55.gif)

 

    
    /*************************************************************************
    	> File Name: code/cf/#322/D.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年09月30日 星期三 17时21分24秒
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
    int ans;
    struct Point
    {
        int x,y;
    }p[10];
    char maze[110][110];
    int ss;
    int lst;
    int a[10],b[10];
    bool solve()
    {
        if (lst==-1) return false;
     //   cout<<"lst:"<<lst<<endl;
        if (p[0].x+p[1].x+p[2].x==p[0].y&&p[0].y==p[1].y&&p[0].y==p[2].y)
        {
    	ans = p[0].y;
    	for ( int i = 0 ; i < p[0].x ; i++)
    	{
    	    for ( int j = 0 ; j < ans ; j++)
    	    {
    		maze[i][j] = 'A';
    	    }
    	}
    	for ( int i = p[0].x ; i < p[0].x+p[1].x;i++)
    	{
    	    for ( int j = 0 ; j < ans ; j++)
    	    {
    		maze[i][j] = 'B';
    	    }
    	}
    	for ( int i = p[0].x + p[1].x ; i < ans ; i++)
    	{
    	    for ( int j = 0 ; j < ans ; j++)
    	    {
    		maze[i][j] = 'C';
    	    }
    	}
    	return true;
        }
    
        if (p[a[lst]].x+p[b[lst]].x==p[lst].y&&p[a[lst]].y==p[b[lst]].y&&p[a[lst]].y+p[lst].x==p[lst].y)
        {
    	ans = p[lst].y;
    	for ( int i = 0 ; i < p[lst].x ; i++)
    	{
    	    for ( int j =  0  ;  j < ans ; j++)
    	    {
    		maze[i][j] = char(lst+'A');
    	    }
    	}
    	for ( int i = p[lst].x ; i < ans ; i++)
    	{
    	    for ( int j = 0  ;  j < ans  ;j++)
    	    {
    		if (j<p[a[lst]].x)
    		{
    		    maze[i][j]=char(a[lst]+'A');
    		   // cout<<i<<" "<<j<<" "<<char(a[lst]+'A')<<endl;
    		}
    		else
    		{
    		    maze[i][j] = char (b[lst] + 'A');
    		}
    	    }
    	}
    	return true;
        }
    
        
        if (p[a[lst]].x+ p[b[lst]].y==p[lst].y&&p[a[lst]].y==p[b[lst]].x&&p[a[lst]].y+p[lst].x==p[lst].y)
        {
    	//cout<<"22222222222222222"<<endl;
    	ans = p[lst].y;
    	for ( int i = 0 ; i < p[lst].x ; i++)
    	{
    	    for ( int j = 0 ;  j < ans ; j ++)
    	    {
    		maze[i][j] = char(lst+'A');
    	    }
    	}
    	
    	for ( int i = p[lst].x ; i < ans ; i++)
    	{
    	    for ( int j = 0 ; j < ans ; j++)
    	    {
    		if (j<p[a[lst]].x)
    		{
    		    maze[i][j] =char(a[lst]+'A');
    		}
    		else
    		{
    		    maze[i][j] = char(b[lst]+'A');
    		}
    	    }
    	}
    	return true;
        }
    if (p[a[lst]].y+p[b[lst]].x==p[lst].y&&p[a[lst]].x==p[b[lst]].y&&p[a[lst]].x+p[lst].x==p[lst].y)
        {
    	//cout<<"3333333333333333333333"<<endl;
    	ans = p[lst].y;
    	for ( int i = 0 ; i < p[lst].x ; i++)
    	{
    	    for ( int j =  0  ;  j < ans ; j++)
    	    {
    		maze[i][j] = char(lst+'A');
    	    }
    	}
    	for ( int i = p[lst].x ; i < ans ; i++)
    	{
    	    for ( int j = 0  ;  j < ans  ;j++)
    	    {
    		if (j<p[a[lst]].y)
    		{
    		    maze[i][j]=char(a[lst]+'A');
    		}
    		else
    		{
    		    maze[i][j] = char (b[lst] + 'A');
    		}
    	    }
    	}
    	return true;
        }
    if (p[a[lst]].y+p[b[lst]].y==p[lst].y&&p[a[lst]].x==p[b[lst]].x&&p[a[lst]].x+p[lst].x==p[lst].y)
        {
    	//	cout<<"44444444444444444444444444"<<endl;
    	ans = p[lst].y;
    	for ( int i = 0 ; i < p[lst].x ; i++)
    	{
    	    for ( int j =  0  ;  j < ans ; j++)
    	    {
    		maze[i][j] = char(lst+'A');
    	    }
    	}
    	for ( int i = p[lst].x ; i < ans ; i++)
    	{
    	    for ( int j = 0  ;  j < ans  ;j++)
    	    {
    		if (j<p[a[lst]].y)
    		{
    		    maze[i][j]=char(a[lst]+'A');
    		 //   cout<<"haaa"<<a[lst]+'A'<<endl;
    		}
    		else
    		{
    		    maze[i][j] = char (b[lst] + 'A');
    		}
    	    }
    	}
    	return true;
        }
        return false;
    }
    int main()
    {
      #ifndef  ONLINE_JUDGE 
       freopen("in.txt","r",stdin);
      #endif
    
       ss = 0;
       lst = -1;
       a[0]=1;b[0]=2;
       a[1]=0;b[1]=2;
       a[2]=0;b[2]=1;
       for ( int i = 0 ; i < 3 ; i++) 
        {
    	scanf("%d %d",&p[i].x,&p[i].y);
    	if (p[i].x>p[i].y) swap(p[i].x,p[i].y);
    	ss += p[i].x*p[i].y;
        }
        for ( int i = 0 ; i < 3 ; i++)
        {
    	if (p[i].y*p[i].y==ss)
    	{
    	    lst = i;
    	}
        }
        if (solve())
        {
    	printf("%d\n",ans);
    	for ( int i = 0 ; i < ans ; i++)
    	{
    	    for ( int j = 0 ; j < ans ;  j++)
    	    {
    		printf("%c",maze[i][j]);
    	    }
    	    printf("\n");
    	}
        }
        else
        {
    	puts("-1");
        }
     #ifndef ONLINE_JUDGE  
      
        fclose(stdin);
      #endif
    	return 0;
    }
    



