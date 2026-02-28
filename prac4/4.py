#1
import json

data = '{"name": "Dias", "age": 20}'
obj = json.loads(data)

print(obj["name"])

#2
import json

person = {"name": "Dias", "age": 20}
json_data = json.dumps(person)

print(json_data)

#3
import json

data = {"name": "Dias", "age": 20}

with open("data.json", "w") as f:
    json.dump(data, f)
print(data)
#4
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)