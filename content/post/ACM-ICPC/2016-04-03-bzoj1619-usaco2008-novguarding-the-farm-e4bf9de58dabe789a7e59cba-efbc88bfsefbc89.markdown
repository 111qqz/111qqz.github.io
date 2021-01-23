---
author: 111qqz
date: 2016-04-03 17:23:04+00:00
draft: false
title: 'BZOJ1619: [Usaco2008 Nov]Guarding the Farm 保卫牧场 （BFS）'
type: post
url: /2016/04/bzoj1619-usaco2008-novguarding-the-farm--bfs/
categories:
- ACM
tags:
- bfs
- dfs
---




## 1619: [Usaco2008 Nov]Guarding the Farm 保卫牧场


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 661  Solved: 292
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1619)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1619)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1619)]


## Description






The farm has many hills upon which Farmer John would like to place guards to ensure the safety of his valuable milk-cows. He wonders how many guards he will need if he wishes to put one on top of each hill. He has a map supplied as a matrix of integers; the matrix has N (1 < N <= 700) rows and M (1 < M <= 700) columns. Each member of the matrix is an altitude H_ij (0 <= H_ij <= 10,000). Help him determine the number of hilltops on the map. A hilltop is one or more adjacent matrix elements of the same value surrounded exclusively by either the edge of the map or elements with a lower (smaller) altitude. Two different elements are adjacent if the magnitude of difference in their X coordinates is no greater than 1 and the magnitude of differences in their Y coordinates is also no greater than 1.



农夫JOHN的农夫上有很多小山丘，他想要在那里布置一些保镖（……）去保卫他的那些相当值钱的奶牛们。 他想知道如果在一座小山丘上布置一名保镖的话，他总共需要招聘多少名保镖。他现在手头有一个用数字矩阵来表示地形的地图。这个矩阵有N行（1 < N < = 100)和M列( 1 < M < = 70) 。矩阵中的每个元素都有一个值H_ij(0 < = H_ij < =10,000)来表示该地区的海拔高度。请你帮助他统计出地图上到底有多少个小山丘。 小山丘的定义是：若地图中一个元素所邻接的所有元素都比这个元素高度要小（或它邻接的是地图的边界），则该元素和其周围所有按照这样顺序排列的元素的集合称为一个小山丘。这里邻接的意义是：若一个元素与另一个横坐标纵坐标和它的横纵坐标相差不超过1，则称这两个元素邻接。 问题名称：guard 输入格式： 第一行：两个由空格隔开的整数N和M 第二行到第N+1行：第I+1行描述了地图上的第I行，有M个由空格隔开的整数：H_ij.






## Input






* Line 1: Two space-separated integers: N and M

* Lines 2..N+1: Line i+1 describes row i of the matrix with M space-separated integers: H_ij






## Output






* Line 1: A single integer that specifies the number of hilltops






## Sample Input




8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0




## Sample Output




3





## HINT







   三个山丘分别是：左上角的高度为4的方格，右上角的高度为1的方格，还有最后一行中高度为2的方格．







## Source






[Silver](http://www.lydsy.com/JudgeOnline/problemset.php?search=Silver)




[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1619)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1619)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1619)]
[HOME](http://www.lydsy.com/JudgeOnline/) Back\





**题目的中文描述的数据范围有问题！**

**题目的中文描述的数据范围有问题！**

**题目的中文描述的数据范围有问题！**

思路：BFS,我的做法是预处理所有“坏点”，也就是如果点（i,j）的相邻点中有比点（i,j）高的，那么点(i,j)就是坏点。

然后bfs的时候，对于存在一个坏点的联通块（只有数字相同的点能构成一个联通块）都标记成坏点。

**然后用左上角开始做bfs...注意遇到坏点跳过但是不要直接标记访问，因为可能之后的点会用到之前的坏点标记自身。**

然而因为数据范围有问题wa了好多次。。。

于是看了题解：

大概都是另一种做法（而且都加入了输入挂，不懂，怎么感觉这些人是互相抄的2333）

从最高的点开始做dfs，每次把不大于当前点高度的点都访问掉。。。算作一次访问。

访问次数就是答案。

想了下确实比较巧妙，比较好写，然而比我的写法要慢。

然而窝不懂为什么这种写法数组开小就是返回RE,而我的写法数组开销就是返回WA...

[![选区_049](https://111qqz.com/wordpress/wp-content/uploads/2016/04/选区_049.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/04/选区_049.png)



我的做法（800ms,bfs）：



    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月03日 星期日 20时01分12秒
    File Name :code/bzoj/1619.cpp
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
    const int dx8[8]={1,1,1,0,0,-1,-1,-1};
    const int dy8[8]={1,0,-1,-1,1,1,0,-1};
    const int inf = 0x3f3f3f3f;
    const int N=705;
    int h[N][N];
    bool bad[N][N];
    int n,m;
    bool vis[N][N];
    void checkvis();
    
    struct node
    {
        int x,y;
    
        bool inmaze ()
        {
    	if (x>=1&&y>=1&&x<=n&&y<=m)  return true;
    	return false;
        }
    
        void look()
        {
    	cout<<x<<" "<<y<<endl;
        }
    }s;
    bool ok ( int x,int y)
    {
     //   if (x-1>=1&&h[x-1][y]>h[x][y])  return false;
     //   if (x+1<=n&&h[x+1][y]>h[x][y])  return false;
     //   if (y-1>=1&&h[x][y-1]>h[x][y])  return false;
     //   if (y+1<=m&&h[x][y+1]>h[x][y])  return false;
    
        for ( int i = 0 ; i < 8 ; i++)
        {
    	int nx = x + dx8[i];
    	int ny = y + dy8[i];
    	if (nx<1||nx>n||ny<1||ny>m) continue;
    	if (h[nx][ny]>h[x][y]) return false;
        }
        return true;
    }
    
    
    bool bfs( int x,int y)
    {
        queue<node>q;
        s.x = x;
        s.y = y;
        q.push(s);
        vis[x][y] = true;
        bool res = true;
        while (!q.empty())
        {
    	node pre = q.front() ;q.pop();
    //	pre.look();
    //	checkvis();
    	if (!res) bad[pre.x][pre.y] = true;
    
    
    	for ( int i = 0 ; i < 8 ; i++)
    	{
    	    node nxt;
    	    nxt.x = pre.x + dx8[i];
    	    nxt.y = pre.y + dy8[i];
    	    if (!nxt.inmaze()) continue;
    	    if (vis[nxt.x][nxt.y]) continue;
    	  //  vis[nxt.x][nxt.y] = true;
    	    if (h[nxt.x][nxt.y]!=h[pre.x][pre.y]) continue;
    	    if (bad[nxt.x][nxt.y])
    	    {
    		res = false;
    	    }
    	    if (!ok(nxt.x,nxt.y))
    	    {
    		res = false;
    	    }
    //	    nxt.look();
    	    q.push(nxt);
    	    vis[nxt.x][nxt.y] = true;
    	}
        }
    
        return res;
    
    }
    
    void checkbad()
    {
        for ( int i = 1 ; i <= n ; i++)
        {
    	for ( int j = 1 ; j <= m ; j++)
    	{
    	    cout<<bad[i][j]<<" ";
    	}
    	cout<<endl;
        }
    }
    
    void checkvis()
    {
        for ( int i = 1 ; i <= n ; i++)
        {
    	for ( int j = 1 ; j <= m ; j++)
    	{
    	    cout<<vis[i][j]<<" "; 
    	}
    	cout<<endl;
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	ios::sync_with_stdio(false);
    	cin>>n>>m;
    	for ( int i = 1 ; i <= n ; i++)
    	    for ( int j = 1 ; j <= m ; j++) cin>>h[i][j];
    	ms(bad,false);
    
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    for ( int j = 1 ; j <= m ; j++)
    	    {
    		if (!ok(i,j)) bad[i][j] = true;
    	    }
    	}
    	ms(vis,false);
    //	checkbad();
    	int ans = 0 ;
    	for ( int i = 1 ; i <= n ; i++)
    	{
    	    for ( int j = 1 ; j  <= m ; j++)
    	    {
    		if (vis[i][j]) continue;
    		if (bad[i][j]) continue;
    		if (bfs(i,j))
    		{
    		    ans++;
    		  //  cout<<i<<" "<<j<<endl;
    		}
    	//	else cout<<"bad:"<<endl;
    	    }
    	}
    
    	cout<<ans<<endl;
    
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




网上题解的做法（940ms,dfs）：

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年04月03日 星期日 21时33分17秒
    File Name :code/bzoj/r1619.cpp
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
    #include <assert.h>
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
    const int dx8[8]={1,1,1,0,0,-1,-1,-1};
    const int dy8[8]={-1,0,1,1,-1,-1,0,1};
    const int inf = 0x3f3f3f3f;
    const int N=705;
    int n,m;
    bool vis[N][N];
    int he[N][N];
    
    struct node
    {
        int x,y;
        int val;
    
        bool operator < (node b)const
        {
    	return val>b.val;
        }
    }h[N*N];
    
    inline int read()
    {
        int x=0,f=1;char ch=getchar();
        while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
        while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
        return x*f;
    }
    void dfs ( int x,int y)
    {
        vis[x][y] = true;
        for ( int i = 0 ; i < 8 ; i++)
        {
    	int nx = x + dx8[i];
    	int ny = y + dy8[i];
    		
    	if (nx<1||ny<1||nx>n||ny>m) continue;
    	if (he[x][y]<he[nx][ny]) continue;
    	if (vis[nx][ny]) continue;
    	dfs(nx,ny);
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n>>m;
    	int cnt = 0 ;
    	for ( int i = 1 ; i <= n ; i++)
    	    for ( int j = 1 ; j <= m ; j++)
    	    {	
    		    cin>>he[i][j];
    		    cnt++;
    		    h[cnt].x = i;
    		    h[cnt].y = j;
    		    h[cnt].val = he[i][j];
    	    }
    
    	sort(h+1,h+cnt+1);
    	ms(vis,false);
    
    	int ans = 0 ;
    	for ( int i = 1 ; i <= cnt ; i++)
    	{
    	    int x = h[i].x;
    	    int y = h[i].y;
    	    assert(x>=1&&x<N);
    	    assert(y>=1&&y<N);
    	    if (!vis[x][y])
    	    {
    		dfs(x,y);
    		ans++;
    	    }
    	    
    	}
    
    	cout<<ans<<endl;
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    
