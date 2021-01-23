---
author: 111qqz
date: 2017-10-21 12:54:40+00:00
draft: false
title: vimrc for ACM-ICPC (赛场用)
type: post
url: /2017/10/vimrc-for-acm-icpc/
categories:
- ACM
---

弄了点比较短的，赛场上用的配置文件orz


    
    map <F5> :call Co()<CR>
    func! Co()
        exec "w"
        exec "!g++ % -std=gnu++11 -Wall -o %<"
        exec "! ./%<"
    
    endfunc
    syntax on
    set nu
    
    autocmd BufNewFile *.cpp  exec ":call SetTitle()"
    func SetTitle()
        let l = 0
        let l = l + 1 | call setline(l,'#include <bits/stdc++.h>')
        let l = l + 1 | call setline(l,'using namespace std;')
        let l = l + 1 | call setline(l,'const int inf = 0x3f3f3f3f;')
        let l = l + 1 | call setline(l,'#define ms(a,x) memset(a,x,sizeof(a))')
        let l = l + 1 | call setline(l,'typedef long long LL;')
        let l = l + 1 | call setline(l,'int main()')
        let l = l + 1 | call setline(l,'{')
        let l = l + 1 | call setline(l,'    return 0;')
        let l = l + 1 | call setline(l,'}')
    endfunc



故地重游，rp++


