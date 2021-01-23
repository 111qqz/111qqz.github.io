---
author: 111qqz
date: 2015-12-28 08:17:03+00:00
draft: false
title: 在linux mint 上安装 Oracle JDK 的方法
type: post
url: /2015/12/linux-mint--oracle-jdk-/
categories:
- 其他
tags:
- jdk
---

1. Open up the Terminal _(Alt + F2 > Terminal)_.

2. Remove OpenJDK installation.

    
    sudo apt-get update && apt-get remove openjdk*


3. Download Oracle JDK from [here](http://www.oracle.com/technetwork/java/javase/downloads/index.html). You are looking for a linux version with tar.gz extension. Also choose the right version from 32-bit (x86)  and 64bit (x64) one.

4. Change directory into one with downloaded tarball. In my case _$HOME/Downloads_.

    
    cd ~/Downloads


5. Extract tarball. Replace with a name of dowloaded file. (just press Tab and it will be autocompleted.)

    
    tar -zxvf jdk-


6. As a root create a folder in /opt where jdk will be stored.

    
    sudo mkdir -p /opt/java


7. Move extracted folder to /opt/java. In my case, version number was **1.7.0_25**.

    
    sudo mv jdk1.7.0_25 /opt/java


8. Make JDK system default.

    
    sudo update-alternatives --install "/usr/bin/java" "java" "/opt/java/jdk1.7.0_25/bin/java" 1
    
    sudo update-alternatives --set java /opt/java/jdk1.7.0_25/bin/java


9. Test installed java version.


java version "1.7.0_25" Java(TM) SE Runtime Environment (build 1.7.0_25-b15) Java HotSpot(TM) 64-Bit Server VM (build 23.25-b01, mixed mode)




    
    $ java -version
