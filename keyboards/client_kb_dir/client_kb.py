from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Собираемые изд')
b2 = KeyboardButton('Список изделий опр модели')
b3 = KeyboardButton('ОЖИД КОЛ-ВО ИЗД')
b4 = KeyboardButton('Процент успешных сборок')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.insert(b1).insert(b2).insert(b3).insert(b4)

# kb_client.add(b1, b2, b3).row(b4).insert(b5).insert(b6)
