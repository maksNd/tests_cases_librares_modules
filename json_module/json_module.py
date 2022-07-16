import json

######################### json - javaScript object notation

string_as_json = '''{"1": "qwe", "2": "wer", "3": "fgh"}'''
######################### json.load преобразует str как json
data_from_json_string = json.loads(string_as_json)
print(data_from_json_string)
print()

json_file = r"json_example.json"
######################### json.load преобразует json файл в питоновский объект
######################### json.loads преобразует json строку в питоновский объект
with open(json_file) as file:
    data_from_json_file = json.load(file)
print(data_from_json_file)
print(type(data_from_json_file))
print()

dict_for_json_dumps = {1: True, 2: False, 3: 'кошка', 4: None}
######################### json.dumps преобразует питоновский объект в json объект
json_dumps = json.dumps(dict_for_json_dumps, indent=4)  # indent - количество отступов для вложенностей
print(json_dumps)
print()

dict_for_json_dump_to_file = {1: True, 2: False, 3: 'кошка', 4: None}
######################### json.dump преобразует питоновский объект в json файл
with open("new_json_example.json", 'w') as file:
    json.dump(dict_for_json_dump_to_file, file)
