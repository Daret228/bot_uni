from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a1 = KeyboardButton('MAX PROD')
a2 = KeyboardButton('GOOD EMPL')
a3 = KeyboardButton('РАБ/ХАЛ')
a4 = KeyboardButton('Провал Лабы')
a5 = KeyboardButton('Собираемые ИЗД')
a6 = KeyboardButton('Back')

kb_admin_other = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin_other.insert(a1).insert(a2).insert(a3).insert(a4).insert(a5).add(a6)
