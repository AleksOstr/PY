import user_interface as ui
import player_vs_player as pvp
import player_vs_bot as pvb
import player_vs_smart_bot as pvsb
import functions as func

def run_game():
    ui.show_rules()
    game_mode = ui.choose_game_mode()
    if game_mode == '1':
        pvp.player_vs_player_mode()
    elif game_mode == '2':
        pvb.player_vs_bot_mode()
    elif game_mode == '3':
        pvsb.player_vs_smart_bot_mode()
    elif game_mode == 'exit':
        func.exit_game()
        