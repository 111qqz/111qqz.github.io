---
author: 111qqz
date: 2016-08-16 08:54:53+00:00
draft: false
title: ac自动机模板by Lalatina （hdu 2222）
type: post
url: /2016/08/acby-lalatina-hdu-2222/
categories:
- ACM

tags:
- ac自动机
---

orzorz 日常%学弟  华科的未来orz

 

    
    #include <cstdio>
    #include <cstring>
    
    using namespace std;
    
    struct tnode {
        int s;
        tnode *f, *w, *c[26];
    } T[5000000], *Q[5000000];
    int C;
    
    inline tnode *tnew() {
        memset(T + C, 0, sizeof(tnode));
        return T + C++;
    }
    
    inline void AcaInsert(tnode *p, const char *s) {
        while (*s) {
            int u = *s - 'a';
            if (!p->c[u])
                p->c[u] = tnew();
            p = p->c[u];
            ++s;
        }
        ++p->s;
    }
    
    inline void AcaBuild(tnode *p) {
        p->f = p->w = p;
        int ql = 0;
        for (int i = 0; i < 26; ++i)
            if (p->c[i]) {
                p->c[i]->f = p->c[i]->w = p;
                Q[ql++] = p->c[i];
            }
        for (int qf = 0; qf < ql; ++qf)
            for (int i = 0; i < 26; ++i)
                if (Q[qf]->c[i]) {
                    tnode *f = Q[qf]->f;
                    while (f != p && !f->c[i])
                        f = f->f;
                    if (f->c[i]) {
                        Q[qf]->c[i]->f = f->c[i];
                        Q[qf]->c[i]->w = f->c[i]->s ? f->c[i] : f->c[i]->w;
                    }
                    else
                        Q[qf]->c[i]->f = Q[qf]->c[i]->w = p;
                    Q[ql++] = Q[qf]->c[i];
                }
    }
    
    inline int AcaMatch(tnode *root, const char *s) {
        int x = 0;
        for (tnode *p = root; *s; ++s) {
            while (p != root && !p->c[*s - 'a'])
                p = p->f;
            if (p->c[*s - 'a']) {
                p = p->c[*s - 'a'];
                for (tnode *q = p; q->s != -1; q = q->w) {
                    x += q->s;
                    q->s = -1;
                }
            }
        }
        return x;
    }
    
    char S[1000001];
    
    int main() {
        int tt;
        scanf("%d", &tt);
        while (tt--) {
            C = 0;
            tnode *root = tnew();
            root->s = -1;
            int N;
            scanf("%d", &N);
            while (N--) {
                scanf("%s", S);
                AcaInsert(root, S);
            }
            AcaBuild(root);
            scanf("%s", S);
            printf("%d\n", AcaMatch(root, S));
        }
        return 0;
    }



