# Load libraries
import csv
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib

with open('../data/train_with_index.csv', 'r') as f:
    reader = csv.reader(f)
    names = next(reader)

dataset = pandas.read_csv('../data/train.csv', names=names, low_memory=False)
dataset2 = pandas.read_csv('../data/one.csv', names=names, low_memory=False)
print("Finished reading")

# Split-out validation dataset
array = dataset.values
# array2 = dataset2.values

X = array[:,0:1530]
# X2 = array2[:,0:1530]
# Y = array[:,1530]
#
# from sklearn import metrics
# model = LogisticRegression()
# model.fit(X, Y)
# joblib.dump(model, 'filename.pkl')

clf = joblib.load('filename.pkl')
predicted = clf.predict(X)
print(predicted)

# display the relative importance of each attribute
# expected = Y
# predicted = model.predict(X2)
# print(predicted)
# validation_size = 0.20
# seed = 7
# X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
#
# # Test options and evaluation metric
# seed = 7
# scoring = 'accuracy'
#
# # Spot Check Algorithms
# models = []
# # models.append(('RFC', RandomForestClassifier()))
# models.append(('LR', LogisticRegression()))
# # models.append(('SVC', SVC()))
# # models.append(('CART', DecisionTreeClassifier()))
# # models.append(('NB', GaussianNB()))
# # models.append(('KNN', KNeighborsClassifier()))
#
# # evaluate each model in turn
# results = []
# names = []
# for name, model in models:
# 	kfold = model_selection.KFold(n_splits=10, random_state=seed)
# 	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
# 	results.append(cv_results)
# 	names.append(name)
# 	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
# 	print(msg)
#
# # Make predictions on validation dataset
# knn = LogisticRegression()
# knn.fit(X_train, Y_train)
# predictions = knn.predict(X_validation)
# print(accuracy_score(Y_validation, predictions))
# print(confusion_matrix(Y_validation, predictions))
# print(classification_report(Y_validation, predictions))
