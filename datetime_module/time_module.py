import time
"""Количество секунд с 1го января 1970 года"""

time_1 = time.time()

time.sleep(5) # усыпляет программу на определенное  количество секунд

time_2 = time.time()
time_interval = time_2 - time_1
print(time_interval)

