from aiogram import types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp,Admin
import logging
import random


async def quiz_2(call: types.CallbackQuery):
    question = "кто из них мульти миллиардер?"
    answer = [
        'Д.Вашингтон',
        'У.Смит',
        'С.Жапаров',
        'P.Кийосаки',
        'Джек Ма',


    ]
    await bot. send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        correct_option_id=0,
        type='quiz',



    )




async def vetka_quiz_good_1(call: types.CallbackQuery):


    await bot.send_message(call.message.chat.id, 'Почему хорошо?')


async def vetka_quiz_bad_1(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id,",болит голова")



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(vetka_quiz_good_1,
                                       lambda call: call.data == "button_call_5")
    dp.register_callback_query_handler(vetka_quiz_bad_1,
                                       lambda call: call.data == "button_call_6")