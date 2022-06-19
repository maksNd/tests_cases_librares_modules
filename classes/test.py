class NewClass:
    def __init__(self):
        self.name = 'qwe'
        self.number = 10

    def __repr__(self):
        return f"{self.name}.{self.number}.NewClass"

unit_1 = NewClass()
print(unit_1.name)
unit_1.second_name = 'new_quality' # добавили новое свойство класса
print(unit_1.second_name)