---
author: 111qqz
date: 2017-06-26 16:09:19+00:00
draft: false
title: archlinux/manjaro 下 安装 qq/tim
type: post
url: /2017/06/install-qq-on-manjaro/
categories:
- 其他
---

参考资料：[install qq/tim on linux with wine](https://infinitescript.com/2017/03/install-qq-in-linux-with-wine/)

[wine运行qq不能输入账号](http://tieba.baidu.com/p/2848294621)

This tutorial introduces how to install QQ/TIM in Linux with Wine, which had been tested on ArchLinux with Wine 2.4.


### Prerequisites


Before start, you need to get the latest Wine. I'm not sure whether QQ/TIM can run on lower version of Wine. In ArchLinux, you can easily get the latest Wine using following command:








?



    
    pacman -S wine
    








However, in Debian, you need to install Wine with some more steps. You can see this [tutorial](https://wiki.winehq.org/Debian).

Then, you need to install a helper of Wine, Winetricks. Winetricks is a script to download and install various redistributable runtime libraries needed to run some programs in Wine. To install Winetricks, you can use following command:

    
    sudo wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks -O /usr/local/bin/winetricks
    sudo chmod a+x /usr/local/bin/winetricks




After that, we need to fix some problems manually caused by Winetricks. According to this [Bug Report](https://github.com/Winetricks/winetricks/issues/600), we need to download `W2KSP4_EN.EXE` from other mirror sites:

Similarly, we need to download `InstMsiW.exe` manually:

    
    mkdir -p $HOME/.cache/winetricks/msls31
    wget ftp://ftp.iop.org/pub/ESXP6/instmsiw.exe -O $HOME/.cache/winetricks/msls31/InstMsiW.exe
    Initialize Wine Environment





### Initialize Wine Environment


To create a 32-bit WINE system, you need to open a terminal and run the following command:

    
    	
    WINEARCH=win32 wine wineboo




Then you need to run `winecfg` in terminal and change Windows version to `Windows 7`.

[![](https://static.haozhexie.com/wordpress/wp-content/uploads/2017/03/Winecfg-Windows-Version.png)
](https://infinitescript.com/wordpress/wp-content/uploads/2017/03/Winecfg-Windows-Version.png)


### Install Core Fonts


Next, we are going to install essential fonts for Wine.

    
    	
    winetricks corefonts cjkfonts


where `corefonts` stands for MS Arial, Courier, Times fonts, and `cjkfonts` denotes all Chinese, Japanese and Korean fonts and alias.


### Install Windows Components


Then, we need to install components which are need by QQ / TIM.

    
    winetricks msxml6 riched20 riched30 vcrun6


where `msxml6` represents MS XML Core Services 6.0 SP1, `riched20` and `riched30` mean MS RichEdit Control 2.0 and MS RichEdit Control 3.0 respectively, and `vcrun6` is Visual C++ 6 SP4 libraries.

You are supposed to be asked to fill in information during the MSXML6 installation.

[![](https://static.haozhexie.com/wordpress/wp-content/uploads/2017/03/MSXML6-Installation.png)
](https://infinitescript.com/wordpress/wp-content/uploads/2017/03/MSXML6-Installation.png)


### Install QQ / TIM


In this section, we are about to install QQ / TIM. We are assume that you have already get installers from [official website](https://im.qq.com/). Run your installer with following command:

    
    LC_ALL=zh_CN.utf8 wine /path/to/installer.exe


In this tutorial, we use TIM installer as an example:

[![](https://static.haozhexie.com/wordpress/wp-content/uploads/2017/03/TIM-Installation.png)
](https://infinitescript.com/wordpress/wp-content/uploads/2017/03/TIM-Installation.png)

Please be patient and ignore following error message in terminal:








[?](https://infinitescript.com/2017/03/install-qq-in-linux-with-wine/#)


<table cellpadding="0" cellspacing="0" border="0" >
<tbody >
<tr >

<td class="gutter" >


1

</td>

<td class="code" >





`[8:142:0322/131343:4128351:ERROR:qd_helper.cpp(234)] 328 Status: 2`




</td>
</tr>
</tbody>
</table>






An instance of QQ / TIM will automatically started after installation finished.[![](https://static.haozhexie.com/wordpress/wp-content/uploads/2017/03/TIM-Login-Window.png)
](https://infinitescript.com/wordpress/wp-content/uploads/2017/03/TIM-Login-Window.png)

Due to security check of QQ / TIM, QQ cannot start normally when you restart your PC. We need to apply a patch to remove security check components. You can download this patch from [this link](https://infinitescript.com/wordpress/wp-content/uploads/2017/03/QQ-Security-Check-Patch.zip) or search "QQ安全校验补丁" from the Internet.

After unzip this patch, use following commands to apply this patch:

    
    mv QQ-Security-Check-10.0.exe ~/.wine/drive_c/Program\ Files/Tencent/QQ/Bin
    LC_ALL=zh_CN.utf8 wine ~/.wine/drive_c/Program\ Files/Tencent/QQ/Bin/QQ-Security-Check-10.0.exe
    





### Create Shortcut


Now you can start QQ using following commands:

    
    # Start QQ
    LC_ALL=zh_CN.utf8 wine ~/.wine/drive_c/Program\ Files/Tencent/QQ/Bin/QQ.exe
     
    # Or start TIM
    LC_ALL=zh_CN.utf8 wine ~/.wine/drive_c/Program\ Files/Tencent/TIM/Bin/TIM.exe




In order to start up QQ / TIM, you can create a desktop entry in `/usr/share/applications/TIM.desktop`as follows:

    
    [Desktop Entry]
    Categories=Network;InstantMessaging;
    Exec=env LC_ALL=zh_CN.utf8 wine $HOME/.wine/drive_c/Program\ Files/Tencent/TIM/Bin/TIM.exe
    Icon=/path/to/logo.png
    NoDisplay=false
    StartupNotify=true
    Terminal=false
    Type=Application
    Name[en_US]=TIM
    Name[zh_CN]=TIM




Enjoy!



遇到了无法输入账号的bug(但是可以输入密码）

解决办法是：

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/06/798e9b0a304e251fad39eb3ea586c9177d3e5367.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/06/798e9b0a304e251fad39eb3ea586c9177d3e5367.png)[![](https://111qqz.com/wordpress/wp-content/uploads/2017/06/5a6afb03918fa0eca7ca6acb249759ee3c6ddb25.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/06/5a6afb03918fa0eca7ca6acb249759ee3c6ddb25.png)


