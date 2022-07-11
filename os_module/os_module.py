import os
import datetime

"""resource about os module - https://pynative.com/python-file-creation-modification-datetime/"""

example = r'C:\Users\1\Desktop\tests_cases_librares_modules\json_module\json_module.py'

print(os.path.getmtime(example))  # Кроссплатформенный способ получить время (Unix timestamp) модификации файла
print(datetime.datetime.utcfromtimestamp(os.path.getmtime(example)).strftime('%d-%m-%Y %H:%M:%S'))

print()

print(os.path.getctime(example))  # только для win
# print(os.stat(example).st_birthtime) # только mac
