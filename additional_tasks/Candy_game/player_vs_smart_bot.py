from random import randint
import user_interface as ui

def player_vs_smart_bot_mode():
    total = 2021
    max_move = 28
    flag = ui.who_the_first_pvb()
    while total > 0:
        if flag:
            move = ui.player_move_pvb(total, max_move)
            total -= move
            flag = False
            ui.how_much_is_left_pvb(move, total, flag)
        else:
            if total > max_move:
                move = total % 29
                total -= move
                flag = True
                ui.how_much_is_left_pvb(move, total, flag)
            elif total <= max_move:
                move = total
                total -= move
                flag = True
                ui.how_much_is_left_pvb(move, total, flag)
    ui.show_the_winner_pvb(flag)
    ui.another_round()
    