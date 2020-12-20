import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_classification
from sklearn import neighbors
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF']) 
#%% X为样本特征，Y为样本类别输出， 共1000个样本，每个样本2个特征，输出有3个类别，没有冗余特征，每个类别一个簇
n=2000
X, Y = make_classification(n_samples=n, n_features=2, n_redundant=0,shuffle=True,
                           n_clusters_per_class=1, n_classes=3, random_state=708)

#%% 分割数据
k = n // 2  # 一半的数据量
x_train = X[:k, :]
y_train = Y[:k]
x_test = X[k:, :]
y_test = Y[k:]



#%% 训练集样本的在空间的分布
plt.figure(figsize=(8, 6))
plt.scatter(x_train[:, 0], x_train[:, 1], s=8, marker='o', c=y_train)
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

#%% KNN模型
clf = neighbors.KNeighborsClassifier(n_neighbors=19, weights='uniform')
clf.fit(x_train, y_train)

#%%  问题的边界
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

#%%  将空间划分成细网，得到类别的势力范围
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = clf.predict(np.column_stack((xx.ravel(), yy.ravel()))).reshape(xx.shape)
 
#%%  图示类别的界限及训练集样本
plt.figure(figsize=(8, 6))
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)   #必须写在scatter的前边
plt.scatter(x_train[:, 0], x_train[:, 1], s=8, marker='o', c=y_train)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("3-Class KNN classification (train sample)")
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
#%%  图示类别的界限及测试集样本
plt.figure(figsize=(8, 6))
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
plt.scatter(x_test[:, 0], x_test[:, 1], s=8, marker='o', c=y_test)                      
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("3-Class KNN classification (test sample)")
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()

#%%  准确率
print('训练集-KNN分类准确率为：{0:.2f}%'.format(clf.score(x_train, y_train) * 100))
print('测试集-KNN分类准确率为：{0:.2f}%'.format(clf.score(x_test, y_test) * 100))