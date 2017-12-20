import numpy as np
import pandas
import pos_tagger
from collections import Counter

class Vectoriser:

    def __init__(self, ingredients, limit=0, cuisine=True):
        self.count = Counter(ingredients)
        keys = sorted(self.count.keys())
        self.permit = [c for c in keys if self.count[c] >= limit]
        self.cuisine = cuisine

    def get_vectorise(self):
        columns = self.permit
        if self.cuisine:

            def vectorise(row):
                ingredients = row['ingredients']
                vector = [1 if c in ingredients else 0 for c in columns]
                vector.append((row['cuisine']))
                return vector
        else:

            def vectorise(row):
                ingredients = row['ingredients']
                vector = [1 if c in ingredients else 0 for c in columns]
                return vector

        return vectorise

    def vectorise(self, dishes):
        vectoriser = self.get_vectorise()
        df = pandas.DataFrame(
            {dish['id']: vectoriser(dish) for dish in dishes}, 
            dtype=np.int8
            )
        df.index = self.permit + ['cuisine'] if self.cuisine else []
        return df.T
