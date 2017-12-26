# Importing third-party modules
import sys
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

# Importing first-party scripts
sys.path.append('source')
import ingredients
import unpack

class Looper:

    def __init__(self, algorithm):
        self.all_scores = []
        self.algorithm = algorithm

# all_scores = []
# algorithm = LogisticRegression()

def create_train_and_test_sets(data, limit, test_size):
    df = data.vectorise(limit)
    X = df.drop(columns='cuisine')
    y = df['cuisine']
    return train_test_split(X, y, test_size=test_size, random_state=42)

def train_and_score_model(algorithm, X_train, X_test, y_train, y_test):
    model = algorithm.fit(X_train, y_train)
    return model.score(X_test, y_test)


for convert in range(1):
    i = ingredients.Ingredients(unpack.unpack('train.json'), convert)
    current_cycle = []
    single = [convert]
    for limit in range(1):
        single.append(limit)
        X_train, X_test, y_train, y_test = create_train_and_test_sets(i, limit, 0.4)
        score = train_and_score_model(algorithm, X_train, X_test, y_train, y_test)
        single.append(score)
        current_cycle.append(single)
        print(single)
        single = [convert]
    all_scores.append(current_cycle)



class Printer:

    def __init__(self, score_set):
        self.score = 0
        self.result = []
        self.score_set = score_set


    def find_best_result(self):
        for x in self.score_set:
            for y in x:
                if y[2] > self.score:
                    self.score = y[2]
                    self.result = y

    def print_results(self):
        self.find_best_result()
        print("The optimum parameters are a convert of {} and a limit of {}, which yields a score of {}".format(self.result[0], self.result[1], self.result[2]))

p = Printer(all_scores)

p.print_results()
