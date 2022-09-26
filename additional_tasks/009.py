# Задать список случайного размера заполненный случайными неповторяющимися целыми числами

from random import randint


def rand_list():
    list = []
    for i in range(1, randint(20, 50)):
        list.append(i)
    for i in range(len(list)-1, 0, -1):
        j = randint(0, i-1)
        list[i], list[j] = list[j], list[i]
    return list


numbers = rand_list()
print(numbers)