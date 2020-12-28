import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

# 从csv文件中读入数据
data = np.loadtxt("data_logistic.csv", dtype=np.float, delimiter=",")

# 打乱顺序，1：1将数据分割为训练集和测试集
np.random.seed(10)
np.random.shuffle(data)
s = np.shape(data)
length = s[0]  # 总数据量--行数
k = length // 2  # 一半的数据量
x_train = data[:k, 0:2]
y_train = data[:k, -1]
x_test = data[k:, 0:2]
y_test = data[k:, -1]

lr = LogisticRegression()  # 建立LR模型
lr.fit(x_train, y_train)  # 用处理好的数据训练模型
print('训练集-逻辑回归的准确率为：{0:.2f}%'.format(lr.score(x_train, y_train) * 100))
print('测试集-逻辑回归的准确率为：{0:.2f}%'.format(lr.score(x_test, y_test) * 100))
#format的用法见：https://blog.csdn.net/i_chaoren/article/details/77922939

# 画出决策边界
x_min, x_max = x_train[:, 0].min() - 1, x_train[:, 0].max() + 1
y_min, y_max = x_train[:, 1].min() - 1, x_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))


#Z = lr.predict(np.column_stack((xx.ravel(), yy.ravel()))).reshape(xx.shape)  #reshape是行优先
prob = lr.predict_proba(np.column_stack((xx.ravel(), yy.ravel())))
Z=prob[:,0].reshape(xx.shape)   #reshape是行优先
plt.figure(figsize=(12, 9))
plt.scatter(x_train[y_train == 0, 0],
            x_train[y_train == 0, 1],
            s=10, c='r', marker='.', label="+")  # 绘制“+”点  s--点的大小
plt.scatter(x_train[y_train == 1, 0],
            x_train[y_train == 1, 1],
            s=10, c='k', marker='.', label="--")  # 绘制“-”点
plt.title('Logistic Regression')
plt.legend()
plt.contour(xx, yy, Z, c='k',levels=[0.5])   # 绘制预测结果图
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)
plt.show()
