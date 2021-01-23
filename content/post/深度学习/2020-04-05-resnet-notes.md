---
title: "resnet 学习笔记"
date: 2020-04-05T16:49:44+08:00
draft: false
author: "111qqz"
type: post
url: /2020/04/resnet-learning-notes
categories:
- deep-learning

tags:
- resnet

---

## 背景

基于Conv的方法在某年的ImageNet比赛上又重新被人想起之后，大家发现网络堆叠得越深，似乎在cv的各个任务上表现的越好。

然而事情当然没有无脑退跌深度那么简单，人们发现，当网络深到一定程度时，结果还不如浅一些的网络结构。

![resnet.png](https://i.loli.net/2020/04/05/2nS4JljCos9QYOE.png)

可能第一反应是，网路那么深，多了那么多参数，有那么多数据吗？ overfit了吧

然而情况没有那么简单。如果只是单纯得overfit，那么应该只有test error很高才对。然而现在的情况是training error也很高。

那这是怎么回事呢？ Resnet的团队认为，是因为深层的网络在训练的时候很难收敛。

这个想法是有依据的，因为我们可以通过构造一个较深的网络结构，使得后面的layer学成一个"identity mapping"的函数。这样training error和test error应该至少和一个浅层网络的结果一样好才对。

那么问题很可能就出在，深层的网络没办法学到这样的函数。

基于这样的想法，resnet团队提出了一种新的结构，称之为"skip connection",来验证该假设。


## resnet网络结构

![resnet2.png](https://i.loli.net/2020/04/05/SUfAy3FKv7H1QaW.png)

我们可以看到，该结构把原来网络要学的H(x)，变成了F(X)+X的形势。 因此网络只需要学习F(X),也就是在
"identity mapping"上学习一个偏移。

实验表明，这种结构对于深层的网络是非常有效的，因为这种结构将默认设置变为了"identity mapping",整个网络变得更加容易收敛。

resnet也成了目前工业界各种网络结构的标准backbone



## resnet 结构的caffe prototxt

放了resnet50的部分结构，截止到第一个resnet block
``` proto

name: "ResNet-50"
input: "data"
input_dim: 1
input_dim: 3
input_dim: 224
input_dim: 224

layer {
	bottom: "data"
	top: "conv1"
	name: "conv1"
	type: "Convolution"
	convolution_param {
		num_output: 64
		kernel_size: 7
		pad: 3
		stride: 2
	}
}

layer {
	bottom: "conv1"
	top: "conv1"
	name: "bn_conv1"
	type: "BatchNorm"
	batch_norm_param {
		use_global_stats: true
	}
}

layer {
	bottom: "conv1"
	top: "conv1"
	name: "scale_conv1"
	type: "Scale"
	scale_param {
		bias_term: true
	}
}

layer {
	bottom: "conv1"
	top: "conv1"
	name: "conv1_relu"
	type: "ReLU"
}

layer {
	bottom: "conv1"
	top: "pool1"
	name: "pool1"
	type: "Pooling"
	pooling_param {
		kernel_size: 3
		stride: 2
		pool: MAX
	}
}

layer {
	bottom: "pool1"
	top: "res2a_branch1"
	name: "res2a_branch1"
	type: "Convolution"
	convolution_param {
		num_output: 256
		kernel_size: 1
		pad: 0
		stride: 1
		bias_term: false
	}
}

layer {
	bottom: "res2a_branch1"
	top: "res2a_branch1"
	name: "bn2a_branch1"
	type: "BatchNorm"
	batch_norm_param {
		use_global_stats: true
	}
}

layer {
	bottom: "res2a_branch1"
	top: "res2a_branch1"
	name: "scale2a_branch1"
	type: "Scale"
	scale_param {
		bias_term: true
	}
}

layer {
	bottom: "pool1"
	top: "res2a_branch2a"
	name: "res2a_branch2a"
	type: "Convolution"
	convolution_param {
		num_output: 64
		kernel_size: 1
		pad: 0
		stride: 1
		bias_term: false
	}
}

layer {
	bottom: "res2a_branch2a"
	top: "res2a_branch2a"
	name: "bn2a_branch2a"
	type: "BatchNorm"
	batch_norm_param {
		use_global_stats: true
	}
}

layer {
	bottom: "res2a_branch2a"
	top: "res2a_branch2a"
	name: "scale2a_branch2a"
	type: "Scale"
	scale_param {
		bias_term: true
	}
}

layer {
	bottom: "res2a_branch2a"
	top: "res2a_branch2a"
	name: "res2a_branch2a_relu"
	type: "ReLU"
}

layer {
	bottom: "res2a_branch2a"
	top: "res2a_branch2b"
	name: "res2a_branch2b"
	type: "Convolution"
	convolution_param {
		num_output: 64
		kernel_size: 3
		pad: 1
		stride: 1
		bias_term: false
	}
}

layer {
	bottom: "res2a_branch2b"
	top: "res2a_branch2b"
	name: "bn2a_branch2b"
	type: "BatchNorm"
	batch_norm_param {
		use_global_stats: true
	}
}

layer {
	bottom: "res2a_branch2b"
	top: "res2a_branch2b"
	name: "scale2a_branch2b"
	type: "Scale"
	scale_param {
		bias_term: true
	}
}

layer {
	bottom: "res2a_branch2b"
	top: "res2a_branch2b"
	name: "res2a_branch2b_relu"
	type: "ReLU"
}

layer {
	bottom: "res2a_branch2b"
	top: "res2a_branch2c"
	name: "res2a_branch2c"
	type: "Convolution"
	convolution_param {
		num_output: 256
		kernel_size: 1
		pad: 0
		stride: 1
		bias_term: false
	}
}

layer {
	bottom: "res2a_branch2c"
	top: "res2a_branch2c"
	name: "bn2a_branch2c"
	type: "BatchNorm"
	batch_norm_param {
		use_global_stats: true
	}
}

layer {
	bottom: "res2a_branch2c"
	top: "res2a_branch2c"
	name: "scale2a_branch2c"
	type: "Scale"
	scale_param {
		bias_term: true
	}
}

layer {
	bottom: "res2a_branch1"
	bottom: "res2a_branch2c"
	top: "res2a"
	name: "res2a"
	type: "Eltwise"
}

layer {
	bottom: "res2a"
	top: "res2a"
	name: "res2a_relu"
	type: "ReLU"
}
```

可视化的结构为:
![resnet3.png](https://i.loli.net/2020/04/05/91DYFpcI6zqsQKW.png)

重点要关注的是 res2a 这个layer，把两个分支的结果直接加在了一起。
eltwise的layer是按照元素操作的，支持乘积，相加，或者取最大值，默认是相加。 可以参考caffe的proto文件

![eltwise.png](https://i.loli.net/2020/04/05/3yCLrbK8zUFO1oQ.png)



## resnet 结构的pytorch实现

可以直接参考torch vision的代码

因为pytorch是通过代码来定义网络结果，不如caffe那么直观，因此就只放了resnet block的部分，代码非常容易看懂，就不解释了。 完整的代码可以参考
[torchvision.models.resnet](https://github.com/pytorch/vision/blob/master/torchvision/models/resnet.py)

``` python

class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None, groups=1,
                 base_width=64, dilation=1, norm_layer=None):
        super(BasicBlock, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if groups != 1 or base_width != 64:
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')
        if dilation > 1:
            raise NotImplementedError("Dilation > 1 not supported in BasicBlock")
        # Both self.conv1 and self.downsample layers downsample the input when stride != 1
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = norm_layer(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out
```

## resnet的变种

### wide resnet 

强调起作用（对于更低的error）的是resnet block，而不是更深的网络结构。
在每一个resnet block中，使用更多的filter来达到和更深的resnet相媲美的结果。

![wide-resnet.png](https://i.loli.net/2020/04/05/jn1lA85eI9FqBgC.png)

### ResNeXt

收到inception网络的启发，使用更多的路径。

![resnext.png](https://i.loli.net/2020/04/05/fBy2I8KnR7abtgL.png)

## 参考链接

- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)

- [Wide Residual Networks](https://arxiv.org/abs/1605.07146)

- [Aggregated Residual Transformations for Deep Neural Networks](https://arxiv.org/abs/1611.05431)

