from aiogram import Bot, types, Dispatcher, executor

import config
import keyboard
import request
import re

bot = Bot(token=config.TOKEN_BOT)
dp = Dispatcher(bot)
coord = None
dictionary = None




@dp.message_handler(commands='start')
async def output_start_command(message: types.Message):
    await message.reply('Ввести название населённого пункта')


@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(10))
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()


@dp.message_handler(content_types='text')
async def add_keyboard(message: types.Message):
    await message.answer(f'результаты по запросу "{message.text}"',
                         reply_markup=keyboard.make_keyboard(request.get_geolocation_by_city_name(message.text)))


@dp.callback_query_handler(keyboard.cb.filter())
async def callbacks(call: types.CallbackQuery, callback_data: dict):
    dictionary = {'name': callback_data["name"],
                  'lat': callback_data["lat"],
                  'lon': callback_data["lon"]}


# @dp.callback_query_handler(text='callback')
# async def callback_handlers(call: types.CallbackQuery):
#     # lat = callback_data['lat']
#     # lon = callback_data['lon']
#     await call.message.answer('message.text')


if __name__ == '__main__':
    executor.start_polling(dp)
