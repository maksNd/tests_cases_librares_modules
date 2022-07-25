import datetime
import time

now = datetime.datetime.now()  # текущая дата до микросекунд
print(now)

print()

print(f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}.{now.microsecond}")

print()

print(now.strftime("%Y-%m-%d %H:%M"))  # формирование даты в любой формат
print(now.strftime("%X"))  # текущее время без микросекунд

start = datetime.datetime.now()
time.sleep(1)
end = datetime.datetime.now()
print(end - start)  # разница между двумя датами
