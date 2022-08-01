from main import app


def test_text_page():  # тестируем GET запрос (вернуться должен текст)
    response_text_page = app.test_client().get('/text/')
    assert response_text_page.status_code == 200
    assert response_text_page.data == b'it works'


def test_page_with_dict():  # тестируем GET запрос (вернуться должен словарь)
    response_page_with_dict = app.test_client().get('/dict/')
    assert response_page_with_dict.status_code == 200
    assert response_page_with_dict.json == {'name': 'Alice'}  # ожидаем конкретный словарь
    assert response_page_with_dict.json.get('name') == 'Alice'  # ожидаем конкретное значение по ключу


def test_page_with_query_parameters():  # тестируем GET запрос c query параметрами
    parameters = {'s': 'cat'}
    response = app.test_client().get('/query', query_string=parameters)
    assert response.status_code == 200
    assert response.text == 'cat'


def test_post_page_with_json():  # тестируем POST запрос с передачей json и ответом json
    data = {'name': 'Alice'}
    response = app.test_client().post('/post_with_json', json=data)
    assert response.json == {'name_received': 'Alice'}