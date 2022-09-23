# #2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

numeration = [1,2,3,4,5]
list = []
for i in range(5):
    list.append(int(input(f'Введите {numeration[i]} число ')))
print(list)

maximum_element = list[0]
for i in range(len(list)):
    if list[i] > maximum_element:
        maximum_element = list[i]
print(maximum_element)
