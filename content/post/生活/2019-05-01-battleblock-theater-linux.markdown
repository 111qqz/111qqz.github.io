---
author: 111qqz
date: 2019-05-01 12:09:18+00:00
draft: false
title: 'BattleBlock Theater linux下无法启动的解决办法　（　void* MemoryBlock::Alloc(unsigned int):
  Assertion failed ）'
type: post
url: /2019/05/battleblock-theater-linux-start-failed/
categories:
- 其他
tags:
- steam
---

在steam上买了　BattleBlock Theater，　官方说支持linux，但是却无法启动。

在steam里启动看不到log,于是找到游戏的安装目录。

/home/coder/.steam/steam/steamapps/common/BattleBlock Theater

在终端下启动，报错:

BattleBlockTheater: /media/BGBS/BBT_Linux/Core/MemorySystem.cpp:161: void* MemoryBlock::Alloc(unsigned int): Assertion `(!"Got request for zero bytes!")' failed.
^C[1]    22303 abort (core dumped)  ./BattleBlockTheater

google了一下发现这似乎是游戏本身的bug,这里有一个[workaround](https://steamcommunity.com/app/238460/discussions/1/451848855012217196/#c343787920142097238)

办法是使用hex editor将游戏的可执行文件中， **从offset 0x24F2BE 开始的6个字节替换成0x90**

我使用的hex editor 是hexcurse,　这里有一个[使用指南](https://www.maketecheasier.com/using-hex-editor-linux/)　可以参考。

[![](https://111qqz.com/wp-content/uploads/2019/05/battleBlock.png)
](https://111qqz.com/wp-content/uploads/2019/05/battleBlock.png)










