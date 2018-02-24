import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

wine = datasets.load_wine()
print (wine.data.shape, wine.target.shape)

X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.4, random_state=0)

print (X_test.shape, y_test.shape)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)                           
print (score)
