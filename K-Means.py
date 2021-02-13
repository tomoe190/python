# -*- coding:utf-8 -*-
# k-means实验

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.datasets import make_blobs

plt.figure(figsize=(12, 12))

# 选取样本数量
n_samples = 1500
# 选取随机因子
random_state = 170
# 获取数据集
X, y = make_blobs(n_samples=n_samples, random_state=random_state,centers=3)  #默认的群数为3，即centers=3

#%% 聚类数量不正确时的效果
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)  
plt.subplot(221)  
plt.scatter(X[y_pred==0][:, 0], X[y_pred==0][:, 1], marker='+',color='b')  #标出聚类为0的点
plt.scatter(X[y_pred==1][:, 0], X[y_pred==1][:, 1], marker='+',color='r')  #标出聚类为1的点
plt.title("Incorrect Number of Blobs: %0.3f" % metrics.silhouette_score(X, y_pred))

#%% 聚类数量正确时的效果
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)
plt.subplot(222)
plt.scatter(X[y_pred==0][:, 0], X[y_pred==0][:, 1], marker='+',color='b')  #标出聚类为0的点
plt.scatter(X[y_pred==1][:, 0], X[y_pred==1][:, 1], marker='+',color='r')  #标出聚类为1的点
plt.scatter(X[y_pred==2][:, 0], X[y_pred==2][:, 1], marker='+',color='m')  #标出聚类为2的点  
plt.title("Correct Number of Blobs %0.3f" % metrics.silhouette_score(X, y_pred))

#%% 类间的方差存在差异的效果
X_varied, y_varied = make_blobs(n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5],random_state=random_state)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)
plt.subplot(223)
plt.scatter(X_varied[y_pred==0][:, 0], X_varied[y_pred==0][:, 1], marker='+',color='b')
plt.scatter(X_varied[y_pred==1][:, 0], X_varied[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X_varied[y_pred==2][:, 0], X_varied[y_pred==2][:, 1], marker='+',color='m')
plt.title("Unequal Variance: %0.3f" % metrics.silhouette_score(X_varied,y_pred))

#%% 类的规模差异较大的效果
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_filtered)
plt.subplot(224)
plt.scatter(X_filtered[y_pred==0][:, 0], X_filtered[y_pred==0][:, 1], marker='+',color='b')
plt.scatter(X_filtered[y_pred==1][:, 0], X_filtered[y_pred==1][:, 1], marker='+',color='r')
plt.scatter(X_filtered[y_pred==2][:, 0], X_filtered[y_pred==2][:, 1], marker='+',color='m')
plt.title("Unevenly Sized Blobs: %0.3f" % metrics.silhouette_score(X_filtered, y_pred))
plt.show()
