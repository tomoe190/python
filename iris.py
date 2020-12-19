from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz   #先：conda install python-graphviz

#安装Graphviz参照  https://www.jianshu.com/p/8ede808e6f92


iris = load_iris()
n=len(iris.target)     #样本的个数
xh = np.arange(n)
np.random.seed(10)
np.random.shuffle(xh)
k=n//2  #训练集样本数
x_train=iris.data[xh[:k],:]
y_train=iris.target[xh[:k]]
x_test=iris.data[xh[k:],:]
y_test=iris.target[xh[k:]]
clf = tree.DecisionTreeClassifier(max_depth=3)  #uses an optimised version of the CART algorithm
clf = clf.fit(x_train, y_train)


dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("iris")   # the results are saved in an output file iris.pdf
print('训练集判断准确率为： %.2f' % clf.score(x_train, y_train))
print('测试集判断准确率为： %.2f' % clf.score(x_test, y_test))