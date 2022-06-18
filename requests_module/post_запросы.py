import requests

# httpbin - сервис для тестовых запросов, контроля/отладки запросов

headers = {"User-Agent": "mkN"}
params = {'a': 'b'}
response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params=params,
                         json={'username': 'mkN'})  # передаем параметры в post запросе
print(response.text)
