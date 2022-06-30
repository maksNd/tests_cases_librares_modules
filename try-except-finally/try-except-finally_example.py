"""try / except / finally - обработчик исключений, описывает поведение программы при возникновении исключений"""

class ArgumentEqualZeroError(Exception):
    """Можно писать свои классы исключений, наследуясь от класса Exception"""
    """Возникает когда делитель равен 0"""
    pass


def divide(a, b):
    if not isinstance(a, int | float) or not isinstance(b, int | float):
        raise ValueError("Аргументы должны быть числами")  # ValueError - ошибка переданного аргумента

    if b == 0:
        raise ArgumentEqualZeroError("На 0 делить нельзя")

    try:
        return a // b

    except ZeroDivisionError:  # не оставлять exept пустым, хорошая практика - ловить конкретный тип исключений
        return "Ошибка! На ноль делить нельзя"

    except TypeError:
        return "Неверный тип данных"


# досмотреть https://www.youtube.com/watch?v=jiqYwQ9wpQY
a, b = 4, '0'


try:
    result = divide(a, b)
except (ArgumentEqualZeroError, ValueError) as exc:  # 'as exc' нужно, если мы хотим что-т от исключения получить
    print(exc)  # выведет текст исключения
    """Так можно делать когда нужно описать дополнительные действия перед поднятием исключения"""
    raise  # поднимет то исключение, которое перехватил из множества в блоке except
finally:  # блок finaly отработает в любом случае
    print("функция завершилась")