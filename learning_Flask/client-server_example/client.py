import time

import requests


def get_data_from_server():
    data_from_server = requests.get('http://127.0.0.1:5000')
    return data_from_server.json()


for i in range(30):
    print(get_data_from_server())
    time.sleep(2)
