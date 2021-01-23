---
author: 111qqz
date: 2015-07-27 11:01:00+00:00
draft: false
title: I - Fire Game  (两个点开始的bfs)
type: post
url: /2015/07/i-firegamebfs/
categories:
- ACM
tags:
- bfs
---




http://acm.hust.edu.cn/vjudge/contest/view.action?cid=83084#problem/I




I - Fire Game


**Time Limit:**1000MS **Memory Limit:**32768KB **64bit IO Format:**%I64d & %I64u


Submit [Status](http://acm.hust.edu.cn/vjudge/contest/view.action?cid=83084#status//I/0)













Description







Fat brother and Maze are playing a kind of special (hentai) game on an N*M board (N rows, M columns). At the beginning, each grid of this board is consisting of grass or just empty and then they start to fire all the grass. Firstly they choose two grids which are consisting of grass and set fire. As we all know, the fire can spread among the grass. If the grid (x, y) is firing at time t, the grid which is adjacent to this grid will fire at time t+1 which refers to the grid (x+1, y), (x-1, y), (x, y+1), (x, y-1). This process ends when no new grid get fire. If then all the grid which are consisting of grass is get fired, Fat brother and Maze will stand in the middle of the grid and playing a MORE special (hentai) game. (Maybe it's the OOXX game which decrypted in the last problem, who knows.)




You can assume that the grass in the board would never burn out and the empty grid would never get fire.




Note that the two grids they choose can be the same.













Input







The first line of the date is an integer T, which is the number of the text cases.




Then T cases follow, each case contains two integers N and M indicate the size of the board. Then goes N line, each line with M character shows the board. "#" Indicates the grass. You can assume that there is at least one grid which is consisting of grass in the board.




1 <= T <=100, 1 <= n <=10, 1 <= m <=10













Output







For each case, output the case number first, if they can play the MORE special (hentai) game (fire all the grass), output the minimal time they need to wait after they set fire, otherwise just output -1. See the sample input and output for more details.













Sample Input







4 3 3




.#.




###




.#.




3 3




.#.




#.#




.#.




3 3




...




#.#




...




3 3




###




..#




#.#










Sample Output







Case 1: 1




Case 2: -1




Case 3: 0




Case 4: 2













其实一开始是没什么思路的....因为要从两个点开始,太弱,没做过这样的.




然后我看了下数据,如果枚举着火的起点 10*10*10*10*100  10^6,再*bfs的时间复杂度.......




不过这是考虑所有点都是草的情况下,而且实际上枚举的时候两个点是无序的,只需要枚举一半就行...




虽然心里没什么底,我抱着写一发交上去试试tle掉又不会怀孕的心态写了下....







写的时候有两个地方卡了一下




一个是我不知道怎么表示两个点是同时烧的




bfs的时候万一写成了一个点都烧完,另一个点才开始烧,这肯定是错误的.




然后脑子里隐约记得什么控制步数blablabla,但是记得不清....




然后再一想,不用啊,两个点开始烧,我就把两个点初始化为0不就表示两个点开始烧了?







第二个地方小卡了一下,如果烧光,那答案是哪个点?




换句话说,哪个点的代价是最大的




显然是最后的那个点啊2333




然后写完了,交,竟然他妈过了....




喜极而泣!




好开心!




```c++
 
 

    
    /*************************************************************************
    	> File Name: code/2015summer/searching/I.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年07月27日 星期一 18时25分27秒
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
    const int N=1E2+5;
    const int inf = 0x7fffffff;
    int x[N],y[N];
    int cnt;
    int m,n;
    char maze[11][11];
    int d[11][11];
    int dx[4]={0,0,-1,1};
    int dy[4]={1,-1,0,0};
    int k;
    
    bool ok (int x,int y)
    {
        if (x>=0&&x<n&&y>=0&&y<m&&maze[x][y]=='#'&&d[x][y]==-1)
    	  return true;
        return false;
    }
    int bfs(int x1,int y1,int x2,int y2)
    {
        memset(d,-1,sizeof(d));
        queue<int>x;
        queue<int>y;
        x.push(x1);
        x.push(x2);
        y.push(y1);
        y.push(y2);
        d[x1][y1]=0;
        d[x2][y2]=0;
        cnt = 2;
        while (!x.empty()&&!y.empty())
        {
    	  int px = x.front();x.pop();
    	  int py = y.front();y.pop();
    //	  cout<<"px:"<<px<<" py:"<<py<<endl;
    	  int tx,ty;
    	  for ( int i = 0 ; i < 4 ; i++ )
    	  {
    		   int  nx = px + dx[i];
    		   int  ny = py + dy[i];
    		if (ok(nx,ny))
    		{
    		    d[nx][ny]=d[px][py]+1;
    		    x.push(nx);
    		    y.push(ny);
    		    cnt++;
    		    tx = nx;
    		    ty = ny;
    		}
    	  }
    	  if (cnt>=k)
    	  {
    		return  d[tx][ty]; //最后一次烧到的点一定是最远的点
    	  }
    
        }
        return inf;
    }
    int main()
    {
        int T;
        cin>>T;
        int cas = 0;
        while (T--)
        {
    	  cas++;
    	  scanf("%d %d",&n,&m);
    	  for ( int i = 0 ; i < n ; i++ )
    	  {
    		scanf("%s",maze[i]);
    	  }
    	   k = 0 ;
    	  for ( int i = 0 ; i < n ; i++ )
    	  {
    		for ( int j = 0 ; j  < m ; j++ )
    		{
    		    if (maze[i][j]=='#')
    		    {
    			  k++;
    			  x[k]=i;
    			  y[k]=j;
    		    }
    		}
    	  }
    	  if (k<=2)
    	  {
    
    		printf("Case %d: %d\n",cas,0);
    		continue;
    	  }
    	  int ans = inf;
    	  for ( int i = 1 ; i <= k ;  i++ )
    	  {
    		for ( int j = i ; j <= k ; j++ )
    		{
    		    cnt = 0 ;
    		    ans = min(ans,bfs(x[i],y[i],x[j],y[j]));
    		}
    	  }
    	  if (ans!=inf) 
    	  printf("Case %d: %d\n",cas,ans);
    	  else printf("Case %d: %d\n",cas,-1);
    
        }
      
    	return 0;
    }
    


```
