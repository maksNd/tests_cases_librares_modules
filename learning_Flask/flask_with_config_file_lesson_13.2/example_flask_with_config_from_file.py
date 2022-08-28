from flask import Flask

app = Flask(__name__)

app.config.from_pyfile('config.py')  # чтобы все конфиги применились к приложению,
                                     # вызываем такой метод с указанием файла

# print(app.config)


@app.route('/')
def index_page():
    title = app.config.get('PROJECT_NAME')
    description = app.config.get('PROJECT_DESCRIPTION')

    return f'<h1>{title}</h1><p>{description}</p>'


app.run()
