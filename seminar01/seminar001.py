# #1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))

if number1 == number2**2:
    print('Первое число является квадратом второго')
elif number2 == number1**2:
    print('Второе число является квадратом первого')
else:
    print('Ни одно число не является квадратом другого')
