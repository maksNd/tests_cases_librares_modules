import inflect
"""Переводит числа в слова"""

p = inflect.engine()
print(p.number_to_words(1))


new_dict = {}
for i in range(0, 11):
    new_dict[i] = p.number_to_words(i)

print(new_dict)