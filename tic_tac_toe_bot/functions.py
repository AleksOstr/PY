from random import randint
from symbols import *

def new_game():
    return [[sq, sq, sq], [sq, sq, sq], [sq, sq, sq]]

def end_of_game():
    return []

def print_field(field):
    return f' {field[0][0]}{i}{field[0][1]}{i}{field[0][2]}\n\
{m}{m}{m}{m}{m}\n\
{field[1][0]}{i}{field[1][1]}{i}{field[1][2]}\n\
{m}{m}{m}{m}{m}\n\
{field[2][0]}{i}{field[2][1]}{i}{field[2][2]}\n'

def check_input_digit(string: str):
    if string.isdigit():
        return True
    else:
        return False

def check_input_range(string:str):
    if int(string) in range(1, 10):
        return True
    else:
        return False

def check_cell(field, string:str):
    if string == '1' and field[0][0] != sq:
        return False
    elif string == '2' and field[0][1] != sq:
        return False
    elif string == '3' and field[0][2] != sq:
        return False
    elif string == '4' and field[1][0] != sq:
        return False
    elif string == '5' and field[1][1] != sq:
        return False
    elif string == '6' and field[1][2] != sq:
        return False
    elif string == '7' and field[2][0] != sq:
        return False
    elif string == '8' and field[2][1] != sq:
        return False
    elif string == '9' and field[2][2] != sq:
        return False
    else:
        return True        

def player_move(field, string: str):
    if string == '1' and field[0][0] == sq:
        field[0][0] = x
        return field
    elif string == '2' and field[0][1] == sq:
        field[0][1] = x
        return field
    elif string == '3' and field[0][2] == sq:
        field[0][2] = x
        return field
    elif string == '4' and field[1][0] == sq:
        field[1][0] = x
        return field
    elif string == '5' and field[1][1] == sq:
        field[1][1] = x
        return field
    elif string == '6' and field[1][2] == sq:
        field[1][2] = x
        return field
    elif string == '7' and field[2][0] == sq:
        field[2][0] = x
        return field
    elif string == '8' and field[2][1] == sq:
        field[2][1] = x
        return field
    elif string == '9' and field[2][2] == sq:
        field[2][2] = x
        return field
    
    
def check_win(field, symbol:str):
    win = False
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == symbol:
            win = True
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == symbol:
            win = True
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        win = True
    elif field[0][2] == field[1][1] == field[2][0] == symbol:
        win = True
    return win

def check_draw(field):
    draw = False
    if field[0].count(sq) == 0 and field[1].count(sq) == 0 and field[2].count(sq) == 0:
        draw = True
    return draw

def bot_check_line(f1, f2, f3, symbol: str):
    chance = False
    if f1 == sq and f2 == symbol and f3 == symbol:
        chance = True
    elif f1 == symbol and f2 == sq and f3 == symbol:
        chance = True
    elif f1 == symbol and f2 == symbol and f3 == sq:
        chance = True
    return chance

def bot_random_move(field):
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if field[row][col] == sq:
            field[row][col] = o
            break
    return field

def bot_move(field):
    for i in range(3):
        if bot_check_line(field[i][0], field[i][1], field[i][2], o):
            if field[i][0] == sq:
                field[i][0] = o
            elif field[i][1] == sq:
                field[i][1] = o
            elif field[i][2] == sq:
                field[i][2] = o
            return field
    for i in range(3):
        if bot_check_line(field[0][i], field[1][i], field[2][i], o):
            if field[0][i] == sq:
                field[0][i] = o
            elif field[1][i] == sq:
                field[1][i] = o
            elif field[2][i] == sq:
                field[2][i] = o
            return field
    if bot_check_line(field[0][0], field[1][1], field[2][2], o):
        if field[0][0] == sq:
            field[0][0] = o
        elif field[1][1] == sq:
            field[1][1] = o
        elif field[2][2] == sq:
            field[2][2] = o
        return field
    elif bot_check_line(field[0][2], field[1][1], field[2][0], o):
        if field[0][2] == sq:
            field[0][2] = o
        elif field[1][1] == sq:
            field[1][1] = o
        elif field[2][0] == sq:
            field[2][0] = o
        return field
    for i in range(3):
        if bot_check_line(field[i][0], field[i][1], field[i][2], x):
            if field[i][0] == sq:
                field[i][0] = o
            elif field[i][1] == sq:
                field[i][1] = o
            elif field[i][2] == sq:
                field[i][2] = o
            return field
    for i in range(3):
        if bot_check_line(field[0][i], field[1][i], field[2][i], x):
            if field[0][i] == sq:
                field[0][i] = o
            elif field[1][i] == sq:
                field[1][i] = o
            elif field[2][i] == sq:
                field[2][i] = o
            return field
    if bot_check_line(field[0][0], field[1][1], field[2][2], x):
        if field[0][0] == sq:
            field[0][0] = o
        elif field[1][1] == sq:
            field[1][1] = o
        elif field[2][2] == sq:
            field[2][2] = o
        return field
    elif bot_check_line(field[0][2], field[1][1], field[2][0], x):
        if field[0][2] == sq:
            field[0][2] = o
        elif field[1][1] == sq:
            field[1][1] = o
        elif field[2][0] == sq:
            field[2][0] = o
        return field
    else:
        bot_random_move(field)
        return field