# Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

n = int(input('Введите N\n'))
result = []
for i in range(1, n):
    if i % 2 ==0:
        result.append(i)
print(result)