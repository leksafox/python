'''Задача 22: Даны два неупорядоченных набора целых чисел (может 
быть, с повторениями). Выдать без повторений в порядке возрастания 
все те числа, которые встречаются в обоих наборах. Пользователь 
вводит 2 числа.
n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''

arr_n = [0]*int(input("Введите длину первого набора "))
arr_m = [0]*int(input("Введите длину второго набора "))

for i in range(len(arr_n)):
    arr_n[i] = int(input(f'Введите элемент первого множества с индексом {i}: '))
print(arr_n)

for i in range(len(arr_m)):
    arr_m[i] = int(input(f'Введите элемент второго множества с индексом {i}: '))
print(arr_m)

res = {}
for val in arr_n:
    res[val] = 0

for val in arr_m:
    res[val] = 0

print(sorted(res.keys()))

'''import random
n = int(input("Введите длину первого набора: "))
m = int(input("Введите длину второго набора: "))
arr_n = []
for i in range(n):
    arr_n.append(random.randint(0, 100))
print(arr_n)
arr_m = []
for i in range(m):
    arr_m.append(random.randint(0, 100))
print(arr_m)'''