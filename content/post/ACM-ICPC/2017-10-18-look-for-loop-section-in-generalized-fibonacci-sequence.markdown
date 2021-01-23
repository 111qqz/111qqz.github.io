---
author: 111qqz
date: 2017-10-18 05:38:43+00:00
draft: false
title: 广义Fibonacci数列找循环节 （二次剩余）
type: post
url: /2017/10/look-for-loop-section-in-generalized-fibonacci-sequence/
categories:
- ACM
tags:
- 二次剩余
- 循环节
---

**问题：**给定![](http://img.blog.csdn.net/20140512141202250)
，满足![](http://img.blog.csdn.net/20140512141344500)
，求![](http://img.blog.csdn.net/20140512141547343)
的循

环节长度。

原理见[广义Fibonacci数列找循环节](http://blog.csdn.net/acdreamers/article/details/25616461)

这里只说做法

我们先写出递推式的特征式子   x^2 =ax + b,整理得到 x^2-ax-b=0求出 delta = a^2+4b

对于质因数小于等于delta的部分，我们选择暴力求循环节。

暴力求循环节的代码如下：


    
    int get_loop( LL p) //暴力得到不大于13的素数的循环节。
    {                    
        LL a,b,c;
        a = 0 ;
        b = 1 ;
        for ( int i = 2; ; i++)
        {
            c = (a+3*b%p)%p;  //此处为递推式
            a = b;
            b = c;
            if (a==0&&b==1) return i-1;
        }
    }



通常做法是先暴力求出来之后，写进一个表里。

通常不会有很多项。

对于质因数大于delta的部分，我们判断每个质因数是否是delta的二次剩余，如果是，枚举(prime-1)的因子,否则枚举2*(prime+1)的因子。

贴一个板子，需要注意如果是多个函数嵌套的形式，我们只需要从外向里，依次求循环节即可。


    
    /* ***********************************************
    Author :111qqz
    Created Time :Mon 31 Oct 2016 08:22:17 PM CST
    File Name :code/hdu/4291_2.cpp
    ************************************************ */
     
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #define fst first
    #define sec second
    #define lson l,m,rt<<1
    #define rson m+1,r,rt<<1|1
    #define ms(a,x) memset(a,x,sizeof(a))
    typedef long long LL;
    #define pi pair < int ,int >
    #define MP make_pair
     
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    struct Mat
    {
        LL mat[2][2];
        void clear()
        {
            ms(mat,0);
        }
    }M,M1;
    Mat mul (Mat a,Mat b,LL mod)
    {
        Mat c;
        c.clear();
        for ( int i = 0 ; i < 2 ; i++)
            for ( int j = 0 ; j < 2 ; j++)
                for ( int k  = 0 ; k < 2 ; k++)
                    c.mat[i][j] = (c.mat[i][j] + a.mat[i][k] * b.mat[k][j]%mod)%mod;
        return c;
    }
    Mat mat_ksm(Mat a,LL b,LL mod)
    {
        Mat res;
        res.clear();
        for ( int i = 0 ; i < 2 ; i++) res.mat[i][i] = 1;
        while (b>0)
        {
            if (b&1) res = mul(res,a,mod);
            b = b >> 1LL;
            a = mul(a,a,mod);
        }
        return res;
    }
    LL gcd(LL a,LL b)
    {
        return b?gcd(b,a%b):a;
    }
    const int N = 1E6+7;
    bool prime[N];
    int p[N];
    void isprime() //一个普通的筛
    {
        int cnt = 0 ;
        ms(prime,true);
        for ( int i = 2 ; i < N ; i++)
        {
            if (prime[i])
            {
                p[cnt++] = i ;
                for ( int j = i+i ; j < N ; j+=i) prime[j] = false;
            }
        }
    }
    LL ksm( LL a,LL b,LL mod)
    {
       LL res = 1;
       while (b>0)
       {
           if (b&1) res = (res * a) % mod;
           b = b >> 1LL;
           a = a * a % mod;
       }
       return res;
    }
    LL legendre(LL a,LL p) //勒让德符号,判断二次剩余
    {
        if (ksm(a,(p-1)>>1,p)==1) return 1;
        return -1;
    }
    LL pri[N],num[N];//分解质因数的底数和指数。
    int cnt; //质因子的个数
    void solve(LL n,LL pri[],LL num[])
    {
        cnt = 0 ;
        for ( int  i = 0 ; p[i] * p[i] <= n ; i++)
        {
            if (n%p[i]==0)
            {
                int Num = 0 ;
                pri[cnt] = p[i];
                while (n%p[i]==0)
                {
                    Num++;
                    n/=p[i];
                }
                num[cnt] = Num;
                cnt++;
            }
        }
        if (n>1)
        {
            pri[cnt] = n;
            num[cnt] = 1;
            cnt++;
        }
    }
    LL fac[N];
    int cnt2; //n的因子的个数
    void get_fac(LL n)//得到n的所有因子
    {
        cnt2 = 0 ;
        for (int i =  1 ; i*i <= n ; i++)
        {
            if (n%i==0)
            {
                if (i*i!=n)
                {
                    fac[cnt2++] = i ;
                    fac[cnt2++] = n/i;
                }
                else fac[cnt2++] = i;
            }
        }
    }
    int get_loop( LL p) //暴力得到不大于13的素数的循环节。
    {                    
        LL a,b,c;
        a = 0 ;
        b = 1 ;
        for ( int i = 2; ; i++)
        {
            c = (a+3*b%p)%p;
            a = b;
            b = c;
            if (a==0&&b==1) return i-1;
        }
    }
    /*
        2->3
        3->2
        5->12
        7->16
        11->8
        13->52
        */
    const LL LOOP[10]={3,2,12,16,8,52};
    LL ask_loop(int id)
    {
        return LOOP[id];
    }
    LL find_loop(LL n)
    {
        solve(n,pri,num);
        LL ans = 1;
        for ( int i = 0 ; i < cnt ; i++)
        {
            LL rec = 1;
            if (pri[i]<=13) rec = ask_loop(i);
            else
            {
                if (legendre(13,pri[i])==1)  //13就是delta值
                    get_fac(pri[i]-1);
                else get_fac((pri[i]+1)*(3-1)); //为什么可以假设循环节不大于2*(p+1)???
                sort(fac,fac+cnt2);
                for ( int j = 0 ; j < cnt2 ; j++) //挨个验证因子
                {
                    Mat tmp = mat_ksm(M,fac[j],pri[i]); //下标从0开始，验证fac[j]为循环节，应该看fib[0]==fib[fac[j]]和fib[1]==fib[fac[j]+1]是否成立
                    tmp = mul(tmp,M1,pri[i]);
                    if (tmp.mat[0][0]==0&&tmp.mat[1][0]==1)
                    {
                        rec = fac[j];
                        break;
                    }
                }
     
            }
            for ( int j = 1 ; j < num[i] ; j++)
                rec *=pri[i];
            ans = ans / gcd(ans,rec) * rec;
        }
        return ans;
    }
    void init()
    {
        M.clear();
        M.mat[0][1] = M.mat[1][0] = 1;
        M.mat[1][1] = 3;
        M1.clear();
        M1.mat[1][0] = 1;
    }
    LL n;
    LL loop0 = 1E9+7;
    LL loop1,loop2;
    int main()
    {
            #ifndef  ONLINE_JUDGE 
            freopen("code/in.txt","r",stdin);
      #endif
            /*
            printf("%d\n",get_loop(2));
            printf("%d\n",get_loop(3));
            printf("%d\n",get_loop(5));
            printf("%d\n",get_loop(7));
            printf("%d\n",get_loop(11));
            printf("%d\n",get_loop(13));
            */
            init();
            isprime();
            while (~scanf("%lld\n",&n))
            {
                if (n==0||n==1)
                {
                    printf("%lld\n",n);
                    continue;
                }
                LL loop1 = find_loop(loop0);
                LL loop2 = find_loop(loop1);
    //            printf("loop1:%lld loop2:%lld\n",loop1,loop2);
                LL cur = n;
                Mat ans = mat_ksm(M,cur-1,loop2);
                ans = mul(ans,M1,loop2);
                cur = ans.mat[1][0];
                if (cur!=0&&cur!=1)
                {
                    Mat ans = mat_ksm(M,cur-1,loop1);
                    ans = mul(ans,M1,loop1);
                    cur = ans.mat[1][0];
                }
                if (cur!=0&&cur!=1)
                {
                    Mat ans = mat_ksm(M,cur-1,loop0);
                    ans = mul(ans,M1,loop0);
                    cur = ans.mat[1][0];
                }
                printf("%lld\n",cur);
     
            }
     
    #ifndef ONLINE_JUDGE  
            fclose(stdin);
    #endif
            return 0;
    }
    





再补一个，更为常用的，求斐波那契循环节的板子：


    
    /* ***********************************************
    Author :111qqz
    Created Time :Mon 31 Oct 2016 03:54:15 AM CST
    File Name :code/hdu/3977.cpp
    ************************************************ */
     
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    #include <algorithm>
    #include <vector>
    #include <queue>
    #include <set>
    #include <map>
    #include <string>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>
    #define fst first
    #define sec second
    #define lson l,m,rt<<1
    #define rson m+1,r,rt<<1|1
    #define ms(a,x) memset(a,x,sizeof(a))
    typedef long long LL;
    #define pi pair < int ,int >
    #define MP make_pair
     
    using namespace std;
    const double eps = 1E-8;
    const int dx4[4]={1,0,0,-1};
    const int dy4[4]={0,-1,1,0};
    const int inf = 0x3f3f3f3f;
    LL P;
    struct Mat
    {
        LL mat[2][2];
        void clear()
        {
            ms(mat,0);
        }
    }M,M1;
    Mat mul (Mat a,Mat b,LL mod)
    {
        Mat c;
        c.clear();
        for ( int i = 0 ; i < 2 ; i++)
            for ( int j = 0 ; j < 2 ; j++)
                for ( int k  = 0 ; k < 2 ; k++)
                    c.mat[i][j] = (c.mat[i][j] + a.mat[i][k] * b.mat[k][j]%mod)%mod;
        return c;
    }
    Mat mat_ksm(Mat a,LL b,LL mod)
    {
        Mat res;
        res.clear();
        for ( int i = 0 ; i < 2 ; i++) res.mat[i][i] = 1;
        while (b>0)
        {
            if (b&1) res = mul(res,a,mod);
            b = b >> 1LL;
            a = mul(a,a,mod);
        }
        return res;
    }
    LL gcd(LL a,LL b)
    {
        return b?gcd(b,a%b):a;
    }
    const int N = 1E6+7;
    bool prime[N];
    int p[N];
    void isprime() //一个普通的筛
    {
        int cnt = 0 ;
        ms(prime,true);
        for ( int i = 2 ; i < N ; i++)
        {
            if (prime[i])
            {
                p[cnt++] = i ;
                for ( int j = i+i ; j < N ; j+=i) prime[j] = false;
            }
        }
    }
    LL ksm( LL a,LL b,LL mod)
    {
       LL res = 1;
       while (b>0)
       {
           if (b&1) res = (res * a) % mod;
           b = b >> 1LL;
           a = a * a % mod;
       }
       return res;
    }
    LL legendre(LL a,LL p) //勒让德符号,判断二次剩余
    {
        if (ksm(a,(p-1)>>1,p)==1) return 1;
        return -1;
    }
    LL pri[N],num[N];//分解质因数的底数和指数。
    int cnt; //质因子的个数
    void solve(LL n,LL pri[],LL num[])
    {
        cnt = 0 ;
        for ( int  i = 0 ; p[i] * p[i] <= n ; i++)
        {
            if (n%p[i]==0)
            {
                int Num = 0 ;
                pri[cnt] = p[i];
                while (n%p[i]==0)
                {
                    Num++;
                    n/=p[i];
                }
                num[cnt] = Num;
                cnt++;
            }
        }
        if (n>1)
        {
            pri[cnt] = n;
            num[cnt] = 1;
            cnt++;
        }
    }
    LL fac[N];
    int cnt2; //n的因子的个数
    void get_fac(LL n)//得到n的所有因子
    {
        cnt2 = 0 ;
        for (int i =  1 ; i*i <= n ; i++)
        {
            if (n%i==0)
            {
                if (i*i!=n)
                {
                    fac[cnt2++] = i ;
                    fac[cnt2++] = n/i;
                }
                else fac[cnt2++] = i;
            }
        }
    }
    LL find_loop(LL n)
    {
        solve(n,pri,num);
        LL ans = 1;
        for ( int i = 0 ; i < cnt ; i++)
        {
            LL rec = 1;
            if (pri[i]==2) rec = 3;
            else if (pri[i]==3) rec = 8;
            else if (pri[i]==5) rec = 20;
            else
            {
                if (legendre(5,pri[i])==1)
                    get_fac(pri[i]-1);
                else get_fac(2*pri[i]+2);
                sort(fac,fac+cnt2);
                for ( int j = 0 ; j < cnt2 ; j++) //挨个验证因子
                {
                    Mat tmp = mat_ksm(M,fac[j],pri[i]); //下标从0开始，验证fac[j]为循环节，应该看fib[0]==fib[fac[j]]和fib[1]==fib[fac[j]+1]是否成立
                    tmp = mul(tmp,M1,pri[i]);
                    if (tmp.mat[0][0]==1&&tmp.mat[1][0]==1)
                    {
                        rec = fac[j];
                        break;
                    }
                }
     
            }
            for ( int j = 1 ; j < num[i] ; j++)
                rec *=pri[i];
            ans = ans / gcd(ans,rec) * rec;
        }
        return ans;
    }
    void init()
    {
        M.clear();
        M.mat[0][1] = M.mat[1][0] = M.mat[1][1] = 1;
        M1.clear();
        M1.mat[0][0] = M1.mat[1][0] = 1;
    }
    int main()
    {
            #ifndef  ONLINE_JUDGE 
            freopen("code/in.txt","r",stdin);
      #endif
            int T;
            int cas = 0 ;
            isprime();
            scanf("%d",&T);
            while (T--)
            {
                init();
                scanf("%lld",&P);
                printf("Case #%d: ",++cas);
                LL ret = find_loop(P);
                printf("%lld\n",ret);
            }
     
      #ifndef ONLINE_JUDGE  
      fclose(stdin);
      #endif
        return 0;
    }
    




