import sys

sys.path.append('source')

import to_csv

if 'generate' in sys.argv:
    df = to_csv.to_csv('train.json')
elif 'open' in sys.argv:
    df = to_csv.from_csv('train.csv')
