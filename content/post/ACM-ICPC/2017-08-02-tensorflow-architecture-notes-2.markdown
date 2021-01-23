---
author: 111qqz
date: 2017-08-02 03:07:37+00:00
draft: false
title: TensorFlow Architecture 学习笔记（二）Adding a New Op
type: post
url: /2017/08/tensorflow-architecture-notes-2/
categories:
- deep-learning
tags:
- tensorflow
---

# Adding a New Op






 	  * [目录](https://www.tensorflow.org/extend/adding_an_op#top_of_page)
 	  * [定义运算的接口](https://www.tensorflow.org/extend/adding_an_op#define_the_ops_interface)
 	  * [实现运算的核心部分(kernels)](https://www.tensorflow.org/extend/adding_an_op#implement_the_kernel_for_the_op)

 	    * [多线程cpu kernels](https://www.tensorflow.org/extend/adding_an_op#multi-threaded_cpu_kernels)
 	    * [GPU kernels](https://www.tensorflow.org/extend/adding_an_op#gpu_kernels)


 	  * [构建运算库](https://www.tensorflow.org/extend/adding_an_op#build_the_op_library)

 	    * [用系统编译器编译你的运算（TensorFlow binary installation）](https://www.tensorflow.org/extend/adding_an_op#compile_the_op_using_your_system_compiler_tensorflow_binary_installation)
 	    * [使用bazel编译你的运算(TensorFlow source installation)](https://www.tensorflow.org/extend/adding_an_op#compile_the_op_using_bazel_tensorflow_source_installation)


 	  * [在 Python 中使用你的运算](https://www.tensorflow.org/extend/adding_an_op#use_the_op_in_python)
 	  * [验证你添加的运算可以工作](https://www.tensorflow.org/extend/adding_an_op#verify_that_the_op_works)
 	  * [在你的运算中添加高级特性](https://www.tensorflow.org/extend/adding_an_op#building_advanced_features_into_your_op)

 	    * [条件检查和验证](https://www.tensorflow.org/extend/adding_an_op#conditional_checks_and_validation)
 	    * [Op registration](https://www.tensorflow.org/extend/adding_an_op#op_registration)
 	    * [GPU Support](https://www.tensorflow.org/extend/adding_an_op#gpu_support)
 	    * [用python 实现梯度](https://www.tensorflow.org/extend/adding_an_op#implement_the_gradient_in_python)
 	    * [Shape functions in C++](https://www.tensorflow.org/extend/adding_an_op#shape_functions_in_c)



对于要添加原生tensorflow中没有定义的运算的需求，首先建议在python层面，能不能将需要的op用其他原生的op拼凑起来。

如果不能这样做，或者这样做逻辑很复杂，或者这样做效率比较低的时候，我们才考虑在cpp层面添加一个新的op

去实现你自定义的运算需要如下步骤：

 	  1. 在C++文件中注册该运算。包含参数个数，类型，返回值类型，运算名称等。大概就是C++头文件中函数的定义吧.同时在此处也要定义shape function
 	  2. 用C++实现该运算，运算的实现被称之为kernel，该实现与第一步中的注册对应，相同功能的op对于不同的输入输出类型，或者是架构（GPU,CPU)可能 有不同的实现.
 	  3. 创建一个python包装器（**可选**），该包装器使得可以在python层面用API对该运算进行调用。在运算注册阶段会生成默认的包装器
 	  4. 编写计算该运算梯度 的函数**（可选）**
 	  5. 测试你新添加的运算。为了方便一般在python层面进行测试，不过你想在C++层面测试也没什么问题。



## Define the op's interface


直接看代码好了...

发现提供了REGISTER_OP的宏来帮助定义...

    
    #include "tensorflow/core/framework/op.h"
    #include "tensorflow/core/framework/shape_inference.h"
    
    using namespace tensorflow;
    
    REGISTER_OP("ZeroOut")
        .Input("to_zero: int32")
        .Output("zeroed: int32")
        .SetShapeFn([](::tensorflow::shape_inference::InferenceContext* c) {
          c->set_output(0, c->input(0));
          return Status::OK();
        });
    // REGISTER_OP("my_op_name")
    //     .Attr(":")
    //     .Attr(":=")
    //     .Input(":")
    //     .Input(":Ref()")
    //     .Output(":")
    //     .Doc(R"(
    // 
    // 
    // : 
    // : 
    // )");
    //
    // Note: .Doc() should be last.
    // For details, see the OpDefBuilder class in op_def_builder.h.



    
    /* Copyright 2015 Google Inc. All Rights Reserved.
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    ==============================================================================*/
    
    // Class and associated machinery for specifying an Op's OpDef for Op
    // registration.
    
    #ifndef TENSORFLOW_FRAMEWORK_OP_DEF_BUILDER_H_
    #define TENSORFLOW_FRAMEWORK_OP_DEF_BUILDER_H_
    
    #include <string>
    #include <vector>
    #include "tensorflow/core/framework/op_def.pb.h"
    #include "tensorflow/core/lib/core/status.h"
    #include "tensorflow/core/lib/core/stringpiece.h"
    
    namespace tensorflow {
    
    // Builder class passed to the REGISTER_OP() macro.
    class OpDefBuilder {
     public:
      // Constructs an OpDef with just the name field set.
      explicit OpDefBuilder(StringPiece op_name);
    
      // Adds an attr to this OpDefBuilder (and returns *this). The spec has
      // format "<name>:<type>" or "<name>:<type>=<default>"
      // where <name> matches regexp [a-zA-Z][a-zA-Z0-9_]*
      // (by convention only using capital letters for attrs that can be inferred)
      // <type> can be:
      //   "string", "int", "float", "bool", "type", "shape", or "tensor"
      //   "numbertype", "realnumbertype", "quantizedtype", "{int32,int64}"
      //       (meaning "type" with a restriction on valid values)
      //   "{\"foo\", \"bar\n baz\"}", or "{'foo', 'bar\n baz'}"
      //       (meaning "string" with a restriction on valid values)
      //   "list(string)", ..., "list(tensor)", "list(numbertype)", ...
      //       (meaning lists of the above types)
      //   "int >= 2" (meaning "int" with a restriction on valid values)
      //   "list(string) >= 2", "list(int) >= 2"
      //       (meaning "list(string)" / "list(int)" with length at least 2)
      // <default>, if included, should use the Proto text format
      // of <type>.  For lists use [a, b, c] format.
      //
      // Note that any attr specifying the length of an input or output will
      // get a default minimum of 1 unless the >= # syntax is used.
      //
      // TODO(josh11b): Perhaps support restrictions and defaults as optional
      // extra arguments to Attr() instead of encoding them in the spec string.
      // TODO(josh11b): Would like to have better dtype handling for tensor attrs:
      // * Ability to say the type of an input/output matches the type of
      //   the tensor.
      // * Ability to restrict the type of the tensor like the existing
      //   restrictions for type attrs.
      // Perhaps by linking the type of the tensor to a type attr?
      OpDefBuilder& Attr(StringPiece spec);
    
      // Adds an input or output to this OpDefBuilder (and returns *this).
      // The spec has form "<name>:<type-expr>" or "<name>:Ref(<type-expr>)"
      // where <name> matches regexp [a-z][a-z0-9_]* and <type-expr> can be:
      // * For a single tensor: <type>
      // * For a sequence of tensors with the same type: <number>*<type>
      // * For a sequence of tensors with different types: <type-list>
      // Where:
      //   <type> is either one of "float", "int32", "string", ...
      //                 or the name of an attr (see above) with type "type".
      //   <number> is the name of an attr with type "int".
      //   <type-list> is the name of an attr with type "list(type)".
      // TODO(josh11b): Indicate Ref() via an optional argument instead of
      // in the spec?
      // TODO(josh11b): SparseInput() and SparseOutput() matching the Python
      // handling?
      OpDefBuilder& Input(StringPiece spec);
      OpDefBuilder& Output(StringPiece spec);
    
      // Turns on the indicated boolean flag in this OpDefBuilder (and
      // returns *this).
      OpDefBuilder& SetIsCommutative();
      OpDefBuilder& SetIsAggregate();
      OpDefBuilder& SetIsStateful();
      OpDefBuilder& SetAllowsUninitializedInput();
    
      // Deprecate the op at a certain GraphDef version.
      OpDefBuilder& Deprecated(int version, StringPiece explanation);
    
      // Adds docs to this OpDefBuilder (and returns *this).
      // Docs have the format:
      //   <1-line summary>
      //   <rest of the description>
      //   <name>: <description of name>
      //   <name>: <description of name>
      //     <if long, indent the description on subsequent lines>
      // Where <name> is the name of an attr, input, or output.  Please
      // wrap docs at 72 columns so that it may be indented in the
      // generated output.  For tensor inputs or outputs (not attrs), you
      // may start the description with an "=" (like name:= <description>)
      // to suppress the automatically-generated type documentation in
      // generated output.
    #ifndef TF_LEAN_BINARY
      OpDefBuilder& Doc(StringPiece text);
    #else
      OpDefBuilder& Doc(StringPiece text) { return *this; }
    #endif
    
      // Sets *op_def to the requested OpDef, or returns an error.
      // Must be called after all of the above methods.
      // Note that OpDefBuilder only reports parsing errors.  You should also
      // call ValidateOpDef() to detect other problems.
      Status Finalize(OpDef* op_def) const;
    
     private:
      OpDef op_def_;
      std::vector<string> attrs_;
      std::vector<string> inputs_;
      std::vector<string> outputs_;
      string doc_;
      std::vector<string> errors_;
    };
    
    }  // namespace tensorflow


**需要注意运算(op)的明明需要遵循驼峰命名法**




# Implement the kernel for the op



    
    #include "tensorflow/core/framework/op_kernel.h"
    
    using namespace tensorflow;
    
    class ZeroOutOp : public OpKernel {
     public:
      explicit ZeroOutOp(OpKernelConstruction* context) : OpKernel(context) {}
    
      void Compute(OpKernelContext* context) override {
        // Grab the input tensor
        const Tensor& input_tensor = context->input(0);
        auto input = input_tensor.flat<int32>();
    
        // Create an output tensor
        Tensor* output_tensor = NULL;
        OP_REQUIRES_OK(context, context->allocate_output(0, input_tensor.shape(),
                                                         &output_tensor));
        auto output_flat = output_tensor->flat<int32>();
    
        // Set all but the first element of the output tensor to 0.
        const int N = input.size();
        for (int i = 1; i < N; i++) {
          output_flat(i) = 0;
        }
    
        // Preserve the first input value if possible.
        if (N > 0) output_flat(0) = input(0);
      }
    };


需要注意的是，你定义的运算的kernel可能被并行地访问，所以要求`Compute` method 一定是线程安全的。

可以通过添加互斥锁(c++11?)或者完全就不要通过类成员来共享状态。

可以使用 [`ResourceMgr`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/core/framework/resource_mgr.h) 来追踪运算的状态。




## Multi-threaded CPU kernels


要实现多线程cpu版本的kernel,可以参考 [`work_sharder.h`](https://www.github.com/tensorflow/tensorflow/blob/r1.2/tensorflow/core/framework/work_sharder.h)


## GPU kernels


-----先忙手头工作了，有时间再更orz








