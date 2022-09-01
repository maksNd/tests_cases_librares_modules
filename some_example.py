import datetime

from flask import Flask
from time import sleep

app = Flask(__name__)


@app.route('/')
def index():
    sleep(100)
    return 'message after sleeping'


app.run()
