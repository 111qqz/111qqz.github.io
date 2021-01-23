---
author: 111qqz
date: 2017-12-05 02:44:46+00:00
draft: false
title: unicode 汉字表示不唯一的问题 (cjk字符集)
type: post
url: /2017/12/unicode-char-not-unique/
categories:
- 其他
tags:
- NLP
- unicode
---

update:

遇到的汉字：

丹：63838

李：63969

昨天写的正则发现死活识别不了 "年"字...

放到[unicode编码转化公式](http://tool.chinaz.com/tools/unicode.aspx) 查了下发现竟然是不同的字orz..

其实猜想到也许是日文的"年"...结果查询了下发现是韩文的锅?

具体参考[为何Unicode中有字形完全相同的CJK字符？](https://www.zhihu.com/question/21939341)

以及兼容汉字的参考表:[UF900](https://111qqz.com/wordpress/wp-content/uploads/2017/12/UF900.pdf)

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/12/cjk兼容字符部分.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/12/cjk兼容字符部分.png)
