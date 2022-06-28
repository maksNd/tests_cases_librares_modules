import requests

DATA_SOURSE = "https://jsonkeeper.com/b/IWUE"

response = requests.get("https://jsonkeeper.com/b/IWUE")
response.raise_for_status()  # нужна для того, чтобы проверить, понял вас сервер или нет
                             # если нет - упадет с ошибкой
"""
Если не вызвать raise_for_status, программа подумает, что всё в порядке,
что вы так и хотели: отправить запрос на страницу, которой нет.
Обязательно вызывайте .raise_for_status() после каждого запроса в интернет,
иначе вы рискуете потратить кучу времени на поиск ошибки, которую замалчивает библиотека requests.
"""

print(response.text)
