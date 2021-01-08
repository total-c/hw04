# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример:12345 -> 23451

list_1 = [1, 2, 3, 4, 5]

i = 1
len_list_1 = len(list_1)
list_2 = []
while i < len_list_1:
    list_2.append(list_1[i])
    i = i + 1
list_2.append(list_1[0])
print(list_2)
