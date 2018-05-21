import json

with open('test.json') as json_data:
    data = json.load(json_data)

print(data)