import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

data2 = json.dumps(data)
with open('Test.json', 'a') as f:
    f.write(data2)
