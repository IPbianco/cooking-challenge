import sys
import pandas
from sklearn.linear_model import LogisticRegression
import ingredients
import unpack
from sklearn.externals import joblib

# Default values assigned from looper.py results
convert = 40
limit = 0

# Allows user to override default convert and limit values when generating model
for arg in sys.argv:
    if 'limit=' in arg:
        limit = int(arg.split('=')[1])
    elif 'convert=' in arg:
        convert = int(arg.split('=')[1])

i = ingredients.Ingredients(unpack.unpack('train.json'), convert)
df = i.vectorise(limit)
X = df.drop(columns='cuisine')
y = df['cuisine']

clf = LogisticRegression()
model = clf.fit(X, y)

joblib.dump(model, 'fit_model.pkl')
