from aiogram import types, Dispatcher
from messages import *
from keys import kb
import functions as f

async def command_start(message: types.Message):
    await message.answer(welcome, reply_markup=kb)

async def command_help(message: types.Message):
    await message.answer(help)

async def command_examples(message: types.Message):
    await message.answer(examples)

async def calc(message: types.Message):
    try:
        result = str(f.calculate(message.text))
        await message.answer(result)
    except ZeroDivisionError:
            await message.answer(zero_div_error)
    except (ValueError, IndexError):
        await message.answer(error)

def register_handlers_comands(dp: Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(command_help, commands='help')
    dp.register_message_handler(command_examples, commands='examples')
    dp.register_message_handler(calc)
