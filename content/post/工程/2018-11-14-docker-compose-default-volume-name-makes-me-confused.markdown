---
author: 111qqz
date: 2018-11-14 08:06:57+00:00
draft: false
title: 记一次在 docker compose 中使用volume的踩坑记录
type: post
url: /2018/11/docker-compose-default-volume-name-makes-me-confused/
categories:
- 其他
tags:
- docker
---

### 现象:


使用docker compose 挂载 named volume 无效（且没有错误提示)


### 排查过程:


一开始是没有使用docker-compose命令，直接使用docker run  -v 命令，挂载两个绝对路径，没有问题。

然后使用named volume，在这里使用了[local-persist](https://github.com/CWSpear/local-persist) 插件，来指定数据卷(volume)在host上的位置。直接用docker run  -v 命令，依然没有问题。

接下里打算放到docker compose里面，发现并没有挂载成功。

但是在docker compose里面，挂载两个绝对路径是ok的。

于是怀疑是volume的问题

此时使用docker inspect 查看 用docker compose 启动起来的，挂载named volume的容器

发现mount里面，挂载的named volume并不是我在docker-compose.yml填写的名称，而是多了一个前缀，这个前缀恰好是docker-compose.yml 文件所在的目录名称。

查了一下，发现果然不止我一个人被坑到orz [Docker-compose prepends directory name to named volumes](https://forums.docker.com/t/docker-compose-prepends-directory-name-to-named-volumes/32835)

其实应该直接使用docker inspect来排查的...应该会更快找到问题


### 解决办法：


有几种解决办法：



 	  * 不手动创建volume，而是在docker-compose.yml中，设置volume的mountpoint
 	  * 在docker-compose.yml中，添加external: true的选项到 volume中，参考[external](https://docs.docker.com/compose/compose-file/#external)

顺便附上我的docker-compose.yml文件

    
    version: '3'
    services:
      django:
        image: "registry.sensetime.com/spider/sensespider:v1.0"
        volumes:
          - spiderdata:/data
        privileged: true 
        ports:
          - "8000:8000"
        working_dir: /home/renkuanze/workspace/sensespider
        entrypoint: bash run.sh
        tty: true
        container_name: django
       
      splash: 
        image: "scrapinghub/splash"
        container_name: splash
        network_mode: "service:django"
    volumes:
      spiderdata:
        driver: local-persist
        driver_opts:
          mountpoint: /data/spider_data
            
    











