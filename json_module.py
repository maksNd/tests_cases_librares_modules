import json

json_file = r"json_example.json"

with open(json_file) as file:
    data_from_json_file = json.load(file)

print(data_from_json_file)
print(type(data_from_json_file))