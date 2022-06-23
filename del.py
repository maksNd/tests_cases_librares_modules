import inflect

p = inflect.engine()


new_dict = {}
for i in range(0, 15):
    new_dict[i] = p.number_to_words(i)

print(new_dict)
# del new_dict[6]
for key, value in new_dict.items():

    if len(value) == 3: print(key, value)



# keys_list = new_dict.keys()
# values_list = new_dict.values()
# print(keys_list)
# print(values_list)