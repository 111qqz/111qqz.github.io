---
author: 111qqz
date: 2018-05-06 09:45:50+00:00
draft: false
title: C++ STL Algotithms 学习笔记
type: post
url: /2018/05/c-stl-algotithms-notes/
categories:
- 其他
tags:
- c++
- stl
---

迫于拙劣的cpp水平，这次来记录一些关于STL算法部分的内容。

参考内容是[CS106L的course reader](http://web.stanford.edu/class/cs106l)


## Iterator Categories


Iterators分为以下五种:



 	  * Output Iterators:可以使用"++"；可以用*myItr = value,不能用value = *myItr
 	  * Input Iterators:可以使用"++";可以用value = *myItr，不能用*myItr = value
 	  * Forward Iterators: 可以使用"++",可以同时用value = *myItr和*myItr = value
 	  * Bidirectional Iterators:比起Forward Iterator 对了"--",但是不能+或者+=
 	  * Random-Access Iterators：比起Bidirectional Iterators多了+和+=



## Algorithm Naming Conventions


一些关于STL Algorithm的命名规则

后缀_if表示只有当满足一定条件的时候该算法才会执行一定任务。

比如:

    
    bool IsEven(int value) {
    return value % 2 == 0;
    }
    cout << count_if(myVec.begin(), myVec.end(), IsEven) << endl;


_n表示执行一个特定的操作n次。

比如:

    
    fill_n(myDeque.begin(), 10, 0);




## Reordering Algorithms





 	  * sort: 传入的必须是Random-Access Iterators，记得定义<函数
 	  * random_shuffle:传入的必须是Random-Access Iterators,作用是将一个区间内的元素打乱重排。 可以在使用之前先使用srand函数。
 	  * rotate：作用是循环改变容器中元素的顺序。rotate(v.begin(), v.begin() + 2, v.end());会让(0, 1, 2, 3, 4, 5)变为(2, 3, 4, 5, 0, 1)



## Searching Algorithms





 	  * find:三个参数，前面连个迭代器表示寻找的范围，第三个参数表示要找的值。返回第一个该值所在的位置的迭代器或者返回第二个迭代器(如果没找到)
 	  * binary_search:需要有序；返回某个值是否在一个范围内。
 	  * lower_bound:需要有序；返回大于等于某值的第一个位置的迭代器。

**需要注意的是，如果某个容器本身有和STL algorithm同名的成员函数(比如set的find）,那么优先使用该容器的成员函数。**原因是STL Algorithm需要就有普适性，不会针对特定容易优化。因此对于set来说，其成员函数的find的复杂度是logn的，而STL alogithm的find是O(n)的复杂度。


## Iterator Adaptors


具有Iterator的性质，但是比Iterator更强..

比如ostream_iterator

通过copy(myVector.begin(), myVector.end(), ostream_iterator<int>(cout, " ")); 可以直接将一个容器中的元素输出。

比如insert_iterator，对于要从一个容器拷贝元素到另一个容器，但是在编写代码时不知道源容器的元素有多少个的问题，可以很好解决？

    
    set<int> result;
    set_union(setOne.begin(), setOne.end(),
    // All of the elements in setOne
    setTwo.begin(), setTwo.end(),
    // All of the elements in setTwo
    inserter(result, result.begin())); // Store in result.




## Removal Algorithms


需要注意的是并没有真的remove,而是将"remove"的元素放在了容器后面（？），原因是STL Algorithms接受的是Iterator，而不是Container.


## Other Noteworthy Algorithms





 	  * transform：四个参数，前两个迭代器表示要变换的范围，第三个迭代器表示结果的开始位置，第四个参数为一个函数，表示将该范围的每个元素经过该函数的处理。不要求结果和原始的数据类型相同。
 	  * min_element：两个迭代器表示一个范围，返回该范围中最小元素的迭代器；可以有第三个参数来自定义小于关系。max_element与之类似。
 	  * accumulate：template< class InputIt, class T > T accumulate( InputIt first, InputIt last, T init );
 	  * inner_product:求内积;T inner_product( InputIt1 first1, InputIt1 last1,
InputIt2 first2, T value );
 	  * distance:连个参数，表示这两个迭代器之间元素的个数。










