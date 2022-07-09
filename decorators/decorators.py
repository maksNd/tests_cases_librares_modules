import datetime


def time_counter(function):
    """Считает время выполнения функции"""
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = function(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return result

    return wrapper


@time_counter
def func_with_cycle(n):
    my_list = []
    for i in range(n ** 4):
        if i % 2 == 0:
            my_list.append(i)
    return my_list


@time_counter
def func_with_comprehension(n):
    my_list = [num for num in range(n ** 4) if num % 2 == 0]
    return my_list


print(func_with_cycle(10)[::200])
print()
print(func_with_comprehension(10)[::200])
