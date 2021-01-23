---
author: 111qqz
date: 2017-04-10 01:16:43+00:00
draft: false
title: leetcode  73. Set Matrix Zeroes (矩阵置0，乱搞)
type: post
url: /2017/04/leetcode-73-set-matrix-zeroes/
categories:
- 面试
tags:
- leetcode
---

Given a _m_ x _n_ matrix, if an element is 0, set its entire row and column to 0. Do it in place.


[click to show follow up.](https://leetcode.com/problems/set-matrix-zeroes/#)





**Follow up:**Did you use extra space?
A straight forward solution using O(_m__n_) space is probably a bad idea.
A simple improvement uses O(_m_ + _n_) space, but still not the best solution.
Could you devise a constant space solution?


直接放常数空间的做法。

这道题面hypereal的时候遇到过，基本思路就是用已经确定是0的位置来存储其他行和列的信息。

三点注意：



 	  *   (x,y)不要放任何信息，不然行和列的信息，后面处理的那个可能被覆盖掉。
 	  *   (x,y)位置要进行标记，否则默认的0值可能会造成歧义
 	  * 赋值成0的时候要分成两部分，处理的时候避免因为处理前面赋值成了0，把后面标记的行和列的标号覆盖掉。


    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月10日 星期一 08时06分27秒
    File Name :73.cpp
    ************************************************ */
    class Solution {
    public:
        void setZeroes(vector<vector<int>>& a) {
    	int n = a.size();
    	int m = a[0].size();
    	bool ok = false;
    	int x,y;
    	x = y = -1;
    	for ( int i = 0 ; i < n ; i++)
    	{
    	    if (ok) break;
    	    for ( int j =  0 ; j < m; j++)
    	    {
    		if (a[i][j]==0)
    		{
    		    x = i;
    		    y = j;
    		    ok = true;
    		    break;
    		}
    	    }
    	}
    	if (x==-1) return ; //没有0存在
    
    
    	int cntx=0,cnty=0;
    	for ( int i = 0 ; i < n ; i++) // note to avoid the (x,y) to record any info,or it may be coverd by the latter info
    	{
    	    if (i!=x)
    	    for ( int j = 0 ;j  < m ; j++)
    	    {
    		if (a[i][j]==0)
    		{
    		    if (cntx==x)
    		    {
    			a[cntx][y] = -1;
    			cntx++;
    		    }
    		    a[cntx++][y] = i;
    		    break;
    		}
    	    }
    	}
    	for ( int j = 0 ; j < m ; j++)
    	{
    	    if (j!=y)
    	    for ( int  i = 0 ; i < n ; i++)
    	    {
    		if (a[i][j]==0)
    		{
    		    if (cnty==y)
    		    {
    			a[x][cnty] = -1; // set a mark the (x,y),or the original value 0 will mislead the program.
    			cnty++;
    		    }
    		    a[x][cnty++] = j ;
    		    break;
    		}
    	    }
    	}
    	for ( int i =  0 ; i < cntx ; i++)
    	{
    	    int XX = a[i][y];
    	    
    	    if (XX==x||XX==-1) continue;
    	    for ( int j = 0 ; j < m ; j++)
    		if (j!=y)   // fill the 0 in two steps,ensuring not to cover the info
    		a[XX][j] = 0 ;
    	}
    	for ( int j = 0 ; j < cnty ; j++)
    	{
    	    int YY = a[x][j];
    	    if (y==YY||YY==-1) continue;
    	//    cout<<"YY:"<<YY<<endl;
    	    for (int i = 0 ; i < n ; i++)
    		if (i!=x)
    		a[i][YY] = 0;
    	}
    	for ( int i = 0 ; i < n ; i++)
    	    for ( int j = 0 ; j < m ; j++)
    		if (i==x||j==y) a[i][j] = 0 ;
        }
    };
    






下面有一个更精简的思路：

直接用每一行和每一列的第一个位置记录相应行和相应列的状态（(0,0)点会有重合，再加一个变量记录就好）

得到信息后记得从右下角往左上更新，避免信息覆盖。

    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月10日 星期一 08时06分27秒
    File Name :73.cpp
    ************************************************ */
    class Solution {
    public:
     void setZeroes(vector<vector<int> > &matrix) {
        int col0 = 1, n = matrix.size(), m = matrix[0].size();
    
        for (int i = 0; i < n; i++) {
            if (matrix[i][0] == 0) col0 = 0;
            for (int j = 1; j < m; j++)
                if (matrix[i][j] == 0)
                    matrix[i][0] = matrix[0][j] = 0;
        }
        
        for (int i = n-1; i >=0 ;i--) {
            for (int j = m-1; j >=1; j--)
                if (matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            if (col0 == 0) matrix[i][0] = 0;
        }
     }
    };
    
    





