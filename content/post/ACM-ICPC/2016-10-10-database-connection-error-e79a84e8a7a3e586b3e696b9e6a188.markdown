---
author: 111qqz
date: 2016-10-10 10:37:14+00:00
draft: false
title: database connection error 的解决方案
type: post
url: /2016/10/database-connection-error-/
categories:
- 其他
tags:
- mysql
---

其实 东西之前出现过...不过好像重启一下服务器就可以了？

这次比较麻烦。

一开始我是直接google 了这条错误信息，结果答案五花八门，或者说...可能的原因非常多。

排查了几个。。。还是没有搞定。。。

突然想到。。。。为何不直接看log....我好傻啊。

    
    2016-10-10 10:36:54 3755 [Note] IPv6 is not available.
    2016-10-10 10:36:54 3755 [Note]   - '0.0.0.0' resolves to '0.0.0.0';
    2016-10-10 10:36:54 3755 [Note] Server socket created on IP: '0.0.0.0'.
    2016-10-10 10:36:54 3755 [ERROR] /alidata/server/mysql/bin/mysqld: Table './mysql/user' is marked as crashed and last (automatic?) repair failed
    2016-10-10 10:36:54 3755 [ERROR] Fatal error: Can't open and lock privilege tables: Table './mysql/user' is marked as crashed and last (automatic?) repair failed
    161010 10:36:54 mysqld_safe mysqld from pid file /alidata/server/mysql/data/iZ287lyogf4Z.pid ended
    161010 10:42:20 mysqld_safe Starting mysqld daemon with databases from /alidata/server/mysql/data
    2016-10-10 10:42:20 0 [Warning] TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
    2016-10-10 10:42:20 4118 [Note] Plugin 'FEDERATED' is disabled.
    2016-10-10 10:42:20 4118 [Note] InnoDB: Using mutexes to ref count buffer pool pages
    2016-10-10 10:42:20 4118 [Note] InnoDB: The InnoDB memory heap is disabled
    2016-10-10 10:42:20 4118 [Note] InnoDB: Mutexes and rw_locks use InnoDB's own implementation
    2016-10-10 10:42:20 4118 [Note] InnoDB: Memory barrier is not used
    2016-10-10 10:42:20 4118 [Note] InnoDB: Compressed tables use zlib 1.2.3
    2016-10-10 10:42:20 4118 [Note] InnoDB: Using Linux native AIO
    2016-10-10 10:42:20 4118 [Note] InnoDB: Not using CPU crc32 instructions
    2016-10-10 10:42:20 4118 [Note] InnoDB: Initializing buffer pool, size = 128.0M
    2016-10-10 10:42:20 4118 [Note] InnoDB: Completed initialization of buffer pool
    2016-10-10 10:42:20 4118 [Note] InnoDB: Highest supported file format is Barracuda.
    2016-10-10 10:42:20 4118 [Note] InnoDB: The log sequence numbers 414871617 and 414871617 in ibdata files do not match the log sequence number 554212530 in the ib_logfiles!
    2016-10-10 10:42:20 4118 [Note] InnoDB: Database was not shutdown normally!
    2016-10-10 10:42:20 4118 [Note] InnoDB: Starting crash recovery.
    2016-10-10 10:42:20 4118 [Note] InnoDB: Reading tablespace information from the .ibd files...
    2016-10-10 10:42:20 4118 [Note] InnoDB: Restoring possible half-written data pages 
    2016-10-10 10:42:20 4118 [Note] InnoDB: from the doublewrite buffer...
    InnoDB: Last MySQL binlog file position 0 92722334, file name mysql-bin.000005
    2016-10-10 10:42:20 4118 [Note] InnoDB: 128 rollback segment(s) are active.
    2016-10-10 10:42:20 4118 [Note] InnoDB: Waiting for purge to start
    2016-10-10 10:42:20 4118 [Note] InnoDB: 5.6.21 started; log sequence number 554212530
    2016-10-10 10:42:20 4118 [Note] Recovering after a crash using mysql-bin
    2016-10-10 10:42:20 4118 [Note] Starting crash recovery...
    2016-10-10 10:42:20 4118 [Note] Crash recovery finished.
    2016-10-10 10:42:20 4118 [Note] Server hostname (bind-address): '*'; port: 3306
    2016-10-10 10:42:20 4118 [Note] IPv6 is not available.
    2016-10-10 10:42:20 4118 [Note]   - '0.0.0.0' resolves to '0.0.0.0';
    2016-10-10 10:42:20 4118 [Note] Server socket created on IP: '0.0.0.0'.
    2016-10-10 10:42:20 4118 [ERROR] /alidata/server/mysql/bin/mysqld: Table './mysql/user' is marked as crashed and last (automatic?) repair failed
    2016-10-10 10:42:20 4118 [ERROR] Fatal error: Can't open and lock privilege tables: Table './mysql/user' is marked as crashed and last (automatic?) repair failed
    161010 10:42:20 mysqld_safe mysqld from pid file /alidata/server/mysql/data/iZ287lyogf4Z.pid ended
    


发现是说一个表挂掉了。。。。

然后在SO上看到这个[stackoverflow](http://stackoverflow.com/questions/8843776/mysql-table-is-marked-as-crashed-and-last-automatic-repair-failed)

然后惊喜得发现完全不记得数据库密码是啥了...毕竟搭博客的时候我对这些完全没概念...

然后在my.cnf配置文件 加一行 skip-grant-tables  具体位置是在/etc/my.cnf

这样就可以跳过密码直接登录数据库。

[![qq20161010183341](https://111qqz.com/wordpress/wp-content/uploads/2016/10/QQ图片20161010183341-300x162.png)
](https://111qqz.com/wordpress/wp-content/uploads/2016/10/QQ图片20161010183341.png)

查了下果然有问题。。。

然后用 repair table table_name; 命令修复。

注意table_name外面没有引号啊，中括号之类乱七八糟的2333.

然后再check，发现少了条warning，就是日志里error的那条。

尝试了下访问博客。。。发现已经可以了。。感动到哭。。。



感觉这次学到的最主要的事情是。。。出问题直接去找log。。。。不要从表面的症状来找问题。。。。嗯。感动。








![](file:///C:\Users\Administrator.PC-20160710CZQJ\AppData\Roaming\Tencent\Users\491791443\QQ\WinTemp\RichOle\8TTP%5%DN)ZSFGOCG6$[8T2.png)

