import unpack
import csv
import pandas

row = []
data = unpack.unpack('one.json')
selected_ingredients = data[0]['ingredients']

with open('../data/train_with_index.csv', 'r') as f:
    reader = csv.reader(f)
    names = next(reader)

for unique_ingredient in names:
    if unique_ingredient in selected_ingredients:
        row.append(1)
    else:
        row.append(0)

df = pandas.DataFrame([row])
df.to_csv("one.csv", sep=',',index=False, header=False)
