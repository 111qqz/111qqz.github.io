---
author: 111qqz
date: 2019-01-31 12:12:22+00:00
draft: false
title: x86 calling conventions
type: post
url: /2019/01/x86-calling-conventions/
categories:
- 公开课
tags:
- call stack
- gcc
---

x86的调用约定主要说的是这几件事:


<blockquote>

> 
> 
 	  * The order in which atomic (scalar) parameters, or individual parts of a complex parameter, are allocated
 	  * How parameters are passed (pushed on the stack, placed in registers, or a mix of both)
 	  * Which registers the called function must preserve for the caller (also known as: callee-saved registers or non-volatile registers)
 	  * How the task of preparing the stack for, and restoring after, a function call is divided between the caller and the callee

</blockquote>


调用约定实际上并不唯一

我们比较关注gcc编译器下的cdecl(**C declaration**)

对于如下这段代码:

    
    int callee(int, int, int);
    
    int caller(void)
    {
    	return callee(1, 2, 3) + 5;
    }


调用过程如下:

    
    caller:
    	; make new call frame
    	; (some compilers may produce an 'enter' instruction instead)
    	push    ebp       ; save old call frame
    	mov     ebp, esp  ; initialize new call frame
    	; push call arguments, in reverse
    	; (some compilers may subtract the required space from the stack pointer,
    	; then write each argument directly, see below.
    	; The 'enter' instruction can also do something similar)
    	; sub esp, 12      : 'enter' instruction could do this for us
    	; mov [ebp-4], 3   : or mov [esp+8], 3
    	; mov [ebp-8], 2   : or mov [esp+4], 2
    	; mov [ebp-12], 1  : or mov [esp], 1
    	push    3
    	push    2
    	push    1
    	call    callee    ; call subroutine 'callee'
    	add     eax, 5    ; modify subroutine result
    	                  ; (eax is the return value of our callee,
    	                  ; so we don't have to move it into a local variable)
    	; restore old call frame
    	; (some compilers may produce a 'leave' instruction instead)
    	; add   esp, 12   ; remove arguments from frame, ebp - esp = 12.
    	                  ; compilers will usually produce the following instead,
    	                  ; which is just as fast, and, unlike the add instruction,
    	                  ; also works for variable length arguments
    	                  ; and variable length arrays allocated on the stack.
    	mov     esp, ebp  ; most calling conventions dictate ebp be callee-saved,
    	                  ; i.e. it's preserved after calling the callee.
    	                  ; it therefore still points to the start of our stack frame.
    	                  ; we do need to make sure
    	                  ; callee doesn't modify (or restores) ebp, though,
    	                  ; so we need to make sure
    	                  ; it uses a calling convention which does this
    	pop     ebp       ; restore old call frame
    	ret               ; return


**在c语言中，函数的参数被以从右向左的顺序压入栈，也就是最后一个参数最先入栈。**

这里是栈指的是调用栈([Call_stack](https://en.wikipedia.org/wiki/Call_stack))

调用栈的结构如下(**注意此图的栈是从下往上增长的，这与通常情况并不相符**，不过不影响此处的说明)，这是在调用的DrawSquare函数中调用DrawLine函数时的情景

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Call_stack_layout.svg/342px-Call_stack_layout.svg.png)


stack frame通常按照入栈顺序(写在前面的先入栈)由三部分组成（可能某部分为空):



 	  * 函数的参数值（以从右向左的顺序入栈)
 	  * caller的地址值，为的是调用函数之后能继续执行caller其余的代码。
 	  * 函数的局部变量



接下来我们看一下调用过程对寄存器的影响。这里暂且不提eax寄存器通常用来保存结果之类，主要想谈谈调用过程对sp和bp两个寄存器的影响。

sp是stack pointer，保存的是当前栈顶地址

bp是base pointer(就是stack frame中的frame pointer), 值为函数刚刚被调用时的栈顶位置。

bp这个寄存器的作用主要是比较方便，因为如果只有stack pointer，那么在函数里面，stack pointer也是可能变的，显然不如使用base pointer方便。

**具体来说，在使用base pointer的情况下，函数的返回地址永远为ebp + 4，第一个参数的地址为ebp+8,第一个局部变量的地址为ebp-4**

而且使用bp的情况下，回溯调用栈会变得非常方便。


<blockquote>**At ebp is a pointer to ebp for the previous frame** (**this is why push ebp; mov ebp, esp** is such a common way to start a function).  This effectively creates a linked list of base pointers.  This linked list makes it very easy to trace backwards up the stack.  For example if foo() calls bar() and bar() calls baz() and you’re debugging baz() you can easily find the parameters and local variables for foo() and bar().</blockquote>


为什么ebp指向的内容是上一个 stack frame中的ebp？我们看push ebp; mov ebp esp这两条指令。push ebp相当于先esp-=4,然后将ebp放到esp所指向的位置。接着mov ebp esp,相当于把当前的esp，也就是上一个ebp所在的位置，赋值给新的ebp.  所以。。**这其实是个链表啊**！





参考资料:

[x86 calling conventions](https://en.wikipedia.org/wiki/X86_calling_conventions#x86-64_calling_conventions)

[Stack_register](https://en.wikipedia.org/wiki/Stack_register)

[Call_stack#STACK-FRAME](https://en.wikipedia.org/wiki/Call_stack#STACK-FRAME)

[What is exactly the base pointer and stack pointer? To what do they point?](https://stackoverflow.com/questions/1395591/what-is-exactly-the-base-pointer-and-stack-pointer-to-what-do-they-point)

[All About EBP](https://practicalmalwareanalysis.com/2012/04/03/all-about-ebp/)












