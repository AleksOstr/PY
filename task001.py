# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным

print('Введите номер дня недели')
day_number = int(input())
while day_number < 1 or day_number > 7:
    print('Введен неверный номер дня недели, повторите ввод')
    day_number = int(input())
else:
    if day_number == 6 or day_number == 7:
        print('Это выходной день')
    else:
        print('Это будний день')