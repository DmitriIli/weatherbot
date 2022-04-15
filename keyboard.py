from aiogram import types
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('id', 'lat', 'lon')


def make_keyboard(dict={}):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    kb_list = []
    if dict:
        for key in dict.keys():
            kb_list.append(types.InlineKeyboardButton(text=str(dict[key]['name']) + '/' + str(dict[key]['state']),
                                                      callback_data=cb.new(
                                                          lat=f"{dict[key]['lat']:.4f}",
                                                          lon=f"{dict[key]['lon']:.4f}")))
    keyboard.add(*kb_list)
    return keyboard


def make_null_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    return keyboard
