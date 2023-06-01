from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage_db = MemoryStorage()

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot, storage=storage_db)