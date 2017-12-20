import unpack
import pandas
import to_pandas
import pos_tagger


def to_csv(path):
    data = unpack.unpack(path)
    print('Unpacked data, {} rows'.format(len(data)))
    unique = to_pandas.unique_columns(data)
    print('Got {} unique columns'.format(len(unique)))
    filtered = pos_tagger.filter_ingredients(unique, 50)
    print('Reduced to {} unique columns'.format(len(filtered)))
    df = to_pandas.vectorise(data, filtered)
    print('Created dataframe...')
    df.to_csv(path.replace('.json', '') + '.csv')
    print('Saved! ;)')
    return df

def from_csv(path):
    return pandas.read_csv(path)
