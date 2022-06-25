import requests

web_link_3 = r'https://yandex.ru'
saved_html = r'new_file_html.html'
response_3 = requests.get(web_link_3)
############################### скачиваем html страницу
with open(saved_html, 'wb') as file:
    file.write(response_3.content)
