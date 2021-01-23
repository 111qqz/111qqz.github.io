---
author: 111qqz
date: 2017-03-31 08:36:23+00:00
draft: false
title: hihocoder 1197  Give My Text Back (模拟)
type: post
url: /2017/03/hihocoder-1197-give-my-text-back-/
categories:
- ACM
tags:
- 模拟
---




### #1197 : Give My Text Back
















时间限制:10000ms




单点时限:1000ms




内存限制:256MB










### 描述


To prepare for the English exam Little Ho collected many digital reading materials. Unfortunately the materials are messed up by a malware.

It is known that the original text contains only English letters (a-zA-Z), spaces, commas, periods and newlines, conforming to the following format:

1. Each sentence contains at least one word, begins with a letter and ends with a period.

2. In a sentence the only capitalized letter is the first letter.

3. In a sentence the words are separated by a single space or a comma and a space.

4. The sentences are separated by a single space or a single newline.

It is also known the malware changes the text in the following ways:

1. Changing the cases of letters.

2. Adding spaces between words and punctuations.

Given the messed text, can you help Little Ho restore the original text?


### 输入


A string containing no more than 8192 English letters (a-zA-Z), spaces, commas, periods and newlines which is the messed text.


### 输出


The original text.







 	样例输入

 	    

    
    my Name  is Little   Hi.
    His   name IS Little ho  ,  We are   friends.




 	样例输出

 	    

    
    My name is little hi.
    His name is little ho, we are friends.











比较容易忽视的几个细节是:
连续的空格或者换行符只能有一个;

一个句子是某一行最后一个句子的时候,'.'后没有空格

比较难处理的是,'.'或者','前面的空格.

我的做法是,先不处理,最后倒序处理.

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年03月31日 星期五 15时45分46秒
    File Name :code/hiho/107A.cpp
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
    string st;
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("code/in.txt","r",stdin);
    #endif
        while (getline(cin,st))
        {
    //	cout<<st<<endl;
    	int len = st.length();
    	string res="";
    	bool fst = true;
    	bool space = false;
    	bool newl = false;
    	for ( int i = 0 ;i < len ; i++)
    	{
    	    if (st[i]!=' ') space = false;
    	    if (st[i]!='\t') newl = false; //空格和换行符不能连续.
    	    if (fst)
    	    {
    		if (st[i]>='a'&&st[i]<='z') res = res + char(st[i]-32),fst = false;
    		else if (st[i]>='A'&&st[i]<='Z')  res = res + st[i],fst = false;
    		else if (st[i]==' ')
    		     {
    			 if (!space)
    			 {
    			     res = res + " ";
    			     space = true;
    			 }
    		     }
    		     else if (st[i]=='\t')
    			  {
    			      if (!newl)
    			      {
    			    	 // res = res + '\t';
    				  newl = true;
    			      }
    			  }
    		continue;
    	    }
    	    if (!fst)
    	    {
    		if (st[i]>='A'&&st[i]<='Z') res = res + char(st[i]+32);
    		else if (st[i]>='a'&&st[i]<='z') res = res + st[i];
    		else if (st[i]==' ')
    		{
    		    if (!space&&st[i+1]!=',') //逗号前不能有空格
    		    {
    //			cout<<"st[i+1]:"<<st[i+1]<<" i:"<<i<<endl;
    			space = true;
    			res = res + " ";
    		    }
    		}
    		else if (st[i]=='.') 
    		{
    		    fst = true;
    		    res = res + '.';
    		}
    		else if (st[i]==',') res = res + ',';
    
    
    	    }
    	}
    //	cout<<res<<endl;
    	 len = res.length();
    	bool per = false;
    	string ret="";
    	for ( int i = len-1 ; i>= 0 ; i--)
    	{
    	    if (per&&res[i]==' ') continue;
        
    	    if (res[i]==','||res[i]=='.') per = true;
    	    else  per = false;
    	    ret = ret + res[i];
    	}
    	reverse(ret.begin(),ret.end());
    	cout<<ret<<endl;
        }
    
    #ifndef ONLINE_JUDGE  
    	fclose(stdin);
    #endif
    	return 0;
    }
    



