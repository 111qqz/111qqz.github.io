---
author: 111qqz
date: 2016-11-19 16:50:11+00:00
draft: false
title: 'Mutual Training for Wannafly Union #1'
type: post
url: /2016/11/mutual-training-for-wannafly-union-1/
categories:
---

[比赛链接](http://vjudge.net/contest/142053#overview)

题外话：


<blockquote>wannafly union:可能有的学校不能很好得传承……可能某一时间可以进过两三次final ……但是final队过后，这个学校就退出了历史的舞台……</blockquote>




说实话我依然记得我入学那年，也就是14年，看到了华科又一次进final，然后15年仿佛已经开始走下坡路，到了16年，icpc连快银都没有....见证了hust的衰落，我的内心是格外凄凉的。

而又不仅仅是见证...内心是有些愧疚的....总觉得自己没能把某些传统传承下去。。。。

曾经我以为学校的荣誉轮不到我去争取，毕竟我实力很弱，高中noip虽然有全省第二...但是大弱省....其实我当年只有275分...

14级的一队...pyy+zk+tm，三个人都是初一就开始参加比赛了....而且湖南+广东+安徽....

其他人，也至少比我发展均衡....

所以之前想着...弱鸡如我好好提高学校的下限就好了....

但是现在发现并不是那么一回事...

其实每个人...都是和学校相关的....

即使最后轮不到我...但是应该仍然有这个想法才对吧....



好了正题：

这次比赛只做出了三道题，A题之前遇到过，当时不会，忘记补了。目测E题也可以补，不过明天约了妹子自习估计要早睡，所以考完试再说吧。

A：

题意：有一个3*n的maze，一个人初始在最左边的某个格子里（3个中的一个，用s表示），然后有若干由大写字母组成的火车...

每一次运动中：人先向右移动一个格子，然后选择不动，或者向上或者向下（具体取决于现在处在3行中的哪一行），之后每列火车向左移动2个格子。如果某个时刻人和火车位于同一个格子，那么人就狗带了。人的获胜条件是到达最右边。

思路：比赛的时候脑抽。。。竟然觉得是指数模型。。。。然后就觉得想错了orz

这道题可以考虑物理的相对运动，我们可以认为火车是不动的，而人时先向右一个格子，然后换行（或者不换）,然后再向右两个

这样直接bfs搞一下就好咯。。。。果然是水题。。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月19日 星期六 18时56分06秒
    File Name :code/wfly/#1/A.cpp
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
    const int N=3E3+15;
    int n,k;
    char maze[4][N];
    struct node
    {
        int x,y;
        void out()
        {
    	printf("x:%d y : %d\n",x,y);
        }
    }s;
    int a[3][N];
    bool vis[3][N];
    bool ok;
    void bfs()
    {
        ms(vis,false);
        queue<node>q;
        while (!q.empty()) q.pop();
        q.push(s);
        vis[s.x][s.y] = true;
        while (!q.empty())
        {
    	node pre = q.front();
    //	pre.out();
    	q.pop();
    	if (pre.y>=3*n-2) 
    	{
    	    ok = true;
    	    return;
    	}
    	if (a[pre.x][pre.y+1]) continue; //走一步死。
    	for ( int i = 0 ; i < 3 ; i++)
    	{
    	    if (abs(i-pre.x)>=2) continue ; //一次只能移动一步。
    	    if (a[i][pre.y+1]) continue; //必须有空完成上下移动。
    	    if (a[i][pre.y+2]) continue; 
    	    if (a[i][pre.y+3]) continue;
    	    if (vis[i][pre.y+3]) continue;
    	    vis[i][pre.y+3] = true;
    	    node tmp;
    	    tmp.x = i;
    	    tmp.y = pre.y+3;
    	    q.push(tmp);
    	}
        }
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	int T;
    	cin>>T;
    	while (T--)
    	{
    	    scanf("%d%d",&n,&k);
    	    for ( int i = 0 ; i < 3 ; i++) scanf("%s",maze[i]);
    	    for ( int i = 0 ; i < 3 ; i++)
    	    {
    		if (maze[i][0]=='s')
    		{
    		    s.x = i ;
    		    s.y = 0 ;
    		}
    	    }
    	    ms(a,0); // !!!
    	    for ( int i = 0 ; i < 3 ; i++)
    	    {
    		for ( int j = 0 ; j < n ; j++)
    		{
    		    if (maze[i][j]=='.'||maze[i][j]=='s') a[i][j] = 0;
    		    else a[i][j] = 1 ;
    		}
    	    }
    	 /*   for ( int i = 0 ; i < 3 ; i++)
    	    {
    		for ( int j = 0 ; j < n ; j++) printf("%d",a[i][j]);
    		printf("\n");
    	    } */
    	    ok = false;
    	    bfs();
    	    if (ok)
    	    {
    		puts("YES");
    	    }
    	    else
    	    {
    		puts("NO");
    	    }
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




B: 题意：一个字符串，长度最长为10，由小写字母组成，恰好插入一个字母使其变成回文串的方法...

思路：一开始竟然傻傻得分情况讨论。。。。各种漏。。日。。。后来一看数据范围。。。直接暴力。枚举插入的位置和插入的字母。。然后check。复杂度。。10×10*10*26.。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月19日 星期六 20时03分25秒
    File Name :code/wfly/#1/BB.cpp
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
    vector<char>ans;
    bool check()
    {
        int siz = ans.size();
        for ( int i = 0 ; i < siz ; i++)
        {
    	if (ans[i]!=ans[siz-1-i]) return false;
        }
        return true;
    }
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("code/in.txt","r",stdin);
    #endif
        string st;
        cin>>st;
        int len = st.length();
        for ( int i = 0 ; i < len ; i++)
        {
    	for ( int j = 0;  j< 26 ; j++)
    	{
    	    char ch = j +'a';
    	    ans.clear();
    	    for ( int k = 0 ; k < len ; k++)
    	    {
    		if (k==i) ans.push_back(ch);
    		ans.push_back(st[k]);
    	    }
    	//    for ( int k = 0 ; k < ans.size();  k++) printf("%c   ",ans[k]);
    	//    printf("\n");
    	    if (check())
    	    {
    		int siz = ans.size();
    		for ( int ii = 0 ; ii < siz; ii++)
    		{
    		    printf("%c",ans[ii]);
    		}
    		return 0;
    	    }
    	    ans.clear();
    //	    cout<<"st:"<<st<<" ch:"<<ch<<endl;
    	    for ( int k = 0 ; k < len ; k++) ans.push_back(st[k]);
    	    ans.push_back(ch);
    	//    for ( int k = 0 ; k < ans.size() ; k++) printf("%c ",ans[k]);
    	    if (check())
    	    {
    		int siz = ans.size();
    		for ( int ii = 0 ; ii < siz; ii++)
    		{
    		    printf("%c",ans[ii]);
    		}
    		return 0;
    	    }
    	}
        }
        puts("NA");
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
    




D:n*n的格子，初始白皇后在(1,1)，黑皇后在(1,n)，其他点被士兵覆盖（士兵不会动。。。）皇后每次可以横竖或者对角线，走到一个有士兵（或者地方皇后）的位置并吃掉。。。（每次移动必须吃掉士兵或者地方皇后）

白皇后先走，问双方都最优策略。。。谁必赢。。如果白必赢，输出第一步的走的方案。

思路：其实算是构造题。。。？手画一下发现。。。只和奇偶性有关2333，结论很容易发现。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月19日 星期六 20时47分53秒
    File Name :code/wfly/#1/D.cpp
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
    int n;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n;
    	if (n%2==1)
    	{
    	    puts("black");
    	}
    	else
    	{
    	    puts("white");
    	    puts("1 2");
    	}
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




F：题意：猜数游戏。。四种猜法。。大于，大于等于，小于，小于等于。。。并且给出每次猜得对还是错。。。问最后这个数是否存在。。

思路：维护一个L,R。。。最后看L<=R是否成立即可。。。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月19日 星期六 20时21分42秒
    File Name :code/wfly/#1/F.cpp
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
    int n;
    char opt[3];
    int x;
    char cmd[3];
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("code/in.txt","r",stdin);
    #endif
        scanf("%d",&n);
        int L,R;
        L = -2E9;
        R = 2E9;
        for ( int i = 1; i <= n ; i++)
        {
    	scanf("%s %d %s",opt,&x,cmd);
    	if (opt[0]=='>')
    	{
    	    if (opt[1]=='=')
    	    {
    		if (cmd[0]=='Y')
    		{
    		    L = max(L,x);		    
    		}
    		else
    		{
    		    R = min(R,x-1);
    		}
    	    }
    	    else
    	    {
    		if (cmd[0]=='Y')
    		{
    		    L = max(L,x+1);
    		}
    		else
    		{
    		    R = min(R,x);
    		}
    	    }
    	}else
    	{
    	    if (opt[1]=='=')
    	    {
    		if (cmd[0]=='Y')
    		{
    		    R = min(R,x);
    		}
    		else
    		{
    		    L = max(L,x+1);
    		}
    	    }
    	    else
    	    {
    		if (cmd[0]=='Y')
    		{
    		    R = min(R,x-1);
    		}
    		else
    		{
    		    L =max(L,x);
    		}
    	    }
    	}
        }
        if (L<=R)
        {
    	printf("%d\n",L);
        }
        else
        {
    	puts("Impossible");
        }
    
    
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
    









