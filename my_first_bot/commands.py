from aiogram import types, Dispatcher
from calc import allowed_names, evaluate
from datetime import datetime
from jokes import random_joke

def logger(message : types.Message):
    with open('log.txt', 'a') as f:
        f.write(f'{datetime.now()} {message.from_user.id} {message.from_user.username} {message.from_user.first_name}\
 {message.from_user.last_name} {message.text}\n')

async def command_start(message : types.Message):
    logger(message)
    await message.answer(f'Привет, {message.from_user.first_name}!\n\
Я - бот-калькулятор. Более подробную информацию можешь узнать по команде /help')

async def command_help(message : types.Message):
    logger(message)
    await message.answer(f"Собери математическое выражение из чисел и операторов.\
 Можно использовать любые из следующих функций и констант: {', '.join(allowed_names.keys())}\n\
Операторы:\n\
    + - сложение\n\
    - - вычитание\n\
    * - умножение\n\
    ** - возведение в степень\n\
    / - деление\n\
    // - целочисленное деление\n\
    % - остаток от деления\n\
Примеры:\n\
    sqrt(25) -> 5.0\n\
    25**0.5 -> 5.0\n\
    5*5 -> 25.0")

async def evaluator(message : types.Message):
    logger(message)
    try:
        await message.answer(evaluate(message.text.replace(',', '.').lower()))
    except (NameError, SyntaxError, ValueError, ZeroDivisionError):
        await message.answer(random_joke())



def register_handlers_commands(dp : Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(command_help, commands='help')
    dp.register_message_handler(evaluator)

    