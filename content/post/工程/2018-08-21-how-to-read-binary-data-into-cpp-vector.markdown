---
author: 111qqz
date: 2018-08-21 06:08:56+00:00
draft: false
title: 把二进制文件按字节读到vector中
type: post
url: /2018/08/how-to-read-binary-data-into-cpp-vector/
categories:
- 其他
tags:
- c++
---


    
    std::vector<unsigned char> readFromFile1(const char* filePath) {
        FILE* file = fopen(filePath, "rb");
        std::vector<unsigned char> result;
        if (file == nullptr) {
            return result;
        }
    
        // 获取文件大小，尽量一次读完
        size_t fileSize = getFileSize(file);
        if (fileSize != 0) {
            result.resize(fileSize);
            size_t n = fread(&result[0], 1, fileSize, file);
            assert(n <= fileSize);
            if (n != fileSize) {
                result.resize(n);
            }
        }
    
        // 在读取过程当中，有可能文件大小有变化，再尝试读取
        const size_t read_len = 1024;
        char buf[read_len];
        for (;;) {
            size_t n = fread(buf, 1, read_len, file);
            result.insert(result.end(), buf, buf + n);
            if (n < read_len) {
                break;
            }
        }
        fclose(file);
        return result;
    }




另外一种C++风格，但是性能较差的方法：




    
    std::vector<unsigned char> readFromFile2(const char* filePath) {
        std::ifstream inputFile(filePath, std::ios::binary);
        std::vector<unsigned char> fileData((std::istreambuf_iterator<char>(inputFile)),
                                            std::istreambuf_iterator<char>());
        return fileData;
    }
    
    



