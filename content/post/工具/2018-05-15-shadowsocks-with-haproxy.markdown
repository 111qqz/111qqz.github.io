---
author: 111qqz
date: 2018-05-15 06:27:35+00:00
title: 使用haproxy中转酸酸流量
type: post
url: /2018/05/shadowsocks-with-haproxy/
categories:
- 其他
tags:
- haproxy
- shadowsocks
---

一个国内vps，一个国外vps.

前提是国外vps已经配置好。

接下来，我们在国内vps上安装haproxy

yum -y install haproxy 或者 apt-get install haproxy

然后修改配置文件,位置在/etc/haproxy/haproxy.cfg

    
    global
     
    defaults
    	log	global
    	mode	tcp
    	option	dontlognull
            timeout connect 5000
            timeout client  50000
            timeout server  50000
     
    frontend ss-in
        bind *:[port]
        default_backend ss-out
     
    backend ss-out
        server server1 [ip]:[port] maxconn 20480


把其中的[ip]和[port]替换成国外vps的ip和相应服务的port

然后在客户端，ip填写国内vps的ip,密码还是酸酸的密码，其他保持一致。




