---
author: 111qqz
date: 2017-06-07 06:21:12+00:00
draft: false
title: vim下python 的配置
type: post
url: /2017/06/vimrc-for-python/
categories:
- 其他
tags:
- python
- vim
---

### 由于最近要做数字图像处理的大作业，以及之后一段时间，估计写python多一些，所以打算花些时间配置下vim.




## 1. 一键执行




#### 其实之前一直有的。。不过没有效果，就没有管。发现问题是，python对应的filetype为"python"，而不是"py"



    
    func! CompileRunGcc()
    	exec "w"
    	if &filetype == 'c'
    		exec "!g++ % -o %<"
    		exec "! ./%<"
    	elseif &filetype == 'cpp'
    		exec "!g++ % -std=gnu++11  -Wall   -o %<"
    		exec "! ./%<"
    	elseif &filetype == 'java' 
    		exec "!javac %" 
    		exec "!java %<"
    	elseif &filetype == 'sh'
    		:!./%
    	elseif &filetype == 'python'
    	"	exec "!python %"
    	"	exec "!python %<"
    		exec "!python2.7 %"
    	endif
    endfunc




## **2.代码补全**




### 不想折腾了。。既然ycm也支持python,就先用用看好了。。不行再换别的。




### 放一段ycm　for python的配置文件



    
     
    "默认配置文件路径"
    let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
    "打开vim时不再询问是否加载ycm_extra_conf.py配置"
    let g:ycm_confirm_extra_conf=0
    set completeopt=longest,menu
    "python解释器路径"
    let g:ycm_path_to_python_interpreter='/usr/bin/python'
    "是否开启语义补全"
    let g:ycm_seed_identifiers_with_syntax=1
    "是否在注释中也开启补全"
    let g:ycm_complete_in_comments=1
    let g:ycm_collect_identifiers_from_comments_and_strings = 0
    "开始补全的字符数"
    let g:ycm_min_num_of_chars_for_completion=2
    "补全后自动关机预览窗口"
    let g:ycm_autoclose_preview_window_after_completion=1
    " 禁止缓存匹配项,每次都重新生成匹配项"
    let g:ycm_cache_omnifunc=0
    "字符串中也开启补全"
    let g:ycm_complete_in_strings = 1




## **3. 语法检查**




### Syntastic大家都知道了。。。。看到了[异步检测插件ALE](https://zhuanlan.zhihu.com/p/23317292)，打算试一下。




### [ale_github](https://github.com/w0rp/ale)




### 需要注意的是，这个插件需要vim 8.0+的特性。。。




### 放一波配置文件



    
    """"""""""""""""""for ale begin """"""""""""""""
    let g:ale_sign_column_always = 1  "保持侧边栏可见：
    
    let g:ale_sign_error = '>>'    "改变错误和警告标识符
    let g:ale_sign_warning = '--'
    let g:ale_statusline_format = ['⨉ %d', '⚠ %d', '⬥ ok']  "改变状态栏信息格式
    
    "自定义跳转错误行快捷键：
    nmap <silent> <C-k> <Plug>(ale_previous_wrap)
    nmap <silent> <C-j> <Plug>(ale_next_wrap)
    "消除某excption not caught的警告
    let g:ale_emit_conflict_warnings = 0




## **4. 编程提示(jedi-vim)**




### 　据说是vim写python的神器。。。装来看看。。。




### 据说默认配置就够了，先不折腾了





### 







### 









