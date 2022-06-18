import requests

jsonkeepre_link = r'https://jsonkeeper.com/b/OBB3'

response = requests.get(jsonkeepre_link)
print(response.json())
print(type(response.json()))