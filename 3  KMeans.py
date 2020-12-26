import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt

data = pd.read_csv(r"C:\Users\Administrator\Desktop\kekeke\python\k课程设计\testSet.csv",names =[1,2])
#names:指定列名;<class 数据类型'pandas.core.frame.DataFrame'>
x=np.array(data)
plt.scatter(x[:,0],x[:,1])
plt.title('Raw data')
plt.show()

#无监督算法，学习过程就是训练质心的位置，进行聚类
class Kmeans:
    def __init__(self,k):
        self.k = k
        #初始化  k：聚成K个类
    
    def calc_distance(self,x1,x2):
        diff = x1 - x2
        distances = np.sqrt(np.square(diff).sum(axis=1))#欧几里得距离
        #np.square：平方，np.sqrt：平方根
        return distances
    
    def fit(self,x):
        self.x = x
        m,n = self.x.shape
        #随机选定k个数据作为初始质心，不重复选取
        self.original_ = np.random.choice(m,self.k,replace=False)#随机选取索引值
        #默认类别是从0到k-1
        self.original_center = x[self.original_]
        print("初始质心为：",self.original_center)
        
        a=0
        while True:
        #for z in range(10):
            #初始化一个字典，以类别作为key，赋值一个空数组
            y=self.original_center
            dict_y = {}
            for j in range(self.k):
                dict_y[j] = np.empty((0,n))
                #print("字典",dict_y)
            for i in range(m):
                distances =self.calc_distance(x[i],self.original_center)
                #np.argsort：将元素从小到大排序，返回排序后的下标，[0]：取出数组中的最小值
                label = np.argsort(distances)[0]
                #np.r_:按列连接两矩阵，上下相加，要求列数相等
                #reshape:将数据变为一行，只指定行数，对列数无要求
                dict_y[label] = np.r_[dict_y[label],x[i].reshape(1,-1)]
            y_preds = model.predict(x)
            plt.scatter(x[:,0],x[:,1],c=y_preds)
            plt.title('Iteration Result:the num %d'%a)
            plt.plot(y[:,0],y[:,1],'o',color='r')
            plt.show()
            centers = np.empty((0,n))
            #新求质心
            for i in range(self.k):
                center = np.mean(dict_y[i],axis=0).reshape(1,-1)#求平均值
                centers = np.r_[centers,center]
            
            # 与上一次迭代的质心比较，如果没有发生变化，则停止迭代）
            result = np.all(centers == self.original_center)
            if result == True:
                break
            else:
                #继续更新质心
                self.original_center = centers
                a=a+1
                print("第%d次迭代"%a)
                print("新的质心为：",self.original_center)
                
    def predict(self,x):      #预测样本属于的簇  返回类数组，每一个x所属的簇
        y_preds = []
        m,n = x.shape
        for i in range(m):
            distances =self.calc_distance(x[i],self.original_center)
            y_pred = np.argsort(distances)[0]
            y_preds.append(y_pred)
        return y_preds

num=input("请输入要聚类的个数：")
num=int(num)
model = Kmeans(num)
model.fit(x)
y_preds = model.predict(x)
plt.scatter(x[:,0],x[:,1],c=y_preds)
plt.title('Final Result')
plt.show()
