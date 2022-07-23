import json

######################### добавление данных в json, работает с кирилицей
filename = 'json_example.json'
data_for_add = {1: 'коте', '2': 'wer', '3': 'ert'}
with open(filename, encoding='utf-8') as file:
    data = json.load(file)
    data.append(data_for_add)

with open(filename, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)
