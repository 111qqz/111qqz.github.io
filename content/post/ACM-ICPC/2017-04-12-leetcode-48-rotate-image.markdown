---
author: 111qqz
date: 2017-04-12 13:22:33+00:00
draft: false
title: leetcode 48. Rotate Image (旋转方阵(in place))
type: post
url: /2017/04/leetcode-48-rotate-image/
categories:
- 面试
tags:
- leetcode
---

You are given an _n_ x _n_ 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

题意：给一个n*n的方阵，要求顺时针旋转90度。

思路：**(x,y)->(y,n-1-x);**

要求in-place的做法的话，其实是若干长度为4的环，保护一个节点，然后顺次做就好了。

然后对于那些标记已经做过选旋转的问题，实际上没有必要进行标记。

对于偶数，只需要处理 左上角hf * hf个,奇数只需要处理左上角hf*(hf-1)个。

其中hf = (n+1)/2

1A


    
    1 2 3      (0,0) ->(0,2)
    4 5 6
    7 8 9                    
    
    
    
    7 4 1
    8 5 2
    9 6 3
    
      0 1 2 3
    0 1 2 3 4   (0,0)->(0,3)  (0,1)->(1,3)  (0,2)->(2,3) (0,3)->(3,3)
    1 5 6 7 8   (1,1)->(1,2)  (1,2)->(2,2)  (2,2)->(2,1)  
    2 9 A B C   (1,0)->(0,2) (2,0)->(0,1) 
    3 D E F G   //只搞四分之一角落
    
      0 1 2 3
    0 D 9 5 1
    1 E A 6 2
    2 F B 7 3
    3 G C 8 4
    
    
    1 2
    3 4
    
    
    3 1
    4 2
    
    1  2  3  4  5
    6  7  8  9  10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
    
    
    
    
    
    




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年04月12日 星期三 19时56分40秒
    File Name :48.cpp
    ************************************************ */
    class Solution {
    
    public:
        int n;
        void rotate(int &x,int &y,int n)
        {
        int nx,ny;
        nx = y;
        ny = n-1-x;
        //printf("(%d,%d)->(%d,%d)\n",x,y,nx,ny);
        x = nx;
        y = ny;
        }
        void pr(vector<vector<int> >&maze)
        {
        for ( int i = 0 ; i < n ; i++)
            for ( int j = 0 ; j < n ; j++)
            printf("%c%c",maze[i][j]>9?char(maze[i][j]-10+'A'):maze[i][j]+'0',j==n-1?'\n':' ');
        }
        void rotate(vector<vector<int>>& maze) {
        n = maze.size();
    //    pr(maze);
        int hn = (n+1)/2;
        int tmp=-1;
        int curx=0,cury=0;
    
        for ( int i = 0 ; i < hn ; i++ )
        {
            for ( int j = 0 ; j < hn-n%2 ; j++) //根据奇偶分情况
            {
            curx = i;
            cury = j;
            rotate(curx,curx,n);
            tmp = maze[curx][cury];
            maze[curx][cury] = maze[i][j];
            for ( int k = 0 ; k < 4 ; k++) //环的长度固定为4.
            {
                rotate(curx,cury,n);
                swap(tmp,maze[curx][cury]);
        //      printf("%d\n",tmp);
            }
            
            }
        }  
    
        
    }
    
    };
    






