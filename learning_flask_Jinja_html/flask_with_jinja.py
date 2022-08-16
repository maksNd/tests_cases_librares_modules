from flask import Flask, request, render_template
import random

app = Flask(__name__)


@app.route('/')
def using_Jinja():
    name = 'Alex'
    number = "+7 123 456 78 90"
    """Использование Jinja"""
    return render_template('Jinja.html', name=name, number=number)


@app.route('/<int:pk>')
def show_pk(pk):
    """Роут с параметром"""
    return str(pk)


@app.route('/prf/')
def dict_in_Jinja():
    user_data = {
        "name": "Ivan",
        "phone": "+7 123 456 78 90",
        "email": "ivan_dev@gmail.com",
        "telegram": "ivan_dev",
    }
    """Использование словаря в Jinja"""
    return render_template('dict_in_Jinja.html', user=user_data)


@app.route('/ln/')
def cycle_in_Jinja():
    items = ['Python', 'Java', 'Kotlin', 'Go']
    """Циклы в jinja"""
    return render_template('cycle_in_Jinja.html', items=items)  # запускается цикл по списку в шаблоне


@app.route('/acc/')
def condition_in_Jinja():
    is_blocked = random.choice([True, False, None])
    """Условия в jinja"""
    return render_template('condition_in_Jinja.html', is_blocked=is_blocked)


app.run(host='127.0.0.1', port=9999)
