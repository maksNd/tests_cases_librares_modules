import logging

from flask import Flask, request, render_template

# logging.basicConfig(level=logging.INFO) # базовый логер (вывод в консоль)

# add filemode="w" to overwrite
logging.basicConfig(filename="basic.log",
                    level=logging.INFO, filemode='w',
                    encoding='utf-8')  # логи перенаправлены в файл

app = Flask(__name__)


@app.route('/', )
def page_index():
    logging.info("Главная страница запрошена")
    return "Главная страница"


@app.route('/store')
def page_store():
    logging.info("Страница магазина запрошена")
    return "Страница магазина "


@app.route('/store/<cat>')
def page_cat(cat):
    logging.info(f"Страница категории {cat} запрошена")
    return f"Страница категории {cat} "


app.run()
