---
author: 111qqz
date: 2017-06-08 18:26:14+00:00
draft: false
title: manjaro installation guide
type: post
url: /2017/06/manjaro-installation-guide/
categories:
- 其他
tags:
- manjaro
---

20180214 update:

第一个版本已经比较久了，于是更新一下，顺便写了个脚本orz


    
    pacman-mirrors -c China
    echo " [archlinuxcn] " >> /etc/pacman.conf
    echo " SigLevel = Optional TrustedOnly "  >> /etc/pacman.conf
    echo " Server = https://mirrors.ustc.edu.cn/archlinuxcn/\$arch" >> /etc/pacman.conf
    
    
    echo "[arch4edu]" >> /etc/pacman.conf
    echo "SigLevel = Never" >> /etc/pacman.conf
    echo "Server = http://mirrors.tuna.tsinghua.edu.cn/arch4edu/\$arch " >> /etc/pacman.conf
    pacman -Syyu
    pacman -S archlinuxcn-keyring
    
     pacman -S yakuake fish gvim 
     pacman -S google-chrome chromium
     pacman -S  wget aria2  remarkable netease-cloud-music
     pacman -S fcitx fcitx-configtool fcitx-sogoupinyin fcitx-im kcm-fcitx
     pacman -S shadowsocks-qt5
     pacman -S wqy-microhei wqy-microhei-lite wqy-bitmapfont wqy-zenhei ttf-arphic-ukai ttf-arphic-uming adobe-source-han-sans-cn-fonts
    
    cat >> ~/.xprofile  <<EOF
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS="@im=fcitx"
    EOF
    
     pacman -S proxychains-ng
    cat >> /etc/proxychains.conf <<EOF
    quiet_mode
    dynamic_chain
    chain_len = 1 #round_robin_chain和random_chain使用
    proxy_dns
    remote_dns_subnet 224
    tcp_read_time_out 15000
    tcp_connect_time_out 8000
    localnet 127.0.0.0/255.0.0.0
    localnet 10.0.0.0/255.0.0.0
    localnet 172.16.0.0/255.240.0.0
    localnet 192.168.0.0/255.255.0.0
     
    [ProxyList]
    socks5  127.0.0.1 1080
    http    127.0.0.1 1087
    EOF
     
    pacman -S vundle-git
    cat >> ~/.vimrc  <<EOF
    set guifont=Neep\ 18
    
    map <F9> :call SaveInputData()<CR>
    func! SaveInputData()
        exec "tabnew"
        exec 'normal "+gP'
        exec "w! code/in.txt"
    endfunc
    
    
    
    "colorscheme torte
    " colorscheme murphy
    colorscheme elflord
    " colorscheme molokai
    "colorscheme elisex
    "colorscheme colorer
    "colorscheme blacklight
    "colorscheme blue
    "colorscheme darkblue
    "colorscheme evening
    "colorscheme shine
    
    "colorscheme molokai
    "colorscheme solarized
    "colorscheme sift
    "colorscheme advantage
    "colorscheme 256_jungle
    
    
    "set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
    "set termencoding=utf-8
    "set encoding=utf-8
    "set fileencodings=ucs-bom,utf-8,cp936
    "set fileencoding=utf-8
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " 显示相关
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "set shortmess=atI   " 启动的时候不显示那个援助乌干达儿童的提示
    "winpos 5 5          " 设定窗口位置
    "set lines=40 columns=155    " 设定窗口大小
    set go=             " 不要图形按钮
    "color asmanian2     " 设置背景主题
    "set guifont=Courier_New:h10:cANSI   " 设置字体
    syntax on           " 语法高亮
    autocmd InsertLeave * se nocul  " 用浅色高亮当前行
    autocmd InsertEnter * se cul    " 用浅色高亮当前行
    "set ruler           " 显示标尺
    set showcmd         " 输入的命令显示出来，看的清楚些
    "set cmdheight=1     " 命令行（在状态行下）的高度，设置为1
    "set whichwrap+=<,>,h,l   " 允许backspace和光标键跨越行边界(不建议)
    "set scrolloff=3     " 光标移动到buffer的顶部和底部时保持3行距离
    set novisualbell    " 不要闪烁(不明白)
    set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}   "状态行显示的内容
    set laststatus=1    " 启动显示状态行(1),总是显示状态行(2)
    "set foldenable      " 允许折叠
    set foldmethod=manual   " 手动折叠
    "set background=dark "背景使用黑色
    set nocompatible  "去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限
    " 显示中文帮助
    if version >= 603
        set helplang=cn
        set encoding=utf-8
    endif
    " 设置配色方案
    "colorscheme murphy
    "字体
    "if (has("gui_running"))
    "   set guifont=Bitstream\ Vera\ Sans\ Mono\ 10
    "endif
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """""新文件标题
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "新建.c,.h,.sh,.java文件，自动插入文件头
    autocmd BufNewFile *.cpp,*.[ch],*.sh,*.java exec ":call SetTitle()"
    ""定义函数SetTitle，自动插入文件头
    "map <F4> :call SetTitle()<CR>
    func SetTitle()
        "如果文件类型为.sh文件
        if &filetype == 'sh'
            call setline(1,"\#########################################################################")
            call append(line("."), "\# File Name: ".expand("%"))
            call append(line(".")+1, "\# Author: 111qqz")
            call append(line(".")+2, "\# mail: renkuanze@sensetime.com")
            call append(line(".")+3, "\# Created Time: ".strftime("%c"))
            call append(line(".")+4, "\#########################################################################")
            call append(line(".")+5, "\#!/bin/bash")
            call append(line(".")+6, "")
        else
            let l = 0
            let l = l + 1 | call setline(l,'/* ***********************************************')
            let l = l + 1 | call setline(l,'Author :111qqz')
                    let l = l + 1 | call setline(l,'mail: renkuanze@sensetime.com'
            let l = l + 1 | call setline(l,'Created Time :'.strftime('%c'))
            let l = l + 1 | call setline(l,'File Name :'.expand('%'))
            let l = l + 1 | call setline(l,'************************************************ */')
            let l = l + 1 | call setline(l,'')
        endif
        if &filetype == 'cpp'
            let l = l + 1 | call setline(l,'#include <bits/stdc++.h>')
            let l = l + 1 | call setline(l,'')
            let l = l + 1 | call setline(l,'using namespace std;')
            let l = l + 1 | call setline(l,'int main()')
            let l = l + 1 | call setline(l,'{')
            let l = l + 1 | call setline(l,'    return 0;')
            let l = l + 1 | call setline(l,'}')
    
    
        endif
        if &filetype == 'c'
            call append(line(".")+6, "#include<stdio.h>")
            call append(line(".")+7, "")
        endif
        if &filetype == 'java'
            call append(line(".")+6,"public class ".expand("%"))
            call append(line(".")+7,"")
        endif
        "新建文件后，自动定位到文件末尾
        autocmd BufNewFile * normal G23
    endfunc
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "键盘命令
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""v""""""""""""""""""""""""""""""""""""""""
    
    nmap <leader>w :w!<cr>
    nmap <leader>f :find<cr>
    
    nmap <F8> :TagbarToggle<CR>
    
    
    " 映射全选+复制 ctrl+a
    map <C-A> ggvG"+Y
    map! <C-A> <Esc>ggVGY
    map <F12> gg=G
    " 选中状态下 Ctrl+c 复制
    vmap <C-c> "+y
    "去空行
    nnoremap <F2> :g/^\s*$/d<CR>
    "比较文件
    nnoremap <C-F2> :vert diffsplit
    "新建标签
    map <M-F2> :tabnew<CR>
    "列出当前目录文件
    map <F3> :tabnew .<CR>
    "打开树状文件目录
    map <C-F3> \be
    "C，C++ 按F5编译运行
    map <F5> :call CompileRunGcc()<CR>
    
    au BufRead *.py map <buffer> <F6> :w<CR>:!/usr/bin/env python % <CR>
    
    let g:tagbar_usearrows = 1
    nnoremap <leader>l :TagbarToggle<CR>
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
        "   exec "!python %"
        "   exec "!python %<"
            exec "!python2.7 %"
        endif
    endfunc
    "C,C++的调试
    map <F8> :call Rungdb()<CR>
    func! Rungdb()
        exec "w"
        exec "!g++ % -std=c++11 -g  -o %<"
        exec "!gdb ./%<"
    endfunc
    
    
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    ""实用设置
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " 设置当文件被改动时自动载入
    set autoread
    " quickfix模式
    autocmd FileType c,cpp map <buffer> <leader><space> :w<cr>:make<cr>
    "代码补全
    set completeopt=preview,menu
    "允许插件
    filetype plugin on
    "共享剪贴板
    set clipboard+=unnamed
    "从不备份
    set nobackup
    "make 运行
    :set makeprg=g++\ -Wall\ \ %
    "自动保存
    set autowrite
    set ruler                   " 打开状态栏标尺
    set cursorline              " 突出显示当前行
    set magic                   " 设置魔术
    set guioptions-=T           " 隐藏工具栏
    set guioptions-=m           " 隐藏菜单栏
    "set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %c:%l/%L%)\
    " 设置在状态行显示的信息
    set foldcolumn=0
    set foldmethod=indent
    set foldlevel=3
    set foldenable              " 开始折叠
    " 不要使用vi的键盘模式，而是vim自己的
    set nocompatible
    " 语法高亮
    set syntax=on
    " 去掉输入错误的提示声音
    set noeb
    " 在处理未保存或只读文件的时候，弹出确认
    set confirm
    " 自动缩进
    set autoindent
    set clipboard+=unnamed
    set cindent
    " Tab键的宽度
    set tabstop=8
    " 统一缩进为8
    set softtabstop=4
    set shiftwidth=4
    " 不要用空格代替制表符
    set noexpandtab
    " 在行和段开始处使用制表符
    set smarttab
    " 显示行号
    set number
    " 历史记录数
    set history=1000
    "禁止生成临时文件
    set nobackup
    set noswapfile
    "搜索忽略大小写
    set ignorecase
    "搜索逐字符高亮
    set hlsearch
    set incsearch
    "行内替换
    set gdefault
    "编码设置
    set enc=utf-8
    set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
    "语言设置
    set langmenu=zh_CN.UTF-8
    set helplang=cn
    " 我的状态行显示的内容（包括文件类型和解码）
    "set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}
    "set statusline=[%F]%y%r%m%*%=[Line:%l/%L,Column:%c][%p%%]
    " 总是显示状态行
    set laststatus=2
    " 命令行（在状态行下）的高度，默认为1，这里是2
    set cmdheight=2
    " 侦测文件类型
    filetype on
    " 载入文件类型插件
    filetype plugin on
    " 为特定文件类型载入相关缩进文件
    filetype indent on
    " 保存全局变量
    set viminfo+=!
    " 带有如下符号的单词不要被换行分割
    set iskeyword+=_,$,@,%,#,-
    " 字符间插入的像素行数目
    set linespace=0
    " 增强模式中的命令行自动完成操作
    set wildmenu
    " 使回格键（backspace）正常处理indent, eol, start等
    set backspace=2
    " 允许backspace和光标键跨越行边界
    set whichwrap+=<,>,h,l
    " 可以在buffer的任何地方使用鼠标（类似office中在工作区双击鼠标定位）
    set mouse=a
    set selection=exclusive
    set selectmode=mouse,key
    " 通过使用: commands命令，告诉我们文件的哪一行被改变过
    set report=0
    " 在被分割的窗口间显示空白，便于阅读
    set fillchars=vert:\ ,stl:\ ,stlnc:\
    " 高亮显示匹配的括号
    set showmatch
    " 匹配括号高亮的时间（单位是十分之一秒）
    set matchtime=1
    " 光标移动到buffer的顶部和底部时保持3行距离
    set scrolloff=3
    " 为C程序提供自动缩进
    set smartindent
    " 高亮显示普通txt文件（需要txt.vim脚本）
    set cursorline
    hi CursorLine  cterm=bold   ctermbg=blue ctermfg=yellow
    au BufRead,BufNewFile *  setfiletype txt
    "自动补全
    ":inoremap ( ()<ESC>i
    ":inoremap ) <c-r>=ClosePair(')')<CR>
    ":inoremap { {<CR>}<ESC>O
    ":inoremap } <c-r>=ClosePair('}')<CR>
    ":inoremap [ []<ESC>i
    ":inoremap ] <c-r>=ClosePair(']')<CR>
    ":inoremap " ""<ESC>i
    ":inoremap ' ''<ESC>i
    function! ClosePair(char)
        if getline('.')[col('.') - 1] == a:char
            return "\<Right>"
        else
            return a:char
        endif
    endfunction
    filetype plugin indent on
    "打开文件类型检测, 加了这句才可以用智能补全
    set completeopt=longest,menu
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    
    
    
    
    
    
    """""""""""""""""vundle设置"""""""""""""""""
    set nocompatible              " be iMproved, required
    "filetype off                  " required
    set shell=/bin/bash
    
    
    " Interface
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    Plugin 'VundleVim/Vundle.vim'
    " vim-scripts repos
    "
    "
    
      Plugin 'MarcWeber/vim-addon-mw-utils'
      Plugin 'tomtom/tlib_vim'
      Plugin 'garbas/vim-snipmate'
    
      " Optional:
     Plugin 'honza/vim-snippets'
     Plugin 'davidhalter/jedi-vim'
     Plugin 'vim-airline/vim-airline'
     Plugin 'vim-airline/vim-airline-themes'
     Plugin 'bash-support.vim'
     Plugin 'perl-support.vim'
     Plugin 'majutsushi/tagbar'
     Plugin 'ZoomWin'
     Plugin 'morhetz/gruvbox'
     Plugin 'scrooloose/syntastic'
    Plugin 'Valloric/YouCompleteMe'
    call vundle#end()            " required
    filetype plugin indent on    " required
    
    
    
    
    """""""""""""""""youcompleteme设置"""""""""""""""""
    
    
    "let g:ycm_autoclose_preview_window_after_completion=1
    "nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>
    
    " YouCompleteMe 功能
    " 补全功能在注释中同样有效
    "let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py'
    "let g:ycm_complete_in_comments=1
     "允许 vim 加载 .ycm_extra_conf.py 文件，不再提示
    "let g:ycm_confirm_extra_conf=0
    
    "let g:ycm_error_symbol = '<<'
    "let g:ycm_warning_symbol = '<'
    "nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR>
    "nnoremap <leader>gf :YcmCompleter GoToDefinition<CR>
    "nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR>
    "nmap <F4> :YcmDiags<CR>
    
    
    
    
    """""""""""""""""youcompleteme设置 by wyz"""""""""""""""""
    let g:cpp_class_scope_highlight=1
    let g:cpp_experimental_template_highlight=1
    let g:ycm_show_diagnostics_ui=0
    let g:ycm_enable_diagnostic_signs=0
    let g:ycm_enable_diagnostic_highlighting = 0
    let g:ycm_echo_current_diagnostic = 0
    let g:ycm_collect_identifiers_from_tags_files = 1
    let g:ycm_key_invoke_completion = '<C-Q>'
    let g:ycm_seed_identifiers_with_syntax = 1
    let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
    let g:ycm_collect_identifiers_from_tags_files = 1
    let g:ycm_confirm_extra_conf = 0
    let g:ycm_autoclose_preview_window_after_completion = 1
    let g:ycm_autoclose_preview_window_after_insertion = 1
    
    
    
    " for python
    "
    "
    
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
    
    
    
    """"""""""""""'for airline""""""""""""""""
    
    let g:airline_powerline_fonts = 1
    let g:airline#extensions#tabline#enabled = 1
     let g:airline#extensions#tabline#buffer_nr_show = 1
    let g:airline#extensions#tabline#left_sep = ' '
    let g:airline#extensions#tabline#left_alt_sep = '|'
    
     nnoremap <F2> :bnext<CR>
     nnoremap <F4> :bprevious<CR>
    
     if !exists('g:airline_symbols')
        let g:airline_symbols = {}
        endif
    
     let g:airline_left_sep = '⮀'
      let g:airline_left_alt_sep = '⮁'
      let g:airline_right_sep = '⮂'
      let g:airline_right_alt_sep = '⮃'
      let g:airline_symbols.branch = '⭠'
      let g:airline_symbols.readonly = '⭤'
    
    EOF
    
    echo " please install vim plug-in"
    





出于目前对manjaro的依赖，以及没有找到很简单易行的备份系统的方案的原因，决定详细记录一下系统安装的过程，以防哪天系统挂掉了，可以快速恢复。



### **1.关于更换源**



坑点主要在系统默认的源是国外源，如何切换成中国源，网上有很多教程，但这些教程都是针对Arch的，弄来弄去也很不容易搞好，而且胡乱修改会把Manjaro的源破坏掉（不要问我怎么知道的）。
其实网上有个blog的方法很方便，附上连接

就两行命令搞定：


    
    sudo pacman-mirrors -c China  //选择中国源并更新
    sudo pacman -Syyu  //更新系统



2.安装搜狗输入法

具体为，安装fcitx,安装fcitx-sogoupinyin,安装kcm-fcitx

然后



~/.xprofile 文件中添加如下内容







    
    export GTK_IM_MODULE=fcitx
    export QT_IM_MODULE=fcitx
    export XMODIFIERS="@im=fcitx"


由于初始安装系统时选择的是英文，在安装搜狗输入法之前先安装了chrome，导致在chrome中无法输入中文（而在firefox中可以），解决办法时，删除掉.config中google-chrome文件夹即可

3 添加archlinuxcn源

在 `/etc/pacman.conf` 文件末尾添加以下两行：

    
    [archlinuxcn]
    SigLevel = Optional TrustedOnly
    Server = https://mirrors.ustc.edu.cn/archlinuxcn/$arch


之后安装 archlinuxcn-keyring 包以导入 GPG key。

4 添加arch4edu源

在/etc/pacman.conf 文件末尾添加

    
    [arch4edu]
    SigLevel = Never
    Server = http://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch








5 安装常用软件()




      * guake
      * fish
      * vim
      * shadowsockq-qt5
      * google-chrome
      * wget,aria2
      * franz,telegram-desktop
      * remarkable (markdown编辑器，轻量级)






6.proxychains-ng


    
    dynamic_chain
    chain_len = 1 
    proxy_dns 
    remote_dns_subnet 224
    tcp_read_time_out 15000
    tcp_connect_time_out 8000
    [ProxyList]
    socks5     127.0.0.1 1080
    
    
    





就很气，配置文件经常失效，再记录一份好了


    
    quiet_mode
    dynamic_chain
    chain_len = 1 #round_robin_chain和random_chain使用
    proxy_dns
    remote_dns_subnet 224
    tcp_read_time_out 15000
    tcp_connect_time_out 8000
    localnet 127.0.0.0/255.0.0.0
    localnet 10.0.0.0/255.0.0.0
    localnet 172.16.0.0/255.240.0.0
    localnet 192.168.0.0/255.255.0.0
    
    [ProxyList]
    socks5  127.0.0.1 1080
    http    127.0.0.1 1087





7 vim 配置


    
    set guifont=Neep\ 18
     
    map <F9> :call SaveInputData()<CR>
    func! SaveInputData()
        exec "tabnew"
        exec 'normal "+gP'
        exec "w! code/in.txt"
    endfunc
     
     
     
    "colorscheme torte
    " colorscheme murphy
    colorscheme elflord
    " colorscheme molokai
    "colorscheme elisex
    "colorscheme colorer
    "colorscheme blacklight
    "colorscheme blue
    "colorscheme darkblue
    "colorscheme evening
    "colorscheme shine
     
    "colorscheme molokai
    "colorscheme solarized
    "colorscheme sift
    "colorscheme advantage
    "colorscheme 256_jungle
     
     
    "set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
    "set termencoding=utf-8
    "set encoding=utf-8
    "set fileencodings=ucs-bom,utf-8,cp936
    "set fileencoding=utf-8
     
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " 显示相关  
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "set shortmess=atI   " 启动的时候不显示那个援助乌干达儿童的提示  
    "winpos 5 5          " 设定窗口位置  
    "set lines=40 columns=155    " 设定窗口大小  
    set go=             " 不要图形按钮  
    "color asmanian2     " 设置背景主题  
    "set guifont=Courier_New:h10:cANSI   " 设置字体  
    syntax on           " 语法高亮  
    autocmd InsertLeave * se nocul  " 用浅色高亮当前行  
    autocmd InsertEnter * se cul    " 用浅色高亮当前行  
    "set ruler           " 显示标尺  
    set showcmd         " 输入的命令显示出来，看的清楚些  
    "set cmdheight=1     " 命令行（在状态行下）的高度，设置为1  
    "set whichwrap+=<,>,h,l   " 允许backspace和光标键跨越行边界(不建议)  
    "set scrolloff=3     " 光标移动到buffer的顶部和底部时保持3行距离  
    set novisualbell    " 不要闪烁(不明白)  
    set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}   "状态行显示的内容  
    set laststatus=1    " 启动显示状态行(1),总是显示状态行(2)  
    "set foldenable      " 允许折叠  
    set foldmethod=manual   " 手动折叠  
    "set background=dark "背景使用黑色 
    set nocompatible  "去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限  
    " 显示中文帮助
    if version >= 603
        set helplang=cn
        set encoding=utf-8
    endif
    " 设置配色方案
    "colorscheme murphy
    "字体 
    "if (has("gui_running")) 
    "   set guifont=Bitstream\ Vera\ Sans\ Mono\ 10 
    "endif 
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """""新文件标题
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "新建.c,.h,.sh,.java文件，自动插入文件头 
    autocmd BufNewFile *.cpp,*.[ch],*.sh,*.java exec ":call SetTitle()" 
    ""定义函数SetTitle，自动插入文件头
    "map <F4> :call SetTitle()<CR>
    func SetTitle() 
        "如果文件类型为.sh文件 
        if &filetype == 'sh' 
            call setline(1,"\#########################################################################") 
            call append(line("."), "\# File Name: ".expand("%")) 
            call append(line(".")+1, "\# Author: 111qqz") 
            call append(line(".")+2, "\# mail: renkuanze@sensetime.com") 
            call append(line(".")+3, "\# Created Time: ".strftime("%c")) 
            call append(line(".")+4, "\#########################################################################") 
            call append(line(".")+5, "\#!/bin/bash") 
            call append(line(".")+6, "") 
        else 
            let l = 0
            let l = l + 1 | call setline(l,'/* ***********************************************')
            let l = l + 1 | call setline(l,'Author :111qqz')
        let l = l + 1 | call setline(l,'mail: renkuanze@sensetime.com')
            let l = l + 1 | call setline(l,'Created Time :'.strftime('%c'))
            let l = l + 1 | call setline(l,'File Name :'.expand('%'))
            let l = l + 1 | call setline(l,'************************************************ */')
            let l = l + 1 | call setline(l,'')
        endif
        if &filetype == 'cpp' 
            let l = l + 1 | call setline(l,'#include <bits/stdc++.h>')
            let l = l + 1 | call setline(l,'')
            let l = l + 1 | call setline(l,'using namespace std;')
            let l = l + 1 | call setline(l,'int main()')
            let l = l + 1 | call setline(l,'{')
            let l = l + 1 | call setline(l,'    return 0;')
            let l = l + 1 | call setline(l,'}')
     
     
        endif
        if &filetype == 'c'
            call append(line(".")+6, "#include<stdio.h>")
            call append(line(".")+7, "")
        endif
        if &filetype == 'java'
            call append(line(".")+6,"public class ".expand("%"))
            call append(line(".")+7,"")
        endif
        "新建文件后，自动定位到文件末尾
        autocmd BufNewFile * normal G23
    endfunc
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    "键盘命令
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""v""""""""""""""""""""""""""""""""""""""""
     
    nmap <leader>w :w!<cr>
    nmap <leader>f :find<cr>
     
    nmap <F8> :TagbarToggle<CR>
     
     
    " 映射全选+复制 ctrl+a
    map <C-A> ggvG"+Y
    map! <C-A> <Esc>ggVGY
    map <F12> gg=G
    " 选中状态下 Ctrl+c 复制
    vmap <C-c> "+y
    "去空行  
    nnoremap <F2> :g/^\s*$/d<CR> 
    "比较文件  
    nnoremap <C-F2> :vert diffsplit 
    "新建标签  
    map <M-F2> :tabnew<CR>  
    "列出当前目录文件  
    map <F3> :tabnew .<CR>  
    "打开树状文件目录  
    map <C-F3> \be  
    "C，C++ 按F5编译运行
    map <F5> :call CompileRunGcc()<CR>
     
    au BufRead *.py map <buffer> <F6> :w<CR>:!/usr/bin/env python % <CR>
     
    let g:tagbar_usearrows = 1
    nnoremap <leader>l :TagbarToggle<CR>
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
        "   exec "!python %"
        "   exec "!python %<"
            exec "!python2.7 %"
        endif
    endfunc
    "C,C++的调试
    map <F8> :call Rungdb()<CR>
    func! Rungdb()
        exec "w"
        exec "!g++ % -std=c++11 -g  -o %<"
        exec "!gdb ./%<"
    endfunc
     
     
     
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    ""实用设置
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    " 设置当文件被改动时自动载入
    set autoread
    " quickfix模式
    autocmd FileType c,cpp map <buffer> <leader><space> :w<cr>:make<cr>
    "代码补全 
    set completeopt=preview,menu 
    "允许插件  
    filetype plugin on
    "共享剪贴板  
    set clipboard+=unnamed 
    "从不备份  
    set nobackup
    "make 运行
    :set makeprg=g++\ -Wall\ \ %
    "自动保存
    set autowrite
    set ruler                   " 打开状态栏标尺
    set cursorline              " 突出显示当前行
    set magic                   " 设置魔术
    set guioptions-=T           " 隐藏工具栏
    set guioptions-=m           " 隐藏菜单栏
    "set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %c:%l/%L%)\
    " 设置在状态行显示的信息
    set foldcolumn=0
    set foldmethod=indent 
    set foldlevel=3 
    set foldenable              " 开始折叠
    " 不要使用vi的键盘模式，而是vim自己的
    set nocompatible
    " 语法高亮
    set syntax=on
    " 去掉输入错误的提示声音
    set noeb
    " 在处理未保存或只读文件的时候，弹出确认
    set confirm
    " 自动缩进
    set autoindent
    set clipboard+=unnamed
    set cindent
    " Tab键的宽度
    set tabstop=8
    " 统一缩进为8
    set softtabstop=4
    set shiftwidth=4
    " 不要用空格代替制表符
    set noexpandtab
    " 在行和段开始处使用制表符
    set smarttab
    " 显示行号
    set number
    " 历史记录数
    set history=1000
    "禁止生成临时文件
    set nobackup
    set noswapfile
    "搜索忽略大小写
    set ignorecase
    "搜索逐字符高亮
    set hlsearch
    set incsearch
    "行内替换
    set gdefault
    "编码设置
    set enc=utf-8
    set fencs=utf-8,ucs-bom,shift-jis,gb18030,gbk,gb2312,cp936
    "语言设置
    set langmenu=zh_CN.UTF-8
    set helplang=cn
    " 我的状态行显示的内容（包括文件类型和解码）
    "set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}
    "set statusline=[%F]%y%r%m%*%=[Line:%l/%L,Column:%c][%p%%]
    " 总是显示状态行
    set laststatus=2
    " 命令行（在状态行下）的高度，默认为1，这里是2
    set cmdheight=2
    " 侦测文件类型
    filetype on
    " 载入文件类型插件
    filetype plugin on
    " 为特定文件类型载入相关缩进文件
    filetype indent on
    " 保存全局变量
    set viminfo+=!
    " 带有如下符号的单词不要被换行分割
    set iskeyword+=_,$,@,%,#,-
    " 字符间插入的像素行数目
    set linespace=0
    " 增强模式中的命令行自动完成操作
    set wildmenu
    " 使回格键（backspace）正常处理indent, eol, start等
    set backspace=2
    " 允许backspace和光标键跨越行边界
    set whichwrap+=<,>,h,l
    " 可以在buffer的任何地方使用鼠标（类似office中在工作区双击鼠标定位）
    set mouse=a
    set selection=exclusive
    set selectmode=mouse,key
    " 通过使用: commands命令，告诉我们文件的哪一行被改变过
    set report=0
    " 在被分割的窗口间显示空白，便于阅读
    set fillchars=vert:\ ,stl:\ ,stlnc:\
    " 高亮显示匹配的括号
    set showmatch
    " 匹配括号高亮的时间（单位是十分之一秒）
    set matchtime=1
    " 光标移动到buffer的顶部和底部时保持3行距离
    set scrolloff=3
    " 为C程序提供自动缩进
    set smartindent
    " 高亮显示普通txt文件（需要txt.vim脚本）
    set cursorline
    hi CursorLine  cterm=bold   ctermbg=blue ctermfg=yellow
    au BufRead,BufNewFile *  setfiletype txt
    "自动补全
    ":inoremap ( ()<ESC>i
    ":inoremap ) <c-r>=ClosePair(')')<CR>
    ":inoremap { {<CR>}<ESC>O
    ":inoremap } <c-r>=ClosePair('}')<CR>
    ":inoremap [ []<ESC>i
    ":inoremap ] <c-r>=ClosePair(']')<CR>
    ":inoremap " ""<ESC>i
    ":inoremap ' ''<ESC>i
    function! ClosePair(char)
        if getline('.')[col('.') - 1] == a:char
            return "\<Right>"
        else
            return a:char
        endif
    endfunction
    filetype plugin indent on 
    "打开文件类型检测, 加了这句才可以用智能补全
    set completeopt=longest,menu
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
     
     
     
     
     
     
     
    """""""""""""""""vundle设置"""""""""""""""""
    set nocompatible              " be iMproved, required
    "filetype off                  " required
    set shell=/bin/bash 
     
     
    " Interface
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    Plugin 'VundleVim/Vundle.vim'
    " vim-scripts repos
    "
    "
     
      Plugin 'MarcWeber/vim-addon-mw-utils'
      Plugin 'tomtom/tlib_vim'
      Plugin 'garbas/vim-snipmate'
     
      " Optional:
     Plugin 'honza/vim-snippets'
     Plugin 'davidhalter/jedi-vim'
     Plugin 'vim-airline/vim-airline'
     Plugin 'vim-airline/vim-airline-themes'
     Plugin 'bash-support.vim'
     Plugin 'perl-support.vim'
     Plugin 'majutsushi/tagbar'
     Plugin 'ZoomWin'
     Plugin 'morhetz/gruvbox' 
     Plugin 'scrooloose/syntastic'
    Plugin 'Valloric/YouCompleteMe'
    call vundle#end()            " required
    filetype plugin indent on    " required
     
     
     
     
    """""""""""""""""youcompleteme设置"""""""""""""""""
     
     
    "let g:ycm_autoclose_preview_window_after_completion=1
    "nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>
     
    " YouCompleteMe 功能
    " 补全功能在注释中同样有效
    "let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/cpp/ycm/.ycm_extra_conf.py'
    "let g:ycm_complete_in_comments=1
     "允许 vim 加载 .ycm_extra_conf.py 文件，不再提示
    "let g:ycm_confirm_extra_conf=0
     
    "let g:ycm_error_symbol = '<<'
    "let g:ycm_warning_symbol = '<'
    "nnoremap <leader>gl :YcmCompleter GoToDeclaration<CR>
    "nnoremap <leader>gf :YcmCompleter GoToDefinition<CR>
    "nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration<CR>
    "nmap <F4> :YcmDiags<CR>
     
     
     
     
    """""""""""""""""youcompleteme设置 by wyz"""""""""""""""""
    let g:cpp_class_scope_highlight=1
    let g:cpp_experimental_template_highlight=1
    let g:ycm_show_diagnostics_ui=0
    let g:ycm_enable_diagnostic_signs=0
    let g:ycm_enable_diagnostic_highlighting = 0
    let g:ycm_echo_current_diagnostic = 0
    let g:ycm_collect_identifiers_from_tags_files = 1
    let g:ycm_key_invoke_completion = '<C-Q>'
    let g:ycm_seed_identifiers_with_syntax = 1
    let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
    let g:ycm_collect_identifiers_from_tags_files = 1
    let g:ycm_confirm_extra_conf = 0
    let g:ycm_autoclose_preview_window_after_completion = 1
    let g:ycm_autoclose_preview_window_after_insertion = 1
     
     
     
    " for python
    "
    "
     
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
     
     
     
    """"""""""""""'for airline""""""""""""""""
     
    let g:airline_powerline_fonts = 1   
    let g:airline#extensions#tabline#enabled = 1
     let g:airline#extensions#tabline#buffer_nr_show = 1
    let g:airline#extensions#tabline#left_sep = ' '
    let g:airline#extensions#tabline#left_alt_sep = '|'
     
     nnoremap <F2> :bnext<CR>
     nnoremap <F4> :bprevious<CR>
     
     if !exists('g:airline_symbols')
        let g:airline_symbols = {}
        endif
     
     let g:airline_left_sep = '⮀'
      let g:airline_left_alt_sep = '⮁'
      let g:airline_right_sep = '⮂'
      let g:airline_right_alt_sep = '⮃'
      let g:airline_symbols.branch = '⭠'
      let g:airline_symbols.readonly = '⭤'
     
     
     
     
     
     
     
    





8修改键盘映射


    
    keysym XF86Back = Page_Up
    keysym XF86Forward = Page_Down



9安装中文字体：


    
    sudo pacman -S wqy-microhei wqy-microhei-lite wqy-bitmapfont wqy-zenhei ttf-arphic-ukai ttf-arphic-uming adobe-source-han-sans-cn-fonts








  1. anaconda with fish


anaconda 默认的环境变量是bash,对于fish,需要修改~/.config/fish/config.fish 如下


    
    #export LD_LIBRARY_PATH=/usr/local/cuda/lib64/
    set -x LD_LIBRARY_PATH /usr/local/cuda/lib64/
    
    # added by Anaconda2 4.4.0 installer
    #export PATH="/home/sensetime/anaconda2/bin:$PATH"
    set -x PATH /home/sensetime/anaconda2/bin $PATH





11 youcompleteme


    
    # This file is NOT licensed under the GPLv3, which is the license for the rest
    # of YouCompleteMe.
    #
    # Here's the license text for this file:
    #
    # This is free and unencumbered software released into the public domain.
    #
    # Anyone is free to copy, modify, publish, use, compile, sell, or
    # distribute this software, either in source code form or as a compiled
    # binary, for any purpose, commercial or non-commercial, and by any
    # means.
    #
    # In jurisdictions that recognize copyright laws, the author or authors
    # of this software dedicate any and all copyright interest in the
    # software to the public domain. We make this dedication for the benefit
    # of the public at large and to the detriment of our heirs and
    # successors. We intend this dedication to be an overt act of
    # relinquishment in perpetuity of all present and future rights to this
    # software under copyright law.
    #
    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    # EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    # MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    # IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
    # OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
    # ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
    # OTHER DEALINGS IN THE SOFTWARE.
    #
    # For more information, please refer to <http://unlicense.org/>
    
    import os
    import ycm_core
    
    # These are the compilation flags that will be used in case there's no
    # compilation database set (by default, one is not set).
    # CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
    flags = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wnoc++98-compat',
    '-Wno-long-long',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    #'-stdlib=libc++',
    # You 100% do NOT need -DUSE_CLANG_COMPLETER in your flags; only the YCM
    # source code needs it.
    '-DUSE_CLANG_COMPLETER',
    # THIS IS IMPORTANT! Without a "-std=<something>" flag, clang won't know which
    # language to use when compiling headers. So it will guess. Badly. So C++
    # headers will be compiled as C headers. You don't want that so ALWAYS specify
    # a "-std=<something>".
    # For a C project, you would set this to something like 'c99' instead of
    # 'c++11'.
    '-std=c++11',
    # ...and the same thing goes for the magic -x option which specifies the
    # language that the files to be compiled are written in. This is mostly
    # relevant for c++ headers.
    # For a C project, you would set this to 'c' instead of 'c++'.
    '-x',
    'c++',
    '-isystem',
    '../BoostParts',
    '-isystem',
    # This path will only work on OS X, but extra paths that don't exist are not
    # harmful
    '/System/Library/Frameworks/Python.framework/Headers',
    '-isystem',
    '../llvm/include',
    '-isystem',
    '../llvm/tools/clang/include',
    '-I',
    '.',
    '-I',
    './ClangCompleter',
    '-isystem',
    './tests/gmock/gtest',
    '-isystem',
    './tests/gmock/gtest/include',
    '-isystem',
    './tests/gmock',
    '-isystem',
    './tests/gmock/include',
    #'-isystem',
    #'/usr/local/include/c++/5.1.0',
    #'-isystem',
    #'/usr/local/include',
    #'-isystem',
    #'/usr/include',
    ]
    
    
    # Set this to the absolute path to the folder (NOT the file!) containing the
    # compile_commands.json file to use that instead of 'flags'. See here for
    # more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
    #
    # You can get CMake to generate this file for you by adding:
    #   set( CMAKE_EXPORT_COMPILE_COMMANDS 1 )
    # to your CMakeLists.txt file.
    #
    # Most projects will NOT need to set this to anything; you can just change the
    # 'flags' list of compilation flags. Notice that YCM itself uses that approach.
    compilation_database_folder = ''
    
    if os.path.exists( compilation_database_folder ):
      database = ycm_core.CompilationDatabase( compilation_database_folder )
    else:
      database = None
    
    SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]
    
    def DirectoryOfThisScript():
      return os.path.dirname( os.path.abspath( __file__ ) )
    
    
    def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
      if not working_directory:
        return list( flags )
      new_flags = []
      make_next_absolute = False
      path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
      for flag in flags:
        new_flag = flag
    
        if make_next_absolute:
          make_next_absolute = False
          if not flag.startswith( '/' ):
            new_flag = os.path.join( working_directory, flag )
    
        for path_flag in path_flags:
          if flag == path_flag:
            make_next_absolute = True
            break
    
          if flag.startswith( path_flag ):
            path = flag[ len( path_flag ): ]
            new_flag = path_flag + os.path.join( working_directory, path )
            break
    
        if new_flag:
          new_flags.append( new_flag )
      return new_flags
    
    
    def IsHeaderFile( filename ):
      extension = os.path.splitext( filename )[ 1 ]
      return extension in [ '.h', '.hxx', '.hpp', '.hh' ]
    
    
    def GetCompilationInfoForFile( filename ):
      # The compilation_commands.json file generated by CMake does not have entries
      # for header files. So we do our best by asking the db for flags for a
      # corresponding source file, if any. If one exists, the flags for that file
      # should be good enough.
      if IsHeaderFile( filename ):
        basename = os.path.splitext( filename )[ 0 ]
        for extension in SOURCE_EXTENSIONS:
          replacement_file = basename + extension
          if os.path.exists( replacement_file ):
            compilation_info = database.GetCompilationInfoForFile(
              replacement_file )
            if compilation_info.compiler_flags_:
              return compilation_info
        return None
      return database.GetCompilationInfoForFile( filename )
    
    
    def FlagsForFile( filename, **kwargs ):
      if database:
        # Bear in mind that compilation_info.compiler_flags_ does NOT return a
        # python list, but a "list-like" StringVec object
        compilation_info = GetCompilationInfoForFile( filename )
        if not compilation_info:
          return None
    
        final_flags = MakeRelativePathsInFlagsAbsolute(
          compilation_info.compiler_flags_,
          compilation_info.compiler_working_dir_ )
    
        # NOTE: This is just for YouCompleteMe; it's highly likely that your project
        # does NOT need to remove the stdlib flag. DO NOT USE THIS IN YOUR
        # ycm_extra_conf IF YOU'RE NOT 100% SURE YOU NEED IT.
        try:
          final_flags.remove( '-stdlib=libc++' )
          pass
        except ValueError:
          pass
      else:
        relative_to = DirectoryOfThisScript()
        final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )
    
      return {
        'flags': final_flags,
        'do_cache': True
      }





12.关于vim 剪贴板的问题

[How do I use the system clipboard with Vim in Arch Linux?](https://vi.stackexchange.com/questions/3076/how-do-i-use-the-system-clipboard-with-vim-in-arch-linux)

uninstall vim,install gvim,and use vim instead of gvim



13 vim 配色文件molokai.vim(透明背景修改


    
    " Vim color file
    "
    " Author: Tomas Restrepo <tomas@winterdom.com>
    " https://github.com/tomasr/molokai
    "
    " Note: Based on the Monokai theme for TextMate
    " by Wimer Hazenberg and its darker variant
    " by Hamish Stuart Macpherson
    "
    
    hi clear
    
    if version > 580
        " no guarantees for version 5.8 and below, but this makes it stop
        " complaining
        hi clear
        if exists("syntax_on")
            syntax reset
        endif
    endif
    let g:colors_name="molokai"
    
    if exists("g:molokai_original")
        let s:molokai_original = g:molokai_original
    else
        let s:molokai_original = 0
    endif
    
    
    hi Boolean         guifg=#AE81FF
    hi Character       guifg=#E6DB74
    hi Number          guifg=#AE81FF
    hi String          guifg=#E6DB74
    hi Conditional     guifg=#F92672               gui=bold
    hi Constant        guifg=#AE81FF               gui=bold
    hi Cursor          guifg=#000000 guibg=#F8F8F0
    hi iCursor         guifg=#000000 guibg=#F8F8F0
    hi Debug           guifg=#BCA3A3               gui=bold
    hi Define          guifg=#66D9EF
    hi Delimiter       guifg=#8F8F8F
    hi DiffAdd                       guibg=#13354A
    hi DiffChange      guifg=#89807D guibg=#4C4745
    hi DiffDelete      guifg=#960050 guibg=#1E0010
    hi DiffText                      guibg=#4C4745 gui=italic,bold
    
    hi Directory       guifg=#A6E22E               gui=bold
    hi Error           guifg=#E6DB74 guibg=#1E0010
    hi ErrorMsg        guifg=#F92672 guibg=#232526 gui=bold
    hi Exception       guifg=#A6E22E               gui=bold
    hi Float           guifg=#AE81FF
    hi FoldColumn      guifg=#465457 guibg=#000000
    hi Folded          guifg=#465457 guibg=#000000
    hi Function        guifg=#A6E22E
    hi Identifier      guifg=#FD971F
    hi Ignore          guifg=#808080 guibg=bg
    hi IncSearch       guifg=#C4BE89 guibg=#000000
    
    hi Keyword         guifg=#F92672               gui=bold
    hi Label           guifg=#E6DB74               gui=none
    hi Macro           guifg=#C4BE89               gui=italic
    hi SpecialKey      guifg=#66D9EF               gui=italic
    
    hi MatchParen      guifg=#000000 guibg=#FD971F gui=bold
    hi ModeMsg         guifg=#E6DB74
    hi MoreMsg         guifg=#E6DB74
    hi Operator        guifg=#F92672
    
    " complete menu
    hi Pmenu           guifg=#66D9EF guibg=#000000
    hi PmenuSel                      guibg=#808080
    hi PmenuSbar                     guibg=#080808
    hi PmenuThumb      guifg=#66D9EF
    
    hi PreCondit       guifg=#A6E22E               gui=bold
    hi PreProc         guifg=#A6E22E
    hi Question        guifg=#66D9EF
    hi Repeat          guifg=#F92672               gui=bold
    hi Search          guifg=#000000 guibg=#FFE792
    " marks
    hi SignColumn      guifg=#A6E22E guibg=#232526
    hi SpecialChar     guifg=#F92672               gui=bold
    hi SpecialComment  guifg=#7E8E91               gui=bold
    hi Special         guifg=#66D9EF guibg=bg      gui=italic
    if has("spell")
        hi SpellBad    guisp=#FF0000 gui=undercurl
        hi SpellCap    guisp=#7070F0 gui=undercurl
        hi SpellLocal  guisp=#70F0F0 gui=undercurl
        hi SpellRare   guisp=#FFFFFF gui=undercurl
    endif
    hi Statement       guifg=#F92672               gui=bold
    hi StatusLine      guifg=#455354 guibg=fg
    hi StatusLineNC    guifg=#808080 guibg=#080808
    hi StorageClass    guifg=#FD971F               gui=italic
    hi Structure       guifg=#66D9EF
    hi Tag             guifg=#F92672               gui=italic
    hi Title           guifg=#ef5939
    hi Todo            guifg=#FFFFFF guibg=bg      gui=bold
    
    hi Typedef         guifg=#66D9EF
    hi Type            guifg=#66D9EF               gui=none
    hi Underlined      guifg=#808080               gui=underline
    
    hi VertSplit       guifg=#808080 guibg=#080808 gui=bold
    hi VisualNOS                     guibg=#403D3D
    hi Visual                        guibg=#403D3D
    hi WarningMsg      guifg=#FFFFFF guibg=#333333 gui=bold
    hi WildMenu        guifg=#66D9EF guibg=#000000
    
    hi TabLineFill     guifg=#1B1D1E guibg=#1B1D1E
    hi TabLine         guibg=#1B1D1E guifg=#808080 gui=none
    
    if s:molokai_original == 1
       hi Normal          guifg=#F8F8F2 guibg=NONE
       hi Comment         guifg=#75715E
       hi CursorLine                    guibg=#3E3D32
       hi CursorLineNr    guifg=#FD971F               gui=none
       hi CursorColumn                  guibg=#3E3D32
       hi ColorColumn                   guibg=#3B3A32
       hi LineNr          guifg=#BCBCBC guibg=#3B3A32
       hi NonText         guifg=#75715E
       hi SpecialKey      guifg=#75715E
    else
       hi Normal          guifg=#F8F8F2 guibg=NONE 
       hi Comment         guifg=#7E8E91
       hi CursorLine                    guibg=#293739
       hi CursorLineNr    guifg=#FD971F               gui=none
       hi CursorColumn                  guibg=#293739
       hi ColorColumn                   guibg=#232526
       hi LineNr          guifg=#465457 guibg=#232526
       hi NonText         guifg=#465457
       hi SpecialKey      guifg=#465457
    end
    
    "
    " Support for 256-color terminal
    "
    if &t_Co > 255
       if s:molokai_original == 1
          hi Normal                   ctermbg=NONE 
          hi CursorLine               ctermbg=235   cterm=none
          hi CursorLineNr ctermfg=208               cterm=none
       else
          hi Normal       ctermfg=252 ctermbg=NONE
          hi CursorLine               ctermbg=234   cterm=none
          hi CursorLineNr ctermfg=208               cterm=none
       endif
       hi Boolean         ctermfg=135
       hi Character       ctermfg=144
       hi Number          ctermfg=135
       hi String          ctermfg=144
       hi Conditional     ctermfg=161               cterm=bold
       hi Constant        ctermfg=135               cterm=bold
       hi Cursor          ctermfg=16  ctermbg=253
       hi Debug           ctermfg=225               cterm=bold
       hi Define          ctermfg=81
       hi Delimiter       ctermfg=241
    
       hi DiffAdd                     ctermbg=24
       hi DiffChange      ctermfg=181 ctermbg=239
       hi DiffDelete      ctermfg=162 ctermbg=53
       hi DiffText                    ctermbg=102 cterm=bold
    
       hi Directory       ctermfg=118               cterm=bold
       hi Error           ctermfg=219 ctermbg=89
       hi ErrorMsg        ctermfg=199 ctermbg=16    cterm=bold
       hi Exception       ctermfg=118               cterm=bold
       hi Float           ctermfg=135
       hi FoldColumn      ctermfg=67  ctermbg=16
       hi Folded          ctermfg=67  ctermbg=16
       hi Function        ctermfg=118
       hi Identifier      ctermfg=208               cterm=none
       hi Ignore          ctermfg=244 ctermbg=232
       hi IncSearch       ctermfg=193 ctermbg=16
    
       hi keyword         ctermfg=161               cterm=bold
       hi Label           ctermfg=229               cterm=none
       hi Macro           ctermfg=193
       hi SpecialKey      ctermfg=81
    
       hi MatchParen      ctermfg=233  ctermbg=208 cterm=bold
       hi ModeMsg         ctermfg=229
       hi MoreMsg         ctermfg=229
       hi Operator        ctermfg=161
    
       " complete menu
       hi Pmenu           ctermfg=81  ctermbg=16
       hi PmenuSel        ctermfg=255 ctermbg=242
       hi PmenuSbar                   ctermbg=232
       hi PmenuThumb      ctermfg=81
    
       hi PreCondit       ctermfg=118               cterm=bold
       hi PreProc         ctermfg=118
       hi Question        ctermfg=81
       hi Repeat          ctermfg=161               cterm=bold
       hi Search          ctermfg=0   ctermbg=222   cterm=NONE
    
       " marks column
       hi SignColumn      ctermfg=118 ctermbg=235
       hi SpecialChar     ctermfg=161               cterm=bold
       hi SpecialComment  ctermfg=245               cterm=bold
       hi Special         ctermfg=81
       if has("spell")
           hi SpellBad                ctermbg=52
           hi SpellCap                ctermbg=17
           hi SpellLocal              ctermbg=17
           hi SpellRare  ctermfg=none ctermbg=none  cterm=reverse
       endif
       hi Statement       ctermfg=161               cterm=bold
       hi StatusLine      ctermfg=238 ctermbg=253
       hi StatusLineNC    ctermfg=244 ctermbg=232
       hi StorageClass    ctermfg=208
       hi Structure       ctermfg=81
       hi Tag             ctermfg=161
       hi Title           ctermfg=166
       hi Todo            ctermfg=231 ctermbg=232   cterm=bold
    
       hi Typedef         ctermfg=81
       hi Type            ctermfg=81                cterm=none
       hi Underlined      ctermfg=244               cterm=underline
    
       hi VertSplit       ctermfg=244 ctermbg=232   cterm=bold
       hi VisualNOS                   ctermbg=238
       hi Visual                      ctermbg=235
       hi WarningMsg      ctermfg=231 ctermbg=238   cterm=bold
       hi WildMenu        ctermfg=81  ctermbg=16
    
       hi Comment         ctermfg=59
       hi CursorColumn                ctermbg=236
       hi ColorColumn                 ctermbg=236
       hi LineNr          ctermfg=250 ctermbg=236
       hi NonText         ctermfg=59
    
       hi SpecialKey      ctermfg=59
    
       if exists("g:rehash256") && g:rehash256 == 1
           hi Normal       ctermfg=252 ctermbg=NONE 
           hi CursorLine               ctermbg=236   cterm=none
           hi CursorLineNr ctermfg=208               cterm=none
    
           hi Boolean         ctermfg=141
           hi Character       ctermfg=222
           hi Number          ctermfg=141
           hi String          ctermfg=222
           hi Conditional     ctermfg=197               cterm=bold
           hi Constant        ctermfg=141               cterm=bold
    
           hi DiffDelete      ctermfg=125 ctermbg=233
    
           hi Directory       ctermfg=154               cterm=bold
           hi Error           ctermfg=222 ctermbg=233
           hi Exception       ctermfg=154               cterm=bold
           hi Float           ctermfg=141
           hi Function        ctermfg=154
           hi Identifier      ctermfg=208
    
           hi Keyword         ctermfg=197               cterm=bold
           hi Operator        ctermfg=197
           hi PreCondit       ctermfg=154               cterm=bold
           hi PreProc         ctermfg=154
           hi Repeat          ctermfg=197               cterm=bold
    
           hi Statement       ctermfg=197               cterm=bold
           hi Tag             ctermfg=197
           hi Title           ctermfg=203
           hi Visual                      ctermbg=238
    
           hi Comment         ctermfg=244
           hi LineNr          ctermfg=239 ctermbg=235
           hi NonText         ctermfg=239
           hi SpecialKey      ctermfg=239
       endif
    end
    
    " Must be at the end, because of ctermbg=234 bug.
    " https://groups.google.com/forum/#!msg/vim_dev/afPqwAFNdrU/nqh6tOM87QUJ
    set background=dark
    






