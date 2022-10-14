import user_interface as ui

def player_vs_player_mode():
    total = 2021
    max_move = 28
    name1 = ui.get_name1()
    name2 = ui.get_name2()
    flag = ui.who_the_first_pvp(name1, name2)
    while total > 0:
        if flag:
            move = ui.player_move_pvp(name1, total, max_move)
            total -= move
            flag = False
            ui.how_much_is_left_pvp(name1, move, total)
        else:
            move = ui.player_move_pvp(name2, total, max_move)
            total -= move
            flag = True
            ui.how_much_is_left_pvp(name2, move, total)
    ui.show_the_winner_pvp(name1, name2, flag)
    ui.another_round()
    