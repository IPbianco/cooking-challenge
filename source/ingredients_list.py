import csv
import sys

with open('data/train.csv', 'r') as f:
    reader = csv.reader(f)
    names = next(reader)

print(names)
