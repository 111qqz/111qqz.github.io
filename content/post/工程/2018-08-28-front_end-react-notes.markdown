---
author: 111qqz
date: 2018-08-28 10:16:16+00:00
draft: false
title: react学习笔记
type: post
url: /2018/08/react-notes/
categories:
- 其他
tags:
- react
- 前端
---

首先介绍一个fb家的快速开发react的工具 [create-react-app](https://github.com/facebook/create-react-app)

这个东西依赖node6.0或者更高版本。

关于在ubuntu 14.04上安装node ，可以参考[这个链接](https://www.hostingadvice.com/how-to/install-nodejs-ubuntu-14-04/#node-version-manager)

发现执行nvm install 6.0会没有任何相应...但是实际上已经安装好了。

接下来安装create-react-app

命令是: npm install --global create-react-app

然后创建一个react app

命令为:create-react-app first_react_app

挂着代理大概需要半小时左右。

或者可以使用淘宝npm镜像:

设置方法为：`npm config set registry https://registry.npm.taobao.org`，设置完成后，重新执行`create-react-app first-app`

实现的第一个组件，功能是点击按钮增加计数...

    
    import React, { Component } from 'react';
    class ClickCounter extends Component{
        constructor(props){
            super(props);
            this.onClickButton = this.onClickButton.bind(this);
            this.state = {count:0};
        }
        onClickButton(){
            this.setState({count: this.state.count+1});
        }
    
        render(){
            return(
                <div>
                    <button onClick={this.onClickButton}>Who am I?</button>
                    <div>
                        click Count: {this.state.count}
                    </div>
                </div>
    
            )
        }
    }
    export default ClickCounter;




JSX是JS的语法扩展。JSX中使用的元素包含html中的元素和React中的组件。React 判断一个元素是 HTML 元素还是 React 组件的原则就是看第一个字母是否大
写。

React设计上的分离是逻辑上的分离，而不是技术上的分离。如果是要实现一件事，就会把CSS,html,JS三种语言混在一起。

React的数据分为prop(property)和state两种。区别是:



 	  * prop 用于定义外部接口, state 用于记录内部状态;
 	  * prop 的赋值在外部世界使用组件时, state 的赋值在组件内部;
 	  * 组件不应该改变 prop 的值,而 state 存在的目的就是让组件来改变的



扩展属性:

    
    function App1() {
      return <Greeting firstName="Ben" lastName="Hector" />;
    }
    
    function App2() {
      const props = {firstName: 'Ben', lastName: 'Hector'};
      return <Greeting {...props} />;
    }




[react父组件获得子组件的值](https://segmentfault.com/q/1010000007295553)





参考资料:

[react.express](http://www.react.express)

[React + antd怎么上传图片](http://react-china.org/t/react-antd/6462/3)












