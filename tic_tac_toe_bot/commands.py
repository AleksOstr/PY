from aiogram import types, Dispatcher
from functions import *

field = []

async def command_start(message: types.Message):
    global field
    field = new_game()
    await message.answer(print_field(field))

async def making_moves(message: types.Message):
    global field
    if field != []:
        field = player_move(field, message.text)
        if check_win(field, 'X'):
            await message.answer(print_field(field))
            await message.answer('Вы выиграли! Если хотите сыграть еще отправьте мне /start')
            field = end_of_game()
        elif check_draw(field):
            await message.answer(print_field(field))
            await message.answer('Ничья! Если хотите сыграть еще отправьте мне /start')
            field = end_of_game()
        else:
            field = bot_move(field)
            if check_win(field, 'O'):
                await message.answer(print_field(field))
                await message.answer('Вы проиграли! Если хотите сыграть еще отправьте мне /start')
                field = end_of_game()
            elif check_draw(field):
                await message.answer(print_field(field))
                await message.answer('Ничья! Если хотите сыграть еще отправьте мне /start')
                field = end_of_game()
    else:
        await message.answer('Начните новую игру /start')
    if field != []:
        await message.answer(print_field(field))

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(making_moves)
