from pos_tagger import PosTagger
from collections import Counter
from vectorise import Vectoriser

class Ingredients:

    def __init__(self, data, pos_tag_threshold=0):
        self.data = data
        self.original = self.get_all(data)
        self.mapping = self.get_mapping(self.original, pos_tag_threshold)
        self.converted = self._map(self.original, self.mapping)
        self.convert_data(self.data, self.mapping)
        self.df = None

    def get_all(self, data):
        ingredients = []
        for dish in data:
            ingredients.extend(dish['ingredients'])
        return ingredients

    def get_mapping(self, original, threshold):
        unique = set(original)
        converted = PosTagger().convert(
            unique, Counter(self.original), threshold
            )
        return {a: b for a, b in zip(unique, converted)}

    def get_reduced(self, converted, limit):
        counts = Counter(converted)
        reduced = []
        for ingredient, count in counts.items():
            if count < limit:
                reduced.extend([ingredient] * count)
        return reduced

    def _map(self, original, mapping):
        return list(map(mapping.__getitem__, original))

    def convert_data(self, data, mapping):
        for dish in data:
            ingredients = dish['ingredients']
            dish['ingredients'] = self._map(ingredients, mapping)

    def vectorise(self, limit):
        self.df = Vectoriser(self.converted, limit).vectorise(self.data)
        return self.df

    def save(self, path):
        if self.df is None:
            raise ValueError('not yet vectorised')
        self.df.to_csv(path, index=False, header=False)
