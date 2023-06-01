from aiogram import types, Dispatcher
from keyboards.admin_kb_dir import admin_kb, admin_kb_user, admin_kb_user_update, admin_kb_equip, admin_kb_other
from keyboards.other_kb_dir import other_kb
from aiogram.dispatcher.filters import Text

####################################################################################
# Блок Admin
####################################################################################


"""Функция вызывает клаву Админа
@dp.message_handlers(commands='Админ')"""


async def command_admin(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=admin_kb.kb_admin)


"""Функция возвращает назад из Админ
@dp.message_handlers(commands='Назад')"""


async def command_back_admin(message: types.Message):
    await message.answer("Кто вы сегодня?", reply_markup=other_kb.kb_other)


####################################################################################
# Блок Admin.User
####################################################################################

"""Функция вызывает клаву Админа.User
@dp.message_handlers(commands='Users')"""


async def command_admin_user(message: types.Message):
    await message.answer("Что вы хотите сделать с Пользователями?", reply_markup=admin_kb_user.kb_admin_user)


"""Функция возвращает назад из User
@dp.message_handlers(commands='Back')"""


async def command_back_user(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=admin_kb.kb_admin)


####################################################################################
# Блок Admin.User.Update
####################################################################################


"""Функция возвращает назад из User_Update
@dp.message_handlers(commands='Вернуться')"""


async def command_back_user_update(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=admin_kb_user.kb_admin_user)


"""Функция вызывает клаву Админа.User.Update
@dp.message_handlers(commands='UpdateUser')"""


async def command_admin_user_update(message: types.Message):
    await message.answer("Что вы хотите изменить у Пользователя?",
                         reply_markup=admin_kb_user_update.kb_admin_user_update)


####################################################################################
# Блок Admin.Оборудование
####################################################################################


async def command_admin_equip(message: types.Message):
    await message.answer("Что вы хотите сделать с Оборудованием?", reply_markup=admin_kb_equip.kb_admin_equip)


####################################################################################
# Блок Admin.Другое
####################################################################################


async def command_admin_other(message: types.Message):
    await message.answer("Что вы хотите узнать?", reply_markup=admin_kb_other.kb_admin_other)


####################################################################################
# Блок регистрации хэндлеров
####################################################################################


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(command_admin, Text(equals="Админ", ignore_case=True))
    dp.register_message_handler(command_back_admin, Text(equals="Назад", ignore_case=True))
    dp.register_message_handler(command_back_user, Text(equals="Back", ignore_case=True))
    dp.register_message_handler(command_back_user_update, Text(equals="Вернуться", ignore_case=True))
    dp.register_message_handler(command_admin_user, Text(equals="Users", ignore_case=True))
    dp.register_message_handler(command_admin_user_update, Text(equals="UpdateUser", ignore_case=True))
    dp.register_message_handler(command_admin_equip, Text(equals="Оборудование", ignore_case=True))
    dp.register_message_handler(command_admin_other, Text(equals="Другое", ignore_case=True))
