from aiogram import Bot, types, Dispatcher, executor
from config import *
import config
import keyboard
import request
import time


bot = Bot(token=config.TOKEN_BOT)
dp = Dispatcher(bot)
coord = None
dictionary = None


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await message.answer(
        'Актуальная погода\n'
        'Ввести название населённого пункта')


@dp.message_handler(content_types='text')
async def add_keyboard(message: types.Message):
    if request.get_geolocation_by_city_name(message.text):
        await message.answer(f'результаты по запросу "{message.text}"',
                             reply_markup=keyboard.make_keyboard(request.get_geolocation_by_city_name(message.text)))
    else:
        await message.answer('совпадений не найдено')


@dp.callback_query_handler(keyboard.cb.filter())
async def callbacks(call: types.CallbackQuery, callback_data: dict):
    weather_json = request.get_weather_by_geolocation_yandex(list(callback_data.values())[1],
                                                             list(callback_data.values())[2])

    dt = weather_json['now']
    current = {
        'temp': weather_json['fact']['temp'],
        'feels_like': weather_json['fact']['feels_like'],
        'condition': weather_json['fact']['condition'],
        'humidity': weather_json['fact']['humidity'],
        'wind_dir': weather_json['fact']['wind_dir'],
        'wind_speed': weather_json['fact']['wind_speed']
    }

    date = time.strftime('%d-%m-%Y', time.localtime(dt))
    string = f"сегодня: {date}\n" \
             f"Температура воздуха:  {weather_json['fact']['temp']}°C \n" \
             f"Ощущается как:  {weather_json['fact']['feels_like']}°C, {condition[current['condition']]} \n" \
             f"Влажность воздуха: {current['humidity']}%\n" \
             f"Скорость ветра: {current['wind_speed']}м/c, направление ветра: {wind_dir[current['wind_dir']]}\n"

    forecast_str = '---------------------'
    for i in (0, 1):
        forecast_str = forecast_str + f"Погода на {part_name[weather_json['forecast']['parts'][i]['part_name']]} \n" \
                                      f"Ожидаемая температура: {weather_json['forecast']['parts'][i]['temp_avg']}°C " \
                                      f" {condition[weather_json['forecast']['parts'][1]['condition']]} \n" \
                                      f"Вероятность осадков: {weather_json['forecast']['parts'][i]['prec_prob']}%, " \
                                      f"длительность: {weather_json['forecast']['parts'][i]['prec_period']} минут\n" \
                                      f"Скорость ветра: {weather_json['forecast']['parts'][i]['wind_speed']}м/c, " \
                                      f"направление ветра: {wind_dir[weather_json['forecast']['parts'][i]['wind_dir']]}\n" \
                                      f"---------------------"

    string = string + forecast_str
    await call.message.delete()
    await call.message.answer(string)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
