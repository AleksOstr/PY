# Найдите произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результаты запишите в новый список

from random import randint


def get_random_list():
    list = []
    for i in range(randint(2,20)):
        list.append(randint(1, 20))
    return list

result = []
numbers = get_random_list()
print(numbers)

for i in range(len(numbers) // 2):
    result.append(numbers[i] * numbers[len(numbers) - 1 - i])
print(result)