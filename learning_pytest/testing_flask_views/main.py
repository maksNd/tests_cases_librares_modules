"""
Какого рода тесты можно выполнять:
1.Проверить, что обращение к эндпоинту (маршрут + метод) обрабатывается.
2.Проверить, что обращение к эндпоинту возвращает верную структуру данных.
3.Проверить, что обращение к эндпоинту возвращает нужные данные.
4.Проверить, что запрос на создание или изменение данных действительно изменяет их.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

data = {'name': 'Alice'}

"""
Все нижеследующее написано для демонстрации тестирования
различных запросов с различными параметрами в main_test.py

Еcли вы отправляете запрос, а в представлении установлен редирект, то нужно разрешить редиректы
response = app.test_client().post('/', json=data, follow_redirects=True)
"""


@app.route('/')
def example():
    return 'test message'


@app.route('/text/')
def page_text():
    return 'it works'


@app.route('/dict/')
def page_with_dict():
    data = {'name': 'Alice'}
    return jsonify(data)


@app.route('/query')
def page_with_query():
    s = request.args.get('s')
    return f'{s}'


@app.route('/post_with_json', methods=['POST'])
def post_page_with_json():
    name = request.json.get('name')
    data_to_return = {'name_received': name}
    return jsonify(data_to_return)


if __name__ == '__main__':
    app.run()
