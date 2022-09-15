from aiogram import types
from aiogram.utils import executor
from config import bot, dp,Admin
from handlers import admin,callback,client,extra


admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
extra.register_handlers_extra(dp)









if __name__ == "__main__":
    executor. start_polling(dp, skip_updates=True)



