---
author: 111qqz
date: 2018-10-17 03:29:03+00:00
draft: false
title: java-grpc 踩坑记录
type: post
url: /2018/10/java-grpc-notes/
categories:
- 其他
tags:
- gRPC
- java
---

最近的项目需要java和python之间的进程通信，想到了之前使用过的的grpc.

参考官方[quickstart](https://grpc.io/docs/quickstart/java.html)


<blockquote>

> 
> 
 	  * JDK: version 7 or higher

</blockquote>


看起来只依赖jdk,美滋滋

然后按照文档执行

./gradlew installDist

报错:

    
    Task :grpc-compiler:compileJava_pluginExecutableJava_pluginCpp FAILED
    
    FAILURE: Build failed with an exception.
    
    * What went wrong:
    Execution failed for task ':grpc-compiler:compileJava_pluginExecutableJava_pluginCpp'.
    > No tool chain is available to build for platform 'x86_64':
        - Tool chain 'visualCpp' (Visual Studio): Visual Studio is not available on this operating system.
        - Tool chain 'gcc' (GNU GCC): Could not determine GCC metadata: could not find vendor in output of /usr/local/gcc-4.9.4/bin/gcc.
        - Tool chain 'clang' (Clang): Could not find C compiler 'clang' in system path.
    
    * Try:
    Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
    
    * Get more help at https://help.gradle.org
    
    BUILD FAILED in 3m 47s
    
    ~


看起来是gcc或者clang的问题... 先装个clang再说，可能clang太常用了，所以文档没有提到，这下一定可以了。

然而又报错:

    
    > Task :grpc-compiler:linkJava_pluginExecutable FAILED
    /usr/bin/ld: cannot find -lstdc++
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    
    
    
    
    FAILURE: Build failed with an exception.                                                                                
    
    
    * What went wrong:                                                                                                      
    Execution failed for task ':grpc-compiler:linkJava_pluginExecutable'.                                                   
    > A build operation failed.                                                                                             
          Linker failed while linking protoc-gen-grpc-java.                                                                 
      See the complete log at: file:///home/renkuanze/github/grpc-java/compiler/build/tmp/linkJava_pluginExecutable/output.txt
    
    
    * Try:                                                                                                                  
    Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
    
    
    * Get more help at https://help.gradle.org
    ~                                                                                                                      
    ~                                                                                                                      
    ~                                                                                                                      
    ~


??????

看起来是stdc++的lib没有找到。

在centos上安装了:libstdc++.x86_64 4.8.5-28.el7_5.1 @updates
libstdc++-devel.x86_64 4.8.5-28.el7_5.1 @updates
libstdc++-static.x86_64

这回一定没问题了吧？

然而继续报错，变成了javedoc找不到

    
    *** Skipping the build of codegen and compilation of proto files because skipCodegen=true
    > Task :grpc-all:javadoc FAILED
    
    FAILURE: Build failed with an exception.
    
    * What went wrong:
    Execution failed for task ':grpc-all:javadoc'.
    > Javadoc generation failed. Generated Javadoc options file (useful for troubleshooting): '/home/renkuanze/github/grpc-java/all/build/tmp/javadoc/javadoc.options'
    
    * Try:
    Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
    
    * Get more help at https://help.gradle.org
    
    BUILD FAILED in 1s
    30 actionable tasks: 1 executed, 29 up-to-date
    
    


<del>简直了。。。grpc的文档还是一如既往的辣鸡。。。目前还在坑里面，先把前面踩的坑记录一下。</del>

然后继续报错:

    
    *** Skipping the build of codegen and compilation of proto files because skipCodegen=true
    > Task :grpc-all:javadoc FAILED
    
    FAILURE: Build failed with an exception.
    
    * What went wrong:
    Execution failed for task ':grpc-all:javadoc'.
    > Javadoc generation failed. Generated Javadoc options file (useful for troubleshooting): '/home/renkuanze/github/grpc-java/all/build/tmp/javadoc/javadoc.options'
    
    * Try:
    Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.
    
    * Get more help at https://help.gradle.org
    
    BUILD FAILED in 3s
    30 actionable tasks: 6 executed, 24 up-to-date
    
    ~                                                                                                                                                                                             
    ~




好像不是很对啊...

文档固然辣鸡，但是会不会有其他打开方式?

于是跑到工程院那边请教了同事...发现果然打开方式不正确...

正确的方式是直接在依赖管理工具如maven中添加，并不需要手动编译安装...

[参考这个搞它一发先](https://www.codenotfound.com/grpc-spring-boot-example.html)

同时按照[maven-in-five-minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)　了解一下maven的使用


<blockquote>Although hardly a comprehensive list, these are the most common _default_ lifecycle phases executed.

> 
> 
 	  * **validate**: validate the project is correct and all necessary information is available
 	  * **compile**: compile the source code of the project
 	  * **test**: test the compiled source code using a suitable unit testing framework. These tests should not require the code be packaged or deployed
 	  * **package**: take the compiled code and package it in its distributable format, such as a JAR.
 	  * **integration-test**: process and deploy the package if necessary into an environment where integration tests can be run
 	  * **verify**: run any checks to verify the package is valid and meets quality criteria
 	  * **install**: install the package into the local repository, for use as a dependency in other projects locally
 	  * **deploy**: done in an integration or release environment, copies the final package to the remote repository for sharing with other developers and projects.

There are two other Maven lifecycles of note beyond the _default_ list above. They are

> 
> 
 	  * **clean**: cleans up artifacts created by prior builds
 	  * **site**: generates site documentation for this project

</blockquote>


发现mvn package的时候会报几百行的错误

于是先执行mvn validate验证一下情况,
最上面的错误如下:

    
    [INFO] Scanning for projects...
    [INFO] ------------------------------------------------------------------------
    [INFO] Detecting the operating system and CPU architecture
    [INFO] ------------------------------------------------------------------------
    [INFO] os.detected.name: osx
    [INFO] os.detected.arch: x86_64
    [INFO] os.detected.classifier: osx-x86_64
    [WARNING] Failed to inject repository session properties.
    java.lang.NoSuchMethodError: org.apache.maven.execution.MavenSession.getRepositorySession()Lorg/eclipse/aether/RepositorySystemSession;
        at kr.motd.maven.os.RepositorySessionInjector.injectRepositorySession(RepositorySessionInjector.java:22)
        at kr.motd.maven.os.DetectExtension.injectSession(DetectExtension.java:148)
        at kr.motd.maven.os.DetectExtension.afterProjectsRead(DetectExtension.java:107)
        at org.apache.maven.DefaultMaven.doExecute(DefaultMaven.java:274)
        at org.apache.maven.DefaultMaven.execute(DefaultMaven.java:156)
        at org.apache.maven.cli.MavenCli.execute(MavenCli.java:537)
        at org.apache.maven.cli.MavenCli.doMain(MavenCli.java:196)
        at org.apache.maven.cli.MavenCli.main(MavenCli.java:141)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:483)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced(Launcher.java:290)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:230)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:409)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:352)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:47)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:483)
        at com.intellij.rt.execution.application.AppMain.main(AppMain.java:147)
    [INFO]


参考[An exception occurred when I use maven plugin, Why?](https://github.com/grpc/grpc-java/issues/2267)　　发现可能是maven版本不行,去官网下载了目前的最近版本3.5.4,ok了

下一步该进行mvn compile，也ok

然后是mvn test,又是几百行错误...核心的信息是java.lang.NoSuchMethodError: com.google.common.base.Preconditions.checkArgument

参考[java.lang.NoSuchMethodError: com.google.common.base.Preconditions.checkArgument](https://stackoverflow.com/questions/42206440/java-lang-nosuchmethoderror-com-google-common-base-preconditions-checkargument)

添加了两个依赖(再次吐槽grpc-java官方文档＆demo的不靠谱)

    
    **Please add following dependencies in your project.**
    <dependency>
        <groupId>com.google.guava</groupId>
        <artifactId>guava</artifactId>
        <version>23.6-jre</version>
    </dependency> 
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpcore</artifactId>
        <version>4.4.8</version>
    </dependency>


似乎是ok了．

然后执行mvn package，继续报错,好在只有几十行...

    
    [ERROR] Failed to execute goal org.springframework.boot:spring-boot-maven-plugin:2.0.3.RELEASE:repackage (default) on project grpc-demo: Execution default of goal org.springframework.boot:spring-boot-maven-plugin:2.0.3.RELEASE:repackage failed: Unable to find a single main class from the following candidates [io.grpc.examples.advanced.HelloJsonClient, io.grpc.examples.advanced.HelloJsonServer, io.grpc.examples.alts.HelloWorldAltsClient, io.grpc.examples.alts.HelloWorldAltsServer, io.grpc.examples.errorhandling.DetailErrorSample, io.grpc.examples.errorhandling.ErrorHandlingClient, io.grpc.examples.experimental.CompressingHelloWorldClient, io.grpc.examples.header.CustomHeaderClient, io.grpc.examples.header.CustomHeaderServer, io.grpc.examples.helloworld.HelloWorldClient, io.grpc.examples.helloworld.HelloWorldServer, io.grpc.examples.helloworldtls.HelloWorldClientTls, io.grpc.examples.helloworldtls.HelloWorldServerTls, io.grpc.examples.manualflowcontrol.ManualFlowControlClient, io.grpc.examples.manualflowcontrol.ManualFlowControlServer, io.grpc.examples.routeguide.RouteGuideClient, io.grpc.examples.routeguide.RouteGuideServer] -> [Help 1]
    [ERROR] 
    [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
    [ERROR] Re-run Maven using the -X switch to enable full debug logging.
    [ERROR] 
    [ERROR] For more information about the errors and possible solutions, please read the following articles:
    [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/PluginExecutionException


摘重点: Unable to find a single main class from the following candidates

看样子是找不到程序入口在哪里了...好像很合理，毕竟grpc-java的example里每个文件都带了main函数

参考[SpringBoot: Unable to find a single main class from the following candidates](https://stackoverflow.com/questions/42840576/springboot-unable-to-find-a-single-main-class-from-the-following-candidates)，在pom.xml中添加如下的属性就行了．

    
    <profiles>
        <profile>
            <id>profile1</id>
            <properties>
              <spring.boot.mainclass>com.SomeClass</spring.boot.mainclass>
            </properties>
        </profile>
        <profile>
            <id>profile2</id>
            <properties>
              <spring.boot.mainclass>com.SomeOtherClass</spring.boot.mainclass>
            </properties>
        </profile>
    </profiles>



    
    <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <version>1.5.2.RELEASE</version>
        <executions>
          <execution>
            <goals>
              <goal>repackage</goal>
            </goals>
            <configuration>
              <mainClass>${spring.boot.mainclass}</mainClass>
            </configuration>
          </execution>
        </executions>
        ...
    </plugin>




然后另一边，将python的server启动起来

注意ip和端口号要保持一致．　ok了

    
    java -jar  /data/downloads/grpc-demo/target/grpc-demo-0.0.1-SNAPSHOT-exec.jar
    十月 18, 2018 11:48:06 上午 io.grpc.examples.helloworld.HelloWorldClient greet
    信息: Will try to greet sensetime autobots java backend ...
    十月 18, 2018 11:48:06 上午 io.grpc.examples.helloworld.HelloWorldClient greet
    信息: Greeting: Hello, sensetime autobots java backend  from python server




最后的代码请参考[grpc-java-maven-exmaple](https://github.com/111qqz/grpc-java-maven-exmaple)














