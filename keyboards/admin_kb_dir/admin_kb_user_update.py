from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a1 = KeyboardButton('+Стаж')
a2 = KeyboardButton('+Премия')
a3 = KeyboardButton('UPD_TG')
a4 = KeyboardButton('Вернуться')

kb_admin_user_update = ReplyKeyboardMarkup(resize_keyboard=True)

kb_admin_user_update.insert(a1).insert(a2).insert(a3).add(a4)
