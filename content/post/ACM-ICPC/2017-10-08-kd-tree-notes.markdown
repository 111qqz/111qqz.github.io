---
author: 111qqz
date: 2017-10-08 11:46:46+00:00
draft: false
title: kd tree 学习笔记
type: post
url: /2017/10/kd-tree-notes/
categories:
- ACM
tags:
- kd-tree
---

老规矩，资料先行。

好久没学新算法了，有点忘记怎么学了orz

[K-D tree 数据结构](http://blog.csdn.net/zhjchengfeng5/article/details/7855241)

[hdu 2966 In case of failure　（k-d树　最近邻近点）](http://www.voidcn.com/article/p-hxhzjhet-px.html)



首先来看算法的提出。

现在二维平面上有n个点，知道这n个点的坐标，然后再添加一个点，问n个点中，距离新添加的点距离最近的点。

如果不做任何预处理，那么就是暴力枚举每个点，与该定点的距离。

如何优化呢？ 我们可以考虑把点域均等划分成若干个方块。

这样每次询问的时候只需要查询定点所在方格，以及定点相邻的8个方格中的点与该定点的距离即可。（除非这九个方格中没有点）

这种划分方法，对于随机数据大概是美滋滋，但是数据不会那么随机，因此划分也不能均等划 分。

这个时候， [kd-tree](https://zh.wikipedia.org/wiki/K-d) 登场。**_k_-d树**（ **k-维[树](https://zh.wikipedia.org/wiki/_())**的缩写）是在_k_维[欧几里德空间](https://zh.wikipedia.org/wiki/)组织[点](https://zh.wikipedia.org/wiki/)的数据结构

**对于二维平面，kd-tree的思想是，提供一种平面的划分方法，使得对于任意输入数据，划分尽可能均匀。**

**划分方法其实不唯一，常用的划分方法是，**对于k维中的每一维，按照方差最大的那一维划分。

**（看到有些题解中，用该维度的极差（就是最大值-最小值）来作为度量，也就是按照极差最大的那一维度划分。）**

**(用方差的度量往往比较慢，看到根据二叉树的深度，交替维度也是一种常用做法 比如2016青岛 onsite)**

下面是具体的划分过程。



<blockquote>

> 
>  假设现在我们有平面上的点集 E ，其中有 5 个二维平面上的点 ： （1,4）（5,8） （4,2） （7,9） （10，11）
> 
> 

> 
>         它们在平面上的分布如图：
> 
> 

> 
>                                                                 ![](http://my.csdn.net/uploads/201208/11/1344683756_8292.png)

> 
> 

> 
>         首先，我们对区间 [ 1 , 5 ] 建树：
> 
> 

> 
>         先计算区间中所有点在第一维（也就是 x 坐标）上的方差：
> 
> 

> 
>                 平均值 ： ave_1 =5.4
> 
> 

> 
>                 方差 ： varance_1 =9.04
> 
> 

> 
>         再计算区间中所有点在第二维（也就是 y 坐标）上的方差：
> 
> 

> 
>                 平均值：ave_2 =6.8
> 
> 

> 
>                 方差：varance_2 =10.96
> 
> 

> 
>         明显看见，varance_2 > varance_1 ，那么我们在本次建树中，分裂方式 ：split_method =2 ， 再将所有的点按照 第 2 维 的大小从小到大排序，得到了新的点的一个排列：
> 
> 

> 
>                 （4,2） （1,4）（5,8） （7,9） （10,11）
> 
> 

> 
>         取中间的点作为分裂点 sorted_mid =（5，8）作为根节点，再把区间 [ 1 , 2] 建成左子树 , [ 4 , 5] 建成右子树，此时，直线 ： y = 8 将平面分裂成了两半，前面一半给左儿子，后面一半给了右儿子，如图：
> 
> 

> 
>                                                                 ![](http://my.csdn.net/uploads/201208/11/1344684720_8773.png)

> 
> 

> 
>         建左子树 [1 , 3 ] 的时候可以发现，这时候是 第一维 的方差大 ，分裂方式就是1 ，把区间 [ 1, 2 ] 中的点按照 第一维 的大小，从小到大排序 ，取中间点（1,4） 根节点，再以区间 [ 2, 2] 建立右子树 得到节点 （4,2）
> 
> 

> 
>                                                                 ![](http://my.csdn.net/uploads/201208/11/1344685538_5357.png)

> 
> 

> 
>          建右子树 [4 , 5 ] 的时候可以发现，这时还是 第一维 的方差大， 于是，我们便得到了这样的一颗二叉树 也就是 K-D tree，它把平面分成了如下的小平面，使得每个小平面中最多有一个点：
> 
> 

> 
>                                                                  ![](http://my.csdn.net/uploads/201208/11/1344685811_4836.png)

> 
> 

> 
>         可以看见，我们实际上在建树的过程中，把整个平面分成了 4 个部分
> 
> 

> 
>         树是建了，那么查询呢?
> 
> 

> 
>         查询过程：
> 
> 

> 
>                 查询，其实相当于我们要将一个点“添加”到已经建好的 K-D tree 中，但并不是真的添加进去，只是找到他应该处于的子空间即可，所以查询就显得简单的毒攻了
> 
> 

> 
>                 每次在一个区间中查询的时候，先看这个区间的分裂方式是什么，也就是说，先看这个区间是按照哪一维来分裂的，这样如果这个点对应的那一维上面的值比根节点的小，就在根节点的左子树上进行查询操作，如果是大的话，就在右子树上进查询操作
> 
> 

> 
>                 每次回溯到了根节点（也就是说，对他的一个子树的查找已经完成了）的时候，判断一下，以该点为圆心，目前找到的最小距离为半径，看是否和分裂区间的那一维所构成的平面相交，要是相交的话，最近点可能还在另一个子树上，所以还要再查询另一个子树，同时，还要看能否用根节点到该点的距离来更新我们的最近距离。为什么是这样的，我们可以用一幅图来说明：
> 
> 

> 
>                                                                 ![](http://my.csdn.net/uploads/201208/11/1344687429_2577.png)

> 
> 

> 
>          在查询到左儿子的时候，我们发现，现在最小的距离是 r = 10 ，当回溯到父亲节点的时候，我们发现，以目标点（10,1）为圆心，现在的最小距离 r = 10 为半径做圆，与分割平面 y = 8 相交，这时候，如果我们不在父亲节点的右儿子进行一次查找的话，就会漏掉 （10,9） 这个点，实际上，这个点才是距离目标点 （10,1） 最近的点
> 
> 

> 
> 由于每次查询的时候可能会把左右两边的子树都查询完，所以，查询并不是简单的 log(n) 的，最坏的时候能够达到 sqrt(n)
> 
> 
</blockquote>





放一份kd-tree的代码，按照上面讲解的过程（不是作为模板）


    
    #include <iostream>
    #include <cstdio>
    #include <cstring>
    #include <cmath>
    #include <algorithm>
    #include <vector>
    #include <string>
    #include <queue>
    #include <stack>
    
    #define INT_INF 0x3fffffff
    #define LL_INF 0x3fffffffffffffff
    #define EPS 1e-12
    #define MOD 1000000007
    #define PI 3.141592653579798
    #define N 60000
    
    using namespace std;
    
    typedef long long LL;
    typedef unsigned long long ULL;
    typedef double DB;
    
    struct data
    {
        LL pos[10];
        int id;
    } T[N] , op , point;
    int split[N],now,n,demension;
    
    bool use[N];
    LL ans,id;
    DB var[10];
    
    bool cmp(data a,data b)
    {
        return a.pos[split[now]]<b.pos[split[now]];
    }
    
    void build(int L,int R)
    {
        if(L>R) return;
    
        int mid=(L+R)>>1;
        
        //求出 每一维 上面的方差
        for(int pos=0;pos<demension;pos++)
        {
            DB ave=var[pos]=0.0;
            for(int i=L;i<=R;i++)
                ave+=T[i].pos[pos];
            ave/=(R-L+1);
            for(int i=L;i<=R;i++)
                var[pos]+=(T[i].pos[pos]-ave)*(T[i].pos[pos]-ave);
            var[pos]/=(R-L+1);
        }
        
        //找到方差最大的那一维，用它来作为当前区间的 split_method
        split[now=mid]=0;
        for(int i=1;i<demension;i++)
            if(var[split[mid]]<var[i]) split[mid]=i;
        
        //对区间排排序，找到中间点
        nth_element(T+L,T+mid,T+R+1,cmp);
        
        build(L,mid-1);
        build(mid+1,R);
    }
    
    void query(int L,int R)
    {
        if(L>R) return;
        int mid=(L+R)>>1;
        
        //求出目标点 op 到现在的根节点的距离
        LL dis=0;
        for(int i=0;i<demension;i++)
            dis+=(op.pos[i]-T[mid].pos[i])*(op.pos[i]-T[mid].pos[i]);
        
        //如果当前区间的根节点能够用来更新最近距离，并且 dis 小于已经求得的 ans
        if(!use[T[mid].id] && dis<ans)
        {
            ans=dis;  //更新最近距离
            point=T[mid];  //更新取得最近距离下的点
            id=T[mid].id;  //更新取得最近距离的点的 id
        }
        
        //计算 op 到分裂平面的距离
        LL radius=(op.pos[split[mid]]-T[mid].pos[split[mid]])*(op.pos[split[mid]]-T[mid].pos[split[mid]]);
        
        //对子区间进行查询
        if(op.pos[split[mid]]<T[mid].pos[split[mid]])
        {
            query(L,mid-1);
            if(radius<=ans) query(mid+1,R);
        }
        else
        {
            query(mid+1,R);
            if(radius<=ans) query(L,mid-1);
        }
    }
    
    int main()
    {
        while(scanf("%d%d",&n,&demension)!=EOF)
        {
            //读入 n 个点
            for(int i=1;i<=n;i++)
            {
                for(int j=0;j<demension;j++)
                    scanf("%I64d",&T[i].pos[j]);
                T[i].id=i;
            }
            
            build(1,n);  //建树
    
            int m,q; scanf("%d",&q);  // q 个询问
            while(q--)
            {
                memset(use,0,sizeof(use));
                
                for(int i=0;i<demension;i++)
                    scanf("%I64d",&op.pos[i]);
                scanf("%d",&m);
                printf("the closest %d points are:\n",m);
                while(m--)
                {
                    ans=(((LL)INT_INF)*INT_INF);
                    query(1,n);
                    for(int i=0;i<demension;i++)
                    {
                        printf("%I64d",point.pos[i]);
                        if(i==demension-1) printf("\n");
                        else printf(" ");
                    }
                    use[id]=1;
                }
            }
        }
        return 0;
    }
    





然后放一道例题：[hdu2966  ](http://acm.split.hdu.edu.cn/showproblem.php?pid=2966)








