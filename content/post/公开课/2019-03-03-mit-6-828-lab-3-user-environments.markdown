---
author: 111qqz
date: 2019-03-03 12:45:25+00:00
draft: false
title: '【施工中】MIT 6.828 lab 3: User Environments'
type: post
url: /2019/03/mit-6-828-lab-3-user-environments/
categories:
- mooc
tags:
- '6.828'
---

JOS的environments基本可以理解成"process"进程的同义词，但是由于"process"是一个unix术语，因此使用environment这个词．


## Part A: User Environments and Exception Handling


查看　kern/env.c文件，看到三个全局变量:

```c   
    struct Env *envs = NULL;		// All environments
    struct Env *curenv = NULL;		// The current env
    static struct Env *env_free_list;	// Free environment list
```

envs会在JOS启动后会指向一个Env structures的数组，表示JOS中的全部environments. 理论上，JOS kernel最多能支持NENV个同时运行的environments.　但是实际上不会远不会达到这个数量．

env_free_list是一个链表结构，用来存放当前没有在运行的Env structure.. 和page_free_list　类似．

curenv表示的是当前正在运行的environment,当JOS刚刚启动，第一个environment运行之前，curenv的值为NULL.

<!-- more -->

接下来我们来阅读一下inc/env.h文件
```c
    
    /* See COPYRIGHT for copyright information. */
    
    #ifndef JOS_INC_ENV_H
    #define JOS_INC_ENV_H
    
    #include <inc/types.h>
    #include <inc/trap.h>
    #include <inc/memlayout.h>
    
    typedef int32_t envid_t;
    
    // An environment ID 'envid_t' has three parts:
    //
    // +1+---------------21-----------------+--------10--------+
    // |0|          Uniqueifier             |   Environment    |
    // | |                                  |      Index       |
    // +------------------------------------+------------------+
    //                                       \--- ENVX(eid) --/
    //
    // The environment index ENVX(eid) equals the environment's index in the
    // 'envs[]' array.  The uniqueifier distinguishes environments that were
    // created at different times, but share the same environment index.
    //
    // All real environments are greater than 0 (so the sign bit is zero).
    // envid_ts less than 0 signify errors.  The envid_t == 0 is special, and
    // stands for the current environment.
    
    #define LOG2NENV		10
    #define NENV			(1 << LOG2NENV)
    #define ENVX(envid)		((envid) & (NENV - 1))
    
    // Values of env_status in struct Env
    enum {
    	ENV_FREE = 0,
    	ENV_DYING,
    	ENV_RUNNABLE,
    	ENV_RUNNING,
    	ENV_NOT_RUNNABLE
    };
    
    // Special environment types
    enum EnvType {
    	ENV_TYPE_USER = 0,
    };
    
    struct Env {
    	struct Trapframe env_tf;	// Saved registers
    	struct Env *env_link;		// Next free Env
    	envid_t env_id;			// Unique environment identifier
    	envid_t env_parent_id;		// env_id of this env's parent
    	enum EnvType env_type;		// Indicates special system environments
    	unsigned env_status;		// Status of the environment
    	uint32_t env_runs;		// Number of times environment has run
    
    	// Address space
    	pde_t *env_pgdir;		// Kernel virtual address of page dir
    };
    
    #endif // !JOS_INC_ENV_H
    
```





 	  * **env_tf**:　用来在切换环境时保存各种register的值，以便之后恢复现场．
 	  * **env_link**:　用于构成一个链表结构，指向喜爱一个空闲的 environment.
 	  * **env_id**: 用于唯一标识使用当前这个Env structure（也就是envs数组中的某个位置）的environment的ID.当这个environment终止时，**envs数组中的用一个位置可能会被re-allocate一个新的environment,但是env_id是不同的．**虽然env_id不同，但是env_id的最后10bit是用来标识在envs的下标的，如果使用的是envs数组中的同一个位置，这部分是相同的．具体可以参考inc/env.h．
 	  * **env_parent_id**:　创建这个environment的environment 的env_id. 就是父进程id...
 	  * **env_type:  **用于区分不同种类的环境．对于大部分环境，类型都是**ENV_TYPE_USER.******
 	  * **env_status**: 用来标识当前这个environment的状态．

 	    * ENV_FREE: 标识一个environment是inactive的，因此在env_free_list上．
 	    * ENV_RUNNABLE: 标识一个environment等待运行在处理器上．
 	    * ENV_RUNNING:标识正在运行
 	    * ENV_NOT_RUNNABLE: 标识一个目前active的环境，但是没有准备好运行，原因可能是正在等待一个其他environment的交互．
 	    * ENV_DYING：　可以类比"僵尸进程"


 	  * **env_pgdir: 当前这个environment的page directory.**




### Allocating the Environments Array




<blockquote>Modify `mem_init()` in kern/pmap.c to allocate and map the `envs` array. This array consists of exactly `NENV` instances of the `Env` structure allocated much like how you allocated the `pages` array. Also like the `pages` array, the memory backing `envs`should also be mapped user read-only at `UENVS` (defined in inc/memlayout.h) so user processes can read from this array.

You should run your code and make sure `check_kern_pgdir()` succeeds.</blockquote>


和mem_init中申请pages的空间是一样的．

    
    envs = (struct Env *)boot_alloc(sizeof(struct Env*)*NENV);




<del>后面有空再写</del>


### Creating and Running Environments


由于现在JOS还没有一个文件系统，因此将可执行文件以ELF格式嵌入到kernel中．

练习２：


<blockquote>In the file env.c, finish coding the following functions:

> 
> 
 	`env_init()`
> 
 	    Initialize all of the `Env` structures in the `envs` array and add them to the `env_free_list`. Also calls `env_init_percpu`, which configures the segmentation hardware with separate segments for privilege level 0 (kernel) and privilege level 3 (user).
> 
 	`env_setup_vm()`
> 
 	    Allocate a page directory for a new environment and initialize the kernel portion of the new environment's address space.
> 
 	`region_alloc()`
> 
 	    Allocates and maps physical memory for an environment
> 
 	`load_icode()`
> 
 	    You will need to parse an ELF binary image, much like the boot loader already does, and load its contents into the user address space of a new environment.
> 
 	`env_create()`
> 
 	    Allocate an environment with `env_alloc` and call `load_icode` to load an ELF binary into it.
> 
 	`env_run()`
> 
 	    Start a given environment running in user mode.
> 

As you write these functions, you might find the new cprintf verb `%e` useful -- it prints a description corresponding to an error code. For example,

>     
>     	r = -E_NO_MEM;
>     	panic("env_alloc: %e", r);
> 
> 
will panic with the message "env_alloc: out of memory".</blockquote>


env_init()是这些函数中最简单的一个，只需要注意为了保证env_free_list的顺序和envs array的相同，需要倒序遍历．

    
    // Mark all environments in 'envs' as free, set their env_ids to 0,
    // and insert them into the env_free_list.
    // Make sure the environments are in the free list in the same order
    // they are in the envs array (i.e., so that the first call to
    // env_alloc() returns envs[0]).
    //
    void
    env_init(void)
    {
    	// Set up envs array
    	// LAB 3: Your code here.
    	cprintf("env_init start\n");
    	for ( int i = NENV-1 ; i >= 0 ;  i--)
    	{
    		envs[i].env_id = 0;
    		envs[i].env_status = ENV_FREE;
    		envs[i].env_link = env_free_list;
    		env_free_list = &envs[i];
    	}
    
    	// Per-CPU part of the initialization
    	cprintf("env_init before init_precpu\n");
    	env_init_percpu();
    	cprintf("env_init end\n");
    }


接下来看env_setup_vm函数，作用是为新的environment初始化一个page directory. **每个environment都有一个自己的page directory.**

注释里提示用kern_pgdir作为一个template... 说实话完全没get到含义...查阅资料发现其实就是...copy过来的意思...orz  注意头文件string.h中可能有些有用的函数，比如memcpy

    
    // Initialize the kernel virtual memory layout for environment e.
    // Allocate a page directory, set e->env_pgdir accordingly,
    // and initialize the kernel portion of the new environment's address space.
    // Do NOT (yet) map anything into the user portion
    // of the environment's virtual address space.
    //
    // Returns 0 on success, < 0 on error.  Errors include:
    //	-E_NO_MEM if page directory or table could not be allocated.
    //
    static int
    env_setup_vm(struct Env *e)
    {
    
    	cprintf("env_setup_vm start\n");
    	int i;
    	struct PageInfo *p = NULL;
    
    	// Allocate a page for the page directory
    	if (!(p = page_alloc(ALLOC_ZERO)))
    		return -E_NO_MEM;
    
    	// Now, set e->env_pgdir and initialize the page directory.
    	//
    	// Hint:
    	//    - The VA space of all envs is identical above UTOP
    	//	(except at UVPT, which we've set below).
    	//	See inc/memlayout.h for permissions and layout.
    	//	Can you use kern_pgdir as a template?  Hint: Yes.
    	//	(Make sure you got the permissions right in Lab 2.)
    	//    - The initial VA below UTOP is empty.
    	//    - You do not need to make any more calls to page_alloc.
    	//    - Note: In general, pp_ref is not maintained for
    	//	physical pages mapped only above UTOP, but env_pgdir
    	//	is an exception -- you need to increment env_pgdir's
    	//	pp_ref for env_free to work correctly.
    	//    - The functions in kern/pmap.h are handy.
    
    	// LAB 3: Your code here.
    	// 去看一下string.h，里面有些函数可能有用
    	p->pp_ref++;
    	e->env_pgdir = (pde_t *)KADDR(page2pa(p));
    	memcpy(e->env_pgdir,kern_pgdir,PGSIZE);
    	// 不知道有memcpy函数可以用...orz
    
    	cprintf("PA e->env_pgdir:x\n",PADDR(e->env_pgdir));
    	// UVPT maps the env's own page table read-only.
    	// Permissions: kernel R, user R
    	e->env_pgdir[PDX(UVPT)] = PADDR(e->env_pgdir) | PTE_P | PTE_U;
    	cprintf("env_setup_vim  end\n");
    
    	return 0;
    }


接下来是函数region_alloc,作用是为一个函数分配并映射物理内存．使用page_insert即可

    
    // Allocate len bytes of physical memory for environment env,
    // and map it at virtual address va in the environment's address space.
    // Does not zero or otherwise initialize the mapped pages in any way.
    // Pages should be writable by user and kernel.
    // Panic if any allocation attempt fails.
    //
    static void
    region_alloc(struct Env *e, void *va, size_t len)
    {
    	cprintf("region_alloc start\n");
    	// LAB 3: Your code here.
    	// (But only if you need it for load_icode.)
    	// use page_insert
    	uintptr_t VA = ROUNDDOWN((uintptr_t)va,PGSIZE);
    	uintptr_t VA_end = ROUNDUP((uintptr_t)(va + len),PGSIZE);
    	struct PageInfo *pginfo = NULL;
    	for (; VA < VA_end ; VA+=PGSIZE)
    	{
    		if (!(pginfo=page_alloc(ALLOC_ZERO)))
    		{
    			panic("page_alloc in region_alloc failed!");
    		}
    		int ret = page_insert(e->env_pgdir, pginfo, (void *)VA, PTE_U | PTE_W | PTE_P);
    		if (ret)
    		{
    			panic("page insert failed %e",ret);
    		}
    	}
    	cprintf("rgion_alloc end\n");
    	
    	// Hint: It is easier to use region_alloc if the caller can pass
    	//   'va' and 'len' values that are not page-aligned.
    	//
    	//   You should round va down, and round (va + len) up.
    	//   (Watch out for corner-cases!)
    }


接下里要实现的函数是**load_icode()，作用是将ELF格式的二进制文件加载到新环境的用户地址空间．**

这个函数是相对比较难实现的一个，可以参考boot/main.c中boot loader加载 kernel image的过程．区别在于，boot loader是从disk中加载kernel image,而load_icode()要加载的二进制文件已经在memory中了．

实现参考[lab3 抢占式调度](http://grid.hust.edu.cn/zyshao/Teaching_Material/OSEngineering/Chapter5.pdf)

**主要的难点在于在load program segment的时候，是load到user的environment,因此需要在load之前使用lcr3指令切换到当前environment的page dir.**

**以及在指定完program的entry point之后，需要将page dir切换回kern_pgdir**

**还有就是指定入口点的方法，是将该环境的指令寄存器eip的值设置为该elf格式文件的e_entry的值**



    
    // Set up the initial program binary, stack, and processor flags
    // for a user process.
    // This function is ONLY called during kernel initialization,
    // before running the first user-mode environment.
    //
    // This function loads all loadable segments from the ELF binary image
    // into the environment's user memory, starting at the appropriate
    // virtual addresses indicated in the ELF program header.
    // At the same time it clears to zero any portions of these segments
    // that are marked in the program header as being mapped
    // but not actually present in the ELF file - i.e., the program's bss section.
    //
    // All this is very similar to what our boot loader does, except the boot
    // loader also needs to read the code from disk.  Take a look at
    // boot/main.c to get ideas.
    //
    // Finally, this function maps one page for the program's initial stack.
    //
    // load_icode panics if it encounters problems.
    //  - How might load_icode fail?  What might be wrong with the given input?
    //
    static void
    load_icode(struct Env *e, uint8_t *binary)
    {
    	cprintf("load icode start\n");
    	// Hints:
    	//  Load each program segment into virtual memory
    	//  at the address specified in the ELF segment header.
    	//  You should only load segments with ph->p_type == ELF_PROG_LOAD.
    	//  Each segment's virtual address can be found in ph->p_va
    	//  and its size in memory can be found in ph->p_memsz.
    	//  The ph->p_filesz bytes from the ELF binary, starting at
    	//  'binary + ph->p_offset', should be copied to virtual address
    	//  ph->p_va.  Any remaining memory bytes should be cleared to zero.
    	//  (The ELF header should have ph->p_filesz <= ph->p_memsz.)
    	//  Use functions from the previous lab to allocate and map pages.
    	// 
    	//	question: how to copy memory?   for-loop and assgin?
    	//	// no! use memcpy in string.h
    	//
    	//  All page protection bits should be user read/write for now.
    	//  ELF segments are not necessarily page-aligned, but you can
    	//  assume for this function that no two segments will touch
    	//  the same virtual page.
    	//
    	//  You may find a function like region_alloc useful.
    	//  Q: how to use region_alloc? 
    	//
    	//  Loading the segments is much simpler if you can move data
    	//  directly into the virtual addresses stored in the ELF binary.
    	//  So which page directory should be in force during
    	//  this function?
    	//
    	//  You must also do something with the program's entry point,
    	//  to make sure that the environment starts executing there.
    	//  What?  (See env_run() and env_pop_tf() below.)
    
    	// LAB 3: Your code here.
    	struct Elf * elf = (struct Elf *)binary;
    	cprintf("elf->e_magic :x\n",elf->e_magic);
    	if (elf->e_magic != ELF_MAGIC)
    	{
    		panic("invalid ELF file!");
    	}
    	struct Proghdr *ph,*eph;
    	ph = (struct Proghdr *)((uint8_t *)elf + elf->e_phoff);
    	eph = ph + elf->e_phnum;
    	cprintf("ph: x  eph:x\n",ph,eph);
    	cprintf("binary:x p_offset:x filesz:x\n",binary,ph->p_offset,ph->p_filesz);
    	lcr3(PADDR(e->env_pgdir));
    	
    	for (; ph < eph ; ph++)
    	{
    		//cprintf("ph->ptype: %d\n",ph->p_type);
    		// ph->ptype should be 1 instead of 0 .
    		if (ph->p_type != ELF_PROG_LOAD) continue;
    		uint8_t * src = binary + ph->p_offset;
    		uint8_t * dst  =  (uint8_t *)ph->p_va;
    		region_alloc(e,(void *)dst, ph->p_memsz);
    		memcpy(dst,src,ph->p_filesz);
    		// use memcpy .
    		memset(dst  + ph->p_filesz, 0, ph->p_memsz - ph->p_filesz);
    	}
    	e->env_tf.tf_eip = elf->e_entry;
    	lcr3(PADDR(kern_pgdir));
    	// lcr3 is too hard for me...
    
    	cprintf("load_icode before env_run\n");	
    	//env_run(e);
    
    	// Now map one page for the program's initial stack
    	// at virtual address USTACKTOP - PGSIZE.
    	region_alloc(e, (void*)(USTACKTOP - PGSIZE), PGSIZE);
    	// LAB 3: Your code here.
    }


接下来是函数env_create()，作用是申请一个新的environment,加载二进制文件，没有什么难度

    
    // Allocates a new env with env_alloc, loads the named elf
    // binary into it with load_icode, and sets its env_type.
    // This function is ONLY called during kernel initialization,
    // before running the first user-mode environment.
    // The new env's parent ID is set to 0.
    //
    void
    env_create(uint8_t *binary, enum EnvType type)
    {
    	cprintf("env_create start\n");
    	// LAB 3: Your code here.
    	struct Env *env;
    	int ret = env_alloc( &env, 0);
    	if (ret)
    	{
    		panic("env_alloc:%e", ret);
    	}
    	
    	cprintf("env_create before load_icode\n");
    
    	env->env_type = type;
    	load_icode(env, binary);
    	env_run(env);
    
    }


之后是env_run,也没什么难度．

    
    //
    // Context switch from curenv to env e.
    // Note: if this is the first call to env_run, curenv is NULL.
    //
    // This function does not return.
    //
    void env_run(struct Env *e)
    {
    	cprintf("env_run start\n");
    	// Step 1: If this is a context switch (a new environment is running):
    	//	   1. Set the current environment (if any) back to
    	//	      ENV_RUNNABLE if it is ENV_RUNNING (think about
    	//	      what other states it can be in),
    	//	   2. Set 'curenv' to the new environment,
    	//	   3. Set its status to ENV_RUNNING,
    	//	   4. Update its 'env_runs' counter,
    	//	   5. Use lcr3() to switch to its address space.
    	// Step 2: Use env_pop_tf() to restore the environment's
    	//	   registers and drop into user mode in the
    	//	   environment.
    
    	// Hint: This function loads the new environment's state from
    	//	e->env_tf.  Go back through the code you wrote above
    	//	and make sure you have set the relevant parts of
    	//	e->env_tf to sensible values.
    
    	// LAB 3: Your code here.
    	if (curenv && curenv->env_status == ENV_RUNNING)
    	{
    		curenv->env_status = ENV_RUNNABLE;
    	}
    	cprintf("miao 1 in env_run\n");
    	curenv = e;
    	curenv->env_status = ENV_RUNNING;
    	curenv->env_runs++;
    	cprintf(" miao 2 in env_run\n");
    	// env_pgdir[0] == 0, which is wrong.
    	cprintf("env_run curenv->env_pgdir :x\n", curenv->env_pgdir[PDX(UVPT)]);
    	lcr3(PADDR(curenv->env_pgdir));
    	cprintf("miao 3 in env_run\n");
    
    	env_pop_tf(&curenv->env_tf);
    	cprintf("miao 4 in env_run\n");
    
    	panic("env_run not yet implemented");
    }
    


代码实现完了，但是发现直接crash了．．显示**triple fault**

不要慌，问题不大．这是因为JOS目前还没有允许user space转化到kernel的机制，因此抛出了"general protection exception" ．　然后JOS也处理不了抛出的"general protection exception",因此再次抛出异常．　最后以抛出triple fault结束．

但是我们肯定需要一个办法来验证我们的实现是对的．

方式是使用gdb，在kern/env.c的env_pop_tf函数上设置断点．该函数是进入user mode之前运行的最好一个函数．然后单步发现运行的恰好是lib/entry.S中start label后的几个

    
    #include <inc/mmu.h>
    #include <inc/memlayout.h>
    
    .data
    // Define the global symbols 'envs', 'pages', 'uvpt', and 'uvpd'
    // so that they can be used in C as if they were ordinary global arrays.
    	.globl envs
    	.set envs, UENVS
    	.globl pages
    	.set pages, UPAGES
    	.globl uvpt
    	.set uvpt, UVPT
    	.globl uvpd
    	.set uvpd, (UVPT+(UVPT>>12)*4)
    
    
    // Entrypoint - this is where the kernel (or our parent environment)
    // starts us running when we are initially loaded into a new environment.
    .text
    .globl _start
    _start:
    	// See if we were started with arguments on the stack
    	cmpl $USTACKTOP, %esp
    	jne args_exist
    
    	// If not, push dummy argc/argv arguments.
    	// This happens when we are loaded by the kernel,
    	// because the kernel does not know about passing arguments.
    	pushl $0
    	pushl $0
    
    args_exist:
    	call libmain
    1:	jmp 1b
    
    


然后查看obj/user/hello.asm 文件，找到sys_cputs()函数中的 int $0x30指令(在第1934行左右)，该指令对应的user-space address是0x00800add

在该地址处设置断点，**如果可以顺利执行到　0x800add: int $0x30  　,说明之前的实现没有问题．**






















