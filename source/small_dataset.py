import nltk
import unpack
import collections

train = unpack.unpack('train.json')
ing = []
for dish in train:
    ing.extend(dish['ingredients'])

unique = set(ing)
counts = collections.Counter(ing)

print(len(unique))

def is_ok(tag):
    return tag == 'NN' or tag == 'NNS'

def do(limit):
    converted = []
    for ingredient in ing:
        if counts[ingredient] < limit:
            tokens = nltk.word_tokenize(ingredient)
            pos_tagged = nltk.pos_tag(tokens)
            filtered = [token for token, tag in pos_tagged if is_ok(tag)]
            converted.append(' '.join(filtered).lower())
        else:
            converted.append(ingredient.lower())
    return collections.Counter(converted)

data = do(50)
