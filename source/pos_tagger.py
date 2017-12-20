import nltk
import unpack
import collections

class PosTagger:

    def remove(self, ingredient):
        tokens = nltk.pos_tag(nltk.word_tokenize(ingredient))
        new = [token for token, tag in tokens if self.tag_ok(tag)]
        return ' '.join(new).lower()

    def get_conditional_remove(self, counter, limit):

        def conditional_remove(ingredient):
            if counter[ingredient] < limit:
                return self.remove(ingredient)
            return ingredient.lower()

        return conditional_remove

    def tag_ok(self, tag):
        return tag in ['NN', 'NNS']

    def convert(self, ingredients, counter, limit=0):
        converter = self.get_conditional_remove(counter, limit)
        return list(map(converter, ingredients))

