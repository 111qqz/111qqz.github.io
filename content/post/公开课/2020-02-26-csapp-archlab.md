---
title: "【施工完成】CSAPP archlab"
date: 2020-02-26T22:54:33+08:00
draft: false
author: "111qqz"
type: post
url: /2020/02/csapp-archlab/
categories:
- mooc

tags:

- CSAPP

---


## 背景
CSAPP:3e第四章配套的实验。 第四章是讲处理器架构的，章节的重点是实现一个六阶段流水线。

lab的内容也是，需要实现一个Y86-64的流水线，并进行性能调优。


## 准备工作

材料里面sim.tar解压之后，有可能是没办法编译通过的。
原因是tk（a windowing toolkit ）在8.5版本的时候废弃了某个接口，与8.6版本不兼容。

因此需要安装tk 8.5或者更低的版本。 在archlinux/manjaro下可以通过aur安装tk85.


### use tk<=8.5,8.6 or above will not compile

### Modify the corresponding header file in seq/ssim.c and pipe/psim.c (assmue tk8.5 header file is located in /usr/local/tk8.5)

```c++

#ifdef HAS_GUI
#include <tk8.5/tk.h>  // #include <tk/tk.h>
#endif /* HAS_GUI */



```


### modify Makefile in sim


```mak



# Comment this out if you don't have Tcl/Tk on your system

GUIMODE=-DHAS_GUI 

# Modify the following line so that gcc can find the libtcl.so and
# libtk.so libraries on your system. You may need to use the -L option
# to tell gcc which directory to look in. Comment this out if you
# don't have Tcl/Tk.

TKLIBS=-L/usr/lib/tcl8.5/ -ltk -ltcl

# Modify the following line so that gcc can find the tcl.h and tk.h
# header files on your system. Comment this out if you don't have
# Tcl/Tk.

TKINC=-isystem /usr/include/tcl8.5/



```

### comment matherr in seq/ssim.c and pipe/psim.c

```c++

/* Hack for SunOS */
// extern int matherr();
// int *tclDummyMathPtr = (int *) matherr;



```


## PART A

### Iteratively sum linked list elements

要求写一段y86-64的汇编代码，实现对一个链表元素求和，也就是如下c语言的相同功能代码。

```c

/* sum_list - Sum the elements of a linked list */
long sum_list(list_ptr ls)
{
    long val = 0;
    while (ls) {
	val += ls->val;
	ls = ls->next;
    }
    return val;
}


```

我们可以先瞅瞅这段c代码被汇编成x86-64的汇编代码是什么样。记得编译选项要 gcc -S -Og，不然默认的优化选项可能不是很容易明白。

得到

```GAS

sum_list:
.LFB0:
	.cfi_startproc
	movl	$0, %eax
.L2:
	testq	%rdi, %rdi
	je	.L4
	addq	(%rdi), %rax
	movq	8(%rdi), %rdi
	jmp	.L2
.L4:
	ret


```

同时，我们可以参考CSAPP:3e Figure 4.7 Y86-64的代码示例


```GAS
# Execution begins at address 0
.pos 0
irmovq stack, %rsp
# Set up stack pointer
call main
# Execute main program
halt
# Terminate program

# Array of 4 elements
.align 8
array:
.quad 0x000d000d000d
.quad 0x00c000c000c0
.quad 0x0b000b000b00
.quad 0xa000a000a000

main:
irmovq array,%rdi
irmovq $4,%rsi
call sum
ret
# sum(array, 4)

# long sum(long *start, long count)
# start in %rdi, count in %rsi
sum:
irmovq $8,%r8
# Constant 8
irmovq $1,%r9
# Constant 1
xorq %rax,%rax
# sum = 0
andq %rsi,%rsi
# Set CC
jmp
test
# Goto test
loop:
mrmovq (%rdi),%r10
# Get *start
addq %r10,%rax
# Add to sum
addq %r8,%rdi
# start++
subq %r9,%rsi
# count--. Set CC
test:
jne
loop
# Stop when 0
ret
# Return
# Stack starts here and grows to lower addresses
.pos 0x200
stack:

```

比较容易得到，我们需要的sum_list函数的Y86-64代码是:

```GAS

    .pos 0
    irmovq stack, %rsp  # Set up stack pointer
    call main # Execute main function
    halt

# Sample linked list
    .align 8
ele1:
    .quad 0x00a
    .quad ele2
ele2:
    .quad 0x0b0
    .quad ele3
ele3:
    .quad 0xc00
    .quad 0


main:
    irmovq ele1,%rdi
    call sum_list
    ret

sum_list:
    irmovq $0, %rax 
loop:
    andq  %rdi, %rdi
    je finish
    mrmovq (%rdi),%r8
    addq %r8, %rax
    mrmovq 8(%rdi), %rdi
    jmp loop
finish:
    ret

.pos 0x200
stack:

```

这里有几点要注意:

- Y86-64的代码最后必须有空行
- Y86-64的cpu中，ALU的输入不能是立即数，因此如果操作数有立即数，需要先将立即数mov到寄存器中。
- 与上一条类似，Y86-64的ALU的输入不能是内存中的地址，因此如果操作数有内存中的地址，需要先将改地址的内容mov到寄存器中。
- Y86-64的mov根据操作数的不同类别分了不同的指令，但是没有根据操作数的size来区分不同指令。
- Y86-64在ALU做完操作之后会自动设置相应的condition code(CC)



那么如何验证正确性呢？

```shell

$  ./yas sum.ys
$  ./yis sum.yo

```

得到结果:

```GAS

Stopped in 28 steps at PC = 0x13.  Status 'HLT', CC Z=1 S=0 O=0
Changes to registers:
%rax:   0x0000000000000000      0x0000000000000cba
%rsp:   0x0000000000000000      0x0000000000000200
%r8:    0x0000000000000000      0x0000000000000c00

Changes to memory:
0x01f0: 0x0000000000000000      0x000000000000005b
0x01f8: 0x0000000000000000      0x0000000000000013

```

%rax中存放的结果为0xcba,结果正确。


### Recursively sum linked list elements

思路和上面类似，不多说了。

```GAS

    .pos 0
    irmovq stack, %rsp  # Set up stack pointer
    call main # Execute main function
    halt

# Sample linked list
    .align 8
ele1:
    .quad 0x00a
    .quad ele2
ele2:
    .quad 0x0b0
    .quad ele3
ele3:
    .quad 0xc00
    .quad 0


main:
    irmovq ele1,%rdi
    call rsum_list
    ret

rsum_list:
    andq  %rdi, %rdi
    je finish
    pushq %rbx
    mrmovq (%rdi),%rbx     # val
    mrmovq 8(%rdi), %rdi   # ls->next
    call rsum_list
    addq %rbx, %rax
    popq %rbx
    ret 

finish:
    irmovq $0, %rax 
    ret

.pos 0x200
stack:




```



### Copy a source block to a destination block


注意有三个参数，按照x86-64调用惯例，三个参数依次放入寄存器:

%rdi,%rsi,%rdx

![x86-64调用惯例.png](https://i.loli.net/2020/02/28/PNsgDbqRGU793Hm.png)

除此以外没什么需要注意的。。


```GAS

    .pos 0
    irmovq stack, %rsp  # Set up stack pointer
    call main # Execute main function
    halt

.align 8
# Source block
src:
    .quad 0x00a
    .quad 0x0b0
    .quad 0xc00
# Destination block
dest:
    .quad 0x111
    .quad 0x222
    .quad 0x333


main:
    irmovq src,%rdi
    irmovq dest,%rsi
    irmovq $3,%rdx

    call copy_block
    ret

copy_block:
    irmovq $8,%r8
    irmovq $1,%r9
    irmovq $0, %rcx 
loop:
    andq  %rdx, %rdx
    jle finish
    mrmovq (%rdi),%rax
    rmmovq %rax,(%rsi)
    xorq %rax,%rcx
    subq %r9, %rdx
    addq %r8,%rdi
    addq %r8,%rsi
    jmp loop
finish:
    rrmovq  %rcx,%rax
    ret

.pos 0x200
stack:




```

## PART B

### 要求

part B要求扩展 SEQ processor 来实现iadd指令，也就是支持立即数的加法指令。具体的要求可以参考CSAPP:3e的Homework problems 4.51 and 4.52

> 4.51 ◆
Practice Problem 4.3 introduced the iaddq instruction to add immediate data to a
register. Describe the computations performed to implement this instruction. Use
the computations for irmovq and OPq (Figure 4.18) as a guide.


>4.52 ◆◆
The file seq-full.hcl contains the HCL description for SEQ, along with the
declaration of a constant IIADDQ having hexadecimal value C, the instruction code
for iaddq. Modify the HCL descriptions of the control logic blocks to implement
the iaddq instruction, as described in Practice Problem 4.3 and Problem 4.51. See
the lab material for directions on how to generate a simulator for your solution
and how to test it.


Figure 4.18
![Y86-64指令描述.png](https://i.loli.net/2020/02/29/ae4cUnPl9yWNLS6.png)

Practice Problem 4.3
![practice_4.3.png](https://i.loli.net/2020/02/29/jIgOynPMzfAxWoK.png)


### 实现

先写出iaddq的stage描述:

iaddq V,rB

- Fetch
    - icode:ifun  <-- M1[PC]
    - rA:rB       <-- M1[PC+1]
    - valC        <-- M8[PC+2]
    - valP        <-- PC+10
- Decode
    - valB        <-- R[rB]
- Execute
    - valE        <-- valB + valC
- Memory
- Write back
    - R[rB]       <-- valE
- PC update
    - PC          <-- valP


然后修改seq-full.hcl。 参考IOPQ 和IIRMOVQ 来实现还是比较容易的。
下面把修改过的位置放了出来:



```hcl

################ Fetch Stage     ###################################

bool instr_valid = icode in 
	{ INOP, IHALT, IRRMOVQ, IIRMOVQ, IRMMOVQ, IMRMOVQ,
	       IOPQ, IIADDQ, IJXX, ICALL, IRET, IPUSHQ, IPOPQ };  
             

// Does fetched instruction require a regid byte?   
bool need_regids =
	icode in { IRRMOVQ, IOPQ, IIADDQ, IPUSHQ, IPOPQ, 
		     IIRMOVQ, IRMMOVQ, IMRMOVQ };


// Does fetched instruction require a constant word?
bool need_valC =
	icode in { IIRMOVQ, IIADDQ,IRMMOVQ, IMRMOVQ, IJXX, ICALL };


// ################ Decode Stage    ###################################


// What register should be used as the B source?
word srcB = [
	icode in { IOPQ, IIADDQ, IRMMOVQ, IMRMOVQ  } : rB;
	icode in { IPUSHQ, IPOPQ, ICALL, IRET } : RRSP;
	1 : RNONE;  # Don't need register
];


// What register should be used as the E destination?
word dstE = [
	icode in { IRRMOVQ } && Cnd : rB;
	icode in { IIRMOVQ, IOPQ,IIADDQ} : rB;
	icode in { IPUSHQ, IPOPQ, ICALL, IRET } : RRSP;
	1 : RNONE;  # Don't write any register
];

// ################ Execute Stage   ###################################



// Select input A to ALU
word aluA = [
	icode in { IRRMOVQ, IOPQ } : valA;
	icode in { IIRMOVQ, IRMMOVQ, IMRMOVQ, IIADDQ } : valC;
	icode in { ICALL, IPUSHQ } : -8;
	icode in { IRET, IPOPQ } : 8;
	# Other instructions don't need ALU
];


// Select input B to ALU
word aluB = [
	icode in { IRMMOVQ, IMRMOVQ, IOPQ, IIADDQ, ICALL, 
		      IPUSHQ, IRET, IPOPQ } : valB;
	icode in { IRRMOVQ, IIRMOVQ } : 0;
	# Other instructions don't need ALU
];


// Set the ALU function
word alufun = [
	icode == IOPQ : ifun;
	1 : ALUADD;
];


// Should the condition codes be updated?
bool set_cc = icode in { IOPQ,IIADDQ };


```
### 测试

在benchmark上测试

```shell

➜  y86-code git:(master) ✗ make testssim
../seq/ssim -t asum.yo > asum.seq
../seq/ssim -t asumr.yo > asumr.seq
../seq/ssim -t cjr.yo > cjr.seq
../seq/ssim -t j-cc.yo > j-cc.seq
../seq/ssim -t poptest.yo > poptest.seq
../seq/ssim -t pushquestion.yo > pushquestion.seq
../seq/ssim -t pushtest.yo > pushtest.seq
../seq/ssim -t prog1.yo > prog1.seq
../seq/ssim -t prog2.yo > prog2.seq
../seq/ssim -t prog3.yo > prog3.seq
../seq/ssim -t prog4.yo > prog4.seq
../seq/ssim -t prog5.yo > prog5.seq
../seq/ssim -t prog6.yo > prog6.seq
../seq/ssim -t prog7.yo > prog7.seq
../seq/ssim -t prog8.yo > prog8.seq
../seq/ssim -t ret-hazard.yo > ret-hazard.seq
grep "ISA Check" *.seq
asumr.seq:ISA Check Succeeds
asum.seq:ISA Check Succeeds
cjr.seq:ISA Check Succeeds
j-cc.seq:ISA Check Succeeds
poptest.seq:ISA Check Succeeds
prog1.seq:ISA Check Succeeds
prog2.seq:ISA Check Succeeds
prog3.seq:ISA Check Succeeds
prog4.seq:ISA Check Succeeds
prog5.seq:ISA Check Succeeds
prog6.seq:ISA Check Succeeds
prog7.seq:ISA Check Succeeds
prog8.seq:ISA Check Succeeds
pushquestion.seq:ISA Check Succeeds
pushtest.seq:ISA Check Succeeds
ret-hazard.seq:ISA Check Succeeds
rm asum.seq asumr.seq cjr.seq j-cc.seq poptest.seq pushquestion.seq pushtest.seq prog1.seq prog2.seq prog3.seq prog4.seq prog5.seq prog6.seq prog7.seq prog8.seq ret-hazard.seq

```
执行回归测试

```shell

➜  ptest git:(master) ✗ make SIM=../seq/ssim
./optest.pl -s ../seq/ssim 
Simulating with ../seq/ssim
  All 49 ISA Checks Succeed
./jtest.pl -s ../seq/ssim 
Simulating with ../seq/ssim
  All 64 ISA Checks Succeed
./ctest.pl -s ../seq/ssim 
Simulating with ../seq/ssim
  All 22 ISA Checks Succeed
./htest.pl -s ../seq/ssim 
Simulating with ../seq/ssim
  All 600 ISA Checks Succeed
➜  ptest git:(master) ✗ make SIM=../seq/ssim TFLAGS=-i
./optest.pl -s ../seq/ssim -i
Simulating with ../seq/ssim
  All 58 ISA Checks Succeed
./jtest.pl -s ../seq/ssim -i
Simulating with ../seq/ssim
  All 96 ISA Checks Succeed
./ctest.pl -s ../seq/ssim -i
Simulating with ../seq/ssim
  All 22 ISA Checks Succeed
./htest.pl -s ../seq/ssim -i
Simulating with ../seq/ssim
  All 756 ISA Checks Succeed


```

全部都是" ISA Checks Succeed"，说明结果应该OK



## PART C

这个lab的前两部分给人一种很简单的错觉。。。。让人觉得，不过如此嘛

然后就死了。。。也可能是我的思路不对。。。

以为homework会比lab内容简单。。。 于是先跑去做了pipe-bt..把分支预测改成not token... 没做出来。。

又去做了pipe-nobypass,改成没有forwarding机制。。 发现要考虑的case多到爆炸。。调到怀疑人生，怀疑我是不是不适合CS.

大概卡了一周。。不得已去搜答案。。发现做课后几个pipeline相关题目的人并不多。。而且似乎比lab本身要难很多。。。



然后循环展开的优化打算读完第五章再说。。


20200425更新:

转眼都快五月了,终于把这个坑填了. 

说一下我优化的思路吧.
根据提示,循环展开肯定是一个非常重要的优化. 于是先尝试实现一个2x1的循环展开看下效果.

先把对应的c的代码写了出来:

```c

typedef int word_t;
word_t ncopy2(word_t *src, word_t *dst, word_t len)
{
    word_t count = 0;
    word_t val;
    word_t val2;

    while (len > 1) {
        val = *src++;
        val2 = *src++;
        *dst++ = val;
        *dst++ = val2;
        if (val > 0)
            count++;
        if (val2 > 0)
            count++;
        len-=2;
    }
    while (len>0){
        val = *src;
        *dst = val;
        if (val>0)
        count++;
        len--;
    }
    return count;
}

```

遇到的第一个问题是如何判断len>1..
如果是x86汇编可以使用cmp指令,但是Y86并没有这个指令.

考虑到cmp是不影响寄存器值的sub,参考[How to convert IA32 'cmp' instruction to Y86?](https://stackoverflow.com/questions/15098073/how-to-convert-ia32-cmp-instruction-to-y86)

我们可以用栈来保护被sub影响的值

```GAS

pushl %ecx
subl  %ebx, %ecx
popl  %ecx

```


于是得到2x1循环展开的初始版本,CPE是11.6,分数是0

```GAS

# You can modify this portion
	# Loop header
	xorq %rax,%rax		# count = 0;
	irmovq $1, %r10
	pushq %rdx
	subq  %r10, %rdx
	popq  %rdx		# len <= 1?
	jle Single		# if so, goto Done:

Loop:	
	mrmovq (%rdi), %r10	# read val from src...
	mrmovq 8(%rdi), %r11 # read val2 from src++
	rmmovq %r10, (%rsi)	# ...and store it to dst
	rmmovq %r11, 8(%rsi) # .. store val2 to dst++
	andq %r10, %r10		# val <= 0?
	jle Npos		# if so, goto Npos:
	iaddq $1, %rax
	# irmovq $1, %r10
	# addq %r10, %rax		# count++

Npos:
	andq %r11, %r11
	jle	Npos2
	# irmovq $1, %r10
	# addq %r10, %rax
	iaddq $1, %rax

Npos2:	
    irmovq $2, %r10
	subq %r10, %rdx		# len-=2
	irmovq $16, %r10
	addq %r10, %rdi		# src++
	addq %r10, %rsi		# dst++
	irmovq $1, %r10
	pushq %rdx
	subq  %r10, %rdx
	popq  %rdx		# len > 1?

	jg Loop			# if so, goto Loop:

Single:
	andq %rdx, %rdx
	jle Done
	mrmovq (%rdi),%r10
	rmmovq %r10, (%rsi)
	andq %r10, %r10
	jle Done 
	# irmovq $1, %r10
	# addq %r10, %rax		# count++
	iaddq $1, %rax
##################################################################
# Do not modify the following section of code
# Function epilogue.
Done:
	ret

```


接下来,我们发现由于一些指令无法使用立即数作为参数,%r10这个寄存器在频繁地作为临时变量存储一些常数. 我们考虑使用更多的寄存器,来存储这几个常数. CPE可以从11.6提高到10.6.  这个时候,仍然是0分.


想起我们之前实现了的iaddq指令. 不妨把所有的加法和减法运算都用iaddq来替代..CPE课可以从10.6到10.41. 终于有分了.

然后观察代码..发现瓶颈可能在push和pop... 因为压栈和出栈都要访问内存.仔细思考一下,其实不是一定要和x86的cmp指令等价. 因此其实是没必要来保护对应寄存器的值的.


于是得到如下CPE可以到9.48的版本:


```GAS

# You can modify this portion
	# Loop header
	xorq %rax,%rax		# count = 0;
	irmovq $1, %r10
	pushq %rdx
	subq  %r10, %rdx
	popq  %rdx		# len <= 1?
	jle Single		# if so, goto Done:

Loop:	
	mrmovq (%rdi), %r10	# read val from src...
	mrmovq 8(%rdi), %r11 # read val2 from src++
	rmmovq %r10, (%rsi)	# ...and store it to dst
	rmmovq %r11, 8(%rsi) # .. store val2 to dst++
	andq %r10, %r10		# val <= 0?
	jle Npos		# if so, goto Npos:
	iaddq $1, %rax
	# irmovq $1, %r10
	# addq %r10, %rax		# count++

Npos:
	andq %r11, %r11
	jle	Npos2
	# irmovq $1, %r10
	# addq %r10, %rax
	iaddq $1, %rax

Npos2:	
    irmovq $2, %r10
	subq %r10, %rdx		# len-=2
	irmovq $16, %r10
	addq %r10, %rdi		# src++
	addq %r10, %rsi		# dst++
	irmovq $1, %r10
	pushq %rdx
	subq  %r10, %rdx
	popq  %rdx		# len > 1?

	jg Loop			# if so, goto Loop:

Single:
	andq %rdx, %rdx
	jle Done
	mrmovq (%rdi),%r10
	rmmovq %r10, (%rsi)
	andq %r10, %r10
	jle Done 
	# irmovq $1, %r10
	# addq %r10, %rax		# count++
	iaddq $1, %rax
##################################################################
# Do not modify the following section of code
# Function epilogue.
Done:
	ret

```


至此,我们已经确认循环展开是有效的. 因此不妨使用4x1的循环展开. 同时我们删除了一些冗余的代码,最终达到了8.68的CPE.

分数为36.4/60.. 及格了...orz

完整代码可以参考[ncopy.ys](https://github.com/111qqz/csapp-lab/blob/master/archlab/sim/pipe/ncopy.ys)


然后接下来的优化方向.. 毕竟容易想到的是条件mov的指令..
但是条件mov指令应该主要控制分支跳转的代价比较大时,才会比较有用.而我们的程序应该不存在比较大的开销.

然后其他的就是.. pipe-full.hcl文件我们除了增加iaddq指令外还没修改过... 可能会有进一步的优化空间


