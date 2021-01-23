---
author: 111qqz
date: 2018-08-30 03:42:19+00:00
draft: false
title: JavaScript 学习笔记
type: post
url: /2018/08/javascript-notes/
categories:
- 其他
tags:
- JavaScript
- 前端
---

<del>暂时没空从头开始搞...用到哪里先记录一下好了orz</del>

我觉得不行，还是要先大致了解一下。

参考资料:

[A re-introduction to JavaScript (JS tutorial)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

[继承与原型链](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

    
    // 让我们假设我们有一个对象 o, 其有自己的属性 a 和 b：
    // {a: 1, b: 2}
    // o 的 [[Prototype]] 有属性 b 和 c：
    // {b: 3, c: 4}
    // 最后, o.[[Prototype]].[[Prototype]] 是 null.
    // 这就是原型链的末尾，即 null，
    // 根据定义，null 没有[[Prototype]].
    // 综上，整个原型链如下: 
    // {a:1, b:2} ---> {b:3, c:4} ---> null
    
    console.log(o.a); // 1
    // a是o的自身属性吗？是的，该属性的值为1
    
    console.log(o.b); // 2
    // b是o的自身属性吗？是的，该属性的值为2
    // 原型上也有一个'b'属性,但是它不会被访问到.这种情况称为"属性遮蔽 (property shadowing)"
    
    console.log(o.c); // 4
    // c是o的自身属性吗？不是，那看看原型上有没有
    // c是o.[[Prototype]]的属性吗？是的，该属性的值为4
    
    console.log(o.d); // undefined
    // d是o的自身属性吗？不是,那看看原型上有没有
    // d是o.[[Prototype]]的属性吗？不是，那看看它的原型上有没有
    // o.[[Prototype]].[[Prototype]] 为 null，停止搜索
    // 没有d属性，返回undefined



    
     hasOwnProperty方法,用来检查对象是否有自己定义的属性，而不是从原型链上继承的属性。
    该方法不需要遍历原型链。
    function Graph() {
      this.vertices = [];
      this.edges = [];
    }
    
    Graph.prototype = {
      addVertex: function(v){
        this.vertices.push(v);
      }
    };
    
    console.log(g.hasOwnProperty('vertices'));
    // true
    
    console.log(g.hasOwnProperty('nope'));
    // false
    
    console.log(g.hasOwnProperty('addVertex'));
    // false
    
    console.log(g.__proto__.hasOwnProperty('addVertex'));
    // true
    
    var g = new Graph();
    // g是生成的对象,他的自身属性有'vertices'和'edges'.
    // 在g被实例化时,g.[[Prototype]]指向了Graph.prototype.




    
    const array1 = [1, 2, 3, 4];
    const reducer = (accumulator, currentValue) => accumulator + currentValue;
    
    // 1 + 2 + 3 + 4
    console.log(array1.reduce(reducer));
    // expected output: 10
    
    // 5 + 1 + 2 + 3 + 4
    console.log(array1.reduce(reducer, 5));
    // expected output: 15



    
    const object1 = {
      a: 1,
      b: 2,
      c: 3,
      a: 4
    };
    
    const object2 = Object.assign({a: 14, d: 5,h:12}, object1);
    
    console.log(object2.a, object2.d,object2.h);
    // expected output: 1 5 12
    // Properties in the target object will be overwritten by properties in the sources if they have the same key. 
    //Later sources' properties will similarly overwrite earlier ones.
    



    
    function multiply(multiplier, ...theArgs) {
      return theArgs.map(function (element) {
        return multiplier * element;
      });
    }
    
    var arr = multiply(2, 1, 2, 3); 
    console.log(arr);  // [2, 4, 6]



    
    function parentFunc() {
      var a = 1;
    
      function nestedFunc() {
        var b = 4; // parentFunc can't use this
        return a + b; 
      }
      return nestedFunc(); // 5
    }



    
    (参数1, 参数2, …, 参数N) => { 函数声明 }
    (参数1, 参数2, …, 参数N) => 表达式（单一）
    //相当于：(参数1, 参数2, …, 参数N) =>{ return 表达式; }
    
    // 当只有一个参数时，圆括号是可选的：
    (单一参数) => {函数声明}
    单一参数 => {函数声明}
    
    // 没有参数的函数应该写成一对圆括号。
    () => {函数声明}
    
    var materials = [
      'Hydrogen',
      'Helium',
      'Lithium',
      'Beryllium'
    ];
    
    materials.map(function(material) { 
      return material.length; 
    }); // [8, 6, 7, 9]
    
    materials.map((material) => {
      return material.length;
    }); // [8, 6, 7, 9]
    
    materials.map(material => material.length); // [8, 6, 7, 9]



    
    class ChildClass extends ParentClass { ... }

















