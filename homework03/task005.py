# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(num):
    if num in (1, 2):
        return 1
    return fib(num-1) + fib(num-2)


n = int(input('Введите число '))
result = [0]

for i in range(1, n+1):
    result.append(-fib(i))
    result.append(fib(i))
result.sort()
print(result)