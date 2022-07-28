def ticket_price(age):
    if 0 <= age < 7 or age >= 60:
        return "Бесплатно"
    elif 7 <= age < 18:
        return "100 рублей"
    elif 18 <= age < 25:
        return "200 рублей"
    elif 25 <= age < 60:
        return "300 рублей"
    else:
        return "Ошибка"


def divide(first, second):
    return first / second


def double(value):
    return value * 2


def sum_of_two(first, second):
    return first + second


import math


def get_circle_square(radius):
    if type(radius) not in [int, float]:
        raise TypeError("should be in or float more than zero")
    if radius < 0:
        raise ValueError("should be in or float more than zero")
    return radius ** 2 * math.pi


def get_grade(points):
    if type(points) != int: raise TypeError("Должно быть int")
    if points < 0 or points > 100: raise ValueError("Должно быть от 0 до 100")

    if points < 20:
        return 2
    elif points < 40:
        return 3
    elif points < 80:
        return 4
    else:
        return 5


def get_period(hour):
    if type(hour) != int: raise TypeError("Должно быть int")
    if hour < 0 or hour > 24: raise ValueError("Допустимое значение 0-24")
    if hour < 7:
        return "ночь"
    elif hour < 12:
        return "утро"
    elif hour < 18:
        return "день"
    else:
        return "вечер"
