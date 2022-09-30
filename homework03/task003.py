# Задайте список из веществвенных чисел. Напишите программу, которая найдет
# разницу между максимальным и минимальным значением дробной части элементов
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] -> 0.19

from random import randint


nums = []
for i in range(randint(5, 10)):
    nums.append(round(randint(1,15) * 1.131, 2))
print(nums, end=' -> ')

nums = list(map(lambda x: round(x - int(x), 2), nums))
print(max(nums) - min(nums))