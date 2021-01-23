---
author: 111qqz
date: 2018-05-04 03:48:37+00:00
draft: false
title: C++ IO Streams 学习笔记
type: post
url: /2018/05/cpp-io-streams-notes/
categories:
- 其他
tags:
- c++
---

迫于拙劣的cpp水平，来补补以前忽略掉的cpp细节。

老规矩，先放资料。

参考资料:

[A Gentle Introduction to C++ IO Streams](https://www.cprogramming.com/tutorial/c++-iostreams.html)


<blockquote>"Designing and implementing a general input/output facility for a
programming language is notoriously difficult"
- Bjarne Stroustrup</blockquote>




### Stream的基本认识


说说我的理解。stream(流)可以看做输入输出的抽象。我们通过流可以忽略掉device的细节，采取同样的输入输出方式。

对于任何原生的cpp类型，都可以用stream来处理。用户自定义的类，也可以通过重载<<和>>而让stream可以处理。

    
    #include <iostream>
    #include <ctime>
    #include <sstream>
    #include <fstream>
     
    using namespace std;
     
    // timestamp returns the current time as a string 
    std::string timestamp();    
     
    class LogStatement;
    ostream& operator<<(ostream& ost, const LogStatement& ls);
     
    class LogStatement
    {
    public:
            LogStatement(std::string s): data(s), time_string( timestamp() )
            { };
     
            //This method handles all the outputs.    
            friend ostream& operator<<(ostream&, const LogStatement&);   
    private:
            std::string data;
            std::string time_string;
        
    };
     
    ostream& operator<<(ostream& ost, const LogStatement& ls)
    {
            ost<<"~|"<<ls.time_string<<'|'<<ls.data<<"|~";
            return ost;
    }
     
    std::string timestamp() 
    {
            //Notice the use of a stringstream, yet another useful stream medium!
            ostringstream stream;    
            time_t rawtime;
            tm * timeinfo;
     
            time(&rawtime);
            timeinfo = localtime( &rawtime );
     
            stream << (timeinfo->tm_year)+1900<<" "<<timeinfo->tm_mon
            <<" "<<timeinfo->tm_mday<<" "<<timeinfo->tm_hour
            <<" "<<timeinfo->tm_min<<" "<<timeinfo->tm_sec;
            // The str() function of output stringstreams return a std::string.
            return stream.str();   
    }
     
    int main(int argc, char** argv)
    {
            if(argc<2)
            {
                  // A return of -1 denotes an error condition.
                  return -1;  
            }
            ostringstream log_data;
            // This takes all the char arrays in the argv 
            // (except the filename) and produces a stream.
            for(int i=1;i<argc;i++)    
            {
                   log_data<<argv[i]<<' '; 
            }
      
            LogStatement log_entry(log_data.str());
     
            clog<<log_entry<<endl;
     
            ofstream logfile("logfile",ios::app);
     
            // check for errors opening the file
            if ( ! logfile )      
            {
                    return -1;
            }       
     
            logfile<<log_entry<<endl;
            logfile.close();
     
            return 0;
    }




stream大致分为inputstream和outputstream两种，分别对应的类型为std::istream和std::ostream.

stream大概有如下操作:



 	  *     使用适当的值类型(如stringstream的STD : : string和fstream的文件名)和适当的模式(如用于输入的IOs : : in和用于输出的IOs : : out等，具体取决于流的类型)初始化流
 	  * 可以通过get和put指针指定I / O应该发生的位置。根据您打开流的方式，可能已经适当地设置了位置(例如，如果使用IOs : : app打开文件，则在流的末尾设置get指针，允许附加)。

    
    seekg(0); seekg(0,ios::beg);         //sets the get pointer to the beginning.
    seekg(5,ios::beg);      //sets the get pointer to 5 chars forward of the beginning.
    tellp(); tellg()              //returns the current value of the put/get pointer
    seekp(-10,ios::end);   //sets the put pointer to 10 chars before the end
    seekp(1,ios::cur);      //proceeds to next char


注意:**如果需要在一个stream的中间位置插入数据的话，需要手动将指针位置后面的数据移动，否则会被覆盖掉。**
 	  * 使用<<或者>>来读或者写。



### stream的错误处理


将stream当成bool来处理是比较常见的，

    
    ifstream file( "test.txt" );
    if ( ! file )
    {
            cout << "An error occurred opening the file" << endl;
    }


但是实际上有四种status:



 	  * good() returns true when everything is okay.
 	  * bad() returns true when a fatal error has occurred.
 	  * fail() returns true after an unsuccessful stream operation like an unexpected type of input being encountered.
 	  * eof() returns true when the end of file is reached.



### String Streams


emm,其实string和stream好像挺像的。 区别是,string是可以随机访问的，stream是顺序访问。

    
    #include <iostream>
    #include <sstream>
     
    using namespace std;
     
    int main()
    {
            stringstream my_stream(ios::in|ios::out);
            std::string dat("Hey, I have a double : 74.79 .");
     
            my_stream.str(dat);
            my_stream.seekg(-7,ios::end);
     
            double val;
            my_stream>>val;
     
            val= val*val;
     
            my_stream.seekp(-7,ios::end);
            my_stream<<val;
     
            std::string new_val = my_stream.str();
            cout<<new_val;
     
            return 0;
    }


输出是:

    
    Hey, I have a double : 5593.54


我们观察到原本句子末尾的英文句号"."被覆盖掉了。


### buffer的使用


I/O操作是相对来说比较花时间的操作，如果我们要多次写很多小文件，那会浪费大量的时间。于是我们的想法是，使用一个临时的Buffer将数据存起来，当这个buffer满了之后再去读或者写。

注意不是所有的stream都采用了这种机制，比如cerr就没有采用。

下面放一段代码来感受下buffer

    
    #include <iostream>
    #include <string>
    
    using std::cout;    using std::endl;
    using std::cerr;    using std::ostream;
    using std::string;
    
    /*
     * A helpful function that halts the program until
     * the user presses enter.
     */
    void waitForEnter(const string& msg) {
        cout << msg;
        string l;
        std::getline(std::cin, l);
        cout << endl;
    }
    
    
    /*
     * Tests the buffer without flushing anything.
     *
     * Tries outputting a string to the stream, then does some slow
     * operation and then ouputs another string to the stream. We
     * see nothing is printed for a while then everything is printed at
     * once, suggesting cout is buffered.
     */
    void testBuffer(ostream& os) {
        os << "Before loop - ";
        for(int i = 0; i < 2000000000; ++i) {
            // waste time
        }
        os << "After loop" << endl;
    }
    
    /*
     * Tests the buffer with flushing.
     *
     * Here we see that the first string is printed
     * to the console, and then there is a delay due to
     * the for loop before the second string is printed.
     */
    void testBufferFlush(ostream& os) {
        os << "Before loop - " << std::flush;
        for(int i = 0; i < 2000000000; ++i) {
            // waste time
        }
        os << "After loop" << endl;
    }
    
    
    
    int main() {
           waitForEnter("Enter to continue: ");
           cout << "Testing cout..." << endl;
           testBuffer(cout);
           cout << endl;
    
           /* Prints a line of 20 = characters. */
           cout << string(20, '=') << endl;
    
           waitForEnter("Enter to continue: ");
           cout << "Testing flushed cout..." << endl;
           testBufferFlush(cout);
           cout << endl;
    }
    




此处flush的含义是将buffer中的内容立即输出

我们观察发现，在testBUffer中，"before loop"是在循环之后才输出的。暗示cout使用了buffer.










