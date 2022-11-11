from aiogram import types, Dispatcher
from functions import *

async def command_start(message: types.Message):
    new_game()
    await message.answer(f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n')

async def making_moves(message: types.Message):
    if field != []:
        player_move(message.text)
        if check_win('X'):
            end_of_game()
            await message.answer(f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n')
            await message.answer('Вы выиграли! Если хотите сыграть еще отправьте мне /start')
        elif check_draw():
            end_of_game()
            await message.answer(f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n')
            await message.answer('Ничья! Если хотите сыграть еще отправьте мне /start')
        else:
            bot_move()
            if check_win('O'):
                end_of_game()
                await message.answer(f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n')
                await message.answer('Вы проиграли! Если хотите сыграть еще отправьте мне /start')
            elif check_draw():
                end_of_game()
                await message.answer(f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n')
                await message.answer('Ничья! Если хотите сыграть еще отправьте мне /start')
            else:
                await message.answer(f' {field[0][0]} | {field[0][1]} | {field[0][2]} \n\
{field[1][0]} | {field[1][1]} | {field[1][2]} \n\
{field[2][0]} | {field[2][1]} | {field[2][2]} \n')
    else:
        await message.answer('Начните новую игру /start')

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(making_moves)
