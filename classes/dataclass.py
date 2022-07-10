"""
video - https://www.youtube.com/watch?v=CvQ7e6yUtnw
"""
from dataclasses import dataclass

"""
dataclasses предназначены для хранения данных.
Автоматически создает __repr__(генерируется декоратором).
Позволяет упростить __init__.
"""


@dataclass  # (frozen = True) сделат экземпляры класса неизменяемыми
class Person:
    name: str  # инициализатор будет сгенерирован декоратором
    address: str
    active: bool = True


user_1 = Person('Ivan', 'qwe 12/3')
print(user_1)
