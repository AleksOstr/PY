# Играем с конфетами

from random import randint


def check_input(data: str):
    while not data.isdigit():
        data = input('Введено неверное значение. Повторите ввод')
    return data


game_is_on = True
while game_is_on:
    print('Добро пожаловать в игру!\n Правила игры следующие: На столе лежит 2021 конфета.Первый ход определяется жеребьёвкой.\n\
        За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход игроку.')
    game_mode = input('Выберите режим игры: 1 - игрок против игрока, 2 - игрок против бота, 3 - игрок против "умного" бота\n\
        exit - выход из игры\n')
        
    if game_mode == '1':
        total = 500
        coin = randint(1, 2)
        if coin == 1:
            print('Первым ходит игрок 1')
            player1, player2 = True, False
        else:
            print('Первым ходит игрок 2')
            player1, player2 = False, True
        while total > 0:
            if player1:
                move = int(check_input(input('Ход игрока 1\n Сколько конфет вы возьмете?\n')))
                if total > 28:
                    while not 0 < move <= 28:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                elif total <= 28:
                    while not 0 < move <= total:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                total -= move
                player1, player2 = player2, player1
                print(f'Игрок 1 взял {move} конфет. Осталось {total} конфет')
            else:
                move = int(check_input(input('Ход игрока 2\n Сколько конфет вы возьмете?\n')))
                if total > 28:
                    while not 0 < move <= 28:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                elif total <= 28:
                    while not 0 < move <= total:
                        move = int(check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
                total -= move
                player1, player2 = player2, player1
                print(f'Игрок 2 взял {move} конфет. Осталось {total} конфет')
        if player1:
            print('Последний ход сделал Игрок 2, все конфеты достаются ему\n Конец игры')
        else:
            print('Последний ход сделал Игрок 1, все конфеты достаются ему\n Конец игры')


    # elif game_mode == '2':


    # elif game_mode == '3':

    elif game_mode == 'exit':
        print('До свидания!')
        game_is_on = False
