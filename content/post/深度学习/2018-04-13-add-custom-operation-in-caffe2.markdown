---
author: 111qqz
date: 2018-04-13 03:08:19+00:00
draft: false
title: caffe2 添加自定义operater
type: post
url: /2018/04/add-custom-operation-in-caffe2/
categories:
- deep-learning
tags:
- caffe2
---

记录一些一个没有之前没有接触过caffe/caffe2的人为了添加自定义的op 到caffe2需要做的工作.

首先参考caffe2 tutorial,随便跑个op来试试,不妨以比较简单的  [Accumulate_op](https://caffe2.ai/docs/operators-catalogue.html#accumulate) 为例子.

这个op的作用就是计算Y=X+gamma*Y, 其中X为输入,Y为输出,gamma是参数.

跑起来这个运算所需要的代码如下:

    
    from caffe2.python import workspace, model_helper
    import numpy as np
    # Create the input data
    data = np.arange(6).reshape(2,3).astype(np.float32)
    print ("data=",data)
    
    # Create labels for the data as integers [0, 9].
    
    workspace.FeedBlob("data", data)
    # Create model using a model helper
    m = model_helper.ModelHelper(name="my first net")
    output = m.net.Accumulate(["data"], "output")
    print(m.net.Proto())
    workspace.RunNetOnce(m.param_init_net)
    workspace.CreateNet(m.net)
    workspace.RunNet(m.name,2)  # run 2 times
    print("output=",workspace.FetchBlob('output'))
    
    


c之后我们仿照caffe2/operators/accumultate_op.h和affe2/operators/accumultate_op.cc,仿写一个我们自己的运算atest_op.h和atest_op.cc

实现的功能为Y=5*X+gamma*Y

    
     
    #include "caffe2/operators/atest_op.h"
     
    namespace caffe2 {
    REGISTER_CPU_OPERATOR(Atest, AtestOp<float, CPUContext>);
     
    OPERATOR_SCHEMA(Atest)
     .NumInputs(1)
     .NumOutputs(1)
     .IdenticalTypeAndShape()
     .SetDoc(R"DOC(
    Accumulate operator accumulates the input tensor to the output tensor. If the
    output tensor already has the right size, we add to it; otherwise, we first
    initialize the output tensor to all zeros, and then do accumulation. Any
    further calls to the operator, given that no one else fiddles with the output
    in the interim, will do simple accumulations.
    Accumulation is done using Axpby operation as shown:
     Y = 1*X + gamma*Y
    where X is the input tensor, Y is the output tensor and gamma is the multiplier
    argument.
    )DOC")
     .Arg("gamma", "(float, default 1.0) Accumulation multiplier")
     .Input(0, "input", "The input tensor that has to be accumulated to the "
     "output tensor. If the output size is not the same as input size, the "
     "output tensor is first reshaped and initialized to zero, and only "
     "then, accumulation is done.")
     .Output(0, "output", "Accumulated output tensor");
     
    SHOULD_NOT_DO_GRADIENT(Atest);
    } // namespace caffe2
    



    
    #ifndef CAFFE2_OPERATORS_ATEST_OP_H_
    #define CAFFE2_OPERATORS_ATEST_OP_H_
     
    #include "caffe2/core/context.h"
    #include "caffe2/core/operator.h"
    #include "caffe2/utils/math.h"
     
    namespace caffe2 {
     
    template <typename T, class Context>
    class AtestOp final : public Operator<Context> {
     public:
     AtestOp(const OperatorDef& operator_def, Workspace* ws)
     : Operator<Context>(operator_def, ws),
     gamma_(static_cast<T>(
     OperatorBase::template GetSingleArgument<float>("gamma", 1.0))) {}
     USE_OPERATOR_CONTEXT_FUNCTIONS;
     
     bool RunOnDevice() override {
     auto& input = Input(0);
     auto* output = Output(0);
     if (output->dims() != input.dims()) {
     LOG(INFO) << "Reshaping and initializing output.";
     output->ResizeLike(input);
     math::Set<T, Context>(
     output->size(), 0, output->template mutable_data<T>(), &context_);
     }
     math::Axpby<T, Context>(
     input.size(),
     static_cast<T>(5),
     input.template data<T>(),
     gamma_,
     output->template mutable_data<T>(),
     &context_);
     return true;
     }
     
     protected:
     T gamma_;
    };
     
    } // namespace caffe2
     
    #endif // CAFFE2_OPERATORS_Atest_OP_H_
     
    


之后我们编译整个caffe2,编译方式是运行pytorch/scripts/build_local.sh

编译成功后,需要将pytorch目录添加到PYTHONPATH中

    
    export PYTHONPATH=$PYTHONPATH:/mnt/lustre/renkuanze/workspace/rjm_pytorch


然后运行

    
    cd ~ && python -c 'from caffe2.python import core' 2>/dev/null && echo "Success" || echo "Failure"


看是否成功

编译的时候可能出现[mpi_test.cc.o: undefined reference to symbol '_ZN3MPI8Datatype4FreeEv](https://github.com/caffe2/caffe2/issues/2144)  的报错。。解决办法是把CMakeList中的MPI关掉就好了。。。

**以及。。。operators中的文件都不要删。。。本想删一些不相关的op来减少编译时间。。。想法是对的。。。但是似乎只删op是行不通的。。。。不如不删。。。不然会编译出现奇怪的错误！**

**不然会编译出现奇怪的错误！**

**不然会编译出现奇怪的错误！**

以及。。。从github download的速度太慢了。。。干脆开了个40$/m的vps来搞。。。

编译成功后修改测试的python代码，来测试一下我们定义的op

    
    from caffe2.python import workspace, model_helper
    import numpy as np
    # Create the input data
    data = np.arange(6).reshape(2,3).astype(np.float32)
    print ("data=",data)
     
    # Create labels for the data as integers [0, 9].
     
    workspace.FeedBlob("data", data)
    # Create model using a model helper
    m = model_helper.ModelHelper(name="my first net")
    output = m.net.Atest(["data"], "output")
    print(m.net.Proto())
    workspace.RunNetOnce(m.param_init_net)
    workspace.CreateNet(m.net)
    workspace.RunNet(m.name,1)  # run 2 times
    print("output=",workspace.FetchBlob('output'))
    


发现确实是得到了Y=5*X+gamma*Y 的结果。。

撒花！（然而这只是最近要做的任务中最容易的一条线orz...

需要注意的是,运行bash build_local.sh脚本之后会在pytorch目录下生成build文件夹,下次**编译的时候直接在build目录下执行make -j20,这样才是增量编译**

**编译的时候直接在build目录下执行make -j20,这样才是增量编译**

**编译的时候直接在build目录下执行make -j20,这样才是增量编译**

不然每次执行build_local.sh...不知caffe2用了什么机制...每次要把所有文件编译一遍...简直没有人性啊...16个cpu一起编也要5分钟Orz

以及．．．要在自己定义的函数最后返回true...这样在运行的时候才不会报错．否则会报net error 的错误Ｏｒｚ....我好傻啊？












