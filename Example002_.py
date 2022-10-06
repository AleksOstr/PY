# В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадрат числа)

f = open('nums.txt', 'r')
nums = f.readlines()
f.close()

numbers = nums[0].split(' ')
numbers = list(map(int, numbers))
result = [(i, i**2) for i in numbers if i % 2 == 0]
print(result)