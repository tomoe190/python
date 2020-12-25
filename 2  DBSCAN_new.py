import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import datasets
from sklearn.cluster import DBSCAN

#%% 生成、展示数据，make_moons生成的数据分布是两个半圆形状的，经常用于可视化聚类及分类算法
#n_samples表示生成样本的数量
X1, y1=datasets.make_moons(n_samples=1000, noise=0.1,random_state=18050412123%30) 

#factor:外圈与内圈的尺度因子
#n_samples样本数量，n_features样本维度，centers有几簇聚类数据，
# cluster_std表示每簇的标准差，可以设置[1.0,2.0,4.0]，random_state随机数
X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2,1.2]],
                              cluster_std=[[0.1]], random_state=18050412123%30)

X = np.concatenate((X1, X2))  #纵向拼接
plt.figure(figsize=(12, 9))   #表格长宽
plt.plot(X[:, 0], X[:, 1],  'o',markersize=5)
plt.show()

#用DBSCAN 进行调整的过程   传入默认参数
db = DBSCAN().fit(X) #调用密度聚类
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#设置一个样本个数长度的全false向量
core_samples_mask[db.core_sample_indices_] = True   #将核心样本部分设置为true
#为所有核心样本的索引
labels = db.labels_#为所有样本的聚类索引，没有聚类 索引为-1
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  
#获取聚类个数 （聚类结果中-1表示没有聚类，为离散点） 
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)   
          for each in np.linspace(0, 1, len(unique_labels))]
#   1)np.linspace 返回[0,1]之间的len(unique_labels) 个数
#   2)plt.cm 一个颜色映射模块
#   3)生成的每个colors包含4个值，分别是RGBA:
#    RGBA是代表Red（红色） Green（绿色） Blue（蓝色）和 Alpha的色彩空间，
#    也就是透明度/不透明度
#   4)其实这行代码的意思就是生成len(unique_labels)个可以和光谱对应的颜色值
plt.figure(figsize=(12, 9))

for k, col in zip(unique_labels, colors): #把两个对象合成一个tuple
    class_member_mask = (labels == k)  #将所有属于该聚类的位置设置为true
    if k == -1:   #被判定的噪声点
        cls =  'noise'
        xy = X[class_member_mask] 
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor='k',
             markeredgecolor='k', markersize=6,label=cls)
    else:
        xy = X[class_member_mask & core_samples_mask]   #核心点
        #将所有属于该类的核心样本取出，使用设置的图标进行绘制
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=10,label= 'class '+ str(k)+' core')
        xy = X[class_member_mask & ~core_samples_mask]  #边缘点
        
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6,label= 'class '+ str(k)+' border')
plt.legend(loc='best')
plt.title('Estimated number of clusters: %d' % n_clusters_)

plt.show()

#%% 对DBSCAN的两个关键的参数eps和min_samples进行调参，类别数太少，增加类别数，eps0.5减到0.1
db = DBSCAN(eps=0.1).fit(X)  #X是输入数据，db就是最终的分类器   预测模型
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
                      #db.labels_聚类，将每个实例的簇标签放入labels序列
                      #np.zeros_like:创建同shape的全0矩阵
                      
core_samples_mask[db.core_sample_indices_] = True
#db.core_sample_indices_是核心点的索引，db.labels_不能区分核心点还是边界点，
# 所以需要用这个索引确定核心点
labels = db.labels_  

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)   
          for each in np.linspace(0, 1, len(unique_labels))]
plt.figure(figsize=(12, 9))

for k, col in zip(unique_labels, colors):
    class_member_mask = (labels == k)
    if k == -1:   #被判定的噪声点
        cls =  'noise'
        xy = X[class_member_mask]
        plt.plot(xy[:, 0], xy[:, 1], '.', markerfacecolor='k',
             markeredgecolor='k', markersize=6,label=cls)
    else:
        xy = X[class_member_mask & core_samples_mask]   #核心点
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=12,label='class '+ str(k)+' core')
        xy = X[class_member_mask & ~core_samples_mask]  #边缘点
        plt.plot(xy[:, 0], xy[:, 1], '^', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6,label='class '+ str(k)+' border')
plt.legend(loc='best')
plt.title('Estimated number of clusters: %d' % n_clusters_)

plt.show()
