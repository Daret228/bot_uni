import asyncpg
import asyncio
from config import config
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


####################################################################################
# Машина состояния:
####################################################################################


class FSMAdmin(StatesGroup):
    id_empl = State()
    del_empl = State()

    id_empl_prize = State()
    upd_prize_count = State()
    upd_prize = State()

    ####################################################################################
    # Машина состояния на Список изд опр
    ####################################################################################

    """Начало диалога, загрузка нового пункта меню, Спрашиваем id
    @dp.message_handlers(commands='DeleteEquip', state=None)"""


async def cm_start_del_equip(message: types.Message):
    await FSMAdmin.id_empl.set()
    await message.answer(
        "|...Запуск Диалога...|\n|...Для завершения напишите <b>«Отмена»</b>...|"
        "\n\nВыберите Модель:",
        parse_mode="HTML")

    # Вывод таблы Модель
    try:
        conn = await asyncpg.connect(user=config.user_bd, password=config.password_bd,
                                     database=config.database, host=config.host, port=config.port_bd)
    except:
        print("\n========= Не удалось установить соединение с БД =========")
        exit()

    rows = await conn.fetch('''select * from "Модель"''')
    await conn.close()
    str_row = "<b>ID_MODEL | NAME_MODEL | ID_MARK </b>"
    for row in rows:
        str_row += "\n" + (
                "     " + str(row[0]) + "     |       " + str(row[1]) + "    |    " + str(row[2]))
    await message.answer(str_row, parse_mode="HTML")


async def del_equip_funk(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_equip'] = message.text
        # вывод модели
        try:
            conn = await asyncpg.connect(user=config.user_bd, password=config.password_bd,
                                         database=config.database, host=config.host, port=config.port_bd)
        except:
            print("\n========= Не удалось установить соединение с БД =========")
            exit()

    try:
        await conn.execute('''call products($1);''', int(data['id_equip']))
        rows = await conn.fetch('''select * from ans''')
        str_row = "<b>ID_PROD</b>"
        for row in rows:
            str_row += "\n" + ("  " + str(row[0]))
        await message.answer("Номера Изделий данной модели:\n\n" + str_row, parse_mode="HTML")
    except:
        await message.answer("Такой модели нет :(")
    await conn.close()
    await state.finish()


####################################################################################
# Блок User
####################################################################################


async def prod_proc(message: types.Message):
    # Вывод таблы product_process
    try:
        conn = await asyncpg.connect(user=config.user_bd, password=config.password_bd,
                                     database=config.database, host=config.host, port=config.port_bd)
    except:
        print("\n========= Не удалось установить соединение с БД =========")
        exit()

    rows = await conn.fetch('''select * from "product_process"''')
    await conn.close()
    str_row = "<b>ID_PROD</b>"
    for row in rows:
        str_row += "\n" + ("  " + str(row[0]))
    await message.answer("Изделия в производстве:\n\n" + str_row, parse_mode="HTML")


async def procent_prod(message: types.Message):
    # Вывод таблы product_process
    try:
        conn = await asyncpg.connect(user=config.user_bd, password=config.password_bd,
                                     database=config.database, host=config.host, port=config.port_bd)
    except:
        print("\n========= Не удалось установить соединение с БД =========")
        exit()

    await conn.fetchrow('''select success_products()''')
    rows = await conn.fetchrow('''select success_products()''')
    await conn.close()
    await message.answer("Процент успешно выпущенных изделий составляет: " + str(rows[0]), parse_mode="HTML")


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer("Всё ок, продолжай работу!")
        return 0
    await state.finish()
    await message.answer("END!!!")

    # ####################################################################################
    # # Машина состояния на Ожид кол-во изделий
    # ####################################################################################


async def cm_start_tg_id(message: types.Message):
    await FSMAdmin.id_empl_prize.set()
    await message.answer(
        "|...Запуск Диалога...|\n|...Для завершения напишите <b>«Отмена»</b>...|"
        "\n\nВведите начало периода в формате: гггг-мм-дд",
        parse_mode="HTML")


async def update_tg_id_get(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id_user'] = message.text
    await message.answer("Введите конец периода в формате: гггг-мм-дд ")
    await FSMAdmin.next()


async def upd_tg_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tg_id'] = message.text
    # Добавление TG_ID пользователю
    try:
        conn = await asyncpg.connect(user=config.user_bd, password=config.password_bd,
                                     database=config.database, host=config.host, port=config.port_bd)
    except:
        print("\n========= Не удалось установить соединение с БД =========")
        exit()

    try:

        rows = await conn.fetchrow(f'''call quantity_product('{data['id_user']}','{data['tg_id']}',{'543'})''')
        str_row = f"<b>QUANTITY: {rows[0]}</b>"
        await message.answer(str_row, parse_mode="HTML")
    except:
        await message.answer("GG НИчего не робит (((")

    await conn.close()
    await state.finish()

    # ####################################################################################
    # # Блок регистрации хэндлеров
    # ####################################################################################
    #
    #


def register_handlers_db(dp: Dispatcher):
    dp.register_message_handler(prod_proc, Text(equals="Собираемые изд", ignore_case=True))
    dp.register_message_handler(procent_prod, Text(equals="Процент успешных сборок", ignore_case=True))

    dp.register_message_handler(cancel_handler, Text(equals="Отмена", ignore_case=True), state="*")

    dp.register_message_handler(cm_start_del_equip, Text(equals="Список изделий опр модели", ignore_case=True),
                                state=None)
    dp.register_message_handler(del_equip_funk, state=FSMAdmin.id_empl)

    dp.register_message_handler(cm_start_tg_id, Text(equals="ОЖИД КОЛ-ВО ИЗД", ignore_case=True), state=None)
    dp.register_message_handler(update_tg_id_get, state=FSMAdmin.id_empl_prize)
    dp.register_message_handler(upd_tg_id, state=FSMAdmin.upd_prize_count)
