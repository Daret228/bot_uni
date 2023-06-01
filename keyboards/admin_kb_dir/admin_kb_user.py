from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a1 = KeyboardButton('AddUser')
a2 = KeyboardButton('UpdateUser')
a3 = KeyboardButton('DeleteUser')
a4 = KeyboardButton('Текущий список сотрудников')
a5 = KeyboardButton('Back')

kb_admin_user = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin_user.insert(a1).insert(a2).insert(a3).add(a4).add(a5)
