---
author: 111qqz
date: 2017-07-28 09:13:34+00:00
draft: false
title: manjaro(archlinux) 安装 YouCompleteMe
type: post
url: /2017/07/install-YouCompleteMe-on-manjaro/
categories:
- 其他
tags:
- archlinux
- vim
- youcompleteme
---

来来回回折腾了好多次，aur直接安装或者手动编译，安装后都无法补全

ycm的log文件是在/tmp目录下的。

发现问题是缺少libtinfo.so.5

    
    2017-07-28 17:02:12,667 - ERROR - Error occurred while loading global extra conf /home/coder/.ycm_extra_conf.py
    Traceback (most recent call last):
      File "/home/coder/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/../ycmd/extra_conf_store.py", line 94, in _CallGlobalExtraConfMethod
        module = Load( global_ycm_extra_conf, force = True )
      File "/home/coder/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/../ycmd/extra_conf_store.py", line 173, in Load
        module = LoadPythonSource( _RandomName(), module_file )
      File "/home/coder/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/../ycmd/utils.py", line 400, in LoadPythonSource
        return imp.load_source( name, pathname )
      File "/home/coder/.ycm_extra_conf.py", line 32, in <module>
        import ycm_core
    ImportError: libtinfo.so.5: cannot open shared object file: No such file or directory
    2017-07-28 17:02:12,667 - ERROR - libtinfo.so.5: cannot open shared object file: No such file or directory
    Traceback (most recent call last):
      File "/home/coder/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/server_utils.py", line 96, in CompatibleWithCurrentCore
        ycm_core = ImportCore()
      File "/home/coder/.vim/bundle/YouCompleteMe/third_party/ycmd/ycmd/server_utils.py", line 88, in ImportCore
        import ycm_core as ycm_core
    ImportError: libtinfo.so.5: cannot open shared object file: No such file or directory
    


解决办法：

    
     sudo pacman-key --refresh-keys
     gpg --keyserver pgp.mit.edu --recv-keys C52048C0C0748FEE227D47A2702353E0F7E48EDB
     yaourt -S libtinfo5
    
    


[参考a资料](https://github.com/Valloric/YouCompleteMe/issues/778)

比较诡异的是，我把vim配置删掉，就可以补全，以至于之前一直以为是ycm和配置文件中的某个内容冲突。
