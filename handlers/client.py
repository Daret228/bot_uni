from aiogram import types, Dispatcher
from keyboards.client_kb_dir import client_kb
from keyboards.other_kb_dir import other_kb
from aiogram.dispatcher.filters import Text
import asyncio


# Функция вызывает клаву Пользователя
# @dp.message_handlers(commands='Начать')
async def command_client(message: types.Message):
    await message.answer("Выберите интересующую вас информацию", reply_markup=client_kb.kb_client)


async def start_client(message: types.Message):
    await message.answer("Добро пожаловать!\n\nНажмите кнопку «НАЧАТЬ»", reply_markup=other_kb.kb_other)

    # Функция возвращает назад
    # @dp.message_handlers(commands='Назад')
    # async def command_back(message: types.Message):
    #     await message.answer("Кто вы сегодня?", reply_markup=other_kb.kb_other)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_client, Text(equals="НАЧАТЬ", ignore_case=True))
    dp.register_message_handler(start_client, commands=["start", "help"])
