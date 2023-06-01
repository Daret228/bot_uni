from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a1 = KeyboardButton('AddEquip')
a2 = KeyboardButton('DeleteEquip')
a3 = KeyboardButton('Текущий список Оборудования')
a4 = KeyboardButton('Back')

kb_admin_equip = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin_equip.insert(a1).insert(a2).add(a3).add(a4)
