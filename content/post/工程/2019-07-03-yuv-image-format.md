---
title: "yuv 图像格式初探"
date: 2019-07-03T20:31:11+08:00
draft: false
author: "111qqz"
type: post
url: /2019/07/Yuv-Image-Format
categories:
- 其他

tags:
- image processing
- yuv image format

---

## 概述
YUV是一种图像编码方式,或者称为[色彩空间](https://zh.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%96%93),与RGB是同级的概念.
YUV是三个分量,Y,U和V,其中:

- Y 表示明亮度(Luminance或Luma),也就是灰度值,
- U,V表示色度,浓度（Chrominance、Chroma）,可以简单理解成用来表示某个像素的颜色的量.

YUV格式的特点是,在对照片或影片编码时，考虑到人类的感知能力，允许降低色度的带宽。
也就是说,YUV不像RGB那样要求三个独立的视频信号同时传输，**所以用YUV方式传送占用极少的频宽。**

其中**YCbCr**是YUV压缩和偏移的版本。YCbCr的Y与YUV中的Y含义一致，Cb和Cr与UV同样都指色彩，Cb指蓝色色度，Cr指红色色度，在应用上很广泛，JPEG、MPEG、DVD、摄影机、数字电视等皆采此一格式。因此一般俗称的YUV大多是指YCbCr。

## YUV采样方式
主流的采样方式有三种:
其中**Y 分量用叉表示，UV 分量用圆圈表示。**

- YUV4:4:4
- YUV4:2:2
- YUV4:2:0


下面三张图分别为YUV444,YUV422和YUV420的采样方式. <br>
![YUV444](https://i-msdn.sec.s-msft.com/dynimg/IC130499.gif) 

![YUV422](https://i-msdn.sec.s-msft.com/dynimg/IC84769.gif)

![YUV420](https://i-msdn.sec.s-msft.com/dynimg/IC173152.gif)

但是注意,**上面的三张图只是说明了每个分量的比例,并不能说明排列方式.**

需要注意的是yuv420并不是说只采样U分量或者只采样V分量,而是指，在每一行扫描时，只扫描一种色度分量（U 或者 V），和 Y 分量按照 2 : 1 的方式采样。比如，第一行扫描时，YU 按照 2 : 1 的方式采样，那么第二行扫描时，YV 分量按照 2:1 的方式采样


## YUV封装格式
采样方式主要是告诉我们各个分量的比例,下面看一下封装格式.
**YUV格式有两大类：planar和packed。**

- planar: 先连续存储所有像素点的Y，紧接着存储所有像素点的U，随后是所有像素点的V。
- packed: 每个像素点的Y,U,V是连续交错存储的。

其中,planar格式还分为**SEMI PLANAR**和**PLANAR**

+ semi planar:先连续存储所有的Y, 然后UV交错存储.
+ planar:先连续存储所有像素点的Y，紧接着存储所有像素点的U，随后是所有像素点的V。

以YUV420为例,前面的图为平面的封装格式,也就是YUV420P(Planar) <br>
后面的图为半平面的封装格式,也就是YUV420SP(semi planar) <br>
![YUV420P封装格式](https://blog.sunzhihao.com/YUV%E6%A0%BC%E5%BC%8F%E7%9A%84%E8%AF%B4%E6%98%8E/3.png)
![YUV420SP封装格式](https://blog.sunzhihao.com/YUV%E6%A0%BC%E5%BC%8F%E7%9A%84%E8%AF%B4%E6%98%8E/4.png)

或者以1920*1080的图片具体举例:<br>
左边的图为平面的封装格式,也就是YUV420P(Planar) <br>
右边的图为半平面的封装格式,也就是YUV420SP(semi planar) <br>
![YUV420P封装格式](https://blog.sunzhihao.com/YUV%E6%A0%BC%E5%BC%8F%E7%9A%84%E8%AF%B4%E6%98%8E/1.png)



## YUV格式的名称,傻傻分不清楚
由于最近使用的YUV420格式的,因此主要会涉及这一种.
YUV420分为**YUV420P**和**YUV420SP**两种.
其中YUV420P又有两种,一种是Y(w×h) + U(w×h/4) + V(w×h/4)的格式,这一种也叫**I420**或者**420P**或者**IYUV**(存疑,参考opencv convert_color函数文档)
另一种是Y(w×h) + V(w×h/4) + U(w×h/4)的格式,这一种也叫**YV12**

YUV420SP也分两种,分别是**NV12**和**NV21**.
其中NV12的格式为: Y(w×h) + UV(w×h/4)
NV21的格式为: Y(w×h) + VU(w×h/4)


## YUV格式转BGR格式
方法有很多,可以直接用公式转.
这里介绍一种借助opencv的比较简单可行的办法
方法是读入时按照二进制文件的方式读入YUV文件,
然后使用opencv的 cvtColor 函数.
```c++
Mat mYUV(height + height/2, width, CV_8UC1, (void*) frameData);
Mat mRGB(height, width, CV_8UC3);
cvtColor(mYUV, mRGB, CV_YUV2RGB_YV12, 3);
```

## 小结

由于最近遇到的是YUV420的图片格式,所以虽然题目叫YUV格式初探,但是没怎么涉及到其他YUV格式,可能以后有机会补充吧.

放一个表格,懒得一点一点写了,直接贴了其他人博客的截图
![表格](https://i.loli.net/2019/07/03/5d1cb4a02756074474.png)



## 参考链接
[YUV格式的说明](https://blog.sunzhihao.com/YUV%E6%A0%BC%E5%BC%8F%E7%9A%84%E8%AF%B4%E6%98%8E/) <br>
[一文读懂 YUV 的采样与格式](https://glumes.com/post/ffmpeg/understand-yuv-format/) <br>
[How to read a frame from YUV file in OpenCV?](https://stackoverflow.com/questions/2231518/how-to-read-a-frame-from-yuv-file-in-opencv/30539306#30539306)





