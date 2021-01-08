# Дан список целых чисел. Подсчитать сколько четных чисел в списке

a = [2, 7, 6, 4, 5]
count_chetn = 0
i = 0
dlina = len(a)
while i < dlina:
    n = a[i] % 2
    i += 1
    if n == 0:
        count_chetn += 1

print(count_chetn)
