---
author: 111qqz
date: 2017-11-24 03:18:01+00:00
draft: false
title: 基础 Haskell 学习笔记
type: post
url: /2017/11/haskell-notes/
categories:
- 其他
tags:
- Haskell
---

出于对函数式编程语言这一技能点的缺失...<del>以及退役之后闲得蛋疼</del>

打算**浅尝辄止**地学一下haskell

这篇笔记不会写成文档那样的详尽..毕竟函数式编程语言也是编程语言...有很多和其他编程语言(命令式？)相似的地方...

所以只会写一些简单的语法+让我感到惊讶的地方orz

总体的感觉...在里面看到了些python和pascal的影子orz...比如子界...已经好久没见到了

<!-- more -->



### 变量






      * 命令式语言中，变量用来跟踪状态（keeping track of state）。
      * Haskell中，变量保存了一个值，**然后再也不可以修改它了。**
      * 变量不仅可以保存像3.14这样的数值，还可以保存任何Haskell表达式






### 函数






      * 函数中的函数

    
    Prelude> let areaRect l w = l * w
    Prelude> let areaSquare s = areaRect s s
    Prelude> areaSquare 5
    25







### 列表






      * 创建列表/添加元素



    
    Prelude> let numbers = [1,2,3,4]
    Prelude> numbers
    [1,2,3,4]
    Prelude> 0:numbers
    [0,1,2,3,4]
    Prelude> 1:0:numbers
    [1,0,1,2,3,4]
    Prelude> 2:1:0:numbers
    [2,1,0,1,2,3,4]
    Prelude> 5:4:3:2:1:0:numbers
    [5,4,3,2,1,0,1,2,3,4]






      * 事实上所有的列表都是在一个空的列表（`[]`）的基础上通过附加数据创建的。逗号与方括号的记法实际上是一种**语法糖**般的令人愉快的形式。 换句话说，`[1,2,3,4,5]`精确地等同于`1:2:3:4:5:[]`
      * 列表中的元素必须有相同的类型
      * 列表的嵌套(二维以及高维度)
      * 列表大概可以类比数组或者python 中的list
      * 将两个List合并是很常见的操作，这可以通过++运算符实现。运算时会遍历左边的list,**因此用:运算符往一个List前端插入元素会是更好的选择。**
      * 若是要按照索引取得List中的元素，可以使用!!运算符，索引的下标是从0开始的。

    
    ghci> "Steve Buscemi" !! 6   
    'B'   
    ghci> [9.4,33.2,96.2,11.2,23.25] !! 1   
    33.2



      * ![](http://fleurer-lee.com/lyah/img/listmonster.png)

      * 




### 元组






      * 类似C++中的pair,只不过不一定是2个元素
      * 事先知道你要储存多少个值为一组**元组（例如数据是二维坐标)**
      * **元组**对其中值的类型没有同一性的要求
      * 若元组的长度为n则称其为_n_-tuple。特殊地如果元组的长度为2则称其为'pairs'（对），如果元组的长度为3则称其为'triples'。





    
    Prelude> fst (2, 5)
    2
    Prelude> fst (True, "boo")
    True
    Prelude> snd (5, "Hello")
    "Hello"




    
     Prelude> let first (x, y) = x
     Prelude> first (3, True) 
     3






      * 列表和元组可以任意方式嵌套






### 在源文件里写代码（和在解释器里的区别）






      * 定义变量没有let
      * 不能定义同一个量两次
      * **顺序不重要**你声明变量的顺序不重要。例如，下面的代码片段可以得到完全同样的结果：
<table border="1" >
<tbody >
<tr >

<td >

    
     y = x * 2
     x = 3
    



</td>

<td >

    
     x = 3
     y = x * 2
    



</td>
</tr>
</tbody>
</table>

      * 变量不可改变的事实意味着我们随意选择以任何顺序写代码（但是这也是我们不能声明一个量一次以上的原因--否则那将是模棱两可的的）。






### 条件表达式






      * if/else/then

    
    mySignum x =
        if x < 0 then 
            -1
        else if x > 0 then 
            1
        else 
            0



      * case语句

    
    f x =
        case x of
          0 -> 1
          1 -> 5
          2 -> 2
          _ -> (-1)
    
    "_"为“通配符”表示任何值都可以符合这个条件







### 缩进






      * 上面的代码中缩进是非常重要的。
      * Haskell 使用一个叫“layout"的布局系统对程序的代码进行维护（Python 语言也使用一个相似的系统）。这个布局系统允许我们可以不需要像C,Java语言那样加分号跟花括号来对代码段进行分割。






### 为不同参数定义一个函数(分段函数)




    
    f 0 = 1
    f 1 = 5
    f 2 = 2
    f _ = -1






      * **该定义与顺序有关，如果把f _ = -1放在最前面，那么无论输入何值，都会得到-1**






### 函数合成






      * 函数合成就是把一个函数的结果作为另一个函数的参数。
      * 函数的这种合成方式普遍存在于其它编程语言中。在Haskell中有另外一种更数学化的表达方法：(`.`) 点函数。点函数源于数学中的(![{\displaystyle \circ }](https://wikimedia.org/api/rest_v1/media/math/render/svg/99add39d2b681e2de7ff62422c32704a05c7ec31)
)符号。
      * 在数学里我们用表达式 ![{\displaystyle f\circ g}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b2f61ca7838709fbae07dce9c0d513770f10cfae)
 表达 "f following g." 在Haskell , 代码`f . g` 也表达为 "f following g."其中![{\displaystyle f\circ g}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b2f61ca7838709fbae07dce9c0d513770f10cfae)
 等同于 ![{\displaystyle (f\circ g)(x)=f(g(x))}](https://wikimedia.org/api/rest_v1/media/math/render/svg/09bac32279e79498a14c3f27741d08cf59aac1b3)
。




### let绑定(类似局部变量)



要求![{\displaystyle x={\frac {-b\pm {\sqrt {b^{2}-4ac}}}{2a}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/00c22777378f9c594c71158fea8946f2495f2a28)



    
    roots a b c =
        ((-b + sqrt(b*b - 4*a*c)) / (2*a),
         (-b - sqrt(b*b - 4*a*c)) / (2*a))




    
    roots a b c =
        let disc = sqrt (b*b - 4*a*c)
        in  ((-b + disc) / (2*a),
             (-b - disc) / (2*a))




    
    roots a b c =
        let disc = sqrt (b*b - 4*a*c)
            twice_a = 2*a
        in  ((-b + disc) / twice_a,
             (-b - disc) / twice_a)













参考资料：[wibibooks_Haskell](https://zh.wikibooks.org/zh-cn/Haskell)

[Haskell 趣学指南](http://fleurer-lee.com/lyah/)


