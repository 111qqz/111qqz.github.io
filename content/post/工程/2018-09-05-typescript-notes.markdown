---
author: 111qqz
date: 2018-09-05 08:02:42+00:00
draft: false
title: typescript学习笔记
type: post
url: /2018/09/typescript-notes/
categories:
- 其他
tags:
- typescript
- 前端
---

先放参考资料:

[TypeScript 入门教程](https://ts.xcatliu.com/)

[React & Webpack](http://www.typescriptlang.org/docs/handbook/react-&-webpack.html)

[react-typescript-cheatsheet ](https://github.com/sw-yx/react-typescript-cheatsheet/blob/master/README.md)(强推一波，讲了很多react+ts的实践）

typescript是javascript的语法扩展。。。好处是提供了类型。。可以在编译（结果为js文件)的时候提供静态的类型检查。。。

typescript的问号语法:标记某个参数为可选。

例子:

    
    export class Thread {
      id: string;
      lastMessage: Message;
      name: string;
      avatarSrc: string;
    
      constructor(id?: string,
                  name?: string,
                  avatarSrc?: string) {
        this.id = id || uuid();
        this.name = name;
        this.avatarSrc = avatarSrc;
      }
    }




关于typescript的类型推断。。如果在定义时直接赋值则会进行推断，否则会推断类型为any.

    
    let myFavoriteNumber = 'seven';
    myFavoriteNumber = 7;
    
    // index.ts(2,1): error TS2322: Type 'number' is not assignable to type 'string'.
    //上面的写法会编译错误，原因是定义时已经推断类型为string
    //但是下面的写法没有问题
    
    let myFavoriteNumber;
    myFavoriteNumber = 'seven';
    myFavoriteNumber = 7;




    
    let myFavoriteNumber: string | number;
    myFavoriteNumber = 'seven';
    myFavoriteNumber = 7;
    
    这里的 let myFavoriteNumber: string | number 的含义是，
    允许 myFavoriteNumber 的类型是 string 或者 number，但是不能是其他类型。


当 TypeScript 不确定一个联合类型的变量到底是哪个类型的时候，我们**只能访问此联合类型的所有类型里共有的属性或方法**

    
    function getLength(something: string | number): number {
        return something.length;
    }
    
    // index.ts(2,22): error TS2339: Property 'length' does not exist on type 'string | number'.
    //   Property 'length' does not exist on type 'number'.


类型断言:

    
    functionf  getLength(something: string | number): number {
        if ((<string>something).length) {
            return (<string>something).length;
        } else {
            return something.toString().length;
        }
    }


**类型断言不是类型转换，断言成一个联合类型中不存在的类型是不允许的**

泛型:

    
    function createArray<T>(length: number, value: T): Array<T> {
        let result: T[] = [];
        for (let i = 0; i < length; i++) {
            result[i] = value;
        }
        return result;
    }
    
    createArray<string>(3, 'x'); // ['x', 'x', 'x']



    
    function swap<T, U>(tuple: [T, U]): [U, T] {
        return [tuple[1], tuple[0]];
    }
    
    swap([7, 'seven']); // ['seven', 7]


泛型约束:传入的模板参数必须包含接口的形状:

    
    interface Lengthwise {
        length: number;
    }
    
    function loggingIdentity<T extends Lengthwise>(arg: T): T {
        console.log(arg.length);
        return arg;
    }


上面的代码表示，传入的参数必须包含一个类型为number，**名字为length的属性**

这里要强调的是，这里名字是重要的。如果把length改为其他名字，将不能通过编译。



定义一个普通的class属性（不是props)的办法:

在构造函数之前声明即可，参考如下代码中的pointer:number

    
    class App extends React.Component<{
      message: string,
    }> {
      pointer: number // like this
      componentDidMount() {
        this.pointer = 3;
      }
      render() {
        return (
          <div>{this.props.message} and {this.pointer}</div>
        );
      }
    }

























