from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('НАЧАТЬ')
# b2 = KeyboardButton('Пользователь')

kb_other = ReplyKeyboardMarkup(resize_keyboard=True)

kb_other.add(b1)
