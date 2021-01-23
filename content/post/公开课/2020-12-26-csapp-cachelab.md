---
title: "[施工完成] CSAPP Cachelab"
date: 2020-12-26T16:40:42+08:00
draft: false
author: "111qqz"
type: post
url: /2020/
categories:
- mooc

tags:

- CSAPP

---


## 背景

CSAPP:3e 的配套实验 [地址](http://csapp.cs.cmu.edu/3e/README-cachelab)
分成了两个部分，第一部分是模拟一下cache的miss,hit,evict的规则。第二部分是优化一个矩阵的转置，使得miss尽可能少。

## PART A

给了一个标程csim-ref,要求实现一个程序，输出与该标程一致。

写的时候太心急了。。导致没看完作业要求就开始写了。。  然后就纠结了好久。。如果要访问的地址超过了一个block line的边界该怎么办。。

然而实际上题目里已经把这种情况排除了。。

> For this this lab, you should assume that memory accesses are aligned properly, such that a single
memory access never crosses block boundaries. By making this assumption, you can ignore the
request sizes in the valgrind traces

这样的话。。就没什么难度了。。
LRU的替换策略用纯c去撸hashmap+list有点烦。。。干脆就写了暴力的实现。。反正是模拟题(x

```c++

#include <getopt.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "cachelab.h"

const unsigned int address_space_size = 64;
// https://stackoverflow.com/questions/9642732/parsing-command-line-arguments-in-c

typedef struct {
  bool verbose;
  int set_index_bits;
  int lines_per_set;
  int block_bits;
  char *tracefile;

} Arg;

void ParseArgs(int argc, char **argv, Arg *arg) {
  int opt;
  while ((opt = getopt(argc, argv, "hvs:E:b:t:")) != -1) {
    switch (opt) {
      case 'h':
        printf("Usage: ./csim-ref [-hv] -s <s> -E <E> -b <b> -t <tracefile>\n");
        break;
      case 'v':
        arg->verbose = true;
        break;
      case 's':
        arg->set_index_bits = atoi(optarg);
        break;
      case 'E':
        arg->lines_per_set = atoi(optarg);
        break;
      case 'b':
        arg->block_bits = atoi(optarg);
        break;
      case 't':
        arg->tracefile = optarg;
        break;
      default:
        abort();
    }
  }
}

typedef unsigned long long ULL;
// 注意: 地址是十六进制表示。。。debug 到去世。。
typedef struct {
  ULL tag_bits;
  ULL index_bits;
  ULL offset_bits;
  ULL block_number;

} AddressBits;
// 64 bit address,m=64
// tag bit t = m-(b+s)
// parse 64 address bits into tag bits,index bits and offset bits
void ParseAddress(const Arg *arg, const ULL raw_addr, AddressBits *addr) {
  const unsigned int index_and_block_bit_length =
      arg->block_bits + arg->set_index_bits;
  ULL block_bit_mask = (1ULL << arg->block_bits) - 1;
  ULL index_bit_mask = ((1ULL << arg->set_index_bits) - 1) << arg->block_bits;
  ULL tag_bit_mask =
      ((1ULL << (address_space_size - index_and_block_bit_length)) - 1)
      << index_and_block_bit_length;
  // printf("index_and_block_bit_length:%d\n",index_and_block_bit_length);
  // printf("mask:%lld %lld %lld\n", block_bit_mask, index_bit_mask,
  // tag_bit_mask);
  addr->tag_bits = (raw_addr & tag_bit_mask) >> index_and_block_bit_length;
  addr->index_bits = (raw_addr & index_bit_mask) >> arg->block_bits;
  addr->offset_bits = raw_addr & block_bit_mask;
  addr->block_number = raw_addr / (1ULL << arg->block_bits);
  // printf("addr:%llx tag:%lld index:%lld osset:%lld block:%lld \n", raw_addr,
  //        addr->tag_bits, addr->index_bits, addr->offset_bits,
  //        addr->block_number);
}
void TestParseAddress(const Arg *arg) {
  for (int addr = 0; addr < (1ULL << address_space_size); addr++) {
    AddressBits tmp_addr;
    ParseAddress(arg, addr, &tmp_addr);
  }
}
typedef struct {
  enum operation { instruction_load, data_load, data_store, data_modify } op;
  ULL address;
  int size;
} Trace;
#define MAX_NUM_OF_TRACE 300000
Trace trace[MAX_NUM_OF_TRACE];
int lines_in_trace_file = 0;
void ParseTraceFile(const char *file) {
  FILE *fptr = fopen(file, "r");
  if (fptr == NULL) {
    printf("Error!");
    exit(1);
  }

  char op[5];
  ULL addr;
  int cnt = 0, siz;
  while (fscanf(fptr, "%s %llx,%d", op, &addr, &siz) != EOF) {
    // printf("op:%s addr:%lld size:%d\n", op, addr, siz);
    trace[cnt].address = addr;
    trace[cnt].size = siz;
    if (op[0] == 'L') {
      trace[cnt].op = data_load;
    } else if (op[0] == 'I') {
      trace[cnt].op = instruction_load;
    } else if (op[0] == 'S') {
      trace[cnt].op = data_store;
    } else if (op[0] == 'M') {
      trace[cnt].op = data_modify;
    }
    cnt++;
  }
  lines_in_trace_file = cnt;

  fclose(fptr);
}

void TestParseTraceFile() {
  char *file = "direct-mapped-4-bit.trace";
  ParseTraceFile(file);
}

// 不需要真的做cache,只需要模拟hit,miss,evition 的次数即可

typedef struct {
  unsigned int valid;
  unsigned int tag;
  // used for LRU policy
  // use line number of trace file as age
  // the smallest age is the least recent used line
  unsigned int age;
} Line;

typedef struct {
  int num_of_lines;
  Line *lines;
} Set;

Set *set;
struct cache_summary_t {
  int hits;
  int misses;
  int evitions;
} cache_summary;
char operation_table[5] = {'I', 'L', 'S', 'M'};

bool CheckCacheLineHit(const AddressBits addr, Set *cur_set, const int index) {
  bool any_of_line_hit = false;
  for (int j = 0; j < cur_set->num_of_lines; j++) {
    Line *cur_line = &cur_set->lines[j];
    if (cur_line->valid == 1 && cur_line->tag == addr.tag_bits) {
      // printf("addr.tag_bits:%lld\n", addr.tag_bits);
      cache_summary.hits++;
      cur_line->age = index;
      any_of_line_hit = true;
      break;
    }
  }
  return any_of_line_hit;
}

bool CheckCacheLineEmpty(const AddressBits addr, Set *cur_set,
                         const int index) {
  bool any_of_line_empty = false;
  for (int j = 0; j < cur_set->num_of_lines; j++) {
    Line *cur_line = &cur_set->lines[j];
    if (cur_line->valid == 0) {
      cache_summary.misses++;
      cur_line->valid = 1;
      cur_line->tag = addr.tag_bits;
      cur_line->age = index;

      any_of_line_empty = true;
      break;
    }
  }
  return any_of_line_empty;
}

void NaiveLru(const AddressBits addr, Set *cur_set, const int index) {
  int evict_line;
  int min_age = lines_in_trace_file;
  // printf("set[%lld]->num_of_lines:%d\n",addr.index_bits,cur_set->num_of_lines);
  for (int j = 0; j < cur_set->num_of_lines; j++) {
    Line *cur_line = &cur_set->lines[j];
    // printf("cur_line age:%d\n",cur_line->age);
    if (cur_line->age < min_age) {
      min_age = cur_line->age;
      evict_line = j;
    }
  }
  // printf("evict_line:%d min_age:%d\n",evict_line,min_age);
  cache_summary.misses++;
  cache_summary.evitions++;
  cur_set->lines[evict_line].tag = addr.tag_bits;
  cur_set->lines[evict_line].age = index;
}

void EvicteCacheLine(const AddressBits addr, Set *cur_set, const int index) {
  // I'm too lazy to use Doubly linked list and hashmap
  NaiveLru(addr, cur_set, index);
}

void SimulateCache(const Arg *arg) {
  memset(&cache_summary, 0, sizeof(cache_summary));
  //   instruction_load, data_load, data_store, data_modify

  for (int i = 0; i < lines_in_trace_file; i++) {
    // ignore instruction load
    if (trace[i].op == 0) continue;
    AddressBits addr;
    ParseAddress(arg, trace[i].address, &addr);
    Set *cur_set = &set[addr.index_bits];
    // data load or data store
    if (trace[i].op <= 2) {
      bool any_of_line_hit = CheckCacheLineHit(addr, cur_set, i);
      if (any_of_line_hit) {
        if (arg->verbose) {
          printf("%c %lld,%d hit\n", operation_table[trace[i].op],
                 trace[i].address, trace[i].size);
        }
        continue;
      }
      bool any_of_line_empty = CheckCacheLineEmpty(addr, cur_set, i);
      if (any_of_line_empty) {
        if (arg->verbose) {
          printf("%c %lld,%d miss\n", operation_table[trace[i].op],
                 trace[i].address, trace[i].size);
        }
        continue;
      }
      EvicteCacheLine(addr, cur_set, i);
      if (arg->verbose) {
        printf("%c %lld,%d miss eviction\n", operation_table[trace[i].op],
               trace[i].address, trace[i].size);
      }
    } else {
      // data modify
      bool any_of_line_hit_in_data_load = CheckCacheLineHit(addr, cur_set, i);
      if (any_of_line_hit_in_data_load) {
        // if 'data load' hit cache, then 'data store' must also hit cache
        cache_summary.hits++;
        if (arg->verbose) {
          printf("%c %lld,%d hit hit \n", operation_table[trace[i].op],
                 trace[i].address, trace[i].size);
        }
        continue;
      }
      bool any_of_line_empty = CheckCacheLineEmpty(addr, cur_set, i);
      if (any_of_line_empty) {
        cache_summary.hits++;
        if (arg->verbose) {
          printf("%c %lld,%d miss hit\n", operation_table[trace[i].op],
                 trace[i].address, trace[i].size);
        }
        continue;
      }
      EvicteCacheLine(addr, cur_set, i);
      if (arg->verbose) {
        cache_summary.hits++;
        printf("%c %lld,%d miss eviction hit\n", operation_table[trace[i].op],
               trace[i].address, trace[i].size);
      }
    }
  }
}
int main(int argc, char **argv) {
  Arg arg;
  ParseArgs(argc, argv, &arg);
  ParseTraceFile(arg.tracefile);
  int total_set_num = 1 << arg.set_index_bits;
  // printf("total_set_num:%d\n",total_set_num);
  set = (Set *)malloc(total_set_num * sizeof(Set));
  memset(set, 0, total_set_num * sizeof(Set));
  for (int i = 0; i < total_set_num; i++) {
    set[i].lines = (Line *)malloc(arg.lines_per_set * sizeof(Line));
    memset(set[i].lines, 0, arg.lines_per_set * sizeof(Line));
    set[i].num_of_lines = arg.lines_per_set;
  }
  SimulateCache(&arg);
  printSummary(cache_summary.hits, cache_summary.misses,
               cache_summary.evitions);

  for (int i = 0; i < total_set_num; i++) {
    free(set[i].lines);
  }
  free(set);

  return 0;
}


```


## PART B

三个小题。。矩阵的size分别是:
- 32*32
- 64*64
- 61*67

很重要的一点是。。输入就是这三组固定值。。。**题目是允许根据不同的输入。。来用不同的实现应对的。**

###  32*32

```c++

int tmp, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7;
    for (int i = 0; i < N; i += 8) {
      for (int j = 0; j < M; j++) {
        tmp = A[i][j];
        tmp1 = A[i + 1][j];
        tmp2 = A[i + 2][j];
        tmp3 = A[i + 3][j];
        tmp4 = A[i + 4][j];
        tmp5 = A[i + 5][j];
        tmp6 = A[i + 6][j];
        tmp7 = A[i + 7][j];
        B[j][i] = tmp;
        B[j][i + 1] = tmp1;
        B[j][i + 2] = tmp2;
        B[j][i + 3] = tmp3;
        B[j][i + 4] = tmp4;
        B[j][i + 5] = tmp5;
        B[j][i + 6] = tmp6;
        B[j][i + 7] = tmp7;
      }
    }

```

### 61*67

```c++

 int tmp[8];
    for (int block_i_start = 0; block_i_start < N; block_i_start += 8) {
      for (int block_j_start = 0; block_j_start < M; block_j_start += 8) {
        for (int i = block_i_start; i < min(block_i_start + 8, N); i++) {
          for (int j = block_j_start; j < min(M, block_j_start + 8); j++) {
            tmp[j - block_j_start] = A[i][j];
          }
          for (int j = block_j_start; j < min(M, block_j_start + 8); j++) {
            B[j][i] = tmp[j - block_j_start];
          }
         
        }
      }
    }
```

### 64*64

略难。。留个坑。。日后填

## 最终分数

64*64的没拿到分数。。其他部分是满分

```shell

Cache Lab summary:
                        Points   Max pts      Misses
Csim correctness          27.0        27
Trans perf 32x32           8.0         8         287
Trans perf 64x64           0.0         8        4723
Trans perf 61x67          10.0        10        1997
          Total points    45.0        53

```
