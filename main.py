from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
import requests
from config import API_KEY, country_code, headers, TOKEN_BOT

import request

# {'name': 'Стрижи', 'lat': 58.4606789, 'lon': 49.284097, 'country': 'RU', 'state': 'Kirov Oblast'}


if __name__ == '__main__':
    # r = request.get_weather_by_city_name('Кировск')
    #
    # for line in r:
    #     print(r[line])

    r = request.get_geolocation_by_city_name('Киров')

    for key in r.keys():
        print(r[key])
