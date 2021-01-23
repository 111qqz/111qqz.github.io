---
author: 111qqz
date: 2018-09-10 11:53:31+00:00
draft: false
title: learn java in 21 minutes for C++ Programmers
type: post
url: /2018/09/learn-java-in-21-minutes-for-c-programmers/
categories:
- 其他
tags:
- java
---

先放资料:

[Learning a New Programming Language: Java for C++ Programmers](http://pages.cs.wisc.edu/~hasti/cs368/JavaTutorial/)




## java package


先说几条重要的人话:



 	  * 一个java文件第一行可以声明该文件所属于的package，package的名字必须与整个工作目录的路径名相同。
 	  * 同一个package下的class默认有互相访问的权限。
 	  * 访问属性设置为public的class，如果该class所在的file声明了package，那么可以被其他package下的class访问到。
 	  * .java的文件名必须与文件中设置为public的class名保持一致（如果没有public的类，那么名称任意)



<blockquote>

> 
> 
 	  * Every class is part of some _package_.
 	  * All classes in a file are part of the same package.
 	  * You can specify the package using a _package declaration_:

 	    * 
package


_name_
 ;
as the first (non-comment) line in the file.
 	  * Multiple files can specify the same package name.
 	  * If no package is specified, the classes in the file go into a special unnamed package (the same unnamed package for all files).
 	  * If package _name_ is specified, the file must be in a subdirectory called _name_ (i.e., the directory name must match the package name).
 	  * You can access public classes in another (named) package using:_package-name.class-name_You can access the public fields and methods of such classes using:_package-name.class-name.field-or-method-name_You can avoid having to include the _package-name_ using:

 	    * 
import


_package-name_
.*;
or

 	    * 
import


_package-name.class-name_
;
at the beginning of the file (after the package declaration). The former imports all of the classes in the package, and the second imports just the named class. You must still use:_class-name_to access the classes in the packages, and_class-name.field-or-method-name_to access the fields and methods of the class; the only thing you can leave off is the package name.

</blockquote>


下面是一些例子:


<blockquote>Assume that you are working in a directory called Javadir, and that you create four files, whose contents are shown below.

>     
>     file 1
>     package ListPkg;
>     public class List { ... }
>     class ListNode {...}
>     
>     file 2
>     package ListPkg;
>     public class NoNextItemException { ... }
>     
>     <a name="file3"></a>
>     file 3
>     public class Test { ... }
>     class Utils { ... }
>     
>     file 4
>     class Test2 { ... }
>     
> 
> 
Here are the directories and file names you must use:

> 
> 
 	  * File 1 must be in a subdirectory named ListPkg, in a file named List.java.
 	  * File 2 must also be in the ListPkg subdirectory, in a file named NoNextItemException.java.
 	  * File 3 must be in a file named Test.java (in the Javadir directory).
 	  * File 4 can be in any .java file (in the Javadir directory).

And here are the classes that can be accessed by the code in each file:

 	  * Files 1 and 2:

 	    * The code in the first two files (ListPkg/List.java and ListPkg/NoNextItemException.java) can access the classes defined in the same package (List, ListNode, and NoNextItemException). (No access was specified for those classes, so they get the default, package access.)
 	    * The code in files 1 and 2 _cannot_ access class Test, even though it is a public class. The problem is that Test is in an unnamed package, so the code in the ListPkg package has no way to import that package, or to name class Test.
 	    * The code in files 1 and 2 _cannot_ access classes Utils and Test2, because they have default (package) access, and are in a different package.


 	  * Files 3 and 4:

 	    * The code in file 3 (Test.java) can access classes ListPkg.List, ListPkg.NoNextItemException, Test, Utils, and Test2 (the first two because they are public classes in a named package, and the last three because they are in the same, unnamed package, and have either public or package access). Note however, that if the code in Test.java uses the class Test2, and that class is _not_ in a file called Test2.java, t**hen the file that contains class Test2 must be compiled first, or else the class will not be found.**
 	    * The code in file 4 (the file that contains class Test2) can access the same classes as the code in file 3 (Test.java).



</blockquote>





