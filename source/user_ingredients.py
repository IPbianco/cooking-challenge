import unpack
import ingredients
import csv
import pandas
import sys
from sklearn.externals import joblib

row = []
data = unpack.unpack('user_ingredients.json')
selected_ingredients = data['ingredients']

with open('data/train_with_index.csv', 'r') as f:
    reader = csv.reader(f)
    names = next(reader)

for unique_ingredient in names:
    if unique_ingredient in selected_ingredients:
        row.append(1)
    else:
        row.append(0)

df = pandas.DataFrame([row])
df.to_csv("data/user_ingredients.csv", sep=',',index=False, header=False)

dataset = pandas.read_csv('data/user_ingredients.csv', names=names, low_memory=False)
array = dataset.values
X = array[:,0:1530]
Y = array[:,1530]

model = joblib.load('source/fit_model.pkl')
predicted = model.predict(X)
print(predicted[0])
