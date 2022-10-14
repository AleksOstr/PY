import sys


def check_input(data: str):
    while not data.isdigit():
        data = input('Введено неверное значение. Повторите ввод\n')
    return data
   
def exit_game():
    sys.exit()
