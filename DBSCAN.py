import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

#%%  Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]   #围绕这三点生成
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)


#%%   Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)    #同比例增大密度相同
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)    #  np.zeros_like  生成向量 
core_samples_mask[db.core_sample_indices_] = True     #一维向量，判断若是True就放到其中，存储核心点
labels = db.labels_    

#获取聚类个数，其中-1代表noise    
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)   #当前样本点归属哪一类   4-1=3，聚出来的类是3，减去一个噪声点
#看判断出来的点有几个类别    set转换成集合                       
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))


#%%  绘图 
# Black removed and is used for noise instead.
unique_labels = set(labels)     #把重复的去掉
colors = [plt.cm.Spectral(each)   #给每个类别指定不同颜色，四个标签四个颜色
          for each in np.linspace(0, 1, len(unique_labels))]   #list comprehension列表生成式
#   1)np.linspace 返回[0,1]之间的len(unique_labels) 个数
#   2)plt.cm 一个颜色映射模块
#   3)生成的每个colors包含4个值，分别是RGBA:
#    RGBA是代表Red（红色） Green（绿色） Blue（蓝色）和 Alpha的色彩空间，
#    也就是透明度/不透明度
#   4)其实这行代码的意思就是生成len(unique_labels)个可以和光谱对应的颜色值
plt.figure(figsize=(12, 9))
for k, col in zip(unique_labels, colors):        #把两个对象合成一个tuple
    class_member_mask = (labels == k)   #把labels（向量） == k的找出来
    if k == -1:   #被判定的噪声点  
        cls =  'noise'
        xy = X[class_member_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor='k',
             markeredgecolor='k', markersize=6,label=cls)
    else:
        xy = X[class_member_mask & core_samples_mask]   #核心点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=12,label='class '+ str(k)+' core')
        xy = X[class_member_mask & ~core_samples_mask]  #边缘点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6,label='class '+ str(k)+' border')
plt.legend(loc='best')
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()