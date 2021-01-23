---
author: 111qqz
date: 2015-08-17 01:24:00+00:00
draft: false
title: codeforces 560 D. Equivalent Strings(分治)
type: post
url: /2015/08/codeforces560d-equivalentstrings/
categories:
- ACM
tags:
- 分治
---




问两个长度相同的字符串是否等价．




相等的条件是，两个字符串相等，或者两个偶数长度（因为要分成长度相同的两段，所以一定是偶数长度才可分）字符串平均分成两部分，每部分对应相等(不考虑顺序)




一开始有一点没想清楚.




如果字符串a分成相等长度的两部分a1,a2,字符串b分成相等的两部分b1,b2




我错误得以为,如果a1和a2等价&&b1;和b2等价,那么a 和 b 就相等了(a和b一定等价,但不一定相等),于是只判断了 equal(a1,b2)&&equal;(a2,b1)




wa了一次.


< 

    
    /*************************************************************************
    	> File Name: code/cf/#313/D.cpp
    	> Author: 111qqz
    	> Email: rkz2013@126.com 
    	> Created Time: 2015年08月17日 星期一 08时42分25秒
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
    const int inf = 0x7fffffff;
    const int N=2E5+7;
    string a,b;
    int len;
    
    bool equal( string x,string y,int len)
    {
      //  cout<<"x:"<<x<<" y:"<<y<<" len:"<<len<<endl;
        if (x==y) return true;
        string x1,x2,y1,y2;
        x1 = x.substr(0,len/2);
        x2 = x.substr(len/2,len);
        y1 = y.substr(0,len/2);
        y2 = y.substr(len/2,len);
        if (len%2==0&&equal(x1,y2,len/2)&&equal(x2,y1,len/2))
        {
    	return true;
        }
        if (len%2==0&&equal(x1,y1,len/2)&&equal(x2,y2,len/2))
        {
    	return true;
        }
        return false;
    }
    int main()
    {
        cin>>a;
        cin>>b;
        len = a.length();
        if (equal(a,b,len))
        {
    	puts("YES");
        }
        else
        {
    	puts("NO");
        }
          
    	return 0;
    }
    



