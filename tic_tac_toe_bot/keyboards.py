from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/new_game')
b2 = KeyboardButton('1')
b3 = KeyboardButton('2')
b4 = KeyboardButton('3')
b5 = KeyboardButton('4')
b6 = KeyboardButton('5')
b7 = KeyboardButton('6')
b8 = KeyboardButton('7')
b9 = KeyboardButton('8')
b10 = KeyboardButton('9')

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb.row(b1).row(b2, b3, b4).row(b5, b6, b7).row(b8, b9, b10)