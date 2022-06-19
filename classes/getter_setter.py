from datetime import datetime


class Player:
    __LEVEL, __HEALTH = 1, 100  # константы для создания полей

    __slots__ = ['__level', 'health', 'born']  # разрешенные свойства экземпляра
    # это значит что добавить новых свойств (не перечисленных в атрибуте __slots__ будет невозможно)

    def __init__(self):
        self.__level = Player.__LEVEL  # пишем имя класса чтобы получить доступ к константе
        self.health = Player.__HEALTH
        self.born = datetime.now()

    # def get_level(self):
    #     return self.__level
    #
    # def set_level(self, level):
    #     self.__level += level

    @property # декоратор
    def level(self):
        return self.__level

    @level.setter # декоратор setter не может существовать без декоратора property
    def level(self, level):
        if level > 85: level = 85
        if level < self.__level: level = self.__level
        self.__level = level
    # таким образом можно возвращать или изменять значение level как неинкапсулированные поля (фактически вызывая методы)
    # методы получения и изменения значения level маскируются под свойства класса через декораторы

    @classmethod

player_1 = Player()
print(player_1.level)
player_1.level = 10
print(player_1.level)
player_1.level = 2
print(player_1.level)