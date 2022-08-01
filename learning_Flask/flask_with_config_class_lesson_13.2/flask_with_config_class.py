from flask import Flask
from config_class import Config

app = Flask(__name__)
app.config.from_object(Config)

path = app.config.get("PATH")
print(path)