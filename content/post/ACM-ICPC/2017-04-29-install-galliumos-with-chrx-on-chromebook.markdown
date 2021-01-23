---
author: 111qqz
date: 2017-04-29 15:09:51+00:00
draft: false
title: install galliumOS on chromebook with chrx
type: post
url: /2017/04/install-galliumos-with-chrx-on-chromebook/
categories:
- 其他
tags:
- chromebook
- galliumOS
---

我的chromebook 是　samsung 3

查阅[Hardware Compatibility](https://wiki.galliumos.org/Hardware_Compatibility) 可以知道我的cb支持　gallium,对应的cpu 是Intel Braswell

<del>然后去[galliumos　官网](https://galliumos.org/download)　下载相应版本。 </del> (发现这种做法并不需要自己下载。。。)

安装　galliumOS大体有两种方法，一种是完全去掉chromeOS,这种方法需要需要拆机去除写保护。。。我嫌麻烦。。。于是打算另一种，使用[chrx　](https://chrx.org/#usage)

步骤如下：


<blockquote>

> 
> 
 	  1. Enable [Developer Mode](http://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices) (process is model-specific; for Acer C720, press `ESC+F3(Refresh)+Power`), then reboot
 	  2. Load ChromeOS by pressing `CTRL+D` at the white "OS verification is OFF" screen
 	  3. Configure your Wi-Fi network if necessary, then log in (Guest account is fine)
 	  4. Open the ChromeOS Terminal by pressing `CTRL+ALT+T`, and enter `shell` at the prompt
 	  5. Update firmware, if necessary (_required_ for Bay Trail and Braswell models, _recommended_ for Broadwell and Skylake models, _optional_ for Haswell models -- see [chromebooks](https://chrx.org/#chromebooks))
 	  6. Run **chrx**: `cd ; curl -Os https://chrx.org/go && sh go` (see [options](https://chrx.org/#options))
 	  7. Follow on-screen instructions to prepare your Chromebook for installation
 	  8. Reboot, then repeat steps 2-4 and 6 to install and configure your new system

</blockquote>


对于braswell model，必须要刷一个固件才可以：[mrchromebox](https://mrchromebox.tech/#fwscript)a

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/04/343921857.jpg)
](https://111qqz.com/wordpress/wp-content/uploads/2017/04/343921857.jpg)



刷好之后按照步骤安装。。。



![](http://i2.muimg.com/567571/9d16e1671a96b2a9.jpg)




安装成功以后。。。

做了以下事情：



 	  * 安装搜狗输入法
 	  * 安装中文字体
 	  * 安装vim
 	  * 安装fish个
 	  * 安装shadowsocks
 	  * 安装guake
 	  * 登录chromium 同步各种插件
 	  * 安装aria2
 	  * 安装franz
 	  * 安装ssh
 	  * 安装variety
 	  * 使用xmodmap，将搜索键映射到win,映射了几个不用的功能键（到f1,f3 Page_Down,Page_Up）



补一个xmodmap的配置文件。

    
    keycode 133 = Super_L
    keycode 72  = Page_Up
    keycode 73  = Page_Down











