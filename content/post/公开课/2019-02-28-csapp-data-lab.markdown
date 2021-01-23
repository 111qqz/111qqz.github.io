---
author: 111qqz
date: 2019-02-28 14:06:42+00:00
draft: false
title: 【施工完成】CSAPP data lab
type: post
url: /2019/02/csapp-data-lab/
categories:
- mooc
tags:
- csapp
---

CSAPP第二章的内容以前组成原理基本都学过...所以就简单翻了翻。

对应的lab是用位运算实现各种有的没的...

题目基本都很tricky...

除了用到一些常规的位运算性质，还用到了一些奇怪的条件:



 	  * ~0x7FFFFFFF = 0x7FFFFFFF + 1
 	  * 0xFFFFFFFF +1 =  0x00000000
 	  * 





0 == ~0+1







唯一让我觉得比较有趣的是how many bits这道题

题目要求是给一个32-bit signed int,问最少用多少位能得到它的补码表示。

考虑正数，显然，**高位的连续的多个0是不必要的**，只需要一个符号位的0即可。

那么对于负数，**高位的连续的多个1也是不必要的。 **原因是，-2^k + 2^(k-1) =  -2^(k-1),也就是说，去掉两个连续的1中高位的那个，数值没有改变。

我们可以将正数和负数统一来看，都是找到最高位的0和1的交界。

**这可以通过和相邻的位置求异或，找到最高位的1的方式来实现。**

接下来就是如何找一个数的最高位的1的位置了。

方法是构造一个单调的函数f,假设最高位位置为a,那么f((a,32))=0,f([0,a])=1.

然后在函数f上二分。

全部问题的代码如下,思路写在注释里了。还有3个涉及浮点数的问题之后补。

    
    /* 
     * bitXor - x^y using only ~ and & 
     *   Example: bitXor(4, 5) = 1
     *   Legal ops: ~ &
     *   Max ops: 14
     *   Rating: 1
     */
    /* 0 0 -> 0
       0 1 -> 1
       1 0 - > 1
       1 1 - > 0
    */
    // ~(~a & ~b)&~(a&b)
    int bitXor(int x, int y) {
      int ans = ~(~x & ~y)&(~(x&y));
      // printf("%d\n",ans);
      return ans;
    }
    /* 
     * tmin - return minimum two's complement integer 
     *   Legal ops: ! ~ & ^ | + << >>
     *   Max ops: 4
     *   Rating: 1
     */
    /*
      0X10000000
    */
    int tmin(void) {
    
      int ans = 0x1 << 31;
      return ans;
    
    
    }
    //2
    /* 
     * isTmax - returns 1 if x is the maximum, two's complement number,
     *     and 0 otherwise 
     *   Legal ops: ! ~ & ^ | +
     *   Max ops: 10
     *   Rating: 1
     *   0x7FFFFFFF
     */
    int isTmax(int x) {
      /*
      大体思路首先是根据，如果x是最大值0x7FFFFFFF,那么~x和x+1(自然溢出)应该相等。
      不能用等号，但是我们可以用异或。x==y 等价于  !(x^y). 因此有了后半段!(x+1)^(~x)
      但是满足这个条件的还有-1,也就是0xFFFFFFFF,因此我们需要排除掉-1.
      还是用异或的性质，这回是0异或者任何数都等于其本身。
      因此如果x为-1，那么前后两部分都为1，结果为0.
      如果x为TMAX,那么前面为0，后面为1，结果为1.
      如果x为其他任何数，前后结果都应为0. 结果为0。
      */
      return (!(x+1))^!((x+1)^(~x));                                                                                                                                   
    }
    /* 
     * allOddBits - return 1 if all odd-numbered bits in word set to 1
     *   where bits are numbered from 0 (least significant) to 31 (most significant)
     *   Examples allOddBits(0xFFFFFFFD) = 0, allOddBits(0xAAAAAAAA) = 1
     *   Legal ops: ! ~ & ^ | + << >>
     *   Max ops: 12
     *   Rating: 2
     */
    // 理解错误。误以为是要求当前长度x的所有奇数位上都是1.
    // 实际上要求和x的长度无关，而是要求[0,31]中，所有奇数位上都是1.
    int allOddBits(int x) {
      int half_mask = (0xAA<<8) | 0xAA;
      int mask = (half_mask<<16) + half_mask;
      // printf("mask:X x:x x\n",mask,x,x&mask);
      return  !((x&mask)^mask);  
      
    }
    /* 
     * negate - return -x 
     *   Example: negate(1) = -1.
     *   Legal ops: ! ~ & ^ | + << >>
     *   Max ops: 5
     *   Rating: 2
     */
    int negate(int x) {
      return ~x + 1;
    }
    //3
    /* 
     * isAsciiDigit - return 1 if 0x30 <= x <= 0x39 (ASCII codes for characters '0' to '9')
     *   Example: isAsciiDigit(0x35) = 1.
     *            isAsciiDigit(0x3a) = 0.
     *            isAsciiDigit(0x05) = 0.
     *   Legal ops: ! ~ & ^ | + << >>
     *   Max ops: 15
     *   Rating: 3
     */
    /* 把0-9的二进制写出来，发现0-7占满了3bit的二进制的8种组合。
       因此考虑只判断8和9两种4bit的情况
       构造mask,不在意的bit的位置放0，在意的bit位置放1.
    */
    int isAsciiDigit(int x) {
      int mask = 0x0E;
      int ones = x&mask;
      int ones_3 = ones >> 3;
      int tens = x>>4;
      // printf("x: x tens: x ones:x\n",x,tens,ones);
      int ones_ok = (!(ones^0x8)) | (!ones_3);
      int tens_ok = !(tens^0x3);
      return ones_ok & tens_ok;
    
    }
    /* 
     * conditional - same as x ? y : z 
     *   Example: conditional(2,4,5) = 4
     *   Legal ops: ! ~ & ^ | + << >>
     *   Max ops: 16
     *   Rating: 3
     */
    /*
      关键思路是0xFFFFFFFF和0x00000000之间差了1.
      而这两个数一个是全部位置都取的mask,一个是全部位置都不取的mask.
    */
    int conditional(int x, int y, int z) {
      return   z^(!x + ~0 )&(y^z);
    
    }
    /* 
     * isLessOrEqual - if x <= y  then return 1, else return 0 
     *   Example: isLessOrEqual(4,5) = 1.
     *   Legal ops: ! ~ & ^ | + << >>
     *   Max ops: 24
     *   Rating: 3
     */
    /*
      大体思路是，符号位相同和符号位不同分别考虑
      符号位相同:  考虑差的符号位。
      符号位不同: 当x<0,y>=0时结果为1.
    */
    int isLessOrEqual(int x, int y) {
      int minus = y + (~x+1);
      int s_x = (x>>31)&1;
      int s_y = (y>>31)&1;
      int s_minus = (minus>>31) & 1;
      return (s_x&(!s_y))| (!(s_x^s_y)&!s_minus); 
    }
    //4
    /* 
     * logicalNeg - implement the ! operator, using all of 
     *              the legal operators except !
     *   Examples: logicalNeg(3) = 0, logicalNeg(0) = 1
     *   Legal ops: ~ & ^ | + << >>
     *   Max ops: 12
     *   Rating: 4 
     */
    /* 
      0 == ~0+1
      -2147483648 = ~-2147483648+1
      满足 x == ~x+1
      重点是x和~x+1的符号位相同，如果都是0那么x=0,如果都是1那么x=-214783648`
    */
    int logicalNeg(int x) {
      int s1 = (x>>31)&1;
      int s2 = ((~x+1)>>31)&1;
      // printf("s1: %d s2:%d  %d  %d\n",s1,s2,s1|s2,~(s1|s2));
      //  1 + negate(0) -> 1
      //  1 + neagate(1) -> 0
      return 1+(1+~(s1|s2));
    }
    /* howManyBits - return the minimum number of bits required to represent x in
     *             two's complement
     *  Examples: howManyBits(12) = 5
     *            howManyBits(298) = 10
     *            howManyBits(-5) = 4
     *            howManyBits(0)  = 1
     *            howManyBits(-1) = 1 ??? should be 2?
     *            howManyBits(0x80000000) = 32
     *  Legal ops: ! ~ & ^ | + << >>
     *  Max ops: 90
     *  Rating: 4
     */
    /*
      思路似乎可以转化成判断一个数（可正可负）的最高位的1的位置。
      判断最高位1用二分的办法。
      构造一个单调的函数，假设最高位位置为a,那么f((a,32))=0,f([0,a])=1.
      被 howManyBits(-1)==1 困扰了好久，实际上就是0x1，只有一位，改位就是符号位的情况。 
    */
    int howManyBits(int x) {
      int n = 0 ;
      x^=(x<<1);
      n +=  (!!( x & ((~0) << (n + 16)) )) << 4;   // 看高16位是否为0，是的话区间为[0,16),否的话为[16,32)
      // printf("n:%d\n",n);
      // printf("%d\n",!!(x & ((~0) << (n + 16))));
      n +=  (!!( x & ((~0) << (n + 8)) )) << 3;
      // printf("n:%d\n",n);
      n +=  (!!( x & ((~0) << (n + 4)) )) << 2;
      // printf("n:%d\n",n);
      n +=  (!!( x & ((~0) << (n + 2)) )) << 1;
      // printf("n:%d\n",n);
      n +=  (!!( x & ((~0) << (n + 1)) ));
      // printf("n:%d\n",n);
    
      // int s = (x>>31)&1;
      // int ret = n+1+((1^s)&(!!x));
      // // printf("x:%d ret:%d\n",x,ret);
      
      return n+1;
    }




补上三个涉及浮点数的问题...比较无聊，按照IEEE754操作即可．

    
    //float
    /* 
     * floatScale2 - Return bit-level equivalent of expression 2*f for
     *   floating point argument f.
     *   Both the argument and result are passed as unsigned int's, but
     *   they are to be interpreted as the bit-level representation of
     *   single-precision floating point values.
     *   When argument is NaN, return argument
     *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
     *   Max ops: 30
     *   Rating: 4
     */
    unsigned floatScale2(unsigned uf)
    {
      int exp_ = (uf & 0x7f800000) >> 23;
      int s_ = uf & 0x80000000;
      if (exp_ == 0)
        return (uf << 1) | s_;
      if (exp_ == 255)
        return uf;
      ++exp_;
      if (exp_ == 255)
        return 0x7f800000 | s_;
      return (uf & 0x807fffff) | (exp_ << 23);
    }
    /* 
     * floatFloat2Int - Return bit-level equivalent of expression (int) f
     *   for floating point argument f.
     *   Argument is passed as unsigned int, but
     *   it is to be interpreted as the bit-level representation of a
     *   single-precision floating point value.
     *   Anything out of range (including NaN and infinity) should return
     *   0x80000000u.
     *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
     *   Max ops: 30
     *   Rating: 4
     */
    int floatFloat2Int(unsigned uf)
    {
      int s_ = uf >> 31;
      int exp_ = ((uf & 0x7f800000) >> 23) - 127;
      int frac_ = (uf & 0x007fffff) | 0x00800000;
      if (!(uf & 0x7fffffff))
        return 0;
    
      if (exp_ > 31)
        return 0x80000000;
      if (exp_ < 0)
        return 0;
    
      if (exp_ > 23)
        frac_ <<= (exp_ - 23);
      else
        frac_ >>= (23 - exp_);
    
      if (!((frac_ >> 31) ^ s_))
        return frac_;
      else if (frac_ >> 31)
        return 0x80000000;
      else
        return ~frac_ + 1;
    }
    /* 
     * floatPower2 - Return bit-level equivalent of the expression 2.0^x
     *   (2.0 raised to the power x) for any 32-bit integer x.
     *
     *   The unsigned value that is returned should have the identical bit
     *   representation as the single-precision floating-point number 2.0^x.
     *   If the result is too small to be represented as a denorm, return
     *   0. If too large, return +INF.
     * 
     *   Legal ops: Any integer/unsigned operations incl. ||, &&. Also if, while 
     *   Max ops: 30 
     *   Rating: 4
     */
    unsigned floatPower2(int x)
    {
      int exp = x + 127;
      if (exp <= 0)
        return 0;
      if (exp >= 255)
        return 0x7f800000;
      return exp << 23;
    }
    











