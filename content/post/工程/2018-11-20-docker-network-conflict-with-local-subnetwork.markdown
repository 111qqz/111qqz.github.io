---
author: 111qqz
date: 2018-11-20 08:33:20+00:00
draft: false
title: docker network 与 本地 network 网段冲突
type: post
url: /2018/11/docker-network-conflict-with-local-subnetwork/
categories:
- 其他
tags:
- docker
- network
---

### 起因:


公司部署在hk的爬虫服务器突然挂掉了。后来发现只是在深圳办公区无法访问。排查后发现原因是docker的网络(包括docker network的subnet或者是某个容器的ip)与该host在内网的ip段相同，导致冲突。


### 排查过程：


有两个方面需要排查。一个是docker服务启动时的默认网络。

默认网络使用bridge桥接模式，是容器与宿主机进行通讯的默认办法。

修改默认网段可以参考 http://blog.51cto.com/wsxxsl/2060761

除此之外，还需要注意docker创建的network的网段。

使用docker network ls 命令查看当前的网络

然后可以使用docker inspect 查看每个network的详细信息。

也可以直接使用ip addr 来查看各种奇怪的虚拟网卡的ip,是否有前两位的地址和host的ip地址相同的。


### 解决办法:


本想在docker-compose up 时指定默认网络的subnet

结果发现好像并不支持？[version 1.10.0 error on gateway spec](https://github.com/docker/compose/issues/4366)


<blockquote>Was there any discussion on that? I do need to customize the network, because my company uses the 172.16.0.0/16 address range at some segments and Docker will simply clash with that by default, so every single Docker server in the whole company needs a forced network setting.

Now while upgrading my dev environment to Docker 1.13 it took me hours to stumble into this Github issue, because the removal of those options was completely undocumented.

So please, if I am working on a network which requires a custom docker subnet, how am I supposed to use Docker Compose and Docker Swarm?</blockquote>


最后用了个比较间接的办法。

先手动创建一个docker network，然后再在docker-compose的配置文件中指定。

    
    docker network create --subnet=172.25.0.0/16 spider-network




    
    version: '3.6'
    services:
      django:
        image: "registry.sensetime.com/spider/sensespider:v1.0"
        volumes:
          - spiderdata:/data
        privileged: true 
        networks: 
         - spider-network
        ports:
          - "8080:8080"
        working_dir: /home/renkuanze/workspace/sensespider
        entrypoint: bash run.sh 
        tty: true
        container_name: django
       
      splash: 
        image: "scrapinghub/splash"
        container_name: splash
        network_mode: "service:django"
      react:
        image: "registry.sensetime.com/spider/sensespider-react:v1.0"
        working_dir: /home/node/sensespider-react
        entrypoint: npm start 
        container_name: node
        network_mode: "service:django"
    volumes:
      spiderdata:
        driver: local-persist
        driver_opts:
          mountpoint: /data/spider_data
    
    networks:
      spider-network:
        external: true
    

















