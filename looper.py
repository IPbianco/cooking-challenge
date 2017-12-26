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

    def __init__(self, algorithm=LogisticRegression()):
        self.all_scores = []
        self.current_cycle = []
        self.current_score = None
        self.single_cycle = None
        self.algorithm = algorithm
        self.ingredients = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def create_train_and_test_sets(self, data, limit, test_size=0.4):
        df = data.vectorise(limit)
        X = df.drop(columns='cuisine')
        y = df['cuisine']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.4, random_state=42)

    def train_and_score_model(self):
        model = self.algorithm.fit(self.X_train, self.y_train)
        self.current_score = model.score(self.X_test, self.y_test)

    def create_current_cycle_array(self, convert):
        self.current_cycle = []
        self.ingredients = ingredients.Ingredients(unpack.unpack('train.json'), convert)
        self.single_cycle = [convert]

    def score_parameters(self, limit):
        self.create_train_and_test_sets(self.ingredients, limit)
        self.train_and_score_model()

    def update_single_cycle(self, limit):
        self.single_cycle.append(limit)
        self.single_cycle.append(self.current_score)

    def complete_current_and_reset_single(self, convert):
        self.current_cycle.append(self.single_cycle)
        self.single_cycle = [convert]

    def update_and_reset_cycle(self, limit, convert):
        self.score_parameters(limit)
        self.update_single_cycle(limit)
        self.complete_current_and_reset_single(convert)

    def loop(self):
        for convert in range(1):
            self.create_current_cycle_array(convert)
            for limit in range(1):
                self.update_and_reset_cycle(limit, convert)
            self.all_scores.append(self.current_cycle)

class Printer:

    def __init__(self, score_set):
        self.score = 0
        self.result = []
        self.score_set = score_set

    def update_best_score(self, array):
        if array[2] > self.score:
            self.score = array[2]
            self.result = array

    def find_best_result(self):
        for x in self.score_set:
            for y in x:
                self.update_best_score(y)

    def print_results(self):
        self.find_best_result()
        print("The optimum parameters are a convert of {} and a limit of {}, which yields a score of {}".format(self.result[0], self.result[1], self.result[2]))


l = Looper()
l.loop()
p = Printer(l.all_scores)
p.print_results()
