---
author: 111qqz
date: 2016-11-24 02:09:13+00:00
draft: false
title: 'codeforces #381 div2'
type: post
url: /2016/11/codeforces-381-div2/
categories:
- ACM
---

http://codeforces.com/contest/740

A:现在有n个某种物品，要买k个使得n+k是4的倍数，可以的购买方案为a元1个，b元2个，c元3个，每种方案都可以买无限多。

思路：需要注意买多个未必比买少个贵..

所以分情况讨论：n%4==0，输出0

n%4==1，需要买3+4k个，

**可以的方案为，买1个c，或者3个a，或者1个a 1个b（此处用价钱指代方案，下同）**

n%4==2时，需要买2+4k个

**可以的方案为：2个a，或者1个b，或者2个c**

n%4==3时，需要买4K+1个

**可以的方案为：1个a,或者1个b+1个c，或者3个c**

注意要开long long.

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月24日 星期四 08时09分32秒
    File Name :code/cf/#381/A.cpp
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
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	LL n,a,b,c;
    	cin>>n>>a>>b>>c;
    	LL mn = 0 ;
    	if (n%4==0)
    	{
    	    mn = 0 ;
    	}
    	else if (n%4==1)
    	{
    	    mn = min(3LL*a,a+b);
    	    mn = min(mn,c);
    	}else if (n%4==2)
    	{
    	    mn = min(2LL*a,b);
    	    mn = min(mn,2*c);
    	}else if (n%4==3)
    	{
    	    mn = a;
    	    mn = min(mn,b+c);
    	    mn = min(mn,3LL*c);
    	}
    	printf("%lld\n",mn);
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




B:

题意：给出n个数，以及m个子串，从中选若干个（可以不选或者全选），女孩的幸福值的计算方法为：a[i]*cnt[i]，a[i]为值，cnt[i]为第i个数在选中的子串里出现了几次（只考虑位置，相同的值算成不同的数）

思路：n,m很小，一个子串如果最后收益为正，就选，否则不选，暴力即可。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月24日 星期四 08时09分46秒
    File Name :code/cf/#381/B.cpp
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
    const int N=105;
    int n,m;
    int a[N];
    int sum[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	ms(sum,0);
    	cin>>n>>m;
    	for ( int i = 1 ; i <= n ; i++) cin>>a[i];
    	for ( int i = 1;  i <= m ; i++)
    	{
    	    int l,r;
    	    scanf("%d%d",&l,&r);
    	    for ( int j = l ; j <= r ; j++) sum[i] = sum[i] + a[j];
    	}
    	int ret = 0 ;
    	for ( int i =1 ; i <= m ; i++) if (sum[i]>0) ret = ret + sum[i];
    	cout<<ret<<endl;
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    






c:题意：m个区间，要求构造一个长度为n的数组，满足m个区间中，每个区间的mex值中的最小值最大。

s思路：很容易想到的是...这个最大的mex 不可能超过每一组区间长度，假设最小的区间长度为mn

那么是否一定可以构造出mex为mn的数组呢？

是的。

只需要按照

0,1,2...mn-1,0,1....的方式构造即可。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月24日 星期四 09时00分04秒
    File Name :code/cf/#381/C.cpp
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
    const int N=1E5+7;
    int n,m;
    struct node
    {
        int l,r;
        int len;
        bool operator < ( node b)const
        {
    	if (r==b.r) return l<b.l;
    	return r<b.r;
        }
    }a[N];
    int ans[N];
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	scanf("%d%d",&n,&m);
    	int mx = inf ;
    	for ( int i = 1; i <= m ; i++)
    	{
    	    scanf("%d%d",&a[i].l,&a[i].r);
    	    a[i].len = a[i].r-a[i].l+1;
    	    mx = min(mx,a[i].len);
    	}
    	printf("%d\n",mx);
    	int cur = 0 ;
    	for ( int i = 1 ; i <= n ; i++)
    	{
    //	    cout<<"miao"<<endl;
    	    ans[i] = cur;
    	    cur++;
    	    cur = cur % mx;
    	}
    	for ( int i = 1;  i <= n ; i++) printf("%d ",ans[i]);
    	printf("\n");
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    


d:题意：一棵树，给出边权和点权，定义点v控制点u，当且仅当u是v的子树中的点，并且dis(u,v)<=a[u]，其中dis(u,v)为点u到点v路径上的边权和，a[u]为点u的点权，现在问对于每个节点v，其能控制的点有多少个。

思路：<del>先写了个rmq+dfs的lca。。。那么任意两个点的距离都可以O(1)得到了。然后不会了233333.</del>

**upd**:和lca没有什么关系，因为一个点能控制另一个点这两个点一定在一条通向根的链上，因此距离直接减一下就好了。

**机智的做法**：dfs的时候维护一个栈，对于栈中序列，后面一半是对当前点有贡献的。问题时求对于每个v统计其能控制多少个u，现在我们固定u，考虑能控制他的v。这些v在树上的形态时一条链 ，借助第二类前缀和的思想，对于u标记+1，对于u往上的离根最近的且能统治u的v上面的一个标记-1，然后dfs后序遍历（也就是链的起点时距离根远的那一边），距离处理的时候，只需要在递归之后更新ans就好了。

栈里面维护，到哪个节点，从根下来，边权和最大，找边权和>=当前边权和-a[u]的地方。

**启示：由于两个存在统治关系的点在一条链上，边权都为正，边权和具有单调性，单调的东西，容易想到二分处理。**

    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年11月24日 星期四 09时17分48秒
    File Name :code/cf/#381/D.cpp
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
    const int N=2E5+7;
    int n;
    int a[N];
    LL dis[N];
    vector< pair<int,LL> >edge[N];
    vector< pair<LL,int> >path;
    int ans[N];
    void dfs( int u,int pre)
    {
        ans[u]++;
        int idx = lower_bound(path.begin(),path.end(),make_pair(dis[u]-a[u],-1))-path.begin()-1;
        if (idx>=0) ans[path[idx].sec]--;
        path.push_back(make_pair(dis[u],u));
        for ( auto x : edge[u])
        {
    	int v  = x.first;
    	if (v==pre) continue;
    	dis[v] = dis[u] + x.sec;
    	dfs(v,u);
    	ans[u]+=ans[v];//后序遍历...链的起点原理根，终点靠近根
        }
        path.pop_back();
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>n;
    	ms(dis,0);
    	for ( int i = 1 ; i <= n ; i++) scanf("%d",&a[i]);
    	for ( int i =2 ; i <= n ; i++)
    	{
    	    int u,v;
    	    LL w;
    	    u = i ;
    	    scanf("%d%lld",&v,&w);
    	    edge[u].push_back(make_pair(v,w));
    	    edge[v].push_back(make_pair(u,w));
    	}
    	dfs(1,0);
    	for ( int i = 1 ; i <= n ; i++) printf("%d ",ans[i]-1);
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    








e:题意：那个数，定义hill为一段连续的区间，满足该区间为严格单峰。现在有若干操作，每个操作是对某段区间的数同时增加一个数，问每次操作后，所有的hill中，宽度最大的（区间长度最大）的是多少。

思路：同时增加一个数很线段树。。。但是要维护什么呢。。。？

猜测：肯定要维护一个区间中hill的最大宽度...

但是合并的时候要怎么办呢。。。

考虑两个方向的合并。。。

所以还要维护一个区间中，包含右端点的向左单调减延伸的长度，以及左端点的值。

同理，要维护一个区间中，包含左端点的向右单调增延伸的长度，以及右端点的值。

那么每次pushup的时候，就是两个区间hill的最大值，以及两个方向合并的最大值中取最大。。。

。。。上面是我口胡的。。。

[解题报告](https://111qqz.com/wordpress/2016/11/cf740e/)
