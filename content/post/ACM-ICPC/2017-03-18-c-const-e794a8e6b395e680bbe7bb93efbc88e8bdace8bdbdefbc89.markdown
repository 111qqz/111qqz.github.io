---
author: 111qqz
date: 2017-03-18 12:22:32+00:00
draft: false
title: C++ const 用法总结（转载）
type: post
url: /2017/03/c-const-/
categories:
- c++
---

基本全文照搬了：[关于C++ const 的全面总结](http://blog.csdn.net/eric_jo/article/details/4138548)

总结全面还是要一点时间的orz..感谢原作者，暂时没发现有什么错误（?

其中对我而言比较陌生的是“**const修饰成员函数**”的用法。。已经加粗。


<blockquote>    C++中的const关键字的用法非常灵活，而使用const将大大改善程序的健壮性，本人根据各方面查到的资料进行总结如下，期望对朋友们有所帮助。

Const 是C++中常用的类型修饰符,常类型是指使用类型修饰符const说明的类型，常类型的变量或对象的值是不能被更新的。



**一、Const作用**

**   **如下表所示：
<table width="100%" >
<tbody >
<tr >

> <td width="5%" >**No.**
> </td>

> <td width="16%" >**作用**
> </td>

> <td width="20%" >**说明**
> </td>

> <td width="57%" >**参考代码**
> </td>
</tr>
<tr >

> <td width="5%" >1
> </td>

> <td width="16%" >可以定义const常量
> </td>

> <td width="57%" >const int Max = 100;
> </td>
</tr>
<tr >

> <td width="5%" >2
> </td>

> <td width="16%" >便于进行类型检查
> </td>

> <td width="20%" >const常量有数据类型，而宏常量没有数据类型。编译器可以对前者进行类型安全检查，而对后者只进行字符替换，没有类型安全检查，并且在字符替换时可能会产生意料不到的错误
> </td>

> <td width="57%" >void f(const int i) { .........}
//对传入的参数进行类型检查，不匹配进行提示
> </td>
</tr>
<tr >

> <td width="5%" >3
> </td>

> <td width="16%" >可以保护被修饰的东西
> </td>

> <td width="20%" >防止意外的修改，增强程序的健壮性。
> </td>

> <td width="57%" >void f(const int i) { i=10;//error! }
//如果在函数体内修改了i，编译器就会报错
> </td>
</tr>
<tr >

> <td width="5%" >4
> </td>

> <td width="16%" >可以很方便地进行参数的调整和修改
> </td>

> <td width="20%" >同宏定义一样，可以做到不变则已，一变都变
> </td>
</tr>
<tr >

> <td width="5%" >5
> </td>

> <td width="16%" >为函数重载提供了一个参考
> </td>

> <td width="57%" >class A
{
......
void f(int i)       {......} //一个函数
void f(int i) const {......} //上一个函数的重载
......
};
> </td>
</tr>
<tr >

> <td width="5%" >6
> </td>

> <td width="16%" >可以节省空间，避免不必要的内存分配
> </td>

> <td width="20%" >const定义常量从汇编的角度来看，只是给出了对应的内存地址，而不是象#define一样给出的是立即数，所以，const定义的常量在程序运行过程中只有一份拷贝，而#define定义的常量在内存中有若干个拷贝
> </td>

> <td width="57%" >#define PI 3.14159         //常量宏
const doulbe  Pi=3.14159;  //此时并未将Pi放入ROM中
......
double i=Pi;   //此时为Pi分配内存，以后不再分配！
double I=PI;  //编译期间进行宏替换，分配内存
double j=Pi;  //没有内存分配
double J=PI;  //再进行宏替换，又一次分配内存！
> </td>
</tr>
<tr >

> <td width="5%" >7
> </td>

> <td width="16%" > 提高了效率
> </td>

> <td width="20%" >编译器通常不为普通const常量分配存储空间，而是将它们保存在符号表中，这使得它成为一个编译期间的常量，没有了存储与读内存的操作，使得它的效率也很高
> </td>
</tr>
</tbody>
</table>


**二、Const的使用**

**1、定义常量**
(1)const修饰变量，以下两种定义形式在本质上是一样的。它的含义是：const修饰的类型为TYPE的变量value是不可变的。

TYPE const ValueName = value;
const TYPE ValueName = value;
(2)将const改为外部连接,作用于扩大至全局,编译时会分配内存,并且可以不进行初始化,仅仅作为声明,编译器认为在程序其他地方进行了定义.

extend const int ValueName = value;

**2、指针使用CONST**
(1)指针本身是常量不可变
char* const pContent;

(2)指针所指向的内容是常量不可变
const char *pContent;

(3)两者都不可变
const char* const pContent;

(4)还有其中区别方法，沿着*号划一条线：
如果const位于*的左侧，则const就是用来修饰指针所指向的变量，即指针指向为常量；
如果const位于*的右侧，const就是修饰指针本身，即指针本身是常量。



**3、函数中使用CONST**

(1)const修饰函数参数
a.传递过来的参数在函数内不可以改变(无意义，因为Var本身就是形参)

void function(const int Var);

b.参数指针所指内容为常量不可变

void function(const char* Var);

c.参数指针本身为常量不可变(也无意义，因为char* Var也是形参)

void function(char* const Var);

d.参数为引用，为了增加效率同时防止修改。修饰引用参数时：

void function(const Class& Var); //引用参数在函数内不可以改变

void function(const TYPE& Var); //引用参数在函数内为常量不可变

这样的一个const引用传递和最普通的函数按值传递的效果是一模一样的,他禁止对引用的对象的一切修改,唯一不同的是按值传递会先建立一个类对象的副本, 然后传递过去,而它直接传递地址,所以这种传递比按值传递更有效.另外只有引用的const传递可以传递一个临时对象,因为临时对象都是const属性, 且是不可见的,他短时间存在一个局部域中,所以不能使用指针,只有引用的const传递能够捕捉到这个家伙.
(2)const 修饰函数返回值
const修饰函数返回值其实用的并不是很多，它的含义和const修饰普通变量以及指针的含义基本相同。
a.const int fun1() //这个其实无意义，因为参数返回本身就是赋值。
b. const int * fun2() //调用时 const int *pValue = fun2();
//我们可以把fun2()看作成一个变量，即指针内容不可变。
c.int* const fun3()   //调用时 int * const pValue = fun2();
//我们可以把fun2()看作成一个变量，即指针本身不可变。

一般情况下，函数的返回值为某个对象时，如果将其声明为const时，多用于操作符的重载。通常，不建议用const修饰函数的返回值类型为某个对象或对某个对象引用的情况。原因如下：如果返回值为某个对象为const（const A test = A 实例）或某个对象的引用为const（const A& test = A实例） ，则返回值具有const属性，则返回实例只能访问类A中的公有（保护）数据成员和const成员函数，并且不允许对其进行赋值操作，这在一般情况下很少用到。
**4、类相关CONST**

(1)const修饰成员变量
const修饰类的成员函数，表示成员常量，不能被修改，同时它只能在初始化列表中赋值。
class A
{
…
const int nValue;         //成员常量不能被修改
…
A(int x): nValue(x) { } ; //只能在初始化列表中赋值
}

**(2)const修饰成员函数**
** const修饰类的成员函数，则该成员函数不能修改类中成员变量，也不能调用类中任何非const成员函数。一般写在函数的最后来修饰。**
** class A**
** {**
** …**
** void function()const; //常成员函数, 它不改变对象的成员变量.**

**//也不能调用类中任何非const成员函数。**
** }**

**对于const类对象/指针/引用，只能调用类的const成员函数，因此，const修饰成员函数的最重要作用就是限制对于const对象的使用。**

> 
> 
 	  1. **const成员函数不被允许修改它所在对象的任何一个数据成员。**
 	  2. **const成员函数能够访问对象的const成员，而其他成员函数不可以。**



**任何不会修改数据成员(即函数中的变量)的函数都应该声明为const 类型。如果在编写const 成员函数时，不慎修改了数据成员，或者调用了其它非const 成员函数，编译器将指出错误，这无疑会提高程序的健壮性。以下程序中，类stack 的成员函数GetCount 仅用于计数，从逻辑上讲GetCount 应当为const 函数。编译器将指出GetCount 函数中的错误。**</blockquote>





<blockquote>(3)const修饰类对象/对象指针/对象引用

> 
> 
 	  * const修饰类对象表示该对象为常量对象，其中的任何成员都不能被修改。对于对象指针和对象引用也是一样。
 	  * const修饰的对象，该对象的任何非const成员函数都不能被调用，因为任何非const成员函数会有修改成员变量的企图。
例如：
class AAA
{
void func1();
void func2() const;
}
const AAA aObj;
aObj.func1(); ×
aObj.func2(); 正确const AAA* aObj = new AAA();
aObj-> func1(); ×
aObj-> func2(); 正确



**三、将Const类型转化为非Const类型的方法**



采用const_cast 进行转换。
用法：const_cast <type_id>  (expression)
该运算符用来修改类型的const或volatile属性。除了const 或volatile修饰之外， type_id和expression的类型是一样的。

> 
> 
 	  * 常量指针被转化成非常量指针，并且仍然指向原来的对象；
 	  * 常量引用被转换成非常量引用，并且仍然指向原来的对象；
 	  * 常量对象被转换成非常量对象。



**四、使用const的一些建议**

> 
> 
 	  * 要大胆的使用const，这将给你带来无尽的益处，但前提是你必须搞清楚原委；
 	  * 要避免最一般的赋值操作错误，如将const变量赋值，具体可见思考题；
 	  * 在参数中使用const应该使用引用或指针，而不是一般的对象实例，原因同上；
 	  * const在成员函数中的三种用法（参数、返回值、函数）要很好的使用；
 	  * 不要轻易的将函数的返回值类型定为const;
 	  * 除了重载操作符外一般不要将返回值类型定为对某个对象的const引用;
 	  * 任何不会修改数据成员的函数都应该声明为const 类型。



**五、补充重要说明**



> 
> 
 	  * 类内部的常量限制：使用这种类内部的初始化语法的时候，常量必须是被一个常量表达式

初始化的整型或枚举类型，而且必须是static和const形式。

 	  * 如何初始化类内部的常量：一种方法就是static 和 const 并用，在外部初始化，例如：

class A { public: A() {} private: static const int i; file://注意必须是静态的！ }；

const int A::i=3;另一个很常见的方法就是初始化列表： class A { public: A(int

i=0):test(i) {} private: const int i; }； 还有一种方式就是在外部初始化，

 	  * 如果在非const成员函数中，this指针只是一个类类型的；如果在const成员函数中，

this指针是一个const类类型的；如果在volatile成员函数中,this指针就是一个

volatile类类型的。

 	  * new返回的指针必须是const类型的。

</blockquote>
