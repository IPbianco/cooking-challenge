import nltk
import unpack
import collections


def get_counts(ingredients):
    return collections.Counter(ingredients)


def tag_ok(tag):
    return tag == 'NN' or tag == 'NNS'


def filter_pos_tags(ingredient):
    tokens = nltk.pos_tag(nltk.word_tokenize(ingredient))
    filtered = [token for token, tag in tokens if tag_ok(tag)]
    return ' '.join(filtered).lower()


def filter_ingredients(ing, limit):
    converted = []
    counts = get_counts(ing)
    for ingredient in ing:
        if counts[ingredient] < limit:
            converted.append(filter_pos_tags(ingredient))
        else:
            converted.append(ingredient.lower())
    return list(filter(lambda i: i.islower(), set(converted)))
