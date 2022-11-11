from random import randint

field = [['', '', ''], ['', '', ''], ['', '', '']]

def new_game():
    global field
    field = [['', '', ''], ['', '', ''], ['', '', '']]
    return field

def end_of_game():
    global field
    field = []

def player_move(string: str):
    global field
    if string == '1' and field[0][0] == '':
        field[0][0] = 'X'
    elif string == '2' and field[0][1] == '':
        field[0][1] = 'X'
    elif string == '3' and field[0][2] == '':
        field[0][2] = 'X'
    elif string == '4' and field[1][0] == '':
        field[1][0] = 'X'
    elif string == '5' and field[1][1] == '':
        field[1][1] = 'X'
    elif string == '6' and field[1][2] == '':
        field[1][2] = 'X'
    elif string == '7' and field[2][0] == '':
        field[2][0] = 'X'
    elif string == '8' and field[2][1] == '':
        field[2][1] = 'X'
    elif string == '9' and field[2][2] == '':
        field[2][2] = 'X'
    return field
    
def check_win(symbol):
    global field
    win = False
    if field[0][0] == field[0][1] == field[0][2] == symbol:
        win = True
    elif field[1][0] == field[1][1] == field[1][2] == symbol:
        win = True
    elif field[2][0] == field[2][1] == field[2][2] == symbol:
        win = True
    elif field[0][0] == field[1][0] == field[2][0] == symbol:
        win = True
    elif field[0][1] == field[1][1] == field[2][1] == symbol:
        win = True
    elif field[0][2] == field[1][2] == field[2][2] == symbol:
        win = True
    elif field[0][0] == field[1][1] == field[2][2] == symbol:
        win = True
    elif field[0][2] == field[1][1] == field[2][0] == symbol:
        win = True
    return win

def check_draw():
    global field
    draw = False
    if field[0].count('') == 0 and field[1].count('') == 0 and field.count('') == 0:
        draw = True
    return draw

def bot_check_line(f1, f2, f3, symbol):
    bot_done = False
    if f1 == '' and f2 == symbol and f3 == symbol:
        f1 = 'O'
        bot_done = True
    elif f1 == symbol and f2 == '' and f3 == symbol:
        f2 = 'O'
        bot_done = True
    elif f1 == symbol and f2 == symbol and f3 == '':
        f3 == 'O'
        bot_done = True
    return bot_done

def bot_random_move():
    global field
    row = randint(0, 2)
    col = randint(0, 2)
    if field[row][col] == '':
        field[row][col] == 'O'
    return field

def bot_move():
    global field
    if bot_check_line(field[0][0], field[0][1], field[0][2], 'O'):
        return field
    elif bot_check_line(field[1][0], field[1][1], field[1][2], 'O'):
        return field
    elif bot_check_line(field[2][0], field[2][1], field[2][2], 'O'):
        return field
    elif bot_check_line(field[0][0], field[1][0], field[2][0], 'O'):
        return field
    elif bot_check_line(field[0][1], field[1][1], field[2][1], 'O'):
        return field
    elif bot_check_line(field[0][2], field[1][2], field[2][2], 'O'):
        return field
    elif bot_check_line(field[0][0], field[1][1], field[2][2], 'O'):
        return field
    elif bot_check_line(field[0][2], field[1][1], field[2][0], 'O'):
        return field
    elif bot_check_line(field[0][0], field[0][1], field[0][2], 'X'):
        return field
    elif bot_check_line(field[1][0], field[1][1], field[1][2], 'X'):
        return field
    elif bot_check_line(field[2][0], field[2][1], field[2][2], 'X'):
        return field
    elif bot_check_line(field[0][0], field[1][0], field[2][0], 'X'):
        return field
    elif bot_check_line(field[0][1], field[1][1], field[2][1], 'X'):
        return field
    elif bot_check_line(field[0][2], field[1][2], field[2][2], 'X'):
        return field
    elif bot_check_line(field[0][0], field[1][1], field[2][2], 'X'):
        return
    elif bot_check_line(field[0][2], field[1][1], field[2][0], 'X'):
        return field
    else:
        bot_random_move()
    return field