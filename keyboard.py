from aiogram import types
from aiogram.utils.callback_data import CallbackData

# {'name': 'Стрижи', 'lat': 58.4606789, 'lon': 49.284097, 'country': 'RU', 'state': 'Kirov Oblast'}

cb = CallbackData('name', 'id', 'lat', 'lon')


def make_keyboard(dict={}):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    kb_list = []
    if dict:
        for key in dict.keys():
            # kb_list.append(str(dict[key]['name']) + '/' + str(dict[key]['state']))
            kb_list.append(types.InlineKeyboardButton(text=str(dict[key]['name']) + '/' + str(dict[key]['state']),
                                                      callback_data=cb.new(id=key, lat=dict[key]['lat'],
                                                                           lon=dict[key]['lon'])))
    keyboard.add(*kb_list)
    return keyboard
