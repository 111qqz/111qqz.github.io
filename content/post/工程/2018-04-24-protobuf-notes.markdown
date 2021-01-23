---
author: 111qqz
date: 2018-04-24 03:05:09+00:00
draft: false
title: protobuf学习笔记
type: post
url: /2018/04/protobuf-notes/
categories:
- 其他
tags:
- protobuf
---

Protobuff 是一种轻便高效的结构化数据存储格式，可以用于结构化数据序列化。它很适合做数据存储或 RPC 数据交换格式。可用于通讯协议、数据存储等领域的语言无关、平台无关、可扩展的序列化结构数据格式。

之前由于要用levelDB存feature,而levelDB的key只能是string(?,反正不能是一个数组)， 使用了protobuf. protobuf本身还比较easy,不过目前似乎protobuf2仍然是主流，但是由于最近在看gRPC的缘故，要使用protobuf3.　如果protobuf2没有卸载干净，绝对欲仙欲死...记录一些坑．详细一点的笔记之后补．

<del>// protobuf3坑好多啊...语法全靠猜，也是有毒 </del>

<del>行吧，怪我没找到orz,生成的cpp语法部分在 [这里](https://developers.google.com/protocol-buffers/docs/reference/cpp-generated)。</del>

先放参考资料好了。一开始找到一个pdf文档，说是官方文档的翻译版...但实际上感觉，讲得很烂。直接看官方文档比较好。

其中[ Language Guide (proto3)](https://developers.google.com/protocol-buffers/docs/proto3) 讲了protobuf3的proto文件的语法相关。

[ Protocol Buffer Basics: C++](https://developers.google.com/protocol-buffers/docs/cpptutorial) 讲了怎么从编写proto文件到在cpp中使用的一般步骤（注意此处貌似是按照protobuf2讲的）

[ C++ Generated Code](https://developers.google.com/protocol-buffers/docs/reference/cpp-generated) 讲了生成的cpp代码的接口，并且强调了protobuf2和protobuf3的区别。

    
    syntax = "proto3";
    package test;
    message Feature
    {
        int32 ver = 1;
        int32 idx = 2;
        int32 len = 3;
        repeated float feat = 4;
    }
    
    


生成相应代码的语法为: protoc  --cpp_out=.    test.proto

    
    #include <iostream>
    #include <cassert>
    #include <cstdlib>
    #include <string>
    #include  <vector>
    #include "test.pb.h"
    
    using namespace std;
    
    using namespace test;
    int main()
    {
    	 
    	float arr[10]={4,5,6,7,8,9};
    	Feature feature;
            puts("def feature");
    	float ft;
    	for ( int i = 0 ; i < 4 ; i++)
    	{
                feature.add_feat(arr[i]);
    	    //feature.set_feat(3,arr[i]);
                cout<<"arr[i]:"<<arr[i]<<endl;
    	}
    	for ( int i = 0 ; i < feature.feat_size() ; i++)
    	{
    	    float ftval = feature.feat(i);
    	    cout<<i+1<<" "<<ftval<<endl;
    	}
    
    
    
    	return 0;
    }


编译选项为:g++ mytest.cc test.pb.cc -o test -lprotobuf

可能遇到这个问题

[Undefined reference to google protobuf](https://github.com/BVLC/caffe/issues/3046)

解决办法是卸载掉系统自带的protobuf相关（ubuntu14.04默认还都是protbuf2,protobuf3我是从源码自己编译的）
apt-get remove libprotobuf-dev



如果X是单个的变量，那么语法为set_X(val)

如果X是repeated类型，语法为add_X(val)

protobuf中message的嵌套:

对于如下的.proto

    
    syntax = "proto3";
    package test;
    message Feature
    {
        int32 ver = 1;
        int32 idx = 2;
        int32 len = 3;
        repeated float feat = 4;
        message Single
        {
    	int64 xxx = 1;
    	string imagePath=2;
        }
    }
    
    





使用cpp代码访问如下：

    
    #include <iostream>
    #include <cassert>
    #include <cstdlib>
    #include <string>
    #include  <vector>
    #include "test.pb.h"
    
    using namespace std;
    
    using namespace test;
    int main()
    {
    	  
    	Feature_Single single;
    	single.set_imagepath("asdzxcxzc");
            cout<<"imagepath:"<<single.imagepath()<<endl;
    	single.set_xxx(456);
    	cout<<"xxx:"<<single.xxx()<<endl;
    
    	return 0;
    }


需要注意，如果我们想要修改某个class中的另一个class的单个值，需要用mutable_name()方法，而不是name()方法．参考如下例子：

    
    syntax = "proto3";
    package test;
    message Feature
    {
        int32 ver = 1;
        int32 idx = 2;
        int32 len = 3;
        repeated float feat = 4;
        message Single
        {
    	int64 QxXx = 1;
    	string imagePath=2;
        }
        Single sin = 6;
    }
    


Feature里嵌套了一个Single，我现在想修改某个feature中的sin,代码如下：

    
    #include <iostream>
    #include <cassert>
    #include <cstdlib>
    #include <string>
    #include  <vector>
    #include "test.pb.h"
    
    using namespace std;
    
    using namespace test;
    int main()
    {
    	    GOOGLE_PROTOBUF_VERIFY_VERSION;  
    	
    	Feature feature;
    	Feature::Single* haha = feature.mutable_sin();
    
    	haha->set_qxxx(256256);
            cout<<"val:"<<feature.sin().qxxx()<<endl;	
    	return 0;
    }


但是如果要修改的是某个class中另一个class的repeated的值，则要使用add_name.

参考如下例子:

    
    syntax = "proto3";
    package test;
    message Feature
    {
        int32 ver = 1;
        int32 idx = 2;
        int32 len = 3;
        repeated float feat = 4;
        message Single
        {
    	int64 QxXx = 1;
    	string imagePath=2;
        }
        repeated Single sin = 6;
    }
    
    



    
    #include <iostream>
    #include <cassert>
    #include <cstdlib>
    #include <string>
    #include  <vector>
    #include "test.pb.h"
    using namespace std;
    using namespace test;
    int main()
    {
    	    GOOGLE_PROTOBUF_VERIFY_VERSION;  
    	
    	Feature feature;
    	Feature::Single *haha = feature.add_sin();
    	haha->set_qxxx(256256);
    	haha = feature.add_sin();
    	haha->set_qxxx(456);
    	cout<<"size:"<<feature.sin_size()<<endl;
            cout<<"val:"<<feature.sin(0).qxxx()<<endl<<feature.sin(1).qxxx()<<endl;	
    	return 0;
    }




**需要注意的是生成的代码的大小写敏感问题**

对于生成cpp代码来说，无论.proto文件中的变量名是Abc还是aBc还是ABC,在生成的cpp代码中都是abc...

protobuf的大小写敏感有点坑orz..




## troubleshooting


试图从3.5降级到3.3时编译helloworld无问题，但是运行时报错

    
    ./greeter_client: Symbol `_ZTVN6google8protobuf11MessageLiteE' has different size in shared object, consider re-linking
    ./greeter_client: Symbol `_ZTVN6google8protobuf7MessageE' has different size in shared object, consider re-linking
    [libprotobuf FATAL google/protobuf/stubs/common.cc:79] This program was compiled against version 3.3.0 of the Protocol Buffer runtime library, which is not compatible with the installed version (3.5.1).  Contact the program author for an update.  If you compiled the program yourself, make sure that your headers are from the same version of Protocol Buffers as your link-time library.  (Version verification failed in "google/protobuf/any.pb.cc".)
    terminate called after throwing an instance of 'google::protobuf::FatalException'
      what():  This program was compiled against version 3.3.0 of the Protocol Buffer runtime library, which is not compatible with the installed version (3.5.1).  Contact the program author for an update.  If you compiled the program yourself, make sure that your headers are from the same version of Protocol Buffers as your link-time library.  (Version verification failed in "google/protobuf/any.pb.cc".)


折腾了一下午。。发现其实并不是protobuf的问题。。

用gdb调试发现。。。是grpc的一个动态库中check版本挂掉了。。。

观察grpc。。。发现还是4月20号左右的版本。。。于是删掉了所有之前的grpc在/usr/local/lib下的4月的.so文件。。。

再次运行。。成功了orz....

所以这个问题其实是。。。降级grpc遇到的问题。。。

报错太有误导性了。














