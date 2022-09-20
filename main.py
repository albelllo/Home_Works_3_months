from aiogram import types
from aiogram.utils import executor
from config import bot, dp,Admin
from handlers import admin,callback,client,extra,fsm
from config import storage
from database.bot_db import sql_create



async def on_startup(_):
    sql_create()



admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsm.register_handlers_FSMAdmin(dp)
extra.register_handlers_extra(dp)


if __name__ == "__main__":
    executor. start_polling(dp, skip_updates=True, on_startup=on_startup)



