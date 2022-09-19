from aiogram import types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp,Admin
import logging
import random



async def command_start(message: types. Message):
    await message. answer(f'привет {message. from_user.id}')




async def quiz1(message:types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('NEXT', callback_data='button_1')
    markup. add(button_1)
    question = "кто из них лучший?"
    answer = [
         'нурдин',
         'али',
         'все',
         'вадим',
         'яна',
         'слава'
     ]
    await bot. send_poll(
        chat_id= message. chat. id,
        question=question,
        options=answer,
        correct_option_id=1,
        explanation ='мальчик',
        type='quiz',
        reply_markup=markup,
    )


async def mem(message: types.Message):
    photo = open("photo/2.jpg", "rb")


    await bot.send_photo(message.from_user.id, photo=photo)


async def vetka_quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()

    button_call_5 = InlineKeyboardButton("Хорошо",

                                         callback_data="button_call_5")

    button_call_6 = InlineKeyboardButton("Плохо",

                                         callback_data="button_call_6")

    markup.add(button_call_5, button_call_6)

    await bot.send_message(message.chat.id, 'Как настроение?',

                           reply_markup=markup)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(vetka_quiz_1, commands=['vetka'])