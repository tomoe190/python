import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#%% 当噪声较小时
#rng = np.random.RandomState(10)   # 设置随机局部种子
#x =rng.normal(100,100,50)         #rng.normal变量（平均值：float，标准偏差：float）        
#x =x[:, np.newaxis]#在列上增加一个维度，变为50行1列，每一行是一个样本点
#y = 1.25 * x - 20 + 5 * rng.randn(50, 1)   # randn是标准正态分布；添加一点误差；
rng = np.random.RandomState(10)
x=100*rng.rand(50,4)
x1=x[:,0]
x1.shape=50,1
x2=x[:,1]
x2.shape=50,1
x3=x[:,2]
x3.shape=50,1
x4=x[:,1]
x4.shape=50,1
y=1.25*x1+2.5*x2+3*x3+4*x4+10+5*rng.randn(50,1)

model = LinearRegression(fit_intercept=True)#模型，多一个参数：截距b
model.fit(x, y)  # x,y的每一行是一个样本，即要求是列向量，fit：拟合，最小二乘法

#x_fit = np.linspace(min(x), max(x), 1000)#再生成样本点
#x_fit =x_fit[:, np.newaxis]       #将x_fit转置成列
#y_fit = model.predict(x_fit)#调用模型，测试

a=np.linspace(0,50,1000)       #将0~50创建1000个等差数列,验证模型
x1_fit =a[:, np.newaxis]
x2_fit =a[:, np.newaxis]
x3_fit =a[:, np.newaxis]
x4_fit =a[:, np.newaxis]
x_fit =np.hstack((x1_fit,x2_fit,x3_fit,x4_fit))     #将x1、x2、x3合并在一起
y_fit = model.predict(x_fit)                #根据x对y的预测

print("Model slope: ", model.coef_[0])#coef:参数，取得模型的第一个参数，斜率
print("Model intercept:", model.intercept_)#截距
print("方程的判定系数(R^2): %.6f" % model.score(x, y))     #计算得分

#%% 当噪声较大时
rng = np.random.RandomState(10)
x=100*rng.rand(50,4)
x1=x[:,0]
x1.shape=50,1
x2=x[:,1]
x2.shape=50,1
x3=x[:,2]
x3.shape=50,1
x4=x[:,1]
x4.shape=50,1
y=1.25*x1+2.5*x2+3*x3+4*x4+10+100*rng.randn(50,1)

model = LinearRegression(fit_intercept=True)#模型，多一个参数：截距b
model.fit(x, y)  # x,y的每一行是一个样本，即要求是列向量，fit：拟合，最小二乘法

a=np.linspace(0,50,1000)       #将0~50创建1000个等差数列,验证模型
x1_fit =a[:, np.newaxis]
x2_fit =a[:, np.newaxis]
x3_fit =a[:, np.newaxis]
x4_fit =a[:, np.newaxis]
x_fit =np.hstack((x1_fit,x2_fit,x3_fit,x4_fit))     #将x1、x2、x3合并在一起
y_fit = model.predict(x_fit)                #根据x对y的预测

print("Model slope: ", model.coef_[0])#coef:参数，取得模型的第一个参数，斜率
print("Model intercept:", model.intercept_)#截距
print("方程的判定系数(R^2): %.6f" % model.score(x, y))    
