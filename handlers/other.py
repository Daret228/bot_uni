from aiogram import types, Dispatcher
from keyboards.other_kb_dir import other_kb


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer("Выберите роль", reply_markup=other_kb.kb_other)


# @dp.message_handler(Любое сообщение)
async def echo_send(message: types.Message):
    await message.reply("Вы написали: | " + message.text)


def register_handlers_other(dp: Dispatcher):
    # dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(echo_send)
