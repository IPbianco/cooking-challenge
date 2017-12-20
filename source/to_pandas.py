import numpy as np
import pandas
import unpack


def unique_columns(data):
    unique = set()
    for row in data:
        for i in row['ingredients']:
            unique.add(i)
    return list(unique)


def get_vectorise_row(data, columns):

    def vectorise_row(row):
        ingredients = row['ingredients']
        vector = [1 if c in ingredients else 0 for c in columns]
        vector.append((row['cuisine']))
        return vector

    return vectorise_row


def vectorise(dishes, columns):
    v = get_vectorise_row(dishes, columns)
    df = pandas.DataFrame(
        {dish['id']: v(dish) for dish in dishes}, 
        dtype=np.int8
    )
    df.index = columns + ['cuisine']
    return df.T
