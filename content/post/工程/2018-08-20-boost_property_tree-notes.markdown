---
author: 111qqz
date: 2018-08-20 08:10:16+00:00
draft: false
title: boost:property_tree 学习笔记
type: post
url: /2018/08/boost_property_tree-notes/
categories:
- 其他
tags:
- boost
- json
- property_tree
---

先放资料:

[How to use boost::property_tree to load and write JSON](http://zenol.fr/blog/boost-property-tree/en.html)

[How to iterate a boost property tree?](https://stackoverflow.com/questions/4586768/how-to-iterate-a-boost-property-tree)



不出现key的方法遍历一个json文件:

    
    /* ***********************************************
    Author :111qqz
    mail: renkuanze@sensetime.com
    Created Time :2018年08月17日 星期五 15时29分23秒
    File Name :ptree.cpp
    ************************************************ */
    #include <boost/property_tree/ptree.hpp>
    #include <boost/property_tree/json_parser.hpp>
    #include <bits/stdc++.h>
    #include <vector>
    using namespace std;
    using boost::property_tree::ptree;
    
    string indent(int level) {
      string s; 
      for (int i=0; i<level; i++) s += "  ";
      return s; 
    } 
    
    void printTree (ptree &pt, int level) {
      if (pt.empty()) {
        cerr << "\""<< pt.data()<< "\"";
      }
    
      else {
        if (level) cerr << endl; 
    
        cerr << indent(level) << "{" << endl;     
    
        for (ptree::iterator pos = pt.begin(); pos != pt.end();) {
          cerr << indent(level+1) << "\"" << pos->first << "\": "; 
    
          printTree(pos->second, level + 1); 
          ++pos; 
          if (pos != pt.end()) {
            cerr << ","; 
          }
          cerr << endl;
        } 
    
       cerr << indent(level) << " }";     
      }
    
      return; 
    }
    int main()
    {
    	ptree root;
    	read_json("terr.json",root);
    	printTree(root,0);
    
    
    	return 0;
    
    }
    



