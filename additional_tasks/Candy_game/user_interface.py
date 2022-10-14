from random import randint
import functions as func
import engine as en


def show_rules():
    print('Добро пожаловать в игру!\nПравила игры следующие: На столе лежит 2021 конфета.Первый ход определяется жеребьёвкой.\n\
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход игроку.\n')

def choose_game_mode():
    game_mode = input('Выберите режим игры:\n1 - игрок против игрока\n2 - игрок против компьютера\n3 - игрок против "умного" компьютера\n\
Если вы передумали и хотите выйти - exit\n')
    return game_mode if game_mode == '1' or game_mode == '2' or game_mode == '3' or game_mode.lower() == 'exit' else choose_game_mode()

def another_round():
    if input('Хотите сыграть еще? да / нет\n') == 'да':
        return en.run_game()
    else:
        return func.exit_game()

def get_name1():
    return input('Игрок 1, как вас зовут?\n')

def get_name2():
    return input('Игрок 2, как вас зовут?\n')

def who_the_first_pvp(name1, name2):
    coin = randint(0, 1)
    if coin:
        print(f'{name1} ходит первым!\n')
        return True
    else:
        print(f'{name2} ходит первым!\n')
        return False

def who_the_first_pvb():
    coin = randint(0, 1)
    if coin:
        print(f'Вы ходите первым!\n')
        return True
    else:
        print(f'Компьютер ходит первым!\n')
        return False

def player_move_pvp(name, total, max_move):
    move = int(func.check_input(input(f'Ход {name}\nСколько конфет вы возьмете?\n')))
    if total > max_move:
        while not 0 <= move <= max_move:
            move = int(func.check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
    elif total <= max_move:
        while not 0 <= move <= total:
            move = int(func.check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
    return move

def player_move_pvb(total, max_move):
    move = int(func.check_input(input(f'Ваш ход\nСколько конфет вы возьмете?\n')))
    if total > max_move:
        while not 0 <= move <= max_move:
            move = int(func.check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
    elif total <= max_move:
        while not 0 <= move <= total:
            move = int(func.check_input(input('Вы не можете взять столько конфет. Повторите попытку\n')))
    return move

def how_much_is_left_pvp(name, move, total):
    print(f'{name} взял {move} конфет. Осталось {total} конфет\n')

def how_much_is_left_pvb(move, total, flag):
    if flag:
        print(f'Компьютер берет {move} конфет. Осталось {total} конфет\n')
    else:
        print(f'Вы берете {move} конфет. Осталось {total} конфет\n')

def show_the_winner_pvp(name1, name2, flag):
    if flag:
        print(f'Последний ход сделал {name2}, все конфеты достаются ему\nКонец игры\n')
    else:
        print(f'Последний ход сделал {name1}, все конфеты достаются ему\nКонец игры\n')
    
def show_the_winner_pvb(flag):
    if flag:
        print('Последний ход сделал компьютер и забрал себе все конфеты\n Конец игры\n')
    else:
        print('Поздравляем! Вы сделали последний ход и все конфеты достаются вам!\nКонец игры\n')
        