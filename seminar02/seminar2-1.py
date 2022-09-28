# # 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81


n = int(input('Введите N= '))
result = 1
for i in range(1, n+1):
    if i == 1:
        print(result, end = ' ')
    else:
        result *= -3
        print(result, end=' ')
