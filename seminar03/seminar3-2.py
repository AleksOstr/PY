# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), 
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# # Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих
# nn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от
# 55 до 100100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1:
# 6222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8


n = int(input('Укажите число холодильников '))
for i in range(1, n+1):
    fridge_num = input(f'Введите идентификатор {i} холодильника ')
    if fridge_num.find('a') != -1 \
        and fridge_num.find('a') < fridge_num.find('n', fridge_num.find('a')) \
            < fridge_num.find('t', fridge_num.find('n',fridge_num.find('a'))) \
                < fridge_num.find('o', fridge_num.find('t',fridge_num.find('n', fridge_num.find('a')))) \
                    < fridge_num.find('n', fridge_num.find('o', fridge_num.find('t', fridge_num.find('n', fridge_num.find('a'))))):
        print(f'{i} - тут прячется anton', end = '\n')
