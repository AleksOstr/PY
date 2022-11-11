from aiogram import types, Dispatcher
import functions as f
import answers as a

field = []

async def command_start(message: types.Message):
    global field
    field = f.new_game()
    await message.answer(a.welcome)
    await message.answer(f.print_field(field))

async def making_moves(message: types.Message):
    global field
    if field != []:
        if not f.check_input_digit(message.text):
            await message.answer(a.error)
            await message.answer(f.print_field(field))
        if not f.check_input_range(message.text):
            await message.answer(a.wrong_cell)
        else:
            if not f.check_cell(field, message.text):
                await message.answer(a.used_cell)
            else:
                field = f.player_move(field, message.text)
                if f.check_win(field, 'X'):
                    await message.answer(f.print_field(field))
                    await message.answer(a.win_answer)
                    field = f.end_of_game()
                elif f.check_draw(field):
                    await message.answer(f.print_field(field))
                    await message.answer(a.draw_answer)
                    field = f.end_of_game()
                else:
                    field = f.bot_move(field)
                    if f.check_win(field, 'O'):
                        await message.answer(f.print_field(field))
                        await message.answer(a.lose_answer)
                        field = f.end_of_game()
                    elif f.check_draw(field):
                        await message.answer(f.print_field(field))
                        await message.answer(a.draw_answer)
                        field = f.end_of_game()
    else:
        await message.answer(a.ask_for_new_game)
    if field != []:
        await message.answer(f.print_field(field))

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(making_moves)
