# Напишите программу, которая будет преобразовывать десятичное число в двоичное

num = int(input('Введите число '))
result = ''
while num > 0:
    if num % 2 == 0:
        result = '0' + result
    else:
        result = '1' + result
    num //= 2
print(result)