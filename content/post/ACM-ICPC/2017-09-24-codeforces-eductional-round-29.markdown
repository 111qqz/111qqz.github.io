---
author: 111qqz
date: 2017-09-24 08:47:13+00:00
draft: false
title: Codeforces eductional round  29
type: post
url: /2017/09/codeforces-eductional-round-29/
categories:
- ACM
---

[比赛链接](http://codeforces.com/contest/863)

10个月没写题了，菜啊。进行一点恢复性训练好了。

A: 给一个数，可以在填写若干（或者0）个前缀0，问能否变成回文数。

思路是直接删掉后面可能的出现的0再判断回文数就好。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年09月24日 星期日 13时51分06秒
    File Name :A.cpp
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
    #define PB push_back
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
    bool check( int x)
    {
        vector<int>val;
        while (x)
        {
        int tmp = x;
        val.push_back(tmp);
        x/=10;
        }
        int siz = val.size();
        if (siz==1) return true;
        for ( int i = 0 ; i < siz/2 ; i++)
        {
        if (val[i]!=val[siz-1-i]) return false;
        }
        return true;
    }
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        //freopen("./in.txt","r",stdin);
      #endif
        int x;
        cin>>x;
        while(x==0)
        {
            x/=10;
        }
        if (check(x)) puts("YES");
        else puts("NO");
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





B: 2*n个人，每个人的重量为w[i],要分成n-1组，每组2个人，以及2个单独的人。单独的人的不稳定性为0,每组的不稳定是该组的2个人的重量的差的绝对值。总的不稳定为所有组的不稳定性之和。问可能的最小不稳定性是多少。

思路：由于n才50,100个人，暴力枚举单独的人，复杂度O(n_n_nlg(n)),很稳。 注意n给的是组数，所以数组最大值应该为100而不是50.


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年09月24日 星期日 13时57分04秒
    File Name :B.cpp
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
    #define PB push_back
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
    const int N=107;
    int n;
    int w[N];
    bool single[N];
    void print( vector<int> x)
    {
        int siz = x.size();
        for ( int i = 0 ; i < siz ; i++) printf("%d ",x[i]);
        printf("\n");
    }
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        cin>>n;
        n*=2;
        ms(single,false);
        int ret = inf;
        int sum = 0;
        for ( int  i = 1 ; i <= n ; i++) scanf("%d",&w[i]);
        for ( int i = 1 ; i <= n  ; i++)
        {
            single[i] = true;
            for ( int j = i+1 ; j<= n ;j++)
            {
            single[j] = true;
            vector<int>team;
            for ( int k = 1 ; k <= n ; k++)
                if (!single[k]) team.push_back(w[k]);
            sort(team.begin(),team.end());
    //      print(team);
            //cout<<"team_size:"<<team.size()<<endl;
            int siz = team.size();
            sum =  0;
            for ( int i = 0 ; i < siz ; i+=2)
            {
                sum = sum + abs(team[i]-team[i+1]);
            }
            ret = min(ret,sum);
            single[j]=false;
            }
            single[i]=false;
        }
        printf("%d\n",ret);
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    





C: Ali和Bob两个机器人进行一个类似”石头剪子布"的游戏，每次2个机器人同时出{1,2,3}中的一个。 2 beats 1, 3 beats 2 , 1 beats 3. 赢的得1分，输的得0分。数字一样2人都不得分。2个机器人当前回合的策略（也就是出哪个数字）只取决于上一回合2个机器人出的数字。并且规则完全已知，会用2张3*3的表的形式给出。现在要进行k场游戏，问最后的分数是多少。

思路：由于k比较大，所有可能的分数序列(x,y)又非常有限，因此显然是求个循环节搞。

需要注意几点：




      1. k的大小太小，比循环节开始的第一个位置还小
      2. K是LL类型，各种和k有关的变量也要记得是LL类型
      3. 为了寻找循环节第一次出现的位置，将循环节第二次的开始存了进去，但是在算一个循环节的分数以及其他的时候，记得不要把这个多余的一次算进去。



    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年09月24日 星期日 14时26分54秒
    File Name :C.cpp
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
    #define PB push_back
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
    LL k;
    int x,y;
    int a[5][5],b[5][5];
    map< pair<int,int>,bool >mp;
    vector < pair<int,int> >seq; //记录游戏序列，肯定不会很长。
    int nx( int x,int y)
    {
        return a[x][y];
    }
    int ny ( int x,int y)
    {
        return b[x][y];
    }
    LL s_ali( int x,int y)
    {
        
        if (x==2&&y==1) return 1;
        if (x==3&&y==2) return 1;
        if (x==1&&y==3) return 1;
        return 0;
    }
    LL s_bob( int x,int y)
    {
        if (y==2&&x==1) return 1;
        if (y==3&&x==2) return 1;
        if (y==1&&x==3) return 1;
        return 0;
    }
    void print( pair<LL,LL>score)
    {
        
        printf("ali:%lld bob:%lld\n ",score.fst,score.sec);
    }
    
    /* 几种可能错误:
     * k的大小不足以出现循环节
     * 比分序列的时候为了找循环节开始的位置存了最后一个元素进去（第一次循环的开始），但是后面算的时候要去除
     * k的大小是LL,记得各种地方的LL
     */
    pair<LL,LL> solve(int x,int y)
    {
    
        pair< LL,LL >ret;
        ret.fst=ret.sec=0;
        seq.clear();
        mp.clear();
        seq.PB(MP(x,y));
        mp[MP(x,y)]=true;
        while (1)
        {
        int xx = nx(x,y);
        int yy = ny(x,y);
        seq.PB(MP(xx,yy));
        if (mp[MP(xx,yy)])
        {
            break;
        }
        mp[MP(xx,yy)] = true;
        x = xx;
        y = yy;
        }
    
    
        int siz = seq.size();
     //   for ( int i = 0 ; i < siz ; i++) printf("(%d %d)\n",seq[i].fst,seq[i].sec);
        pair<int,int>tar = seq[siz-1];
        int st,en;
        st = -1;
        en = siz-1;
        for ( int i = 0 ; i < siz ; i++)
        {
        pair<int,int> u = seq[i];
        if (u.fst==tar.fst&&u.sec==tar.sec)
        {
            st = i;
            break;
        }
        }
        //printf("st:%d\n",st);
        seq.pop_back();
        siz = seq.size();
        LL ali_sum,bob_sum;
        ali_sum=bob_sum=0LL;
        //有一种可能是k比循环节的开始要小。
        if (k<st) //没有循环节
        {
        for ( int i = 0 ; i < k ; i++)
        {
            int x = seq[i].fst;
            int y = seq[i].sec;
            ret.fst += s_ali(x,y);
            ret.sec += s_bob(x,y);
        }
    //  print(ret);
        return ret;
        }
    
        for ( int i = 0 ; i < st ; i++)
        {
        int x = seq[i].fst;
        int y = seq[i].sec;
        ali_sum+=s_ali(x,y);
        bob_sum+=s_bob(x,y);
        }
        k-=st; //剩下的是循环节部分.
        LL circle_len = siz-st;
        //printf("cir_len:%lld\n",circle_len);
        LL circle_ali=0;
        LL circle_bob=0; //一个循环节中的得分.
        for ( int i = st ; i < siz ; i++)
        {
        int x = seq[i].fst;
        int y = seq[i].sec;
        circle_ali+=1LL*s_ali(x,y);
        circle_bob+=1LL*s_bob(x,y);
        }
        LL num = k/circle_len;
        LL mod = k%circle_len;
        //printf("num:%lld  mod:%lld\n",num,mod);
        ret.fst = 1LL*ali_sum;
        ret.sec = 1LL* bob_sum;
        //print(ret);
        ret.fst += 1LL*num*circle_ali;
        ret.sec += 1LL*num*circle_bob;
       // print(ret);
        for ( int i = st ; i< st+mod ; i++)
        {
        int x = seq[i].fst;
        int y = seq[i].sec;
        ret.fst += 1LL*s_ali(x,y);
        ret.sec += 1LL*s_bob(x,y);
        }
    
        return ret;
    
        
    }
            
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        cin>>k>>x>>y;
        for ( int i = 1 ; i <= 3 ; i++)
            for ( int j = 1 ; j <= 3 ; j++)
            scanf("%d",&a[i][j]);
        for ( int i = 1 ; i <= 3 ; i++)
            for ( int j = 1 ; j <= 3 ; j++)
            scanf("%d",&b[i][j]);
        pair<LL,LL> ans = solve(x,y);
        printf("%lld %lld\n",ans.fst,ans.sec);
    
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    



D：有n(2e5)个数的序列，q(2E5)个区间操作，操作有2种类型，一种是将区间[L,R]循环右移一位。另一种是将区间[L,R]中的数整体反转。最后m（100）个询问，每个询问问b[j] (j属于1..m,b[j]属于1..n)位置上的数是多少。

思路：观察发现m比较小，可以暴力。对于所有操作进行完，b[i]位置上的数是多少， 因为所有的数只是位置改变，大小没有改变.我们想要还原，到最后的b[i]位置，应该对应的是初始序列中的哪个位置。
如果当前位置是pos,那么在进行上一个反转操作之前的位置就是(L+R)-pos, 进行上一个移位操作的位置就是pos-1(注意边界）


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年09月25日 星期一 05时19分52秒
    File Name :D.cpp
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
    #define PB push_back
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
    const int N=2E5+7;
    int n,q,m;
    int a[N];
    int b[105];
    struct Node
    {
        int opt,x,y;
    }qu[N];
    /* 思路：
     * 对于所有操作进行完，b[i]位置上的数是多少，
     * 因为所有的数只是位置改变，大小没有改变
     * 我们想要还原，到最后的b[i]位置，应该对应的是初始序列中的哪个位置。
     * 如果当前位置是pos,那么在进行上一个反转操作之前的位置就是(L+R)-pos,
     * 进行上一个移位操作的位置就是pos-1(注意边界）
     */
    int main()
    {
        #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
      #endif
        cin>>n>>q>>m;
        for ( int i = 1;  i <= n ; i++) scanf("%d",&a[i]);
        for ( int i = 1 ; i <= q ; i++) scanf("%d%d%d",&qu[i].opt,&qu[i].x,&qu[i].y);
        for ( int i = 1 ; i <= m ; i++) scanf("%d",&b[i]);
        
    
        for ( int i = q ; i >= 1 ; i--)
        {
            int opt = qu[i].opt;
            int L = qu[i].x;
            int R = qu[i].y;
            if (opt==1)
            {
            for ( int j = 1 ; j <= m ; j++)
            {
                if (b[j]>=L&&b[j]<=R)
                {
                if (b[j]-1>=L)
                b[j] = b[j]-1;
                else b[j] = R;
                }
            }
            }
            else
            {
            for ( int j = 1 ; j <= m  ;j++)
            {
                if (b[j]>=L&&b[j]<=R)
                {
                b[j] = R+L-b[j];
                }
            }
            }
        }
            for ( int i = 1 ; i <= m ; i++)
            printf("%d ",a[b[i]]);
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }




