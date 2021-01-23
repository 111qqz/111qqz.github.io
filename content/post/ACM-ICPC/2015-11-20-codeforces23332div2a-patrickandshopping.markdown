---
author: 111qqz
date: 2015-11-20 19:30:00+00:00
draft: false
title: 'codeforces #332 div 2   A. Patrick and Shopping'
type: post
url: /2015/11/codeforces332div2a-patrickandshopping/
categories:
- ACM
---





































![](https://111qqz.com/wp-content/uploads/2015/11/ContractedBlock3.gif)
![](https://111qqz.com/wp-content/uploads/2015/11/ExpandedBlockStart3.gif)





    
    <span style="color: #008080;"> 1</span> #include <cstdio>
    <span style="color: #008080;"> 2</span> #include <iostream>
    <span style="color: #008080;"> 3</span> #include <cmath>
    <span style="color: #008080;"> 4</span> <span style="color: #0000ff;">using</span> <span style="color: #0000ff;">namespace</span><span style="color: #000000;"> std;
    </span><span style="color: #008080;"> 5</span> <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span><span style="color: #000000;"> d1,d2,d3;
    </span><span style="color: #008080;"> 6</span> <span style="color: #0000ff;">int</span><span style="color: #000000;"> main()
    </span><span style="color: #008080;"> 7</span> <span style="color: #000000;">{
    </span><span style="color: #008080;"> 8</span>     cin>>d1>>d2>><span style="color: #000000;">d3;
    </span><span style="color: #008080;"> 9</span>     <span style="color: #0000ff;">long</span> <span style="color: #0000ff;">long</span> ans = <span style="color: #800080;">999999999999</span><span style="color: #000000;">;
    </span><span style="color: #008080;">10</span>     ans = min(ans,d1+d2+<span style="color: #000000;">d3);
    </span><span style="color: #008080;">11</span>     ans = min (ans,d1*<span style="color: #800080;">2</span>+d2*<span style="color: #800080;">2</span><span style="color: #000000;">);
    </span><span style="color: #008080;">12</span>     ans = min (ans,d1*<span style="color: #800080;">2</span>+<span style="color: #800080;">2</span>*<span style="color: #000000;">d3);
    </span><span style="color: #008080;">13</span>     ans = min(ans,d2*<span style="color: #800080;">2</span>+<span style="color: #800080;">2</span>*<span style="color: #000000;">d3);
    </span><span style="color: #008080;">14</span>     cout<<ans<<<span style="color: #000000;">endl;
    </span><span style="color: #008080;">15</span>     <span style="color: #0000ff;">return</span> <span style="color: #800080;">0</span><span style="color: #000000;">;
    </span><span style="color: #008080;">16</span> }





View Code













time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Today Patrick waits for a visit from his friend Spongebob. To prepare for the visit, Patrick needs to buy some goodies in two stores located near his house. There is a _d_1 meter long road between his house and the first shop and a _d_2 meter long road between his house and the second shop. Also, there is a road of length _d_3 directly connecting these two shops to each other. Help Patrick calculate the minimum distance that he needs to walk in order to go to both shops and return to his house.


![](http://codeforces.com/predownloaded/92/83/928329b240f22061da1bb38557b8e89d32fd6c0c.png)



Patrick always starts at his house. He should visit both shops moving only along the three existing roads and return back to his house. He doesn't mind visiting the same shop or passing the same road multiple times. The only goal is to minimize the total distance traveled.










Input




The first line of the input contains three integers _d_1, _d_2, _d_3 (1 ≤ _d_1, _d_2, _d_3 ≤ 108) -- the lengths of the paths.





  * _d_1 is the length of the path connecting Patrick's house and the first shop;
  * _d_2 is the length of the path connecting Patrick's house and the second shop;
  * _d_3 is the length of the path connecting both shops.









Output




Print the minimum distance that Patrick will have to walk in order to visit both shops and return to his house.










Sample test(s)










input



    
    10 20 30










output



    
    60










input



    
    1 1 5










output



    
    4
















Note




The first sample is shown on the picture in the problem statement. One of the optimal routes is: house ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
first shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
second shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
house.




In the second sample one of the optimal routes is: house ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
first shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
house ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
second shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
house.




























time limit per test


1 second







memory limit per test


256 megabytes







input


standard input







output


standard output










Today Patrick waits for a visit from his friend Spongebob. To prepare for the visit, Patrick needs to buy some goodies in two stores located near his house. There is a _d_1 meter long road between his house and the first shop and a _d_2 meter long road between his house and the second shop. Also, there is a road of length _d_3 directly connecting these two shops to each other. Help Patrick calculate the minimum distance that he needs to walk in order to go to both shops and return to his house.


![](http://codeforces.com/predownloaded/92/83/928329b240f22061da1bb38557b8e89d32fd6c0c.png)



Patrick always starts at his house. He should visit both shops moving only along the three existing roads and return back to his house. He doesn't mind visiting the same shop or passing the same road multiple times. The only goal is to minimize the total distance traveled.










Input




The first line of the input contains three integers _d_1, _d_2, _d_3 (1 ≤ _d_1, _d_2, _d_3 ≤ 108) -- the lengths of the paths.





  * _d_1 is the length of the path connecting Patrick's house and the first shop;
  * _d_2 is the length of the path connecting Patrick's house and the second shop;
  * _d_3 is the length of the path connecting both shops.









Output




Print the minimum distance that Patrick will have to walk in order to visit both shops and return to his house.










Sample test(s)










input



    
    10 20 30










output



    
    60










input



    
    1 1 5










output



    
    4
















Note




The first sample is shown on the picture in the problem statement. One of the optimal routes is: house ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
first shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
second shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
house.




In the second sample one of the optimal routes is: house ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
first shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
house ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
second shop ![](https://111qqz.com/wp-content/uploads/2015/11/9e58594e343ae98e6885aaa282186965f4b9653b.png)
house.







水题。





















