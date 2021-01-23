---
title: "FPN:Feature Pyramid Networks 学习笔记"
date: 2019-12-08T17:30:50+08:00
draft: false
author: "111qqz"
type: post
url: /2019/12/feature-pyramid-networks
categories:
- deep-learning

tags:
- feature-pyramid-networks
- FPN

---

检测不同尺度的物体一直是计算机视觉领域中比较有挑战性的事情．我们先从之前的工作出发，并对比FPN比起之前的工作有哪些改进．

## 之前的工作

### Featurized image pyramid

![Featurized image pyramid.png](https://i.loli.net/2019/12/08/vhsEbJoYNBcMKdk.png)

思路是对于同一张图，生成不同的scale，然后每个scale的image单独去做检测．
这个方法是手工设计feautre时代的常用办法．
这个办法是比较显然的，也的确可以解决检测不同尺度物体的问题．
缺点非常明显...inference的速度几乎和scale的个数线性相关．
以及由于显存的开销，没办法做end-to-end 的training.


### Single feature map

![single_feature_map.png](https://i.loli.net/2019/12/08/prs9x427mKRWv1o.png)

再之后，手工设计的feature逐渐被由CNN生成的feature取代了．
这种办法更加鲁棒，对image的一些变化不敏感．
但是如果只有一个scale 的图片去过这个feature map,只有最终的feature map去做predict..准确率不太行．．因此还是要与Featurized image pyramid一起．只是优化了得到feature 的部分．


### Pyramidal feature hierarchy

就..CNN本身就有显然的层次结构啊．．．
为什么不直接拿来用，而是提前scale image呢．．．

![Featurized image pyramid.png](https://i.loli.net/2019/12/08/vhsEbJoYNBcMKdk.png)

也就是选若干个feature map直接去做predict..
这个办法美滋滋，既有多个feature map保证了一定的准确率，同时也没有增加很多inference的cost.

SSD应该是率先使用这种方法的．
但是这种办法仍然有不足之处，就是低层的高分辨率的feature map的semantics 太弱了．．
这就导致说对小物体的检测效果不太理想．．．

那么该怎么办呢．．．这时候就该介绍FPN啦


## Feature Pyramid Networks 

![feature_pyramid_network.png](https://i.loli.net/2019/12/08/WLNExRUl4ozFcIk.png)

后面再更．



## FPN 用于 faster rcnn 

FPN同时作用于RPN阶段和fast-rcnn detector 

以下的代码实现出自　[fpn.pytorch](https://github.com/jwyang/fpn.pytorch)

### FPN 作用于RPN 

感觉直接上代码比较容易理解

先看　整个网络的forward函数

```python


 def forward(self, im_data, im_info, gt_boxes, num_boxes):
        batch_size = im_data.size(0)

        im_info = im_info.data
        gt_boxes = gt_boxes.data
        num_boxes = num_boxes.data

        # feed image data to base model to obtain base feature map
        # Bottom-up
        c1 = self.RCNN_layer0(im_data)
        c2 = self.RCNN_layer1(c1)
        c3 = self.RCNN_layer2(c2)
        c4 = self.RCNN_layer3(c3)
        c5 = self.RCNN_layer4(c4)
        # Top-down
        p5 = self.RCNN_toplayer(c5)
        p4 = self._upsample_add(p5, self.RCNN_latlayer1(c4))
        p4 = self.RCNN_smooth1(p4)
        p3 = self._upsample_add(p4, self.RCNN_latlayer2(c3))
        p3 = self.RCNN_smooth2(p3)
        p2 = self._upsample_add(p3, self.RCNN_latlayer3(c2))
        p2 = self.RCNN_smooth3(p2)

        p6 = self.maxpool2d(p5)

        rpn_feature_maps = [p2, p3, p4, p5, p6]
        mrcnn_feature_maps = [p2, p3, p4, p5]

        rois, rpn_loss_cls, rpn_loss_bbox = self.RCNN_rpn(rpn_feature_maps, im_info, gt_boxes, num_boxes)

```

其中RCNN_layer就是用了resnet对应的layer.  可以看出c1,c2,c3,c4是bottom-up的几个feature map, p对应的是top-down的feature map 

**需要注意这里的下标,不管是p还是c,数字越大表示的都是feature map越小. 相同数字的p和c(比如p4和c4)是同一个level的feature.**

然后中间是通过　_upsample_add　直接元素相加

```python

 def _upsample_add(self, x, y):
        '''Upsample and add two feature maps.
        Args:
          x: (Variable) top feature map to be upsampled.
          y: (Variable) lateral feature map.
        Returns:
          (Variable) added feature map.
        Note in PyTorch, when input size is odd, the upsampled feature map
        with `F.upsample(..., scale_factor=2, mode='nearest')`
        maybe not equal to the lateral feature map size.
        e.g.
        original input size: [N,_,15,15] ->
        conv2d feature map size: [N,_,8,8] ->
        upsampled feature map size: [N,_,16,16]
        So we choose bilinear upsample which supports arbitrary output sizes.
        '''
        _,_,H,W = y.size()
        return F.upsample(x, size=(H,W), mode='bilinear') + y

```

至于为什么能相加，

>> 作者解释说这个原因在于我们做了 end-to-end 的 training，因为不同层的参数不是固定的，不同层同时给监督做 end-to-end training，所以相加训练出来的东西能够更有效地融合浅层和深层的信息。

>> da哥解释说，只要work了，故事随便讲


我们看到这里拿了[p2, p3, p4, p5, p6] 这几个feature 输入到rpn网络中．

然后我们看一下RPN-FPN的forward 部分

```python


    def forward(self, rpn_feature_maps, im_info, gt_boxes, num_boxes):        


        n_feat_maps = len(rpn_feature_maps)

        rpn_cls_scores = []
        rpn_cls_probs = []
        rpn_bbox_preds = []
        rpn_shapes = []
        #  对于每一个feature map，来做rpn得到prob和bbox 
        for i in range(n_feat_maps):
            feat_map = rpn_feature_maps[i]
            batch_size = feat_map.size(0)
            
            # return feature map after convrelu layer
            rpn_conv1 = F.relu(self.RPN_Conv(feat_map), inplace=True)
            # get rpn classification score
            rpn_cls_score = self.RPN_cls_score(rpn_conv1)

            rpn_cls_score_reshape = self.reshape(rpn_cls_score, 2)
            rpn_cls_prob_reshape = F.softmax(rpn_cls_score_reshape)
            rpn_cls_prob = self.reshape(rpn_cls_prob_reshape, self.nc_score_out)

            # get rpn offsets to the anchor boxes
            rpn_bbox_pred = self.RPN_bbox_pred(rpn_conv1)

            rpn_shapes.append([rpn_cls_score.size()[2], rpn_cls_score.size()[3]])
            # permute是为了把坐标/分数放在最外面一个维度
            rpn_cls_scores.append(rpn_cls_score.permute(0, 2, 3, 1).contiguous().view(batch_size, -1, 2))
            rpn_cls_probs.append(rpn_cls_prob.permute(0, 2, 3, 1).contiguous().view(batch_size, -1, 2))
            rpn_bbox_preds.append(rpn_bbox_pred.permute(0, 2, 3, 1).contiguous().view(batch_size, -1, 4))

        rpn_cls_score_alls = torch.cat(rpn_cls_scores, 1)
        rpn_cls_prob_alls = torch.cat(rpn_cls_probs, 1)
        rpn_bbox_pred_alls = torch.cat(rpn_bbox_preds, 1)

        n_rpn_pred = rpn_cls_score_alls.size(1)

        # proposal layer
        cfg_key = 'TRAIN' if self.training else 'TEST'
        # 　现在rpn网络已经对anchors的好坏做出了学习，这里的好坏只是指前景或者背景，不包括具体类别的分数．
        #   同时rpn 也学习到了这些anchor的偏移，使得anchor的坐标往更好的方向做一些微调

        # 组成了一个tuple,把这些输入作为一个整体的Input输入了进去
        rois = self.RPN_proposal((rpn_cls_prob_alls.data, rpn_bbox_pred_alls.data,
                                 im_info, cfg_key, rpn_shapes))

```

可以看到是对于每一个scale的feaute_map单独过rpn,然后把得到的结果concat到了一起去做proposal 

接下来我们看一下proposal的代码，细节稍微多一些．

简单来说,proposal　layer按照顺序大概做了如下几件事．

- bbox_transform_inv　根据rpn的结果调整anchors，得到更好的anchors
- clip_boxes　把调整后的anchors根据图片尺寸进行截断，使得所有anchors都在图片范围内
- 按照分数高低选一定数量的anchors做nms,作为nms得到的这些anchors再取topk就称之为rois(或者proposals)


整个proposals流程的代码如下，添加了必要的注释

```python

def forward(self, input):

        # Algorithm:
        #
        # for each (H, W) location i
        #   generate A anchor boxes centered on cell i
        #   apply predicted bbox deltas at cell i to each of the A anchors
        # clip predicted boxes to image
        # remove predicted boxes with either height or width < threshold
        # sort all (proposal, score) pairs by score from highest to lowest
        # take top pre_nms_topN proposals before NMS
        # apply NMS with threshold 0.7 to remaining proposals
        # take after_nms_topN proposals after NMS
        # return the top proposals (-> RoIs top, scores top)


        # the first set of _num_anchors channels are bg probs
        # the second set are the fg probs
        scores = input[0][:, :, 1]  # batch_size x num_rois x 1
        #  0是背景分数,1是前景分数．　这里我们直接取了前景分数

        bbox_deltas = input[1]      # batch_size x num_rois x 4
        im_info = input[2]
        cfg_key = input[3]
        feat_shapes = input[4]        

        pre_nms_topN  = cfg[cfg_key].RPN_PRE_NMS_TOP_N
        post_nms_topN = cfg[cfg_key].RPN_POST_NMS_TOP_N
        nms_thresh    = cfg[cfg_key].RPN_NMS_THRESH
        min_size      = cfg[cfg_key].RPN_MIN_SIZE

        batch_size = bbox_deltas.size(0)

        anchors = torch.from_numpy(generate_anchors_all_pyramids(self._fpn_scales, self._anchor_ratios, 
                feat_shapes, self._fpn_feature_strides, self._fpn_anchor_stride)).type_as(scores)
        # 　anchors shape : [anchor_count, (y1, x1, y2, x2)] 其中anchor_count是所有scale的feature map上的anchor总和
        num_anchors = anchors.size(0)

        anchors = anchors.view(1, num_anchors, 4).expand(batch_size, num_anchors, 4)
        # Any dimension of size 1 can be expanded to an arbitrary value without allocating new memory.　
        # 所以其实是同一份anchor,为了每个batch使用,expand成了batch_size份．
        # 　先view从(num_anchors,4)变成(1,num_anchors,4)增加一个维度
        #   然后变成了(batch_size,num_anchors,4)的维度

        # Convert anchors into proposals via bbox transformations
        proposals = bbox_transform_inv(anchors, bbox_deltas, batch_size)

        # 2. clip predicted boxes to image
        proposals = clip_boxes(proposals, im_info, batch_size)
        # keep_idx = self._filter_boxes(proposals, min_size).squeeze().long().nonzero().squeeze()
                
        scores_keep = scores
        proposals_keep = proposals

        _, order = torch.sort(scores_keep, 1, True)
        # torch.sort(tensor,dim,descending)
        #  因此这里是把分数在num_rois的维度降序排列，返回(values, indices)
        # 我们要用的是indices，就是在排序前的下标
        output = scores.new(batch_size, post_nms_topN, 5).zero_()
        for i in range(batch_size):
            # # 3. remove predicted boxes with either height or width < threshold
            # # (NOTE: convert min_size to input image scale stored in im_info[2])
            proposals_single = proposals_keep[i]
            scores_single = scores_keep[i]

            # # 4. sort all (proposal, score) pairs by score from highest to lowest
            # # 5. take top pre_nms_topN (e.g. 6000)
            order_single = order[i]
            # 　torch.numel() : Returns the total number of elements in the input tensor.
            if pre_nms_topN > 0 and pre_nms_topN < scores_keep.numel():
                order_single = order_single[:pre_nms_topN]
            # 　得到分数最高的前pre_nms_topN个的下标　

            proposals_single = proposals_single[order_single, :]
            # 从下标得到具体的proposals(就是调整过后的anchors)
            scores_single = scores_single[order_single].view(-1,1)

            # 6. apply nms (e.g. threshold = 0.7)
            # 7. take after_nms_topN (e.g. 300)
            # 8. return the top proposals (-> RoIs top)

            keep_idx_i = nms(torch.cat((proposals_single, scores_single), 1), nms_thresh)
            keep_idx_i = keep_idx_i.long().view(-1)

            if post_nms_topN > 0:
                keep_idx_i = keep_idx_i[:post_nms_topN]
            proposals_single = proposals_single[keep_idx_i, :]
            scores_single = scores_single[keep_idx_i, :]

            # padding 0 at the end.
            num_proposal = proposals_single.size(0)
            output[i,:,0] = i
            output[i,:num_proposal,1:] = proposals_single
            # 　output: (batch_size, post_nms_topN, 5)

        return output

```

其中　bbox_transform_inv和　clip_boxes的代码分别如下:

```python


def bbox_transform_inv(boxes, deltas, batch_size):
    # 　boxes: 　(batch_size,num_anchors,4), 4的坐标顺序为(x1, y1, x2, y2)
    # 　（原代码注释写的是　(y1,x1,y2,x2),似乎不正确）　

    # deltas: batch_size x num_rois x 4
    widths = boxes[:, :, 2] - boxes[:, :, 0] + 1.0
    heights = boxes[:, :, 3] - boxes[:, :, 1] + 1.0
    ctr_x = boxes[:, :, 0] + 0.5 * widths
    ctr_y = boxes[:, :, 1] + 0.5 * heights
    # 　widths,heights,ctr_x,ctr_y的维度都是(batch_size,num_rois)

    #  ctx是中心点坐标

    dx = deltas[:, :, 0::4]
    dy = deltas[:, :, 1::4]
    # 　dx,dy是预测得到的中心点偏移距离相对width和height的比例
    dw = deltas[:, :, 2::4]
    dh = deltas[:, :, 3::4]
    # 把　deltas的坐标展开，每一个的shape为(batch_size,num_rois,1),为了方便做向量化操作

    pred_ctr_x = dx * widths.unsqueeze(2) + ctr_x.unsqueeze(2)
    pred_ctr_y = dy * heights.unsqueeze(2) + ctr_y.unsqueeze(2)
    #  dx的维度是(batch_size,num_rois,1),widths和ctr_x的维度为(batch_size,num_rios),unsqueeze是为了做ele-wise的运算

    pred_w = torch.exp(dw) * widths.unsqueeze(2)
    pred_h = torch.exp(dh) * heights.unsqueeze(2)

    # 　按照原公式的log做了逆向运算

    pred_boxes = deltas.clone()
    # x1
    pred_boxes[:, :, 0::4] = pred_ctr_x - 0.5 * pred_w
    # y1
    pred_boxes[:, :, 1::4] = pred_ctr_y - 0.5 * pred_h
    # x2
    pred_boxes[:, :, 2::4] = pred_ctr_x + 0.5 * pred_w
    # y2
    pred_boxes[:, :, 3::4] = pred_ctr_y + 0.5 * pred_h

    # 得到的是经过　deltas修正过的anchors

    return pred_boxes

``` 

```python

def clip_boxes(boxes, im_shape, batch_size):
    #  把修正过的anchors截断到图片范围之内．　
    　
    for i in range(batch_size):
        boxes[i,:,0::4].clamp_(0, im_shape[i, 1]-1)
        boxes[i,:,1::4].clamp_(0, im_shape[i, 0]-1)
        boxes[i,:,2::4].clamp_(0, im_shape[i, 1]-1)
        boxes[i,:,3::4].clamp_(0, im_shape[i, 0]-1)

    return boxes


```

**这两个函数是各种对不齐的重灾区**

至此，我们得到了roi,完成了rpn和proposal 阶段

### FPN 作用于fast rcnn


回想faster rcnn,我们只有一个feature map,因此所有的roi都会作用在feature map上.

但是现在我们有多个不同scale的feature map,因此每个roi作用在哪个feature map上就是一个问题.


按照paper中的描述,我们不妨将这些由FPN生成的不同scale的feature map考虑成是由image pyramid 生成的.
> We view our feature pyramid as if it were produced from
an image pyramid. Thus we can adapt the assignment strategy
of region-based detectors [15, 11] in the case when they
are run on image pyramids

那么显然,越大的roi应该是由越大scale的image得到的. 对应回我们的FPN,也就是越大的roi对应越大scale的feature map.


```python

  def _PyramidRoI_Feat(self, feat_maps, rois, im_info):
        ''' roi pool on pyramid feature maps'''
        # do roi pooling based on predicted rois
        img_area = im_info[0][0] * im_info[0][1]
        h = rois.data[:, 4] - rois.data[:, 2] + 1
        w = rois.data[:, 3] - rois.data[:, 1] + 1
        # 基于roi的scale来判断这个roi对应哪一层的feature 
        # 对于大尺度的roi,就用更深的feature map
        roi_level = torch.log(torch.sqrt(h * w) / 224.0)
        roi_level = torch.round(roi_level + 4)
        roi_level[roi_level < 2] = 2
        roi_level[roi_level > 5] = 5
        # 保护边界为[2,5]
        
```





## 参考

- [Feature Pyramid Networks for Object Detection](https://arxiv.org/abs/1612.03144)
- [fpn.pytorch](https://github.com/jwyang/fpn.pytorch)