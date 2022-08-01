import dotenv
import os
from flask import Flask

app = Flask(__name__)
dotenv.load_dotenv(override=True)  # загружаем в переменные окружения данные из файла .env

# В зависимости от значения APP_CONFIG подключаем тот или другой конфиг
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
if os.environ.get("APP_CONFIG") == "work":
    app.config.from_pyfile('config/production.py')


@app.route('/')
def index_page():
    return f'{app.config.get("TITLE")}'


app.run()
