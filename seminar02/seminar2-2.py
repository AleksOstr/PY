# # 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# *Пример:*
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Ввудите N= '))
list_ind  = []
list_elem = []
print(f'{n}: [', end='')
for i in range(1, n+1):
    list_ind.append(i)
    list_elem.append(3*i+1)
for i in range(len(list_elem)):
    print(f'{list_ind[i]}: {list_elem[i]} ', end='')
print(']')
    