# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input('Введите число\n'))
result = ' '
while number > 0:
    if number % 2 == 0:
        result = '0' + result
    else:
        result = '1' + result
    number //= 2
print(result)
