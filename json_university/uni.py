import json

json_data = open('data.json')
data = json.load(json_data)
for x in data:
    print(data[int(x)])