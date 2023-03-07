'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random
data = [0]*int(input("Введите длину массива: "))
mi = int(input("Введите минимум: "))
ma = int(input("Введите максимум: "))

for i in range(len(data)):
    data[i] = random.randint(-1000, 1000)
print(data)

res = []
for i in range(len(data)):
    if data[i] >= mi and data[i] <= ma:
        res.append(i)

print(res)