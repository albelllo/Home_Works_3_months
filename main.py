from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging
import random


@dp. message_handler(commands=['start'])
async def command_start(message: types. Message):
    await message. answer(f'привет {message. from_user. full_name}')

@dp. message_handler(commands=['quiz'])
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

@dp. callback_query_handler(lambda call: call.data == 'button_1')
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


@dp. message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open("photo/2.jpg", "rb")


    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler(commands=['vetka'])
async def vetka_quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()

    button_call_5 = InlineKeyboardButton("Хорошо",

                                         callback_data="button_call_5")

    button_call_6 = InlineKeyboardButton("Плохо",

                                         callback_data="button_call_6")

    markup.add(button_call_5, button_call_6)

    await bot.send_message(message.chat.id, 'Как настроение?',

                           reply_markup=markup)
@dp.callback_query_handler(lambda call:call.data=="button_call_5")

async def vetka_quiz_good_1(call: types.CallbackQuery):


    await bot.send_message(call.message.chat.id, 'Почему хорошо?')

@dp.callback_query_handler(lambda call:call.data=="button_call_6")

async def vetka_quiz_bad_1(call: types.CallbackQuery):




    await bot.send_message(call.message.chat.id,",болит голова")

@dp.message_handler(commands=['game'])
async def game(message: types.Message):
    games = ["⚽", "⚾", "🏓", "🎯", "🎲", "🎰"]

    value =random.choice(games)

    if message.text.startswith("game"):


        await bot.send_dice(message.chat.id, value)
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id,message.text)






@dp. message_handler()
async def echo(message: types. Message):
    if message. text. isdigit():
        await bot. send_message(message. chat. id, int(message. text) * int(message.text))
    else:
        await bot. send_message(message. from_user. id, message.text)

if __name__ == "__main__":
    executor. start_polling(dp, skip_updates=True)
