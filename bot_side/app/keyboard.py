import requests
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Category'),
        ],
        [
            KeyboardButton(text='Bin'),
            KeyboardButton(text='Contacts')
        ]
    ], resize_keyboard=True,
    selective=True
    # input_field_placeholder='choose!!',
    # one_time_keyboard=True
)

inline_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Help', callback_data='help')
        ],
        [
            InlineKeyboardButton(text='Category', callback_data='category')
        ]
    ]
)

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Youtube', url='https://youtube.com')
        ]
    ]
)


# print(response.json())

async def inline_category():
    keyboard = InlineKeyboardBuilder()
    response = requests.get('http://127.0.0.1:8000/api/v1/category/')
    for i in response.json():
        keyboard.add(InlineKeyboardButton(text=i['name'], callback_data=str(i['id'])))

    return keyboard.adjust(1).as_markup()



