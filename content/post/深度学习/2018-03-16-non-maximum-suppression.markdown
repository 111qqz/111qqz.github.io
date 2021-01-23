---
author: 111qqz
date: 2018-03-16 02:56:14+00:00
draft: false
title: 非极大值抑制（Non-Maximum Suppression，NMS）
type: post
url: /2018/03/non-maximum-suppression/
categories:
- deep-learning
tags:
- nms
---



NMS是为了在诸多CV任务如边缘检测，目标检测等，找到**局部最大值**

**其主要思想是先设定一个阈值，然后计算检测框的IOU(所谓IOU，也就是intersection-over-union，指的是相交面积除以相并面积，是来衡量overlap程度的指数）。如果IOU大于阈值，说明overlap过大，我们要通过某种算法来将其剔除。**

比如下图，在经典的人脸识别任务中，出现了多个检测框，每个检测框有一个置信度confidence，我们通过某个算法，保留一个最好的。

[![](https://111qqz.com/wordpress/wp-content/uploads/2018/03/monroe0.jpg)
](https://111qqz.com/wordpress/wp-content/uploads/2018/03/monroe0.jpg)





顺便说一下算法的实现步骤把，其实不太重要。就是贪心。



<blockquote>其基本操作流程如下：

> 
> 
      * 首先，计算每一个 bounding box 的面积：

        * (x1, y1) ⇒ 左上点的坐标，(x2, y2) ⇒ 右下点的坐标；
        * (x2-x1+1)x(y2-y1+1)


      * 根据 scores 进行排序（一般从小到大），将 score 最大的bounding box置于队列，接下来计算其余 bounding box 与当前 score 最大的 bounding box 的 IoU，抑制（忽略也即去除）IoU大于设定阈值的 bounding box；
      * 重复以上过程，直至候选 bounding boxes 为空；

</blockquote>





最后上一段python代码吧...也很简单，直接转载了别人的...


    
    def nms(dets, thresh):
        x1 = dets[:, 0]
        y1 = dets[:, 1]
        x2 = dets[:, 2]
        y2 = dets[:, 3]
        scores = dets[:, 4]
        
        areas = (x2 - x1 + 1) * (y2 - y1 + 1) # 每个boundingbox的面积
        order = scores.argsort()[::-1] # boundingbox的置信度排序
        keep = [] # 用来保存最后留下来的boundingbox
        while order.size > 0:     
            i = order[0] # 置信度最高的boundingbox的index
            keep.append(i) # 添加本次置信度最高的boundingbox的index
            
            # 当前bbox和剩下bbox之间的交叉区域
            # 选择大于x1,y1和小于x2,y2的区域
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])
            
            # 当前bbox和其他剩下bbox之间交叉区域的面积
            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            
            # 交叉区域面积 / (bbox + 某区域面积 - 交叉区域面积)
            ovr = inter / (areas[i] + areas[order[1:]] - inter)
            #保留交集小于一定阈值的boundingbox
            inds = np.where(ovr <= thresh)[0]
            order = order[inds + 1]
            
        return keep
    print nms(dets, thresh)





参考链接

[目标窗口检测算法-NMS非极大值抑制](https://chenzomi12.github.io/2016/12/14/YOLO-nms/)




