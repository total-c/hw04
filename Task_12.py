# Дан словарь:
# {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа
# (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()
# (подсказка: создается новый ключ с цифрой в конце, старый удаляется)

dict_1 = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub'
}

keys_list = list(dict_1.keys())
i = 0
len_keys_list = len(keys_list)

while i < len_keys_list:
    new_key = f'{keys_list[i]}{len(keys_list[i])}'
    dict_1[new_key] = dict_1.pop(keys_list[i])
    i += 1

print(dict_1)

for key in keys_list:
    new_key_for = f'{key}{len(key)}'
    dict_1[new_key_for] = dict_1.pop(key)

print(dict_1)
