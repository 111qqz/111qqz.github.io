---
author: 111qqz
date: 2018-04-05 07:14:54+00:00
draft: false
title: 'Eigen: C++开源矩阵学习笔记'
type: post
url: /2018/04/eigen-notes/
categories:
- 其他
tags:
- caffe
- Eigen
- c++
---

接触Eigen的原因是最近在看caffe/caffe2源码,caffe2中使用了Eigen库. [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page) 是一个基于C++模板的线性代数库，直接将库下载后放在项目目录下，然后包含头文件就能使用，非常方便。对于Linux用户,只需要把头文件放到/usr/include 下即可此外，Eigen的接口清晰，稳定高效。

之后会更新一些,Eigen中我使用过的函数.


## ubuntu14.04LTS 下使用方式:



    
    sudo apt-get install libeigen3-dev
    cd /usr/include/eigen3
    sudo cp -R Eigen  /usr/include


然后尝试运行如下代码,直接编译即可.如果可以正常运行,表明安装完毕.

    
    #include <iostream>
    #include <Eigen/Dense>
    
    
    //using Eigen::MatrixXd;
    using namespace Eigen;
    using namespace Eigen::internal;
    using namespace Eigen::Architecture;
    
    
    using namespace std;
    
    
    int main()
    {
    
            cout<<"*******************1D-object****************"<<endl;
    
    
            Vector4d v1;
            v1<< 1,2,3,4;
            cout<<"v1=\n"<<v1<<endl;
    
    
            VectorXd v2(3);
            v2<<1,2,3;
            cout<<"v2=\n"<<v2<<endl;
    
    
            Array4i v3;
            v3<<1,2,3,4;
            cout<<"v3=\n"<<v3<<endl;
    
    
            ArrayXf v4(3);
            v4<<1,2,3;
            cout<<"v4=\n"<<v4<<endl;
    
    }
    




### map的使用办法:


double arr[9]={1,2,3,4,5,6,7,8,9};
Map<MatrixXd> A(arr,3,3);
得到
1 4 7
2 5 8
3 6 9

以看出默认是按列优先的...
如果需要按行优先,可以修改矩阵的定义方式:
typedef Matrix<double, Dynamic, Dynamic,RowMajor>rMatrixXd;//定义矩阵行优先
double arr[9]={1,2,3,4,5,6,7,8,9};
Map A(arr,3,3);

map使用的时候,只需要指定map<>中,缺少(dynamic)的维度.
比如

    
    /* ***********************************************
    Author :111qqz
    Created Time :2018年04月05日 星期四 18时21分59秒
    File Name :b.cpp
    ************************************************ */
    
    #include <bits/stdc++.h>
    #include <Eigen/Dense>
    using namespace std;
    using namespace Eigen;
    int main()
    {
        double arr[100]={1,2,3,4,5,6,7,8,9};
        Map<Array<double,Dynamic,1> >A(arr,4);
        cout<<A;
    
    
        return 0;
    }


得到结果

1
2
3
4


### 平均值


对于矩阵:

1 4 7
2 5 8
3 6 9

按行求平均值A.rowwise().mean()

得到:

4
5
6

按列求平均值 A.colwise().mean
得到
2 5 8


### unaryExpr()


参数为一元函数算子,表示对每一项应用该一元算子.具体看例子

    
    /* ***********************************************
    Author :111qqz
    Created Time :2018年04月05日 星期四 18时21分59秒
    File Name :b.cpp
    ************************************************ */
    
    #include <bits/stdc++.h>
    #include <Eigen/Dense>
    using namespace std;
    using namespace Eigen;
    int main()
    {
        double arr[9]={1,2,3,4,5,6,7,8,9};
        Map<MatrixXd> A(arr,3,3);
        cout<<A<<endl;
        auto sqr = [](double f) { return f * f; };
        cout<<A.unaryExpr(sqr);
    
    
        return 0;
    }


返回的结果为:
1 16 49
4 25 64
9 36 81




### replicate


将一个对象重复多干次.

语法为A.replicate(x,y)表示将A横向扩展x次(包含本身),纵向扩展y次(包含本身),共得到x*y个

    
    /* ***********************************************
    Author :111qqz
    Created Time :2018年04月05日 星期四 18时21分59秒
    File Name :b.cpp
    ************************************************ */
    
    #include <bits/stdc++.h>
    #include <Eigen/Dense>
    using namespace std;
    using namespace Eigen;
    int main()
    {
        double arr[9]={1,2,3,4,5,6,7,8,9};
        Map<MatrixXd> A(arr,3,3);
        cout<<A<<endl;
        cout<<A.replicate(3,3);
    
    
    
        return 0;
    }



