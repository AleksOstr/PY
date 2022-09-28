# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


num_input = int(input('Введите N = '))
for i in range(1, num_input + 1):
    print(factorial(i), end=' ')
