# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def func(num):
    if num == 0:
        return 0
    return (1+1/num)**num + func(num-1)


n = int(input('Введите N= '))
result = {}
for i in range(1, n+1):
    result[i] = round(func(i), 0)
print(result)
