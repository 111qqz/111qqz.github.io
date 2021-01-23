---
author: 111qqz
date: 2017-04-30 06:58:27+00:00
draft: false
title: ubuntu  包管理(apt-get)损坏的解决办法
type: post
url: /2017/04/fix-ubuntu-package-manager-broken-problem/
categories:
- 其他
---

症状是不管安装什么，都会说有一大堆依赖无法安装。。。

大概是: a depends b[i],but b[i] is not be installed. (b==0..n)

最后会提示Unable to correct problems, you have held broken packages

解决办法：用synaptic工具，把可能存在问题的包都清除掉。

[参考资料](https://askubuntu.com/questions/118749/package-system-is-broken-how-to-fix-it)

顺便想吐槽。。。ubuntu的包管理工具好辣鸡啊。。

随便装点东西竟然就损坏了？

我刚才装chrome,然后出了错误，提示我apt-get -f install 解决问题。。。

然后包管理就挂了？

想起当年虽然装的第一个发行版是ubuntu,但是并不好用啊？

好好使用的第一个还是mint

所以其实ubuntu不是很适合新手吧。。。只不过知名度高。。。。资料多。。。

要我说  manjaro 或者 linux mint 都要比ubuntu新手友好的多啊orz
