---
author: 111qqz
date: 2018-09-09 11:28:53+00:00
draft: false
title: '[C++11 ] std::ref&&std::reference_wrapper  notes'
type: post
url: /2018/09/reference_wrapper-notes/
categories:
- 其他
tags:
- c++11
---

起因是在看《CplusplusConcurrencyInAction_PracticalMultithreading》的时候，里面讲到初始化std::thread的时候，如果thread funtion的参数列表中有引用，需要传入std::ref才可以得到符合预期的结果。

查阅发现std::ref是用来生成std::reference_wrapper。 按照 [cppreference](https://zh.cppreference.com/w/cpp/utility/functional/reference_wrapper) 上的话来说


<blockquote>`std::reference_wrapper` 是包装引用于可复制、可赋值对象的类模板。它常用作将容器存储入无法正常保有引用的标准容器（类似 [std::vector](https://zh.cppreference.com/w/cpp/container/vector) ）的机制。</blockquote>


用人话来说，就是有的时候一些地方（比如STL容器中传值，又比如std::bind）会默认使用复制，这可能与我们想使用引用的期望不符。

具体见下面的几个例子：

    
    #include <functional>
    #include <iostream>
     
    void f(int& n1, int& n2, const int& n3)
    {
        std::cout << "In function: " << n1 << ' ' << n2 << ' ' << n3 << '\n';
        ++n1; // increments the copy of n1 stored in the function object
        ++n2; // increments the main()'s n2
        // ++n3; // compile error
    }
     
    int main()
    {
        int n1 = 1, n2 = 2, n3 = 3;
        std::function<void()> bound_f = std::bind(f, n1, std::ref(n2), std::cref(n3));
        n1 = 10;
        n2 = 11;
        n3 = 12;
        std::cout << "Before function: " << n1 << ' ' << n2 << ' ' << n3 << '\n';
        bound_f();
        std::cout << "After function: " << n1 << ' ' << n2 << ' ' << n3 << '\n';
    }
    
    Before function: 10 11 12
    In function: 1 11 12
    After function: 10 12 12


我们发现直接传进去的参数n1的值没有改变，而使用std::ref传进去的值的结果符合预期。

n1的值不符合预期的原因是，在调用std::bind的时候，会先将参数复制一份，然后传入函数f时，传入的不是在main函数中定义的n1的引用，而是对n1复制了一份得到的临时变量的引用。在函数f中对n1的修改只会使得n1的复制值与其保持一致，而不会改变n1.

下面是一个关于`std::reference_wrapper 的例子`

    
    #include <algorithm>
    #include <list>
    #include <vector>
    #include <iostream>
    #include <numeric>
    #include <random>
    #include <functional>
     
    int main()
    {
        std::list<int> l(10);
        std::iota(l.begin(), l.end(), -4);
     
        std::vector<std::reference_wrapper<int>> v(l.begin(), l.end());
        // 不能在 list 上用 shuffle （要求随机访问），但能在 vector 上使用它
        std::shuffle(v.begin(), v.end(), std::mt19937{std::random_device{}()});
     
        std::cout << "Contents of the list: ";
        for (int n : l) std::cout << n << ' '; std::cout << '\n';
     
        std::cout << "Contents of the list, as seen through a shuffled vector: ";
        for (int i : v) std::cout << i << ' '; std::cout << '\n';
     
        std::cout << "Doubling the values in the initial list...\n";
        for (int& i : l) {
            i *= 2;
        }
     
        std::cout << "Contents of the list, as seen through a shuffled vector: ";
        for (int i : v) std::cout << i << ' '; std::cout << '\n';
    }
    
    
    Contents of the list: -4 -3 -2 -1 0 1 2 3 4 5 
    Contents of the list, as seen through a shuffled vector: -1 2 -2 1 5 0 3 -3 -4 4 
    Doubling the values in the initial list...
    Contents of the list, as seen through a shuffled vector: -2 4 -4 2 10 0 6 -6 -8 8




最后我们回到开始，将参数在通过创建std::thread传给thread funtion的时候，参数默认情况下仍然是被拷贝了一份，与上面std::bind的情况类似，因此需要使用std::ref



参考资料:



 	  * 《CplusplusConcurrencyInAction_PracticalMultithreading》2.2节
 	  * [std::ref](https://zh.cppreference.com/w/cpp/utility/functional/ref)
 	  * [std::reference_wrapper](https://zh.cppreference.com/w/cpp/utility/functional/reference_wrapper)
 	  * [C++ Difference between std::ref(T) and T&?](https://stackoverflow.com/questions/33240993/c-difference-between-stdreft-and-t)
 	  * 








