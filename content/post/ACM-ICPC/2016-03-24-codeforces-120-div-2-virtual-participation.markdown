---
author: 111qqz
date: 2016-03-24 06:41:11+00:00
draft: false
title: 'codeforces #120 div 2 (Virtual Participation)'
type: post
url: /2016/03/codeforces-120-div-2-virtual-participation/
categories:
- ACM

---

[比赛链接](http://codeforces.com/contest/190)

[![选区_033](https://111qqz.com/wordpress/wp-content/uploads/2016/03/选区_033.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/03/选区_033.png)

[![选区_034](https://111qqz.com/wordpress/wp-content/uploads/2016/03/选区_034.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/03/选区_034.png)

两题QAQ

A：7分钟1A 有n个大人m个小孩乘公交车，票价每人一元，一个大人最多免费带一个小孩，没有大人陪同的小孩不能乘车。 问是否有解，如果有解输出所有乘客付的钱的可能的最小值和可能的最大值。

思路：最小值就是先尽量利用每个大人带一个孩子。最大值就是把所有孩子都给一个大人。

特殊情况是：没有大人的时候，孩子不能乘车，无解。没有小孩的时候，大人没办法免费带孩子，也要特殊考虑。



    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年03月24日 星期四 12时24分27秒
    File Name :code/cf/#120/A.cpp
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
    int n,m;
    int mx,mi;
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    
    	cin>>n>>m;
    	if (n==0&&m>0)
    	{
    	    puts("Impossible");
    	    return 0;
    	}
    	if (n==0&&m==0)
    	{
    	    cout<<0<<" "<<0<<endl;
    	    return 0;
    	}
    	if (m==0&&n>0)
    	{
    	    cout<<n<<" "<<n<<endl;
    	    return 0 ;
    	}
    	if (n>=m)
    	{
    	    mi = n ;
    	    mx = n-1+m;
    	}
    	else
    	{
    	    mi = n + m-n;
    	    mx = n-1+m;
    	}
    	cout<<mi<<" "<<mx<<endl;
    
    
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




B:有两个被包围的城市，给出城市的坐标以及敌人距离城市的距离。敌人向着城市移动。要求建一个雷达，使得雷达能够感应到两伙敌人（分别朝着两个方向移动）的“**the start of the movements**”。问雷达的最小半径是多少。

反思：思维不够清楚，太呆

思路：两个圆有**五种（一开始想成了三种，所以wa7）**位置关系，分别考虑。

相离时，答案为（圆心距-半径之和）/2

外切时：把雷达建在切点，答案为0.

相交时：把雷达建在交点，答案为0

内切时：把雷达建在交点，答案为0.

内含时：答案为（abs(半径之差)-圆心距离）/2.





    
    /* ***********************************************
    Author :111qqz
    Created Time :2016年03月24日 星期四 12时53分05秒
    File Name :code/cf/#120/BB.cpp
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
    int a,b,r1;
    int c,d,r2;
    int dblcmp(double d)
    {
        return d<-eps?-1:d>eps;
    }
    int main()
    {
    	#ifndef  ONLINE_JUDGE 
    	freopen("code/in.txt","r",stdin);
      #endif
    	cin>>a>>b>>r1;
    	cin>>c>>d>>r2;
    	double dis = sqrt((a-c)*(a-c)+(b-d)*(b-d));
    	double r = r1+r2;
    	if (dblcmp(r-dis)==0)
    	{
    	    puts("0.0000000000000000");
    	    return 0;
    	}
    
    	if (dblcmp(r-dis)<0)
    	{
    	    double ans = (dis-r)*0.5;
    	    printf("%.16f\n",ans);
    	}
    	if (dblcmp(r-dis)>0)
    	{
    	    if (dblcmp(dis-abs(r1-r2))>=0)
    	    {
    		puts("0.00000000000000");
    	    }
    	    if (dblcmp(dis-abs(r1-r2))<0)
    	    {
    		double ans = (abs(r1-r2)-dis)*0.5;
    		printf("%.15f\n",ans);
    	    }
    	    
    	}
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    


C:给出一个pair 和int 序列，问能否恢复成一个合法的类型表示。如果能，保证有唯一解，输出这个唯一解。

细节略多。

没搞出来QAQ


