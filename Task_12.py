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

keys_dict_1 = list(dict_1.keys())
i = 0
len_keys_dict_1 = len(keys_dict_1)

while i < len_keys_dict_1:
    new_key = f'{keys_dict_1[i]}{len(keys_dict_1[i])}'
    dict_1[new_key] = dict_1.pop(keys_dict_1[i])
    i += 1

print(dict_1)
