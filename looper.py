import sys
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

sys.path.append('source')

import ingredients
import unpack

all_scores = []

for convert in range(0, 250, 10):
    i = ingredients.Ingredients(unpack.unpack('train.json'), convert)
    current_cycle = []
    single = [convert]
    for limit in range(1):
        single.append(limit)
        df = i.vectorise(limit)
        X = df.drop(columns='cuisine')
        y = df['cuisine']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)
        clf = LogisticRegression()
        model = clf.fit(X_train, y_train)
        single.append(model.score(X_test, y_test))
        current_cycle.append(single)
        print(single)
        single = [convert]
    all_scores.append(current_cycle)

score = 0
result = []

for x in all_scores:
    for y in x:
        if y[2] > score:
            score = y[2]
            result = y
print(result)
print("The optimum parameters are a convert of {} and a limit of {}, which yields a score of {}".format(result[0], result[1], result[2]))
