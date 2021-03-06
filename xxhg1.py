import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#%% 当噪声较小时
rng = np.random.RandomState(10)   # 设置随机局部种子
x =rng.normal(100,100,50)
x =x[:, np.newaxis]#在列上增加一个维度，变为50行1列，每一行是一个样本点
y = 1.25 * x - 20 + 5 * rng.randn(50, 1)   # randn是标准正态分布；添加一点误差；

model = LinearRegression(fit_intercept=True)#模型，多一个参数：截距b
model.fit(x, y)  # x,y的每一行是一个样本，即要求是列向量，fit：拟合，最小二乘法

x_fit = np.linspace(min(x), max(x), 1000)#再生成样本点
#x_fit =x_fit[:, np.newaxis]
y_fit = model.predict(x_fit)#调用模型，测试
print("Model slope: ", model.coef_[0])#coef:参数，取得模型的第一个参数，斜率
print("Model intercept:", model.intercept_)#截距
print('方程的判定系数(R^2): %.6f' % model.score(x, y))
plt.figure(figsize=(16, 12))#画图
plt.scatter(x, y, s=10, c='k', marker='.')
plt.plot(x_fit, y_fit)
ax = plt.gca()
ax.set_aspect("equal")    # 纵横坐标单位相同
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('noise is samll')
plt.show()

#%% 当噪声较大时，受噪声影响较大

rng = np.random.RandomState(10)   # 设置随机局部种子
x =rng.normal(100,100,50)
x =x[:, np.newaxis]
y = 1.25 * x - 20 + 100 * rng.randn(50, 1)   # 加大了噪声，噪声100，淹没真实值

model = LinearRegression(fit_intercept=True)
model.fit(x, y)  # x,y的每一行是一个样本，即要求是列向量

x_fit = np.linspace(min(x), max(x), 1000)
#x_fit =x_fit[:, np.newaxis]
y_fit = model.predict(x_fit)
print("Model slope: ", model.coef_[0])
print("Model intercept:", model.intercept_)
print('方程的判定系数(R^2): %.6f' % model.score(x, y))
plt.figure(figsize=(16, 12))
plt.scatter(x, y, s=10, c='k', marker='.')
plt.plot(x_fit, y_fit)
ax = plt.gca()
ax.set_aspect("equal")    # 纵横坐标单位相同
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('noise is big')
plt.show()
