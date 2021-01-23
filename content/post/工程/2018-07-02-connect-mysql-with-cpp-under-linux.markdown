---
author: 111qqz
date: 2018-07-02 07:02:28+00:00
draft: false
title: linux 下C++ 连接mysql 数据库
type: post
url: /2018/07/connect-mysql-with-cpp-under-linux/
categories:
- 其他
tags:
- cpp
- mysql
- linux
---

资料推荐这个:[MySQL C API programming tutorial](http://zetcode.com/db/mysqlc/)

环境为ubuntu 14.04 lts

需要安装mysql 和mysql 开发包

sudo apt-get install libmysqlclient15-dev  mysql-server mysql-client

先在mysql  中建立test数据库和test表格

    
    　mysql>create database test; 
    
    　　　　mysql>use test;    //切换到test数据库中
    
    　　　　mysql> create table test(name varchar(255),num int(10) ); //创建一个叫test的表
    
    　　　　mysql>show create table test;  //显示刚才创建的表信息
    
    　　　　mysql> select * from test; 　　//查询test表中数据
    
    　　　　mysql>quit
    
    




然后用如下cpp代码连接

    
    #include <cstdio>
    #include <mysql.h>
    #include <cstring>
    int main(int argc,char *argv[])
    {
    	MYSQL conn;
    	int res;
    	mysql_init(&conn);
    	if (mysql_real_connect(&conn,"localhost","root","2254965","test",0,NULL,CLIENT_FOUND_ROWS))
    	{
    		puts("connect success");
    		res = mysql_query(&conn,"insert into test values('sensetime','23333')");
    		if (res) puts("error");
    		else puts("success");
    		printf("res=%d\n",res);
    	}
    
    	return 0;
    }
    


编译:

    
    g++ test.cpp `mysql_config --cflags --libs` -o test
    


此次从mysql中查询，发现成功插入了一条数据．
