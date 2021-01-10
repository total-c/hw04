# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу
# умноженному на -2

list_num = [24, 13, 46, 23]
list_num_1 = []
i = 0
leight = len(list_num)
while i < leight:
    list_num_1.append(list_num[i] * -2)
    i = i + 1

print(list_num_1)

list_num_for = [24, 13, 46, 23]
list_num_1_for = []

for item in list_num_for:
    list_num_1_for.append(item * -2)

print(list_num_1_for)
