---
author: 111qqz
date: 2017-11-04 07:07:26+00:00
draft: false
title: 【施工中】SAM学习笔记
type: post
url: /2017/11/suffix-automaton-notes/
categories:
- ACM
tags:
- 后缀自动机
---

<blockquote>***在学习后缀自动机之前需要熟练掌握WA自动机、RE自动机与TLE自动机***</blockquote>



<del>怕是老年人的最后一篇算法学习笔记了</del>

<del>心情不好，此文无限期tj</del>



# 概述



主要讲解在我学习的过程中比较难理解的地方..并不保证全面

首先，后缀自动机是一个能且只能接受一个字符串的所有后缀的确定性有限状态自动机，也就是[DFA](https://zh.wikipedia.org/wiki/)

SAM同时具有自动机和树的性质。



# 节点（状态）



SAM中的节点，也叫状态。

明确一个说法：“一个节点所表示的字符串”。

由于一个字符串的子串一定是某个后缀的前缀。

因此一个字符串的子串一定可以在SAM上运行。

**因此“一个节点Q所表示的字符串”的含义是说，从初始状态开始，运行该字符串后，到达的状态是Q.**

**一个节点所表示的字符串长度属于范围[MIN,MAX]，并且区间中每个长度的字符串都出现一次**

能表示的字符串长度范围有最大值很好理解，有最小值是因为：长度越小的字符串出现的位置越多，因此当长度小于MIN之后，其出现的位置增加。

由于后文见到，SAM中状态是终点位置集合的等价类，因此一个节点所表示的字符串长度存在一个最小值。

后文还问见到，一个节点的MIN恰好是其父亲节点的MAX+1



# 终点集合 (endpos / Right)



终点集合一般国内的资料叫right集合，国外好像更常见的叫法是endpos集合。

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/深度截图_选择区域_20171113124457.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/深度截图_选择区域_20171113124457.png)

其实就是对于一个子串a,其在母串S中出现的位置的右端点的集合。

那么这个right集合有什么作用呢？

考虑naive的做法，一个串S有O(n^2)的后缀，凉凉

那么我们发现，对于right集合相同的两个子串，代表其子串的状态（意思是说，从初始状态到该状态所表示的字符串）是可以合并的。

为什么？因为这两个子串的所有出现位置的右端点相同，那么在其后面添加若干字符得到的后缀也一定完全相同。

那么我们可以根据right集合，将字符串的子串分成若干个等价类

对于一个等价类，我们在SAM中用一个状态表示就行了。

接下来考虑right集合的性质。

right[v]表示状态v所表示的子串出现的次数。





# 后缀链/parent树



对于不为初始状态的所有状态，一个状态对应着一个等价类，令w作为其中最长的子串，其余的子串都是w的后缀。

w的所有后缀中，一部分在w所在的等价类中，另外一部分位于其他的等价类中。于是定义**后缀链**link(v)连接w所有后缀中**位于其他等价类**并且**长度最长**的那个后缀所在的等价类。

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/深度截图_选择区域_20171110203549.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/深度截图_选择区域_20171110203549.png)



那么根据后缀链的定义，以及后缀的长度是连续的(“后缀的长度是连续的”的含义是说，一个长度为k的字符串，一定有长度为k，为k-1，一直到长度为１的后缀）

因此一个节点的MIN恰好是其父亲节点的MAX+1　　（MIN,MAX分别表示一个节点所能表示的字符串的最小值和最大值）





# 复杂度



[后缀自动机·张的知乎专栏_震惊！SAM复杂度竟如此显然！](https://zhuanlan.zhihu.com/p/25948077)

%%%qc大爷





# 构造方法





<blockquote>这个算法是**在线**的，每次在构造好的自动机的基础上增加一个字符。

对于每个状态，需要保存lenlen、linklink以及转移状态信息。

**初始条件下**，自动机只包含一个起始状态t0t0，len=0len=0并且linklink指向-1。所有算法要做的就是给后缀自动机**增加一个新的字符**c。

> 
> 
      * 我们用lastlast来表示当前需要增加一个字符的状态，初始情况下last=0last=0，之后每次增加字符后都会修改。
      * 创建一个新的状态curcur，要求len(cur)=len(last)+1len(cur)=len(last)+1，linklink先留着。
      * 接下来进行这样的循环：从lastlast状态开始，如果不存在字符c的转移，那么增加一个到达curcur的字符c的转移，然后沿着后缀链继续检查——如果不存在字符串c的转移，那么增加一个转移；如果字符串c的转移已经存在，那么停止循环，将停止时检查的状态记为p。这个时候，会出现两种情况：

        * 如果一直没有遇到存在转移的状态，那么最终我们会到达伪状态-1，只需要让link(cur)=0link(cur)=0后退出。
        * 如果遇到存在字符c转移的状态，另q为转移到的状态，那么又有了两种情况：

          * 如果len(p)+1=len(q)len(p)+1=len(q)，只需要令link(cur)=qlink(cur)=q后退出。
          * 否则，创建一个新的状态cloneclone，将q的转移也拷贝给clone，令len(clone)=len(p)+1len(clone)=len(p)+1。然后，将状态cur和状态q的后缀链指向clone。最后需要完成的事情就是，遍历p的后缀链上的状态，如果存在指向状态q的字符c转移，那么将这个转移重定向到clone（如果不存在，遍历停止）




      * 在任何一种情况下，最后都需要将last设置为cur。

根据后缀链的定义，last开始的后缀链上的状态就是自动机的所有**终止**状态。</blockquote>









# 我的模板



<del>出于太懒的原因，没有封装</del>

**需要注意的是，状态数要开到字符串长度的２倍，以及预处理之前先拓扑**

**需要注意的是，状态数要开到字符串长度的２倍，以及预处理之前先拓扑**

**需要注意的是，状态数要开到字符串长度的２倍，以及预处理之前先拓扑**




    
    /* ***********************************************
    Author :111qqz
    Created Time :2017年11月15日 星期三 19时06分15秒
    File Name :SAM.cpp
    ************************************************ */
    
    #include <bits/stdc++.h>
    #define PB push_back
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
    const int N=5E5+7;
    struct SAM
    {
        #define MAXALP 30
        struct state
        {
        int len, link, nxt[MAXALP];
        int leftmost; //某个状态的right集合中r值最小的
        int rightmost;//某个状态的right集合的r的最大值
        int Right; //right集合大小
        };
        state st[N*2];
        char S[N];
        int sz, last,rt;
        LL tot_str; //子串总数   每个状态本质不同的子串数*出现的次数
        LL tot_unique_str; //本质不同的子串总数  st[v].len - st[st[v].link].len  (v属于1..sz)
        int cnt[2*N],rk[2*N];//for radix sort
        int idx(char c)
        {
        if (c>='a'&&c<='z') return c-'a';
        return c-'A'+26;
        }
        void init()
        {
        sz = 0;
        ms(st,0);
        last = rt = ++sz;
        st[1].len = 0;
        st[1].link=-1;
        st[1].rightmost=0;
        ms(st[1].nxt,-1);
        }
        void extend(int c,int head)
        {
        int cur = ++sz;
        st[cur].len = st[last].len + 1;
        st[cur].leftmost = st[cur].rightmost = head;
        memset(st[cur].nxt, -1, sizeof(st[cur].nxt));
        int p;
        for (p = last; p != -1 && st[p].nxt[c] == -1; p = st[p].link)
            st[p].nxt[c] = cur;
        if (p == -1) {
            st[cur].link = rt;
        } else {
            int q = st[p].nxt[c];
            if (st[p].len + 1 == st[q].len) {
    
            st[cur].link = q;
            } else {
            int clone = ++sz ;
            st[clone].len = st[p].len + 1;
            st[clone].link = st[q].link;
            memcpy(st[clone].nxt, st[q].nxt, sizeof(st[q].nxt));
            st[clone].leftmost = st[q].leftmost;
            st[clone].rightmost = st[q].rightmost;
            for (; p != -1 && st[p].nxt[c] == q; p = st[p].link)
                st[p].nxt[c] = clone;
            st[q].link = st[cur].link = clone;
            }
        }
        last = cur;
        }
        void build()
        {
        init();
        for ( int i = 0,_len = strlen(S) ; i < _len ; i++)
        {
            st[sz+1].Right = 1;
            extend(idx(S[i]),i);
        }
        }
        void topo()
        {
        ms(cnt,0); 
        for (int i = 1 ; i <= sz ; i++) cnt[st[i].len]++;
        for ( int i = 1 ; i <= sz ; i++) cnt[i]+=cnt[i-1];
        //rk[1]是len最小的状态的标号
        for (int i = 1 ; i <= sz  ;i++) rk[cnt[st[i].len]--] = i;
        }
        void pre()  //跑拓扑序，预处理一些东西
        {
        tot_str = tot_unique_str = 0;
        for ( int i = sz ; i >= 2 ; i--)
        {
            int v = rk[i];
            int fa = st[v].link;
            if (fa==-1) continue;
            tot_str += 1LL*st[v].Right*(st[v].len-st[fa].len);
            tot_unique_str += 1LL*(st[v].len-st[fa].len);
            st[fa].rightmost = max(st[fa].rightmost,st[v].rightmost);
            st[fa].Right += st[v].Right;
        }
        }
        void solve()
        {
        LL ans = 0 ;
        for ( int i = sz ; i >= 2 ; i--)
        {
            int v = rk[i];
            if (st[v].link==-1) continue;
            ans = ans + 1LL * st[v].Right*(st[v].Right+1)/2 * (st[v].len-st[st[v].link].len);
        }
        printf("%lld\n",ans);
        }
        int LCS(char *s)
        {
        int ans = 0,len = 0 ;
        int p = rt;
        for ( int i = 0 ,_len = strlen(s) ; i < _len ; i++)
        {
            int ID = s[i]-'a';
            if (st[p].nxt[ID]!=-1) p = st[p].nxt[ID],len++;
            else
            {
            while (p!=-1&&st[p].nxt[ID]==-1) p = st[p].link;
            if (p==-1) p=rt,len=0;else len = st[p].len+1,p = st[p].nxt[ID];
            }
          //  printf("len:%d\n",len);
            ans = max(ans,len);
        }
        return ans;
        }
    
        //把原串复制一遍到后面，然后构建后缀自动机。
        //从初始状态开始，每次走字典序最小的转移，走|S|之后得到的就是最小循环表示。
        //如果求的是最小后缀，就在原串后加入一个比字符集中所有字符的字典序都小的字符作为终止后，再添加一遍原串。
        int smallest_string()  //求一个串的最小循环表示，返回起始位置下标
        {
        int p = 1;
        int slen = strlen(S);
        for ( int i = 0 ; i < slen ; i++)
        {
            bool flag = false;
            for ( int j = 0 ; j < 26 ; j++) //找字典序最小的
            if (st[p].nxt[j])
            {
                flag = true;
                p = st[p].nxt[j];
                break;
            }
            if (!flag) break;
        }
        return st[p].len + 1 - slen;
        }
    }A;
    char B[N]; 
    int main()
    {
    #ifndef  ONLINE_JUDGE 
        freopen("./in.txt","r",stdin);
    #endif
        int T;
        cin>>T;
        while (T--)
        {
        cin>>A.S;
        A.build();
        int ans = A.smallest_string();
        cout<<ans<<endl;
        }
    #ifndef ONLINE_JUDGE  
        fclose(stdin);
    #endif
        return 0;
    }
     
     
     
    
    

















[SA&&SAM论文](https://drive.google.com/drive/folders/1iamJKc9RzL3uxcwtaPPPsczAm8TwnEM0?usp=sharing)

[ SAM学习指南](http://blog.csdn.net/cyendra/article/details/37993603)



[fanhq666_后缀自动机与线性构造后缀树](http://fanhq666.blog.163.com/blog/static/8194342620123352232937/)

[后缀自动机（SAM）](http://www.cnblogs.com/zinthos/p/3899679.html)






