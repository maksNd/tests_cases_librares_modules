import requests

web_link = r'http://bigkarta.ru/geo-map.gif'
picture_from_web = r'picture_from_web.gif'
response = requests.get(web_link)
############################### скачиваем картинку обычным способом
with open(picture_from_web, 'wb') as file:
    file.write(response.content)

web_link_2 = r'http://kartimira.ru/karta-mira-russkom.jpg'
picture_from_web_2 = r'picture_from_web_2.jpeg'
response_2 = requests.get(web_link_2)
############################### скачиваем картинку chunk'ами
with open(picture_from_web_2, 'wb') as file:
    counter = 0
    for chunk in response_2.iter_content(chunk_size=1 * 1000000):
        if counter < 2:
            print('chunk', counter)
            counter += 1
            file.write(chunk)

web_link_3 = r'https://yandex.ru'
saved_html = r'new_file_html.html'
response_3 = requests.get(web_link_3)
############################### скачиваем html страницу
with open(saved_html, 'wb') as file:
    file.write(response_3.content)
