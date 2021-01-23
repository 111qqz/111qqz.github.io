---
author: 111qqz
date: 2018-04-19 15:58:40+00:00
draft: false
title: levelDB 学习笔记
type: post
url: /2018/04/leveldb-notes/
categories:
- 其他
tags:
- levelDB
---

大三的时候看过一点levelDB的源码，不过没有怎么用过。

最近有个需求是存人脸的feature到硬盘，似乎使用levelDB比较合适，因此来学习一下使用。

先放参考资料。

关于levelDB的语法，看[这里](https://github.com/google/leveldb/blob/master/doc/index.md)就好了。

以及由于caffe中使用了levelDB，因此也可以参考下caffe源码。不过caffe中对levelDB的使用是又封装了一层。

具体可以参考：

    
    #ifdef USE_LEVELDB
    #ifndef CAFFE_UTIL_DB_LEVELDB_HPP
    #define CAFFE_UTIL_DB_LEVELDB_HPP
    
    #include <string>
    
    #include "leveldb/db.h"
    #include "leveldb/write_batch.h"
    
    #include "caffe/util/db.hpp"
    
    namespace caffe { namespace db {
    
    class LevelDBCursor : public Cursor {
     public:
      explicit LevelDBCursor(leveldb::Iterator* iter)
        : iter_(iter) {
        SeekToFirst();
        CHECK(iter_->status().ok()) << iter_->status().ToString();
      }
      ~LevelDBCursor() { delete iter_; }
      virtual void SeekToFirst() { iter_->SeekToFirst(); }
      virtual void Next() { iter_->Next(); }
      virtual string key() { return iter_->key().ToString(); }
      virtual string value() { return iter_->value().ToString(); }
      virtual bool valid() { return iter_->Valid(); }
    
     private:
      leveldb::Iterator* iter_;
    };
    
    class LevelDBTransaction : public Transaction {
     public:
      explicit LevelDBTransaction(leveldb::DB* db) : db_(db) { CHECK_NOTNULL(db_); }
      virtual void Put(const string& key, const string& value) {
        batch_.Put(key, value);
      }
      virtual void Commit() {
        leveldb::Status status = db_->Write(leveldb::WriteOptions(), &batch_);
        CHECK(status.ok()) << "Failed to write batch to leveldb "
                           << std::endl << status.ToString();
      }
    
     private:
      leveldb::DB* db_;
      leveldb::WriteBatch batch_;
    
      DISABLE_COPY_AND_ASSIGN(LevelDBTransaction);
    };
    
    class LevelDB : public DB {
     public:
      LevelDB() : db_(NULL) { }
      virtual ~LevelDB() { Close(); }
      virtual void Open(const string& source, Mode mode);
      virtual void Close() {
        if (db_ != NULL) {
          delete db_;
          db_ = NULL;
        }
      }
      virtual LevelDBCursor* NewCursor() {
        return new LevelDBCursor(db_->NewIterator(leveldb::ReadOptions()));
      }
      virtual LevelDBTransaction* NewTransaction() {
        return new LevelDBTransaction(db_);
      }
    
     private:
      leveldb::DB* db_;
    };
    
    
    }  // namespace db
    }  // namespace caffe
    
    #endif  // CAFFE_UTIL_DB_LEVELDB_HPP
    #endif  // USE_LEVELDB
    




    
    #ifndef CAFFE_UTIL_DB_HPP
    #define CAFFE_UTIL_DB_HPP
    
    #include <string>
    
    #include "caffe/common.hpp"
    #include "caffe/proto/caffe.pb.h"
    
    namespace caffe { namespace db {
    
    enum Mode { READ, WRITE, NEW };
    
    class Cursor {
     public:
      Cursor() { }
      virtual ~Cursor() { }
      virtual void SeekToFirst() = 0;
      virtual void Next() = 0;
      virtual string key() = 0;
      virtual string value() = 0;
      virtual bool valid() = 0;
    
      DISABLE_COPY_AND_ASSIGN(Cursor);
    };
    
    class Transaction {
     public:
      Transaction() { }
      virtual ~Transaction() { }
      virtual void Put(const string& key, const string& value) = 0;
      virtual void Commit() = 0;
    
      DISABLE_COPY_AND_ASSIGN(Transaction);
    };
    
    class DB {
     public:
      DB() { }
      virtual ~DB() { }
      virtual void Open(const string& source, Mode mode) = 0;
      virtual void Close() = 0;
      virtual Cursor* NewCursor() = 0;
      virtual Transaction* NewTransaction() = 0;
    
      DISABLE_COPY_AND_ASSIGN(DB);
    };
    
    DB* GetDB(DataParameter::DB backend);
    DB* GetDB(const string& backend);
    
    }  // namespace db
    }  // namespace caffe
    
    #endif  // CAFFE_UTIL_DB_HPP
    




    
    #ifdef USE_LEVELDB
    #include "caffe/util/db_leveldb.hpp"
    
    #include <string>
    
    namespace caffe { namespace db {
    
    void LevelDB::Open(const string& source, Mode mode) {
      leveldb::Options options;
      options.block_size = 65536;
      options.write_buffer_size = 268435456;
      options.max_open_files = 100;
      options.error_if_exists = mode == NEW;
      options.create_if_missing = mode != READ;
      leveldb::Status status = leveldb::DB::Open(options, source, &db_);
      CHECK(status.ok()) << "Failed to open leveldb " << source
                         << std::endl << status.ToString();
      LOG(INFO) << "Opened leveldb " << source;
    }
    
    }  // namespace db
    }  // namespace caffe
    #endif  // USE_LEVELDB
    




    
    #include "caffe/util/db.hpp"
    #include "caffe/util/db_leveldb.hpp"
    #include "caffe/util/db_lmdb.hpp"
    
    #include <string>
    
    namespace caffe { namespace db {
    
    DB* GetDB(DataParameter::DB backend) {
      switch (backend) {
    #ifdef USE_LEVELDB
      case DataParameter_DB_LEVELDB:
        return new LevelDB();
    #endif  // USE_LEVELDB
    #ifdef USE_LMDB
      case DataParameter_DB_LMDB:
        return new LMDB();
    #endif  // USE_LMDB
      default:
        LOG(FATAL) << "Unknown database backend";
        return NULL;
      }
    }
    
    DB* GetDB(const string& backend) {
    #ifdef USE_LEVELDB
      if (backend == "leveldb") {
        return new LevelDB();
      }
    #endif  // USE_LEVELDB
    #ifdef USE_LMDB
      if (backend == "lmdb") {
        return new LMDB();
      }
    #endif  // USE_LMDB
      LOG(FATAL) << "Unknown database backend";
      return NULL;
    }
    
    }  // namespace db
    }  // namespace caffe
    



    
    // This program converts a set of images to a lmdb/leveldb by storing them
    // as Datum proto buffers.
    // Usage:
    //   convert_imageset [FLAGS] ROOTFOLDER/ LISTFILE DB_NAME
    //
    // where ROOTFOLDER is the root folder that holds all the images, and LISTFILE
    // should be a list of files as well as their labels, in the format as
    //   subfolder1/file1.JPEG 7
    //   ....
    
    #include <algorithm>
    #include <fstream>  // NOLINT(readability/streams)
    #include <string>
    #include <utility>
    #include <vector>
    
    #include "boost/scoped_ptr.hpp"
    #include "gflags/gflags.h"
    #include "glog/logging.h"
    
    #include "caffe/proto/caffe.pb.h"
    #include "caffe/util/db.hpp"
    #include "caffe/util/format.hpp"
    #include "caffe/util/io.hpp"
    #include "caffe/util/rng.hpp"
    
    using namespace caffe;  // NOLINT(build/namespaces)
    using std::pair;
    using boost::scoped_ptr;
    
    DEFINE_bool(gray, false,
        "When this option is on, treat images as grayscale ones");
    DEFINE_bool(shuffle, false,
        "Randomly shuffle the order of images and their labels");
    DEFINE_string(backend, "lmdb",
            "The backend {lmdb, leveldb} for storing the result");
    DEFINE_int32(resize_width, 0, "Width images are resized to");
    DEFINE_int32(resize_height, 0, "Height images are resized to");
    DEFINE_bool(check_size, false,
        "When this option is on, check that all the datum have the same size");
    DEFINE_bool(encoded, false,
        "When this option is on, the encoded image will be save in datum");
    DEFINE_string(encode_type, "",
        "Optional: What type should we encode the image as ('png','jpg',...).");
    
    int main(int argc, char** argv) {
    #ifdef USE_OPENCV
      ::google::InitGoogleLogging(argv[0]);
      // Print output to stderr (while still logging)
      FLAGS_alsologtostderr = 1;
    
    #ifndef GFLAGS_GFLAGS_H_
      namespace gflags = google;
    #endif
    
      gflags::SetUsageMessage("Convert a set of images to the leveldb/lmdb\n"
            "format used as input for Caffe.\n"
            "Usage:\n"
            "    convert_imageset [FLAGS] ROOTFOLDER/ LISTFILE DB_NAME\n"
            "The ImageNet dataset for the training demo is at\n"
            "    http://www.image-net.org/download-images\n");
      gflags::ParseCommandLineFlags(&argc, &argv, true);
    
      if (argc < 4) {
        gflags::ShowUsageWithFlagsRestrict(argv[0], "tools/convert_imageset");
        return 1;
      }
    
      const bool is_color = !FLAGS_gray;
      const bool check_size = FLAGS_check_size;
      const bool encoded = FLAGS_encoded;
      const string encode_type = FLAGS_encode_type;
    
      std::ifstream infile(argv[2]);
      std::vector<std::pair<std::string, int> > lines;
      std::string line;
      size_t pos;
      int label;
      while (std::getline(infile, line)) {
        pos = line.find_last_of(' ');
        label = atoi(line.substr(pos + 1).c_str());
        lines.push_back(std::make_pair(line.substr(0, pos), label));
      }
      if (FLAGS_shuffle) {
        // randomly shuffle data
        LOG(INFO) << "Shuffling data";
        shuffle(lines.begin(), lines.end());
      }
      LOG(INFO) << "A total of " << lines.size() << " images.";
    
      if (encode_type.size() && !encoded)
        LOG(INFO) << "encode_type specified, assuming encoded=true.";
    
      int resize_height = std::max<int>(0, FLAGS_resize_height);
      int resize_width = std::max<int>(0, FLAGS_resize_width);
    
      // Create new DB
      scoped_ptr<db::DB> db(db::GetDB(FLAGS_backend));
      db->Open(argv[3], db::NEW);
      scoped_ptr<db::Transaction> txn(db->NewTransaction());
    
      // Storing to db
      std::string root_folder(argv[1]);
      Datum datum;
      int count = 0;
      int data_size = 0;
      bool data_size_initialized = false;
    
      for (int line_id = 0; line_id < lines.size(); ++line_id) {
        bool status;
        std::string enc = encode_type;
        if (encoded && !enc.size()) {
          // Guess the encoding type from the file name
          string fn = lines[line_id].first;
          size_t p = fn.rfind('.');
          if ( p == fn.npos )
            LOG(WARNING) << "Failed to guess the encoding of '" << fn << "'";
          enc = fn.substr(p+1);
          std::transform(enc.begin(), enc.end(), enc.begin(), ::tolower);
        }
        status = ReadImageToDatum(root_folder + lines[line_id].first,
            lines[line_id].second, resize_height, resize_width, is_color,
            enc, &datum);
        if (status == false) continue;
        if (check_size) {
          if (!data_size_initialized) {
            data_size = datum.channels() * datum.height() * datum.width();
            data_size_initialized = true;
          } else {
            const std::string& data = datum.data();
            CHECK_EQ(data.size(), data_size) << "Incorrect data field size "
                << data.size();
          }
        }
        // sequential
        string key_str = caffe::format_int(line_id, 8) + "_" + lines[line_id].first;
    
        // Put in db
        string out;
        CHECK(datum.SerializeToString(&out));
        txn->Put(key_str, out);
    
        if (++count % 1000 == 0) {
          // Commit db
          txn->Commit();
          txn.reset(db->NewTransaction());
          LOG(INFO) << "Processed " << count << " files.";
        }
      }
      // write the last batch
      if (count % 1000 != 0) {
        txn->Commit();
        LOG(INFO) << "Processed " << count << " files.";
      }
    #else
      LOG(FATAL) << "This tool requires OpenCV; compile with USE_OPENCV.";
    #endif  // USE_OPENCV
      return 0;
    }


几个文件。。。感觉比看文档更有实际意义orz


### levelDB简介


Leveldb是google开源的一个高效率的K/V数据库.有如下特点：



 	  1. 首先，LevelDb是一个持久化存储的KV系统，和Redis这种内存型的KV系统不同，LevelDb不会像Redis一样狂吃内存，而是将大部分数据存储到磁盘上。
 	  2. 其次，LevleDb在存储数据时，是根据记录的key值有序存储的，就是说相邻的key值在存储文件中是依次顺序存储的，而应用可以自定义key大小比较函数，LevleDb会按照用户定义的比较函数依序存储这些记录。
 	  3. 再次，像大多数KV系统一样，LevelDb的操作接口很简单，基本操作包括写记录，读记录以及删除记录。也支持针对多条操作的原子批量操作。
 	  4. 另外，LevelDb支持数据快照(snapshot)功能，使得读取操作不受写操作影响，可以在读操作过程中始终看到一致的数据。
 	  5. 除此外，LevelDb还支持数据压缩等操作，这对于减小存储空间以及增快IO效率都有直接的帮助。
 	  6. LevelDb性能非常突出，官方网站报道其随机写性能达到40万条记录每秒，而随机读性能达到6万条记录每秒。总体来说，LevelDb的写操作要大大快于读操作，而顺序读写操作则大大快于随机读写操作。



### LevelDB的安装


以ubuntu14.04为例，但实际上除了路径可能不同，其他部分是系统无关的。

[leveldb_github地址](https://github.com/google/leveldb)

然后记得切换到指定tag

可以使用git tag命令得到,然后用git checkout命令切换，我这里使用的是1.20版本

之后直接执行make

之后将头文件拷贝到系统路径下：

    
    sudo cp -r include/leveldb /usr/include


编译之后分别会得到out-shared和out-static两个文件夹，分别是动态库和静态库

我们进入out-shared文件夹，讲libleveldb.so*的三个文件（有两个是链接）拷贝到/usr/lib下

然后用sudo ldconfig 命令将动态库加到缓存中。

我们用如下代码测试一下：

    
    #include <iostream>
    #include <cassert>
    #include <cstdlib>
    #include <string>
    #include <leveldb/db.h>
    using namespace std;
    int main(void)
    {
    	leveldb::DB *db;
    	leveldb::Options options;
    	options.create_if_missing=true;
    	leveldb::Status status = leveldb::DB::Open(options,"./testdb",&db);
    	assert(status.ok());
    	std::string key1="people";
    	std::string value1="jason";
    	std::string value;
    	leveldb::Status s=db->Put(leveldb::WriteOptions(),key1,value1);
    	if(s.ok())
    		s=db->Get(leveldb::ReadOptions(),"people",&value);
    	if(s.ok())
    		cout<<value<<endl;
    	else
    		cout<<s.ToString()<<endl;
    	delete db;
    	return 0;
    }


编译选项为：

g++ mytest.cc -o mytest -lpthread -lleveldb

如果运行得到jason，表示安装成功。




### LevelDB的使用


一些基本操作可以参考[github文档](https://github.com/google/leveldb/blob/master/doc/index.md)

不过发现levelDB的接口似乎只支持key和value都是string类型。。

然而对于人脸提取feature,实际上需要的是string映射到float**

,偶然发现caffe中使用了levelDB,

发现它的做法是使用protobuf将数据序列化，然后再存储。

[protobuf学习笔记](https://111qqz.com/wordpress/2018/04/protobuf/)




### 注意事项


记录一些踩坑的经历..

如果有100条数据，想要每10条存一个数据库，那么每１０条执行一次DB::Open就行了...不然会报错在put那里，导致core dumped










