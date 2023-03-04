'''Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
'''

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

def summa(a, b):
    if b == 0:
        return a
    return 1 + summa(a, b - 1)
print(summa(a, b))