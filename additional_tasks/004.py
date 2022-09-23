# Задайте список из 123 случайных чисел. Найдите количество элементов списка, лежащих в отрезке [10, 99]

from random import randint


def fil_list(list, list_length):
    for i in range(list_length):
        list.append(randint(-100, 150))
    return list


numbers = []
numbers_length = 123
fil_list(numbers, numbers_length)
print(numbers)

count = 0
for i in range(numbers_length):
    if 10 <= numbers[i] <= 99:
        count += 1
print(f'В списке {count} элемента/ов, лежащих в отрезке [10, 99]')
