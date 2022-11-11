from random import randint

def new_game():
    return [['', '', ''], ['', '', ''], ['', '', '']]

def end_of_game():
    return []

def print_field(field):
    return f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n'

def check_cell(field, string):
    if string == '1' and field[0][0] != '':
        return False
    elif string == '2' and field[0][1] != '':
        return False
    elif string == '3' and field[0][2] != '':
        return False
    elif string == '4' and field[1][0] != '':
        return False
    elif string == '5' and field[1][1] != '':
        return False
    elif string == '6' and field[1][2] != '':
        return False
    elif string == '7' and field[2][0] != '':
        return False
    elif string == '8' and field[2][1] != '':
        return False
    elif string == '9' and field[2][2] != '':
        return False
    else:
        return True        

def player_move(field, string: str):
    if string == '1' and field[0][0] == '':
        field[0][0] = 'X'
        return field
    elif string == '2' and field[0][1] == '':
        field[0][1] = 'X'
        return field
    elif string == '3' and field[0][2] == '':
        field[0][2] = 'X'
        return field
    elif string == '4' and field[1][0] == '':
        field[1][0] = 'X'
        return field
    elif string == '5' and field[1][1] == '':
        field[1][1] = 'X'
        return field
    elif string == '6' and field[1][2] == '':
        field[1][2] = 'X'
        return field
    elif string == '7' and field[2][0] == '':
        field[2][0] = 'X'
        return field
    elif string == '8' and field[2][1] == '':
        field[2][1] = 'X'
        return field
    elif string == '9' and field[2][2] == '':
        field[2][2] = 'X'
        return field
    
    
def check_win(field, symbol):
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
    if field[0].count('') == 0 and field[1].count('') == 0 and field[2].count('') == 0:
        draw = True
    return draw

def bot_check_line(f1, f2, f3, symbol):
    chance = False
    if f1 == '' and f2 == symbol and f3 == symbol:
        chance = True
    elif f1 == symbol and f2 == '' and f3 == symbol:
        chance = True
    elif f1 == symbol and f2 == symbol and f3 == '':
        chance = True
    return chance

def bot_random_move(field):
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if field[row][col] == '':
            field[row][col] = 'O'
            break
    return field

def bot_move(field):
    for i in range(3):
        if bot_check_line(field[i][0], field[i][1], field[i][2], 'O'):
            if field[i][0] == '':
                field[i][0] = 'O'
            elif field[i][1] == '':
                field[i][1] = 'O'
            elif field[i][2] == '':
                field[i][2] = 'O'
            return field
    for i in range(3):
        if bot_check_line(field[0][i], field[1][i], field[2][i], 'O'):
            if field[0][i] == '':
                field[0][i] = 'O'
            elif field[1][i] == '':
                field[1][i] = 'O'
            elif field[2][i] == '':
                field[2][i] = 'O'
            return field
    if bot_check_line(field[0][0], field[1][1], field[2][2], 'O'):
        if field[0][0] == '':
            field[0][0] = 'O'
        elif field[1][1] == '':
            field[1][1] = 'O'
        elif field[2][2] == '':
            field[2][2] = 'O'
        return field
    elif bot_check_line(field[0][2], field[1][1], field[2][0], 'O'):
        if field[0][2] == '':
            field[0][2] = 'O'
        elif field[1][1] == '':
            field[1][1] = 'O'
        elif field[2][0] == '':
            field[2][0] = 'O'
        return field
    for i in range(3):
        if bot_check_line(field[i][0], field[i][1], field[i][2], 'X'):
            if field[i][0] == '':
                field[i][0] = 'O'
            elif field[i][1] == '':
                field[i][1] = 'O'
            elif field[i][2] == '':
                field[i][2] = 'O'
            return field
    for i in range(3):
        if bot_check_line(field[0][i], field[1][i], field[2][i], 'X'):
            if field[0][i] == '':
                field[0][i] = 'O'
            elif field[1][i] == '':
                field[1][i] = 'O'
            elif field[2][i] == '':
                field[2][i] = 'O'
            return field
    if bot_check_line(field[0][0], field[1][1], field[2][2], 'X'):
        if field[0][0] == '':
            field[0][0] = 'O'
        elif field[1][1] == '':
            field[1][1] = 'O'
        elif field[2][2] == '':
            field[2][2] = 'O'
        return field
    elif bot_check_line(field[0][2], field[1][1], field[2][0], 'X'):
        if field[0][2] == '':
            field[0][2] = 'O'
        elif field[1][1] == '':
            field[1][1] = 'O'
        elif field[2][0] == '':
            field[2][0] = 'O'
        return field
    else:
        bot_random_move(field)
        return field