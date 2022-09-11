import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def page_example():
    return jsonify(random.randint(1, 30))


app.run()
