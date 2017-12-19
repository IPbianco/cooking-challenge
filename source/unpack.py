import json
import os

PATH = os.path.dirname(__file__) + '/../data/{}'

def unpack(dataset):
    """Convert a dataset from JSON to a Python dictionary."""
    with open(PATH.format(dataset)) as source:
        return json.loads(source.read())
