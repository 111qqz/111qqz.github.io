---
author: 111qqz
date: 2019-02-18 06:00:51+00:00
draft: false
title: 【施工中】 halide学习笔记
type: post
url: /2019/02/halide-notes/
categories:
- 优化
tags:
- halide
---

<blockquote>

> 
> ### **Halide is a programming language designed to make it easier to write high-performance image and array processing code on modern machines. **
> 
> 
</blockquote>


halide有两个特性比较吸引人。一个是对于各种平台架构的支持。


<blockquote>

> 
> 
 	  * CPU architectures: X86, ARM, MIPS, Hexagon, PowerPC
 	  * Operating systems: Linux, Windows, macOS, Android, iOS, Qualcomm QuRT
 	  * GPU Compute APIs: CUDA, OpenCL, OpenGL, OpenGL Compute Shaders, Apple Metal, Microsoft Direct X 12

</blockquote>


另一个是把计算什么和怎么计算(何时计算)分离开来。
>**Halide的Schedule可以由程序员来指定一些策略，指定硬件的buffer大小，缓冲线的相关设置，这样可以根据不同的计算硬件的特性来实现高效率的计算单元的调度，而图像算法的计算实现却不需要修改。**

>**Halide的运行有两种方式，一种是JIT的模式，另一种是AOT的模式。JIT模式使用起来比较方便，可以直接将算法和Halide的代码生成generator封装成一个类，在程序的其他部分调用这个类即可。在嵌入式环境和交叉编译环境下一般使用AOT模式，此时需要调用compiler函数将算法代码和Halide的代码生成generator编译位目标机器的代码，生成一个.o目标文件和.h头文件。然后在独立的目标机器的应用的工程的源代码中通过头文件调用算法实现的计算函数，并在build的时候链接上.o文件，这样就得到一个可以在目标机器上运行的用Halide实现算法的程序了。一般DSP上都是这种方式来做的。**

>
可以直接参考[tutorials](http://halide-lang.org/tutorials/tutorial_introduction.html) 来学习



下面是一段将Halide Buffer转化成opencv Mat的代码，用于调试。
```c++
    
    // Include some support code for loading pngs.
    // #include "halide_image_io.h"
    #include <iostream>
    #include "para_norm.h"
    #include "HalideBuffer.h"
    #include "clock.h"
    #include "halide_image_io.h"  // for Halide::tools to load image. just for debug
    #include <opencv2/opencv.hpp> // to show image
    
    // #include "Halide.h"
    using namespace std;
    using namespace cv;
    using namespace Halide;
    using namespace Halide::Runtime;
    // using namespace Halide::Tools;
    void convertHalide2Mat(const Buffer<uint8_t> &src, cv::Mat &dest)
    {
        if (dest.empty())
            dest.create(cv::Size(src.width(), src.height()), CV_MAKETYPE(CV_8U, src.channels()));
        const int ch = dest.channels();
        if (ch == 1)
        {
            for (int j = 0; j < dest.rows; j++)
            {
                for (int i = 0; i < dest.cols; i++)
                {
                    dest.at<uchar>(j, i) = src(i, j);
                }
            }
        }
        else if (ch == 3)
        {
            for (int j = 0; j < dest.rows; j++)
            {
                for (int i = 0; i < dest.cols; i++)
                {
                    dest.at<uchar>(j, 3 * i + 0) = src(i, j, 2);
                    dest.at<uchar>(j, 3 * i + 1) = src(i, j, 1);
                    dest.at<uchar>(j, 3 * i + 2) = src(i, j, 0);
                }
            }
        }
    }
    int main(int argc, char **argv)
    {
    
        Halide::Runtime::Buffer<uint8_t> input = Halide::Tools::load_image("/data/github/learnhalide/png.png");
        cv::Mat Img;
        convertHalide2Mat(input,Img);
        cv::imshow("debug", Img);
        cv::waitKey(0);
        return 0;
    }
    

```


吐槽下hahide的文档...各种函数全靠试...

试了好久得到的,opencv Mat转halide::buffer的办法:

```c++
    
    cv::Mat image = cv::imread("/data/github/learnhalide/png.png");
        cv::imshow("input",image);
        cv::waitKey(0);
        halide_buffer_t buffer;
        // memset(&buffer, 0, sizeof(buffer));
    
        buffer.host = image.data;
        printf("image.data %d %d %d\n",image.data[0],image.data[1],image.data[2]);
        printf("buffer.host %d %d %d\n",buffer.host[0],buffer.host[1],buffer.host[2]);
        // 数据没有copy过来
        buffer.type = halide_type_t(halide_type_uint,8);
        buffer.dimensions = 3;
        buffer.dim = (halide_dimension_t *)malloc(3*4*sizeof(uint32_t));
        buffer.dim[0].extent = image.cols;
        buffer.dim[1].extent = image.rows;
        buffer.dim[2].extent = image.channels();
        buffer.dim[0].min = buffer.dim[1].min = buffer.dim[2].min = 0;
    
    
        buffer.dim[0].stride = image.step1(1);
        buffer.dim[1].stride = image.step1(0);
        buffer.dim[2].stride = 1;
    
        Halide::Runtime::Buffer<uint8_t> input(buffer);
        printf("input buffer:%d %d %d\n",input.width(),input.height(),input.channels());
        // printf("%d\n",input(2,2));
        const halide_buffer_t * 	raw_buffer = input.raw_buffer();
        printf("raw buffer: %d %d %d\n",raw_buffer->host[0],raw_buffer->host[1],raw_buffer->host[2]);
    
    
        cv::Mat Img;
        convertHalide2Mat(input, Img);
        printf("Mat(%d %d)\n", Img.cols, Img.rows);
        cv::imshow("debug", Img);
        cv::waitKey(0);
    
```



可能会报错Error: Constraint violated: input.stride.0 (3) == 1 (1),原因是:


<blockquote>**We have a default constraint of stride==1 on the innermost dimension, so that vectorization works out well**</blockquote>


[Constraint violated: f.stride.0 (2) == 1 (1) #3109](https://github.com/halide/Halide/issues/3109)

解决办法是(对于AOT的编译方式):





ImageParam input(type_of<uint8_t>(), 3);




input.dim(0).set_stride(Expr());







一种更简便的opencv Mat得到halide buffer的办法.　一个关键的问题是opencv Mat的memory layout是Interleaved的方式，也就是如下:






// RGBRGBRGBRGBRGBRGBRGBRGB




// RGBRGBRGBRGBRGBRGBRGBRGB




// RGBRGBRGBRGBRGBRGBRGBRGB




// RGBRGBRGBRGBRGBRGBRGBRGB
















但是Halide::buffer的默认memory layout是Planar的方式：










// RRRRRRRR




// RRRRRRRR




// RRRRRRRR




// RRRRRRRR




// GGGGGGGG




// GGGGGGGG




// GGGGGGGG




// GGGGGGGG




// BBBBBBBB




// BBBBBBBB




// BBBBBBBB




// BBBBBBBB













因此需要用到函数


## make_interleaved()



```c++
cv::Mat image = cv::imread("/data/github/learnhalide/png.png");
Halide::Runtime::Buffer<uint8_t> input = Halide::Runtime::Buffer<uint8_t>::make_interleaved(image.data,1240, 460, 3);
```





































