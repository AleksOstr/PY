# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


n = int(input('Введите N= '))
list = []
for i in range(n):
    list.append(randint(-n, n))
print(list)

f = open('file.txt', 'r')
content = f.readlines()
print(content)
f.close()

for i in content:
    mult = 1
    for j in range(len(i)):
        if i[j] != '\n' and int(i[j]) <= len(list)-1:
            mult *= list[int(i[j])]
    print(mult)
