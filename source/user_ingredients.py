import unpack
import ingredients
import csv
import pandas
import sys
from sklearn.externals import joblib

row = []
data = unpack.unpack('user_ingredients.json')
selected_ingredients = data['ingredients']

with open('data/train.csv', 'r') as f:
    reader = csv.reader(f)
    names = next(reader)

number_of_ingredients = len(names) - 2

for unique_ingredient in names:
    if unique_ingredient in selected_ingredients:
        row.append(1)
    else:
        row.append(0)

df = pandas.DataFrame([row])
df.to_csv("data/user_ingredients.csv", sep=',',index=False, header=False)

dataset = pandas.read_csv('data/user_ingredients.csv', names=names, low_memory=False)
array = dataset.values
X = array[:,0:number_of_ingredients]
Y = array[:,number_of_ingredients]

model = joblib.load('source/fit_model.pkl')
predicted = model.predict(X)
print(predicted[0])
