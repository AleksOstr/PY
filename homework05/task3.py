#  Крестики-нолики

from random import randint


def check_input(data: str):
    while not data.isdigit():
        data = input('Введено неверное значение. Повторите ввод\n')
    return data


def another_round():
    if input('Хотите сыграть еще? да / нет\n') == 'да':
        return True
    else:
        return False


def show_field(arr):
    print(f' {arr[0]} | {arr[1]} | {arr[2]}')
    print('--  --  --')
    print(f' {arr[3]} | {arr[4]} | {arr[5]}')
    print('--  --  --')
    print(f' {arr[6]} | {arr[7]} | {arr[8]}')


game_is_on = True
while game_is_on:
    cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    free_cells = 9
    print('Добро пожаловать в игру "Крестики-нолики"! Вы играете крестиками "X", ваш компьютерный противник - "0"')
    coin = randint(1,2)
    if coin == 1:
        player1 = True
    else:
        player1 = False
        
    while not (cells[0] == 'x' and cells[1] == 'x' and cells[2] == 'x')\
        or not (cells[3] == 'x' and cells[4] == 'x' and cells[5] == 'x')\
        or not (cells[6] == 'x' and cells[7] == 'x' and cells[8] == 'x')\
        or not (cells[0] == 'x' and cells[3] == 'x' and cells[6] == 'x')\
        or not (cells[1] == 'x' and cells[4] == 'x' and cells[7] == 'x')\
        or not (cells[2] == 'x' and cells[5] == 'x' and cells[8] == 'x')\
        or not (cells[0] == '0' and cells[1] == '0' and cells[2] == '0')\
        or not (cells[3] == '0' and cells[4] == '0' and cells[5] == '0')\
        or not (cells[6] == '0' and cells[7] == '0' and cells[8] == '0')\
        or not (cells[0] == '0' and cells[3] == '0' and cells[6] == '0')\
        or not (cells[1] == '0' and cells[4] == '0' and cells[7] == '0')\
        or not (cells[2] == '0' and cells[5] == '0' and cells[8] == '0')\
        or not free_cells == 0:

        if player1:

