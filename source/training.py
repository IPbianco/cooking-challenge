import sys
import pandas
from sklearn.linear_model import LogisticRegression
import ingredients
import unpack
from sklearn.externals import joblib

convert = 50
limit = 20

i = ingredients.Ingredients(unpack.unpack('train.json'), convert)
df = i.vectorise(limit)
X = df.drop(columns='cuisine')
y = df['cuisine']

clf = LogisticRegression()
model = clf.fit(X, y)

joblib.dump(model, 'fit_model.pkl')
