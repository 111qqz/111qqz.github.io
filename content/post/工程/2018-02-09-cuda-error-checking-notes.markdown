---
author: 111qqz
date: 2018-02-09 06:55:00+00:00
draft: false
title: cuda error checking 学习笔记
type: post
url: /2018/02/cuda-error-checking-notes/
categories:
- 优化
tags:
- cuda
---

由于发现cuda c++ 的 debug方式和c++ 差别很大,因此打算再开一篇,专门记录一些和error checking 以及debug有关的内容.

Error checks in CUDA code can help catch CUDA errors at their source. There are 2 sources of errors in CUDA source code:




      1. Errors from CUDA **API** calls. For example, a call to `cudaMalloc()` might fail.
      2. Errors from CUDA **kernel** calls. For example, there might be invalid memory access inside a kernel.


All CUDA API calls return a `cudaError` value, so these calls are easy to check:





````

    
    if ( cudaSuccess != cudaMalloc( &fooPtr, fooSize ) )
        printf( "Error!\n" );
    


````







CUDA kernel invocations do not return any value. Error from a CUDA kernel call can be checked after its execution by calling `cudaGetLastError()`:














    
    fooKernel<<< x, y >>>(); // Kernel call
    if ( cudaSuccess != cudaGetLastError() )
        printf( "Error!\n" );
    











以及下面是一个check error的宏...


    
    #define CHECK_ERROR( err ) \
      if( err != cudaSuccess ) { \
        std::cerr << "ERROR: " << cudaGetErrorString( err ) << std::endl; \
        exit( -1 ); \
      }
    
    #define CHECK_LAST_ERROR \
      { cudaError_t err = cudaGetLastError(); \
        if( err != cudaSuccess ) { \
          std::cerr << cudaGetErrorString( err ) << std::endl; \
          exit( -1 ); \
        } \
      }




