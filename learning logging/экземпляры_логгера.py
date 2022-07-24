import logging

"""
Для больших проектов создают несколько экземпляров логеров, например для каждого модуля
Далее настроенный логер можно импортировать в любой модуль
"""

logger = logging.getLogger('one')  # получение экземпляра логера
logger.setLevel(logging.DEBUG)  # устанавливаем уровень сообщений логера

console_handler = logging.StreamHandler()  # создание обработчика логера для консоли
file_handler = logging.FileHandler("log.log", encoding='utf-8')  # создание обработчика логера для файла
file_handler.setLevel(logging.WARNING)  # устанавливаем уровень сообщений хэндлера


formatter_one = logging.Formatter(
    "%(levelname)s : %(asctime)s : %(message)s")  # создаем форматирование для для обработчика

file_handler.setFormatter(formatter_one)  # применяем форматирование к обработчику
console_handler.setFormatter(formatter_one)

logger.addHandler(console_handler)  # добавление обработчика (для консоли) к логеру
logger.addHandler(file_handler)  # добавление обработчика (для файла) к логеру

logger.warning("Все работает")  # выведет лог в консоль и в файл (т.к подключены соответствующие обработчики)
