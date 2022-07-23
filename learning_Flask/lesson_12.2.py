from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def form_page():
    """Все данные из адресной строки храняться в объекте request.args """
    return render_template('form.html')  # шаблон перенаправит на страницу /search


@app.get('/search')
def search_page():
    s = request.args['s']  # получить поисковую строку
    # s = request.args.get('s') # тоже самое (получить поисковую строку)
    return f"You've input '{s}'"


@app.get('/filter')
def filter_page():
    try:
        from_value = request.args['from']
        to_value = request.args['to']
        return f'Search from {from_value} to {to_value}'
    except KeyError:
        return 'No data'

    # if from_value and to_value:


app.run(host='127.0.0.1', port=8888, debug=True)
