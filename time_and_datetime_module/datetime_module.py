import datetime
import time

now = datetime.datetime.now()  # текущая дата до микросекунд
print(now)

print()

"""Так можно получитьтекущий год, месяц, день, час и т.д."""
print(f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond}")

print()

print(now.strftime("%Y-%m-%d %H:%M"))  # формирование даты в любой формат
print(now.strftime("%X"))  # текущее время без микросекунд

start = datetime.datetime.now()
time.sleep(1)
end = datetime.datetime.now()
print(end - start)  # разница между двумя датами
print()

"""Конвертировать Unix timestamp в обычный формат даты"""
ts = int("1284101485")
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try 'ts /= 1000' in that case
print(datetime.datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S'))