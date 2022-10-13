# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму 
# элементов списка, стоящих на нечетной позиции
# Пример:
#  [2, 3, 5, 9, 3] -> 12

# from random import randint


# nums = []
# for i in range(randint(4, 8)):
#     nums.append(randint(5, 11))

# result = 0
# for i in range(len(nums)):
#     if i % 2 != 0:
#         result += nums[i]
# print(nums, result, sep=' -> ')

from random import randint


nums = [randint(1, 11) for i in range(randint(4, 9))]
print(nums)
result = sum([nums[i] for i in range(1, len(nums), 2)])
print(result)