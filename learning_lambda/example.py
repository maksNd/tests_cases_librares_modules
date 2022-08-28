"""
lambda - функция с автоматическим (скрытым) вызовом return
lambda arg_1, arg_2, arg_3, ... : выражение
lambda может не принимать аргументов
lambda стоит использовать в тех случаях, когда требуется выполнить только одно действие
lambda не может заменить ф-ию без return, ф-ию с циклом
"""

func_with_lambda = lambda x: x ** 2

print(func_with_lambda(5), '\n')

triangle_perimetr = lambda a, b, c: a + b + c

print(triangle_perimetr(1, 2, 3), '\n')

h = lambda: 'Hello, world!'

print(h(), '\n')


