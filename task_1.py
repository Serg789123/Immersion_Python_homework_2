# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import math
import fractions

n1 = input('Введите первое дробное число в виде a/b: ')
n2 = input('Введите второе дробное число в виде a/b: ')

a = n1.split('/')
b = n2.split('/')
c = int(a[0]) / int(a[1])
d = int(b[0]) / int(b[1])

f1 = fractions.Fraction(int(a[0]), int(a[1]))
f2 = fractions.Fraction(int(b[0]), int(b[1]))

print(f'Сумма дробей = {c + d}')
print(f'Произведение дробей = {c * d}')
print(f1 + f2)
print(f1 * f2)