#Loading required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

#Loading datasets
iris = datasets.load_iris()

#Display description, features and labels
features = iris.data
labels = iris.target
# print(iris.DESCR) # 3 classes are there
# print(features[0], labels[0])

#Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

# printing class label when sepal length = 1, sepal width =1, petal length =1 , petal width = 1
preds = clf.predict([[12, 10, 1, 8]])
print(preds)