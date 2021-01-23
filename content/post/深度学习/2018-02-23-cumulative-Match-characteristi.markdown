---
author: 111qqz
date: 2018-02-23 08:20:55+00:00
draft: false
title: 分类评价指标之Cumulative Match Characteristi (CMC)曲线
type: post
url: /2018/02/cumulative-Match-characteristi/
categories:
- deep-learning
tags:
- Cumulative Match Characteristi
---

CMC曲线全称是Cumulative Match Characteristic (CMC) curve，也就是累积匹配曲线，同ROC曲线Receiver Operating Characteristic (ROC) curve一样，是模式识别系统，如人脸，指纹，虹膜等的重要评价指标，尤其是在生物特征识别系统中，一般同ROC曲线（ [多标签图像分类任务的评价方法-mean average precision(mAP) 以及top x的评价方法](https://111qqz.com/wordpress/2018/02/-map/)）一起给出，能够综合评价出算法的好坏。

转一篇通俗易懂的解释：



<blockquote>

> 
> Shortly speaking, imagine that you have 5 classes. For simplicity, imagine you have one test per class. Each test produces a score when compared to each class. Let's start from test1 which belongs to class1:
> 
> 

> 
> As your similarity measure, here, is Euclidian distance, the more distance a test has compared to a class, the less similarity is obtained. Without loss of generality, let's suppose that the distance measures are calibrated and normalized in terms of similarity scores.
> 
> 

> 
> If the score between test1 and class1 is larger than the other 4 classes (or the Euclidian distance between test1 and class1 is less than the other 4 classes), class 1 is recognized in the first rank. As an example, let's suppose the following similarity scores (not Euclidian distances):
> 
> 

> 
> Test1 VS class 1= .95
> 
> 

> 
> Test1 VS class 2= .7
> 
> 

> 
> Test1 VS class 3= .9
> 
> 

> 
> Test1 VS class 4= .72
> 
> 

> 
> Test1 VS class 5= .3
> 
> 

> 
> What do these scores say? These similarity scores say that test 1 is more similar to class 1 than the other classes. So, test 1 is correctly recognized in the first rank.
> 
> 

> 
> Let's suppose that test2, test 3, test 4 and test 5 are also recognized in the first rank.
> 
> 

> 
> So, we can conclude that we have a perfect CMC curve (y-x). because all of the 5 test are correctly recognized. A perfect CMC curve is as following:
> 
> 

> 
> Rank 1: 100%
> 
> 

> 
> Rank2: 100%
> 
> 

> 
> ...
> 
> 

> 
> Rank 5:100%
> 
> 

> 
> Now, let's suppose the following situation:
> 
> 

> 
> Test1 VS class 1= .9
> 
> 

> 
> Test1 VS class 2= .95
> 
> 

> 
> Test1 VS class 3= .4
> 
> 

> 
> Test1 VS class 4= .72
> 
> 

> 
> Test1 VS class 5= .3
> 
> 

> 
> What do these scores say? They say that test 1 is more similar to class 2 than class 1 (This is a mismatch and it is not correct!). So, the correct match (.9) is not the top match here (the top match is .95 which is a mismatch). In other words, test 1 is not recognized as the top match, but it is recognized among top "two matches" (the top two matches are .95 and .9). This is what rank 2 recognition means!
> 
> 

> 
> Now, if test 1 is recognized among top two matches but the other tests (i.e., test 2, test 3,... test 5) are recognized in the first rank (Rank 1), the first rank recognition rate is 80% (test 1 is not among the top matches, i,e, 1 out of 5 is incorrect in first rank recognition which yields 80%) but the second rank recognition rate is 100%, because all of the tests are correctly recognized among the top "two matches". Some of them are recognized in the first rank (test 2, test 3, test 4, and test 5) while some of them are recognized in the second rank (test 1). So, the second rank recognition rate is 100%.
> 
> 

> 
> So, the CMC curve will be as following:
> 
> 

> 
> Rank1  80% (tests 2,3,4,5 are among the N=1 top matches )
> 
> 

> 
> Rank2 100% (tests 1,2,3,4,5 are among the N=2 top matches )
> 
> 

> 
> Rank3 100%  (tests 1,2,3,4,5 are among the N=3 top matches )
> 
> 

> 
> ...
> 
> 

> 
> Rank 5 100%  (tests 1,2,3,4,5 are among the N=5 top matches )
> 
> 

> 
> Now, consider that test1, test 2, test 3 are recognized in the first rank, test 4 is recognized in the second rank and test 5 is recognized in the fourth rank. what is the CMC curve>? Here is the answer:
> 
> 

> 
> Rank 1:  60% (tests 1,2,3 are among the N=1 top matches )
> 
> 

> 
> Rank 2: 80% (test 1,2 ,3 ,4 are among N=2 top matches)
> 
> 

> 
> Rank 3: 80% (test 1,2 ,3 ,4 are among N=3 top matches)
> 
> 

> 
> Rank 4: 100% (test 1,2 ,3 ,4 and 5 are among N=4 top matches)
> 
> 

> 
> Rank 5: 100% (test 1,2 ,3 ,4 and 5 are among N=5 top matches)
> 
> 

> 
> Reference:
> 
> 

> 
> Grother, Patrick, Ross J. Micheals, and P. Jonathon Phillips. "Face recognition vendor test 2002 performance metrics." Audio-and Video-Based Biometric Person Authentication. Springer Berlin Heidelberg, 2003.
> 
> </blockquote>

















参考资料：[How_is_CMC_produced_recognition_rate_vs_Rank_for_unknown_faces](https://www.researchgate.net/post/How_is_CMC_produced_recognition_rate_vs_Rank_for_unknown_faces)








