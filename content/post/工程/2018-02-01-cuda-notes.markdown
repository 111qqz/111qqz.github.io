---
author: 111qqz
date: 2018-02-01 07:20:04+00:00
draft: false
title: cuda 学习笔记
type: post
url: /2018/02/cuda-notes/
categories:
- 优化
tags:
- cuda
---

uodate:有毒吧。kernel中出问题原来是不会报错的。。。。

请教了组里的hust学长orz..、

学到了cuda-memcheck命令和cudaGetLastError来查看问题。。可以参考[What is the canonical way to check for errors using the CUDA runtime API?](https://stackoverflow.com/questions/14038589/what-is-the-canonical-way-to-check-for-errors-using-the-cuda-runtime-api)



先放一波资料。




      * <del>[An Even Easier Introduction to CUDA](https://devblogs.nvidia.com/even-easier-introduction-cuda/)</del>
      * <del>[CUDA C/C++ Basics](https://drive.google.com/open?id=1kHYyM4yiJoyjkWjp7FJp0vae_TcvskjK)</del>
      * <del>[nvidia-thrust 官方文档](http://docs.nvidia.com/cuda/thrust/index.html)</del>
      * [how-access-global-memory-efficiently-cuda-c-kernels](https://devblogs.nvidia.com/how-access-global-memory-efficiently-cuda-c-kernels/)
      * [efficient-matrix-transpose-cuda-cc](https://devblogs.nvidia.com/efficient-matrix-transpose-cuda-cc/)
      * [很强大的warp内shuffle](https://devblogs.nvidia.com/faster-parallel-reductions-kepler/)
      * [cuda-GDB官方文档](http://docs.nvidia.com/cuda/cuda-gdb/index.html)
      * [cuda-c-best-practices-guide](http://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)






cuda 提出的目的是能够让程序员透明地使用GPU来高效地进行并行运算。

kernel和c语言中的函数相似，函数名字前通常用**global**来标识。



下面考虑一个2个大小的1M的数组相加的例子。

总的思路是通过并行，来观察到计算速度的加快。

如果不考虑并行，2个数组相加的代码，如下：


    
    #include <iostream>
    #include <math.h>
    
    // function to add the elements of two arrays
    void add(int n, float *x, float *y)
    {
      for (int i = 0; i < n; i++)
          y[i] = x[i] + y[i];
    }
    
    int main(void)
    {
      int N = 1<<20; // 1M elements
    
      float *x = new float[N];
      float *y = new float[N];
    
      // initialize x and y arrays on the host
      for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
      }
    





如果用cuda的方式来搞，代码如下：


    
    #include <iostream>
    #include <math.h>
    // Kernel function to add the elements of two arrays
    __global__
    void add(int n, float *x, float *y)
    {
      for (int i = 0; i < n; i++)
        y[i] = x[i] + y[i];
    }
    
    int main(void)
    {
      int N = 1<<20;
      float *x, *y;
    
      // Allocate Unified Memory – accessible from CPU or GPU
      cudaMallocManaged(&x, N*sizeof(float));
      cudaMallocManaged(&y, N*sizeof(float));
    
      // initialize x and y arrays on the host
      for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
      }
    
      // Run kernel on 1M elements on the GPU
      add<<<1, 1>>>(N, x, y);
    
      // Wait for GPU to finish before accessing on host
      cudaDeviceSynchronize();
    
      // Check for errors (all values should be 3.0f)
      float maxError = 0.0f;
      for (int i = 0; i < N; i++)
        maxError = fmax(maxError, fabs(y[i]-3.0f));
      std::cout << "Max error: " << maxError << std::endl;
    
      // Free memory
      cudaFree(x);
      cudaFree(y);
      
      return 0;
    }



除了代码注释，还有几个地方要说明：




      * 函数名字前面的global 是 cuda kernel  标识符
      * cuda kernel的调用方式是 <<<,>>>  更具体地说，是add<<<numBlocks,blockSize>>>(N,x,y)
      * .cu是 cuda C++ 文件的后缀，类似.cpp
      * nvcc是cuda C++ 的编译器，其将source code分成**host code**和**device code**两部分。前者通过c++编译器编译，后者通过nvidia编译器编译。




关于devide code 和 host code，参考下图。

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-08-145751.png)
](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-08-145751.png)



现在我们单线程地跑了一个cuda kernel, 接下来是如何使它并行.关键在于<<<1,1>>>这部分。

这行代码告诉了cuda runtime 有多少个并行的线程要被执行。
这里有2个参数，不过我们可以先改变第二个，也就是一个线程block中线程的个数。
cuda GPu的kernel 使用的blocks中线程的个数应该是32的倍数（后面会解释32代表什么），所以256看起来很合理。




    
    #include <cstdio>
    #include <iostream>
    #include <math.h>
    // Kernel function to add the elements of two arrays
        __global__
    void add(int n, float *x, float *y)
    {
    
    
         int index = blockIdx.x * blockDim.x + threadIdx.x;
        int stride = blockDim.x * gridDim.x;
    printf(" %d %d",index,stride);
        for ( int i = index ; i < n ; i += stride)
        y[i] = x[i] + y[i];
    }
    
    int main(void)
    {
        int N = 1<<20;
        float *x, *y;
    
        // Allocate Unified Memory – accessible from CPU or GPU
        cudaMallocManaged(&x, N*sizeof(float));
        cudaMallocManaged(&y, N*sizeof(float));
    
        // initialize x and y arrays on the host
        for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
        }
    
    
        int blockSize = 256;
        int numBlocks = (N + blockSize - 1) / blockSize;
        add<<<numBlocks, blockSize>>>(N, x, y);
        // Wait for GPU to finish before accessing on host
        cudaDeviceSynchronize();
    
        // Check for errors (all values should be 3.0f)
        float maxError = 0.0f;
        for (int i = 0; i < N; i++)
        maxError = fmax(maxError, fabs(y[i]-3.0f));
    //    std::cout << "Max error: " << maxError << std::endl;
    
        // Free memory
        cudaFree(x);
        cudaFree(y);
    
        return 0;
    }





不过如果只是修改了<<<1,1>>> 到  <<<1,256>>>
那实际上是对于每个线程都算了整个array的相加，而没有将整个计算任务分给多个并行的线程。
为了解决这个问题，我们需要修改kernel的代码。
cuda C++ 提供了关键字，允许kernel得到正要执行的thread是哪一个
threadIdx.x  表示当前运行的thread是block中的哪一个
blockDim.x 表示block中的线程个数

关于threadIdx.x等 下标问题，参考下图。

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-08-151308.png)
](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-08-151308.png)



我们需要观察到使用cuda的方法之后时间的变化。

可以使用nvprof命令


    
    ➜ learn>nvprof ./add_cuda
    ==9312== NVPROF is profiling process 9312, command: ./add_cuda
    Max error: 0
    ==9312== Profiling application: ./add_cuda
    ==9312== Profiling result:
    Time(%)      Time     Calls       Avg       Min       Max  Name
    100.00%  167.48ms         1  167.48ms  167.48ms  167.48ms  add(int, float*, float*)
    






    
    ==9382== Profiling application: ./add_block
    ==9382== Profiling result:
    Time(%)      Time     Calls       Avg       Min       Max  Name
    100.00%  3.5144ms         1  3.5144ms  3.5144ms  3.5144ms  add(int, float*, float*)
    
    




    
    ==9447== Profiling application: ./add_grid
    ==9447== Profiling result:
    Time(%)      Time     Calls       Avg       Min       Max  Name
    100.00%  1.8084ms         1  1.8084ms  1.8084ms  1.8084ms  add(int, float*, float*)
    
    





可以看出时间的变化，从167.48ms到3.5144ms，再到1.8084ms





我们注意到，对线程的管理实际上是三维的 :grid,block,thread.

为什么要这样设计？

一个这样做的目的是，在一个block中，thread可以通过share_memory 来共享数据。

通过在声明的变量前面添加 **shared**  来表示，这个变量是声明在share memory部分了。

share memory类似与缓存，容量小，但是速度快。不过这个cache是可以编程控制的。

**在一个block中共享的data,对于其他block是不可见的。**

我们不妨考虑一个例子，有2个数组a,b

进行如下运算：

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-08-210339.png)
](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-08-210339.png)



为了加快运行速度，我们还是考虑多线程的办法。

让每一个线程处理一个输出。

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-09-095804.png)
](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-09-095804.png)

然而我们发现，in中除了边界元素，每一个元素都被读了7次。

这显然是没有必要的。

问题的关键在于，不同的线程之间，不知道某个元素已经被读入了。

更进一步，不同线程之间可以共享数据吗？

答案是可以的。也就是上面提到的shared_memory

然而这样就可以了吗。。

由于线程的访问顺序是不固定的(?

会发生如下的问题：

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-09-100824.png)
](https://111qqz.com/wordpress/wp-content/uploads/2018/02/Screenshot-from-2018-02-09-100824.png)



解决办法很无脑。。。因为cuda并没有想象中得那么底层。。。

就是使用__syncthreads(); 来同步一个block中的所有进程。。。

完整代码如下：


    
    #include <iostream>
    #include <cstdio>
    #include <cmath>
    #include <ctime>
    
    const int R=3;
    const int N=1<<20;
    const int BLOCK_SIZE=256;
        __global__ 
    void solve( int *in,int *out)
    {
        __shared__ int tmp[BLOCK_SIZE + 2*R];
        int gindex = threadIdx.x + blockIdx.x * blockDim.x;
        int lindex = threadIdx.x + R;
    //     printf ("%d %d\n",gindex,lindex-R);
    //    printf("wang\n");
        //if (lindex < BLOCK_SIZE+2*R && gindex < N)
          tmp[lindex] = in[gindex];
    
    
    //    if 这部分有问题。。。貌似是访问越界。。
        if (threadIdx.x < R)
        {
        if (lindex>=R && gindex>=R&&lindex-R<BLOCK_SIZE+2*R&&gindex-R<N)
           tmp[lindex-R] = in[gindex-R];
        if (lindex + BLOCK_SIZE< BLOCK_SIZE+2*R && gindex + BLOCK_SIZE < N )
           tmp[lindex+BLOCK_SIZE] = in[gindex + BLOCK_SIZE];
        }
        
      //  printf("miao\n");
        __syncthreads();
        int res = 0 ;
        
        for ( int offset = -R ; offset <= R ; offset++)
        {
    //  printf ("offset:%d\n",offset);
    //  if (lindex + offset < BLOCK_SIZE+2*R)
        res += tmp[lindex + offset];
        }
        
        out[gindex] = res;
        printf("res=%d\n",res);
    }
    
    void pr( int *A,int n)
    {
        for ( int i = 0 ;i  <  10 ; i++) printf ("%d%c",A[i*10],i==9?'\n':' ');
    }
    
    int main(void)
    {
        int *a,*b;
        if (cudaSuccess != cudaMallocManaged(&a,N*sizeof(int)))
        printf("Cuda Malloc error\n");
    
        if (cudaSuccess != cudaMallocManaged(&b,N*sizeof(int)))
        printf("Cuda Malloc error\n");
        for ( int i = 0 ; i < N ; i++)
        {
        a[i] = 1;
        }
        pr(a,N);
        pr(b,N);
        int numBlocks = ( N + BLOCK_SIZE -1 ) / BLOCK_SIZE;
        //solve<<<numBlocks,BLOCK_SIZE>>>(a,b);
        solve<<<1,256>>>(a,b);
        if (cudaSuccess !=cudaGetLastError())
        printf("kernel error!");
        // prt<<<numBlocks,BLOCK_SIZE>>>();
        cudaDeviceSynchronize();
        pr(b,N);
    
        //printf(cudaGetLastError());
        cudaFree(a);
        cudaFree(b);
    
        return 0;
    }







需要特别强调的是，cuda代码的debug问题，很多错误，不用特定的工具查看是不会显示的。
以及，虽然cuda代码是在c++上添加了一些东西，但是device code部分用的是nvidia的编译器。
所以c/cpp中，对于访问非法内存不敏感的特点，在cuda代码中不存在（我猜是因为编译器...）
**在访问之前，一定要check访问地址合法性。。。。**

**在访问之前，一定要check访问地址合法性。。。。**

**在访问之前，一定要check访问地址合法性。。。。**








