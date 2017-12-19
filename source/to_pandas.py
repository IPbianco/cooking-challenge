import numpy as np
import pandas
import unpack

train = unpack.unpack('train.json')

def unique_columns(data):
    unique = set()
    for row in data:
        for i in row['ingredients']:
            unique.add(i)
    return list(unique)

def get_vectorise_row(data):
    columns = unique_columns(data)

    def vectorise_row(row):
        ingredients = row['ingredients']
        return [1 if c in ingredients else 0 for c in columns]

    return vectorise_row

def vectorise(dishes, limit=0):
    v = get_vectorise_row(dishes)
    df = pandas.DataFrame(
        {dish['id']: v(dish) for dish in dishes}, 
        dtype=np.int8
    )
    df.index = unique_columns(dishes)
    return df.fillna(0).T

vectorise(train)
print('done')
