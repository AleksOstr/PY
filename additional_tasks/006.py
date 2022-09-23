# Напишите программу, которая перевернёт одномерный список (последний элемент будет на первом месте, а первый - на последнем и т.д.)

from random import randint


def get_random_list():
    list = []
    for i in range(randint(2, 20)):
        list.append(randint(1, 20))
    return list


numbers = get_random_list()
print(numbers)

for i in range(len(numbers) // 2):
    numbers[i], numbers[len(numbers) - 1 - i] = numbers[len(numbers) - 1 - i], numbers[i]
print(numbers)
