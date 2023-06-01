from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a1 = KeyboardButton('Users')
a2 = KeyboardButton('Оборудование')
a3 = KeyboardButton('Другое')
a4 = KeyboardButton('Назад')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin.insert(a1).insert(a2).insert(a3).add(a4)
