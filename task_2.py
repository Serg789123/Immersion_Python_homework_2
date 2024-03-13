# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))

HEX = 16
hexadecimal_digit = ''

print(hex(num))

hexadecimal_digits = '0123456789abcdef'
while num > 0:
    ordinal = num % HEX
    digit = hexadecimal_digits[ordinal]
    hexadecimal_digit = digit + hexadecimal_digit
    num //= HEX

print(hexadecimal_digit)