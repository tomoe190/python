from sklearn.neural_network import MLPClassifier
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt

# 生成数据，分割为训练集和测试集
trainingSet, trainingLabels = sklearn.datasets.make_moons(400, noise=0.20,random_state=1)
X_test = trainingSet[320:]
y_test = trainingLabels[320:]
X_train = trainingSet[:320]
y_train = trainingLabels[:320]

# 配置MLP（BP算法）的参数，尝试改变hidden_layer_sizes
clf = MLPClassifier(
    solver='lbfgs',
    activation="logistic",
    alpha=1e-5,
    hidden_layer_sizes=(
        10,
        2),
    random_state=1)
#‘lbfgs’ is an optimizer in the family of quasi-Newton methods.
# alpha : L2 penalty (regularization term) parameter.
# hidden_layer_sizes :The ith element represents the number of neurons in
# the ith hidden layer.


# 训练
clf.fit(X_train, y_train)

print('训练集-神经网络分类的准确率为：{0:.2f}%'.format(clf.score(X_train, y_train) * 100))
print('测试集-神经网络分类的准确率为：{0:.2f}%'.format(clf.score(X_test, y_test) * 100))
#format的用法见：https://blog.csdn.net/i_chaoren/article/details/77922939

# 画出决策边界
x_min, x_max = X_train[:, 0].min() - 0.1, X_train[:, 0].max() + 0.1
y_min, y_max = X_train[:, 1].min() - 0.1, X_train[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

#Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
prob = clf.predict_proba(np.column_stack((xx.ravel(), yy.ravel())))
Z=prob[:,0].reshape(xx.shape)
plt.figure(figsize=(8, 6))
plt.scatter(X_train[y_train == 0, 0],
            X_train[y_train == 0, 1], s=10, c='r', marker='.')
plt.scatter(X_train[y_train == 1, 0],
            X_train[y_train == 1, 1], s=10, c='k', marker='.')
plt.contour(xx, yy, Z, colors = 'b', linewidths =2 ,linestyles ='--', levels=[0.5])   # 绘制分界曲线，针对"0.5",contour实际是通过插值得到对应的坐标点
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
