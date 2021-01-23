---
author: 111qqz
date: 2019-02-01 11:19:29+00:00
draft: false
title: C语言变长参数
type: post
url: /2019/02/variadic-function-of-c/
categories:
- c++
tags:
- variadic function
---

说起C语言的变长参数，可能听起来比较陌生，因为很少会需要自己实现。不过想一下scanf和printf，参数个数的确是不固定的。

[stdarg.h](https://en.wikipedia.org/wiki/Stdarg.h#.3Cvarargs.h.3E) 中提供以一套机制来实现变长参数。以及，要说明的是，变长参数不是什么黑魔法，原理依赖于stack frame的结构，具体可以参考[x86-calling-conventions](https://111qqz.com/2019/01/x86-calling-conventions/)   简单来说，由于函数参数入栈的顺序是固定的，**因此一旦我们知道某函数帧的栈上的一个固定参数的位置，我们完全有可能推导出其他变长参数的位置 **

在实现上，需要了解的是：



 	  * va_list，一个类型，可以看做是变长参数列表；
 	  * [va_start](http://en.cppreference.com/w/cpp/utility/variadic/va_start)，用来初始化变长参数列表的宏，声明为void va_start( va_list ap, parm_n );  ap为va_list变量，parm_n为变长参数前一个变量（C语言要求至少有一个named variable作为函数的parameter)
 	  * [va_arg](http://en.cppreference.com/w/cpp/utility/variadic/va_arg),用来得到下一个参数的宏，声明为T va_arg( va_list ap, T ); **返回的类型取决于传入的类型T。特别注意:"If `va_arg` is called when there are no more arguments in `ap`, the behavior is undefined."**
 	  * [va_end](http://en.cppreference.com/w/cpp/utility/variadic/va_end) ,用来将va_list释放的宏。

下面看一个例子就明白怎么用了orz

    
    #include <stdio.h>
    #include <stdarg.h>
    
    /* print all args one at a time until a negative argument is seen;
       all args are assumed to be of int type */
    void printargs(int arg1, ...)
    {
      va_list ap;
      int i;
    
      va_start(ap, arg1); 
      for (i = arg1; i >= 0; i = va_arg(ap, int))
        printf("%d ", i);
      va_end(ap);
      putchar('\n');
    }
    
    int main(void)
    {
       printargs(5, 2, 14, 84, 97, 15, -1, 48, -1);
       printargs(84, 51, -1);
       printargs(-1);
       printargs(1, -1);
       return 0;
    }
    
    
    output:
    5 2 14 84 97 15
    84 51
    
    1


如果想研究c语言中变长参数的具体实现，可以参考 [也谈C语言变长参数](https://tonybai.com/2008/05/07/also-talk-about-c-variable-length-args/)

参考资料:

[Variable numbers of arguments](https://publications.gbdirect.co.uk//c_book/chapter9/stdarg.html)






