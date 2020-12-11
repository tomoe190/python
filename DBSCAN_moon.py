import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import datasets

X1,y1=datasets.make_moons(n_samples=5000,noise=0.1,random_state=15050418105%28) 
X2, y2 = datasets.make_blobs(n_samples=1000, n_features=2, centers=[[1.2,1.2]],
                             cluster_std=0.1, random_state=15050418105%28)
X = np.concatenate((X1, X2))  #纵向拼接
plt.figure(figsize=(12, 9))
plt.scatter(X[:, 0], X[:, 1], s=4, marker='o')
plt.show()

#%% 首先看看K-Means的聚类效果
from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters=3, random_state=9).fit_predict(X)
plt.figure(figsize=(12, 9))
plt.scatter(X[:, 0], X[:, 1],s=4, c=y_pred)
plt.title('k-means:k=3')
plt.show()
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, y_pred))

#%% 那么如果使用DBSCAN效果如何呢？我们先不调参，直接用默认参数，看看聚类效果,：
from sklearn.cluster import DBSCAN
y_pred = DBSCAN().fit_predict(X)     #eps=0.5, min_samples=5
plt.figure(figsize=(12, 9))
plt.scatter(X[:, 0], X[:, 1],s=4, c=y_pred)
plt.title('DBSCAN:eps=0.5, min_samples=5')
plt.show()


#%% 对DBSCAN的两个关键的参数eps和min_samples进行调参！发现，类别数太少，
#需要增加类别数，可以减少eps-邻域的大小，默认是0.5，减到0.1看看效果
y_pred = DBSCAN(eps = 0.1).fit_predict(X)
plt.figure(figsize=(12, 9))
plt.scatter(X[:, 0], X[:, 1],s=4, c=y_pred)
plt.title('DBSCAN:eps=0.1, min_samples=10')
plt.show()
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, y_pred))

#%% 对DBSCAN的两个关键的参数eps和min_samples进行调参！发现，类别数太少，
#需要增加类别数，可以增大min_samples值，增大到15，看看效果
y_pred = DBSCAN(eps = 0.1, min_samples = 15).fit_predict(X)
plt.figure(figsize=(12, 9))
plt.scatter(X[:, 0], X[:, 1],s=4, c=y_pred)
plt.title('DBSCAN:eps=0.1, min_samples=15')
plt.show()
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, y_pred))