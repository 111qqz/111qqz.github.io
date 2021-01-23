---
author: 111qqz
date: 2017-11-26 11:05:50+00:00
draft: false
title: PCA + kmeans
type: post
url: /2017/11/pca-kmeans/
categories:
- deep-learning
tags:
- k-means
- PCA
---

### 先记录一下PCA实战需要用到的安装包(arch下,python2环境)





### [python2-scikit-learn](https://www.archlinux.org/packages/community/x86_64/python-scikit-learn/)



python2-numpy

python2-pandas

python2-matplotlib

python2-seaborn

[pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)

[pandas 数据结构介绍](http://pda.readthedocs.io/en/latest/chp5.html)



几个和科学计算数据分析有关的重要的python库:`Numpy`、`Matplotlib` ,pandas

(之前数字图像处理课程都接触过了orz)

其中matplotlib 主要用于图像绘制

sklearn 是用于机器学习的python 模块

Seaborn也是用于图像绘制





str.fomat() 是 python2语法

format中的变量会按照str中{} 出现的顺序替换




    
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.datasets import fetch_mldata
    from sklearn.decomposition import PCA
    import seaborn as sns
    mnist = fetch_mldata("MNIST original")
    
    X = mnist.data / 255.0
    y = mnist.target
    
    #print X.shape, y.shape
    
    
    feat_cols = [ 'pixel'+str(i) for i in range(X.shape[1]) ]
    df = pd.DataFrame(X,columns=feat_cols) # transform into some pandas DS named DataFrame
    df['label'] = y  # add a column named 'label',valued by variable y
    df['label'] = df['label'].apply(lambda i: str(i))  # df.apply (some funciton)
    X, y = None, None
    #print 'Size of the dataframe: {}' .format(df.shape)   # str.format() , '{}' is replaced by some value 
    
    # Plot the graph
    #print df
    
    #rndperm = np.random.permutation(df.shape[0])
    #plt.gray()
    #fig = plt.figure( figsize=(16,7) )
    #for i in range(0,30):
    #    ax = fig.add_subplot(3,10,i+1, title='Digit: ' + str(df.loc[rndperm[i],'label']) )
    #    ax.matshow(df.loc[rndperm[i],feat_cols].values.reshape((28,28)).astype(float))
    #plt.show()
    
    #print df
    
    n_components_pca = 3
    pca = PCA(n_components=n_components_pca)
    pca_result = pca.fit_transform(df[feat_cols].values)
    
    print 'kkkkk?'
    df['pca-one'] = pca_result[:,0]
    df['pca-two'] = pca_result[:,1] 
    df['pca-three'] = pca_result[:,2]
    
    print 'Explained variation per principal component: {}'.format(pca.explained_variance_ratio_)
    
    
    pca_var_explained_df = pd.DataFrame({'principal component':np.arange(1,n_components_pca+1),
                                        'variance_explained':pca.explained_variance_ratio_})
    print pca_var_explained_df.sum()
    
    
    ax = sns.barplot(x='principal component',
                     y='variance_explained',
                     data=pca_var_explained_df,
                     palette="Set1")
    ax.set_title('PCA - Variance explained')
    plt.show()





[![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_3.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_3.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_3_pic.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_3_pic.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_3_sum.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_3_sum.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_10.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_10.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_10_pic.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_10_pic.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_10_sum.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/pca_10_sum.png) [![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/手写数字.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/手写数字.png)





PCA+kmeans 时间对比:

[![](https://111qqz.com/wordpress/wp-content/uploads/2017/11/kmeans_pca.png)
](https://111qqz.com/wordpress/wp-content/uploads/2017/11/kmeans_pca.png)

代码:


    
    import time
    import numpy as np
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA  
    vec_num=120
    data = np.random.rand(10000, vec_num) #生成一个随机数据，样本大小为10000, 特征数为120
    #print (data)
    
    t0 = time.clock()
    estimator = KMeans(n_clusters=4)#构造聚类器
    estimator.fit(data)#聚类
    print ("kmeans time:",time.clock()-t0)
    inertia = estimator.inertia_ # 某种度量,比如距离平方和,用来check k-means算法的效果
    print ("sum:",inertia/vec_num)
    
    com_num=10
    pca=PCA(n_components=com_num)
    newdata = pca.fit_transform(data)
    t0 = time.clock()
    estimator.fit(newdata)
    print("kmeans time after PCA:",time.clock()-t0)
    inertia = estimator.inertia_
    print ("sum after PCA",inertia/com_num)




