---
author: 111qqz
date: 2015-12-21 13:59:05+00:00
draft: false
title: hdu 1221 Rectangle and Circle
type: post
url: /2015/12/hdu-1221-rectangle-and-circle/
categories:
- ACM
tags:
- 计算几何
---

http://acm.hdu.edu.cn/showproblem.php?pid=1221
题意：问圆和矩形是否相交
思路：主要特殊的包含情况，然后判断与线段相交。
 

    
    /* ***********************************************
    Author :111qqz
    Created Time :2015年12月21日 星期一 21时38分22秒
    File Name :code/hdu/rr1221.cpp
    ************************************************ */
    
    #include <iostream>
    #include <string.h>
    #include <stdio.h>
    #include <algorithm>
    #include <cmath>
    #define eps 1e-8
    using namespace std;
    struct point
    {
        double x;
        double y;
    }circle,a,b,c,d;
    double r;
    double dis(point &a,point &b)
    {
        return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
    }
    
    bool ok()
    {
    
            if(dis(a,circle)<r && dis(b,circle) <r && dis(c,circle)<r && dis(d,circle) <r)
            return false;
            if(circle.x>=a.x && circle.x<=b.x)
            {
                if(fabs(circle.y-a.y) <= r || fabs(circle.y-b.y) <= r)
               return true;
            }
            if((circle.y >= a.y && circle.y <=b.y) || (circle.y>=b.y && circle.y<=a.y))
            {
                if(fabs(circle.x-a.x) <=r || fabs(circle.x-b.x) <=r)
                return true;
            }
            if(dis(a,circle)<=r || dis(b,circle) <=r || dis(c,circle)<=r || dis(d,circle) <=r)
            return true;
            return false;
    }
    int main()
    {
        #ifndef ONLINE_JUDGE
    	freopen("code/in.txt","r",stdin);
        #endif
        int t;
        scanf("%d",&t);
        while(t--)
        {
            scanf("%lf %lf %lf %lf %lf %lf %lf",&circle.x,&circle.y,&r,&a.x,&a.y,&b.x,&b.y);
            if(a.x > b.x)
            swap(a,b);
            c.x=a.x,c.y=b.y;
            d.x=b.x,d.y=a.y;
        
        if (ok())
        {
    	puts("YES");
        }
        else
        {
    	puts("NO");
        }
        }
        return 0;
    }
    




