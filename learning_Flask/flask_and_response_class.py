import json

from flask import Flask

app = Flask(__name__)

my_dict = {1: 'one', 2: 'two'}


@app.get('/')
def index():
    """
    response_class - более гибкий вывод инф-ии
    """
    return app.response_class(
        response=json.dumps(my_dict, indent=4),
        status=200,
        mimetype='content/text'
    )

"""
смотреть ответ на запрос можно также в тирминале
curl -v http://localhost:8888
"""

app.run(host='localhost', port=8888)

