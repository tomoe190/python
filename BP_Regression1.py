from sklearn.neural_network import MLPRegressor
import numpy as np
import matplotlib.pyplot as plt

# 生成数据--训练集和测试集
np.random.seed(42)
n = 500
X_train = np.random.uniform(-10, 10, size=n)
X_train = np.sort(X_train)
y_train = X_train * np.cos(X_train) + 0.5 * np.random.randn(n)
X_train = X_train[:, np.newaxis]
np.random.seed(43)
X_test = np.random.uniform(-10, 10, size=n)
X_test = np.sort(X_test)
y_test = X_test * np.cos(X_test) + 0.5 * np.random.randn(n)
X_test = X_test[:, np.newaxis]

for k in range(4):
    # 配置MLP（BP算法）的参数，尝试改变hidden_layer_sizes
    ref = MLPRegressor(
            solver='lbfgs',
            alpha=0,
            hidden_layer_sizes=(
                    5*(k+1)),     #尝试改变“10”
                    tol=1e-6,
                    random_state=20)
    #‘lbfgs’ is an optimizer in the family of quasi-Newton methods.
    # alpha : L2 penalty (regularization term) parameter.
    # hidden_layer_sizes :The ith element represents the number of neurons in      
    # the ith hidden layer.

    # 模型训练及评价
    ref.fit(X_train, y_train)
    print('训练集-判定系数R^2为：{0:.2f}'.format(ref.score(X_train, y_train)))
    print('测试集-判定系数R^2为：{0:.2f}'.format(ref.score(X_test, y_test)))


   # 画出回归曲线
    y_predict = ref.predict(X_train)

    plt.subplot(221+k)
    plt.scatter(X_train, y_train, s=5, c='k', marker='.')
    plt.plot(X_train, y_predict,color='r',linewidth=4)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
plt.show()
