import pytest
from utils import ticket_price, divide, double, sum_of_two


def test_ticket_price_0():
    """
    Простейший тест
    """
    assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"


def test_ticket_price_1():
    """
    Простейший тест
    """
    assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"


def test_zero_division():
    """
    Чтобы проверить, выбрасывает ли функция ошибку в нужное время,
    нужно использовать специальный менеджер контекста
    pytest.raises(<Тип ошибки>)
    """
    with pytest.raises(ZeroDivisionError):
        divide(100, 0)


def test_type_mismatch():
    with pytest.raises(TypeError):
        divide(True, None)


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6)]
)
def test_double(test_input, expected):
    """
    Встроенный декоратор pytest.mark.parametrize
    позволяет параметризовать аргументы тестовых функций
    """
    assert double(test_input) == expected


# Конечно можно выносить параметры наружу
sum_of_two_parameters = [(0, 0, 0), (1, 1, 2), (-10, 10, 0)]


@pytest.mark.parametrize(
    "first, second, expected", sum_of_two_parameters
)
def test_sum_of_two(first, second, expected):
    assert sum_of_two(first, second) == expected


age_for_test = [(0, 'Бесплатно'), (1, "Бесплатно"), (7, "100 рублей"), (18, "200 рублей"),
                (25, "300 рублей"), (60, "Бесплатно"), (0.5, "Бесплатно"), (-1, "Ошибка")]


@pytest.mark.parametrize(
    'age, expected', age_for_test
)
def test_ticket_price(age, expected):
    assert ticket_price(age) == expected


from utils import get_circle_square


def test_get_circle_square_zero():
    square = get_circle_square(0)
    assert square == 0, "Неверное значение для 0"

def test_get_circle_square_one():
    square = get_circle_square(1)
    assert round(square, 2) == 3.14, "Неверное значение для 1"

def test_get_circle_square_normal():
    square = get_circle_square(3)
    assert round(square, 2) == 28.27, "Неверное значение для 3"

def test_get_circle_square_value_error():
    with pytest.raises(ValueError):
        get_circle_square(-2)

def test_get_circle_square_type_error():
    with pytest.raises(TypeError):
        get_circle_square("2")

from utils import get_grade

arguments_for_get_grade = [(10, 2), (30, 3), (60, 4), (90, 5)]
@pytest.mark.parametrize('value, result', arguments_for_get_grade)
def test_get_grade_normal(value, result):
    assert get_grade(value) == result

exception_for_get_grade = [('20', TypeError),('50', TypeError), (-1, ValueError), (101, ValueError)]
@pytest.mark.parametrize('value, exception', exception_for_get_grade)
def test_get_grade_exceptions(value, exception):
    with pytest.raises(exception):
        get_grade(value)

from utils import get_period
exception_for_get_period = [('10', TypeError), (True, TypeError), (-5, ValueError), (26, ValueError)]
@pytest.mark.parametrize('value, exception', exception_for_get_period)
def test_get_period_exception(value, exception):
    with pytest.raises(exception):
        get_period(value)

arguments_for_get_period = [(3, 'ночь'), (9, 'утро'), (15, 'день'), (20, 'вечер')]
@pytest.mark.parametrize('value, result', arguments_for_get_period)
def test_get_period_normal(value, result):
    assert get_period(value) == result