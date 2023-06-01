from aiogram.utils import executor
from create_bot import dp, bot


async def on_startup(_):
    print("\n=============! BOT BOOT !=============")


from handlers import admin, client, other
import db

# admin.register_handlers_admin(dp)

client.register_handlers_client(dp)

db.register_handlers_db(dp)

other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
