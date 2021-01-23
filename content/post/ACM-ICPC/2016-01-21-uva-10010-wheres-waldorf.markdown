---
author: 111qqz
date: 2016-01-21 17:24:34+00:00
draft: false
title: uva 10010  - Where's Waldorf?
type: post
url: /2016/01/uva-10010-wheres-waldorf/
categories:
- ACM

tags:
- 字符串
---

https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=951
题意：给出一个由大小写字母组成的二维maze...给出k个询问。每个询问一个单词。问能否在maze中找到这个单词。不区分大小写。输出开头字母的坐标（从1开始）。如果有多组输出最上面的。如果还有多组，输出最左边的。数据保证至少有一组。
思路：直接找就好了。。。坑的地方是。。。格式。。数据组数之后会有一个空行。然后每**两组读入数据之间**会有一个空行。。输出的时候**每两组数据之间**也有一个空行。

我因为一直多输出了一个空行一直wa QAQ

= 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年01月21日 星期四 14时52分51秒
    File Name :code/uva/10010.cpp
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
    const int N=80;
    int n,m;
    char maze[N][N];
    string spa;
    int k;
    char target[100];
    char nouse[55];
    
    
    bool hang( int x,int y,char tar[])
    {
        int len = strlen(tar);
      //  cout<<"tar:"<<tar<<endl;
        if (y+len-1>=m) return false;
        int cnt = 0 ;
        for ( int j = y ; j < y+len; j++)
        {
    	if (maze[x][j]!=tar[cnt])
    	    return false;
    	cnt++;
        }
    
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    }
    bool rhang( int x,int y,char tar[])
    {
        int len = strlen(tar);
        if (y-len+1<0) return false;
        int cnt = 0 ;
        for ( int j = y ; j >=y-len+1 ; j-- )
        {
    	
    	if (maze[x][j]!=tar[cnt])
    	    return false;
    	cnt++;
        }
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    }
    
    bool lie( int x,int y,char tar[])
    {
        int len = strlen(tar);
        int cnt = 0 ;
        if (x+len-1>=n) return false;
        for ( int i = x ; i < x + len ; i++)
        {
    	if (maze[i][y]!=tar[cnt])
    	    return false;
    	cnt++;
        }
        
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    }
    
    bool rlie( int x,int y,char tar[])
    {
        int len = strlen(tar);
        int cnt = 0 ;
        if (x-len+1<0) return  false;
        for ( int i = x ; i>=x-len+1 ; i --)
        {
    	if (maze[i][y]!=tar[cnt]) return false;
    	cnt++;
        }
        cout<<x+1<<" "<<y+1<<endl;
        return true;
        
    }
    
    bool zx( int x,int y, char tar[])
    {
        int len = strlen(tar);
        int cnt = 0;
        if (y+len-1>=m||x+len-1>=n) return false;
    
        for ( int i = x ; i < x+len ; i++)
        {
    	if (maze[i][y+cnt]!=tar[cnt]) return false;
    	cnt++;
        }
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    
    }
    
    bool rzx ( int x,int y,char tar[])
    {
        int len = strlen(tar);
        int cnt = 0 ;
        if (y-len+1<0||x-len+1<0) return false;
        for ( int i = x ; i >= x-len+1 ; i--)
        {
    	if (maze[i][y-cnt]!=tar[cnt]) return false;
    	cnt++;
        }
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    }
    bool fx( int x,int y,char tar[])
    {
        int len = strlen(tar);
        int cnt = 0 ; 
        if (y-len+1<0||x+len-1>=m) return false;
    
        for ( int i = x ; i < x+len ; i++)
        {
    	if (maze[i][y-cnt]!=tar[cnt]) return false;
    	cnt++;
        }
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    }
    bool rfx( int x,int y,char tar[])
    {
        int len = strlen(tar);
        int cnt = 0 ;
        if (x-len+1<0||y+len-1>=m) return false;
        
        for ( int j = y ; j < y+len ; j++)
        {
    	if (maze[x-cnt][y]!=tar[cnt]) return false;
    	cnt++;
        }
        cout<<x+1<<" "<<y+1<<endl;
        return true;
    }
    
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int T;
    	scanf("%d",&T);
    	//getline(cin,spa);
    	scanf("*%s",nouse);
    	while (T--)
    	{
    	    scanf("%d%d",&n,&m); //习惯用n表示行。。。与题目相反。
    	    for  ( int i = 0 ;i  < n ; i++)
    	    {
    		scanf("%s",maze[i]);
    		for ( int j = 0 ; j < m ; j++)
    		{
    		    maze[i][j]=toupper(maze[i][j]);
    		}
    	    }
    
    	    //for ( int i = 0 ; i < n ; i++) cout<<maze[i]<<endl;
    
    	    scanf("%d",&k);
    	
    	    while (k--)
    	    {
    		scanf("%s",target);
    		int len ;
    		len = strlen(target);
    		bool ok = false;
    		for (  int i = 0 ;i < len ; i++) target[i] = toupper(target[i]);
    	//	cout<<"target:"<<target<<endl;
    		for ( int i = 0 ; i < n ;i++)
    		{
    		    for ( int j = 0 ; j < m ; j++)
    		    {
    			if( rzx(i,j,target)||rlie(i,j,target)||rfx(i,j,target)||rhang(i,j,target)||hang(i,j,target)||fx(i,j,target)||lie(i,j,target)||zx(i,j,target)) 
    			{
    			    ok = true;
    			    break;
    			}
    		    }
    		    if (ok) break;
    		}
    	    }
    
    	    if (T!=0)
    	    {
    		scanf("*%s",nouse);
    		cout<<endl;
    	    }
    
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



