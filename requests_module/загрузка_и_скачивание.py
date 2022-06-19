import requests

web_link = r'http://bigkarta.ru/geo-map.gif'
new_file = r'jpeg_from_web.gif'

response = requests.get(web_link)
with open(new_file, 'wb') as file:
    file.write(response.content)

# print(response.text)