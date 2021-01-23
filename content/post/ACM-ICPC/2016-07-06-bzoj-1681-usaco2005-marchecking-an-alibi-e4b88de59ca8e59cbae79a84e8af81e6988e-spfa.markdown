---
author: 111qqz
date: 2016-07-06 13:18:30+00:00
draft: false
title: 'BZOJ 1681: [Usaco2005 Mar]Checking an Alibi 不在场的证明 (spfa)'
type: post
url: /2016/07/bzoj-1681-usaco2005-marchecking-an-alibi--spfa/
categories:
- ACM
tags:
- spfa
- 最短路
---




## 1681: [Usaco2005 Mar]Checking an Alibi 不在场的证明


Time Limit: 5 Sec  Memory Limit: 64 MB
Submit: 250  Solved: 178
[[Submit](http://www.lydsy.com/JudgeOnline/submitpage.php?id=1681)][[Status](http://www.lydsy.com/JudgeOnline/problemstatus.php?id=1681)][[Discuss](http://www.lydsy.com/JudgeOnline/bbs.php?id=1681)]


## Description






A crime has been comitted: a load of grain has been taken from the barn by one of FJ's cows. FJ is trying to determine which of his C (1 <= C <= 100) cows is the culprit. Fortunately, a passing satellite took an image of his farm M (1 <= M <= 70000) seconds before the crime took place, giving the location of all of the cows. He wants to know which cows had time to get to the barn to steal the grain. Farmer John's farm comprises F (1 <= F <= 500) fields numbered 1..F and connected by P (1 <= P <= 1,000) bidirectional paths whose traversal time is in the range 1..70000 seconds (cows walk very slowly). Field 1 contains the barn. It takes no time to travel within a field (switch paths). Given the layout of Farmer John's farm and the location of each cow when the satellite flew over, determine set of cows who could be guilty. NOTE: Do not declare a variable named exactly 'time'. This will reference the system call and never give you the results you really want.


    谷仓里发现谷物被盗！约翰正试图从C(1≤C≤100)只奶牛里找出那个偷谷物的罪犯．幸运的是，一个恰好路过的卫星拍下谷物被盗前M(1≤M≤70000)秒的农场的图片．这样约翰就能通过牛们的位置来判断谁有足够的时间来盗窃谷物．




    约翰农场有F(1≤F≤500)草地，标号1到F，还有P(1≤P≤1000)条双向路连接着它们．通过这些路需要的时间在1到70000秒的范围内．田地1上建有那个被盗的谷仓． 给出农场地图，以及卫星照片里每只牛所在的位置．请判断哪些牛有可能犯罪．










## Input






* Line 1: Four space-separated integers: F, P, C, and M * Lines 2..P+1: Three space-separated integers describing a path: F1, F2, and T. The path connects F1 and F2 and requires T seconds to traverse. * Lines P+2..P+C+1: One integer per line, the location of a cow. The first line gives the field number of cow 1, the second of cow 2, etc.

第1行输入四个整数F，只C，和M;

接下来P行每行三个整数描述一条路，起点终点和通过时间．


接下来C行每行一个整数，表示一头牛所在的地点．







## Output






* Line 1: A single integer N, the number of cows that could be guilty of the crime.

* Lines 2..N+1: A single cow number on each line that is one of the cows that could be guilty of the crime. The list must be in ascending order.


    第1行输出嫌疑犯的数目，接下来一行输出一只嫌疑犯的编号．







## Sample Input




7 6 5 8
1 4 2
1 2 1
2 3 6
3 5 5
5 4 6
1 7 9
1
4
5
3
7





## Sample Output




4
1
2
3
4





## HINT






![](http://www.lydsy.com/JudgeOnline/upload/201401/44(4).jpg)







思路： 非常显然的最短路。。。。一个月没写代码还能1A...感动








 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年07月06日 星期三 20时48分00秒
    File Name :code/bzoj/1681.cpp
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
    const int N=1E3+6;
    int n,m,cow,T;
    vector < pi > edge[N];
    
    int d[N];
    bool inq[N];
    int posi[N];
    vector <int>ans;
    void spfa( int s)
    {
        ms(inq,false);
        ms(d,0x3f);
    
        queue<int>q;
        q.push(s);
        d[s] =  0;
        inq[s] = true;
    
        while (!q.empty())
        {
    	int u = q.front();
    	q.pop();
    	inq[u] = false;
    
    	int siz = edge[u].size();
    
    	for ( int i = 0 ; i < siz ; i ++)
    	{
    	    int v = edge[u][i].fst;
    	    if (d[v]>d[u]+edge[u][i].sec)
    	    {
    		d[v] = d[u] + edge[u][i].sec;
    		if (inq[v]) continue;
    		inq[v] = true;
    		q.push(v);
    
    	    }
    	}
    
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	scanf("%d%d%d%d",&n,&m,&cow,&T);
    	
    	for (int i = 1 ; i <= m ; i++)
    	{
    	    int u,v,w;
    	    scanf("%d%d%d",&u,&v,&w);
    	    edge[u].push_back(make_pair(v,w));
    	    edge[v].push_back(make_pair(u,w));
    	}
    	
    	for ( int i = 1 ; i <= cow ; i++) scanf("%d",&posi[i]);
    	spfa(1);
    
    	for ( int i = 1 ; i <= cow ;  i++)
    	{
    	    if (d[posi[i]]<=T) ans.push_back(i);
    	}
    	printf("%d\n",ans.size());
    	for ( int i = 0 ; i < ans.size() ; i++) printf("%d\n",ans[i]);
    
    	    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



