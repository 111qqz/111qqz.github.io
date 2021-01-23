---
author: 111qqz
date: 2019-01-05 06:29:49+00:00
draft: false
title: codeforces hello 2019
type: post
url: /2019/01/codeforces-hello-2019/
categories:
- ACM
---

好久没玩cf了，竟然还能涨分（虽然我用的小号Orz)

三题，D应该是数学+DP...数学实在是忘干净了。。。

前面三题大体还好，都是1A,不过因为没有提前配置环境。。耽误了一些时间。。。[![](https://111qqz.com/wp-content/uploads/2019/01/123123.png)
](https://111qqz.com/wp-content/uploads/2019/01/123123.png)

A:给出一个扑克牌x，和另一个包含5个扑克牌的集合。问扑克牌x是否和扑克牌集合中至少一张扑克牌的花色或者数字相同。

不多说了。

B:一块钟表（只有一个指针），初始指向12点，需要拨动指针恰好n次(n<=15)，每次可能顺时针，也可能逆时针，拨动的角度范围在[1,180],问是否有一种方案，使得拨动n次后，指针回到12点。

思路：观察下数据范围,n最大才15，最多也不过2^15的情况...既然如此，不如暴力。

枚举的话我记得有三种方法来着。。。但是已经不记得怎么写了。。所以用了最朴素的办法。。。

    
    #include <bits/stdc++.h>
    using namespace std;
    const int inf = 0x3f3f3f3f;
    #define ms(a,x) memset(a,x,sizeof(a))
    typedef long long LL;
    int n;
    int a[30];
    vector<int>bin;
    void cal( int x)
    {
        bin.clear();
        while (x>0)
        {
            bin.push_back(x%2);
            x/=2;
        }
        while (bin.size()<n)
        {
            bin.push_back(0);
        }
    }
    int main()
    {
        cin>>n;
        for ( int i = 1 ; i <= n ; i++) cin>>a[i];
        if (n==1)
        {
            puts("NO");
            return 0;
        }
        int total = 1 << n;
        for ( int i = 0 ; i < total ; i++)
        {
            cal(i);
            int ang =  0;
            // for ( auto x : bin) cout<<x;
            // cout<<"bin size:"<<bin.size()<<endl;
            for ( int j = 0 ; j < bin.size() ; j++ )
            {
                int x = bin[j];
                // cout<<"x:"<<x;
                if (x==0) ang = ang + a[j+1];
                else ang = ang - a[j+1];
            }
            // cout<<endl;
            if (ang0==0)
            {
                puts("YES");
                return 0;
            }
            // cout<<endl;
        }
        puts("NO");
    
       
    
    
        
        
        return 0;
    }


C: 给出n(n<=1E5)个括号序列,括号序列可能不合法，现在要从这n个括号序列中，组成尽可能多的有序二元组，使得有序二元组的括号序列合法，并且每个括号序列只能出现在一个有序二元组中，现在问最多能组成多少这样的有序二元组。

思路：我们先考虑一下怎样的两个括号序列组成的有序二元组才是合法的有序序列。容易想到的是，如果两个括号序列本身都是合法的，那么组合在一起也一定是合法的。进一步，对于本身不合法的括号序列，容易知道，其必须只有一种没有完成匹配的括号方向，且该括号方向的数量与相反括号方向的数量相同，才能完成匹配。

因此做法是，对于括号序列预处理，得到该括号序列的状态（本身匹配为0，正数代表'('的个数，负数代表')'的个数，如果有两个方向同时存在，则直接舍弃掉，因为这种括号序列不可能组成合法的括号序列。预处理之后，用multiset搞一下。

代码写得比较乱...flag存的时候其实没必要存index...

    
    #include <bits/stdc++.h>
    using namespace std;
    const int inf = 0x3f3f3f3f;
    #define ms(a,x) memset(a,x,sizeof(a))
    typedef long long LL;
    const int N=1E5+7;
    int n;
    string st[N];
    // 0 for just ok, '-' for num of ), '+' for num of (
    vector< pair<int,int> >flag; // <id,state> 
    
    
    void solve(int index,string str)
    {
        stack<char>S;
        for ( auto ch : str)
        {
            if (S.empty())
            {
                S.push(ch);
                continue;
            }
            if (S.top()=='('&&ch==')')
            {
                S.pop();
                continue;
            }
            S.push(ch);
            // cout<<"S.size():"<<S.size()<<endl;
    
        }
        if (S.empty())  //自己匹配
        {
            flag.push_back(make_pair(0,index));
            // cout<<"empty stack here . just match"<<endl;
            return;
        }
        int  state = 0;
        // cout<<"S.size():"<<S.size()<<endl;
        int siz = S.size();
        while (!S.empty())
        {
            char x = S.top();
            // cout<<"x:"<<x<<endl;
            S.pop();
            if (state==0)
            {
                if (x=='(') state = 1;
                else state = -1;
            }
            else 
            {
                if (state==1&&x==')') return ;
                if (state==-1&&x=='(') return;
            }
        }
        state = state*siz;
        // cout<<"state in function"<<state<<endl;
        flag.push_back(make_pair(state,index));
    }
    int main()
    {
        cin>>n;
        for ( int i = 1; i <= n ; i++) cin>>st[i];
    
        for ( int i = 1; i <= n ; i++)
        {
            solve(i,st[i]);
        }
        if (flag.size()==0)
        {
            puts("0");
            return 0;
        }
        int ans = 0 ;
        int cnt = 0;
        // cout<<"flag size:"<<flag.size()<<endl;
        for ( auto pi:flag)
        {
            // cout<<"state:"<<pi.first<<endl;
            if (pi.first==0) cnt++;
        }
        ans = ans + cnt/2;
        multiset<int>posi,nega;
        set<int>setposi;
        for (auto pi:flag)
        {
            if (pi.first>0) {
                posi.insert(pi.first);
                setposi.insert(pi.first);
            }
            else if (pi.first<0) nega.insert(pi.first);
        }
        for ( auto x:setposi)
        {
            int tmp = min(posi.count(x),nega.count(-x));
            if (tmp==0) continue;
            // coutcoutcout<<"x:"<<x<<" "<<posi.count(x)<<" "<<nega.count(-x)<<endl;
            ans = ans + tmp;
        }
        cout<<ans<<endl;
    
        
        
        return 0;
    }


D:初始一个数n(n<=1E15)，k次操作，每次操作等概率将当前的数变为其因子中的一个。问k次操作之后，结果的期望是多少。

在@适牛的指导下，以及参考了官方题解。。写了出来。。

dp还是太弱了。。。。

比较重要的一点是，不需要考虑所有因子，只需要考虑质因子。

质因子的个数不超过50个（因为 2^50 > 1E15）

另外一个重要的是，对于每一个质因子的概率是积性函数，可以乘在一起。

因此问题变成了，对于一个质因子唯一的n，如何算所求的期望。

我们考虑dp[i][j]表示第i次操作后，质因子还剩j个的概率。

显然dp[0][tot]=1，其中 p^tot = n,p为某个质因子。

转移方程为：

dp[i][j] = sum(dp[i-1][jj]) (j=<jj<=tot)

然后最后结果的期望就是：sum(dp[k][j]*p^j) (0=<j<=tot)

还有一点，由于题目的输出要求，需要用到费马小定理求个逆元。。。

逆元相关的参考 [acdreamer的博客](https://blog.csdn.net/acdreamers/article/details/8220787)。。。

    
    #include <bits/stdc++.h>
    using namespace std;
    typedef long long LL;
    const int mod = 1E9 + 7;
    
    LL n;
    int k;
    vector<pair<LL, int>> fac; //分解质因数
    
    int mul(LL a, LL b)
    {
        // cout<<"a:"<<a <<"  b:"<<b<<" a*b "<< (int)((LL)a * b % mod)<<endl;
        return (int)((LL)a * b % mod);
    }
    void add (int &a,int b)
    {
        // cout<<"a:"<<a<<" b:"<<b<<endl;
        a = a + b;
        if (a>=mod) a-=mod;
    }
    
    int ksm(int a, LL b)
    {
        int ret = 1;
        while (b > 0)
        {
            if (b & 1)
                ret = mul(ret, a);
            a = mul(a, a);
            b = b >> 1;
        }
        return ret;
    }
    int inv(int a)
    {
        return ksm(a, mod - 2);
    }
    
    int main()
    {
        cin >> n >> k;
        for (LL i = 2; i * i <= n; i++)
        {
            int cnt = 0;
            if (n % i == 0)
            {
                while (n % i == 0)
                {
                    n /= i;
                    cnt++;
                }
                fac.push_back(make_pair(i, cnt));
            }
        }
        if (n > 1)
        {
            fac.push_back(make_pair(n, 1));
        }
        // check
        // for ( auto & p:fac) cout<<p.first<<" "<<p.second<<endl;
        int ans = 1;
        for (auto &p : fac)
        {
            int tot = p.second;
            vector<vector<int>> dp(k + 1, vector<int>(tot + 1, 0));
            dp[0][tot] = 1;
            for (int i = 0; i < k; i++)
            {
                for (int j = 0; j <= tot; j++)
                {
                    int cur = mul(dp[i][j], inv(j + 1));
                    // cout<<"cur:"<<cur<<endl
                    for (int t = 0; t <= j; t++)
                    {
                       add(dp[i+1][t],cur);
                    }
                }
            }
            int sum = 0;
            int P = 1;
            for (int j = 0; j <= tot; j++)
            {
                add(sum,mul(P, dp[k][j]));
                P = mul(P, int(p.first % mod));
            }
            // cout<<"sum:"<<sum<<endl;
            ans = mul(ans, sum);
        }
    
        cout << ans << endl;
        return 0;
    }













