---
author: 111qqz
date: 2018-10-20 11:06:56+00:00
draft: false
title: golang 学习笔记
type: post
url: /2018/10/golang-notes/
categories:
- 其他
tags:
- golang
- 系统调用
---

先放资料,可能比较侧重于go在系统调用方面的内容.

这里不会记录详细的go的语法,只会记录学习的过程,踩到的坑,以及其他我认为值得记录的内容.

go的switch语句终于是人类思维的语句了...匹配中了不需要加break..

defer关键字可以延迟语句到上层函数退出时再执行,而且是会把延迟的语句压入栈,然后按照FILO的顺序执行...好像有点有意思?

参数列表..如果有多个变量的类型相同,只写一个类型关键字就行...

:=并不是pascal中的赋值符号(浪费感情...,而是简洁定义变量的语法,不能使用在函数以外.

感觉go中同时有一点C++和很多python的影子...







[30分钟上手GO语言--基础语法](https://studygolang.com/topics/548)

[A Go Programmer’s Guide to Syscalls](https://about.sourcegraph.com/go/a-go-guide-to-syscalls/)

[视频笔记：Go 和 syscall - Liz Rice](https://blog.lab99.org/post/golang-2017-10-05-video-guide-to-syscall.html)




