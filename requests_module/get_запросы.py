import requests

# httpbin - сервис для тестовых запросов, контроля/отладки запросов
"""
############################### get запросы ############################### 
"""
response = requests.get("https://httpbin.org/get")

############################### проверка статуса ответа
if response.status_code == 200:
    print('ok')

if response.ok:
    print('ok')

print(response.text)

############################## headers - есть у каждого запроса, который можно посмотреть в браузере
headers = {"User-Agent": "mkN"}

############################### при создании такого get запроса сервер вернет нам наш же headers
response = requests.get("https://httpbin.org/get", headers=headers)
print(response.text)

############################### при интерпретации ответа можно использовать модуль json (если ответ в формате json)
print(response.json())  # json() здесь - это метод объекта response (импортировать модуль json не нужно)

############################### передача параметров в get запросе
params = {'a': 'b', 'c': 'd', 'e': 10}
response_1 = requests.get("https://httpbin.org/get", headers=headers, params=params)
print(response_1.text)
