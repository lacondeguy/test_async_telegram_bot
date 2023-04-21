from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Формат меню выбора валюты
from_currency_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рубль - RUB", ),
            KeyboardButton(text="Доллар - USD"),
        ],

        [
            KeyboardButton(text="Евро - EUR", ),
            KeyboardButton(text="Тур. лира - TRY"),
        ],
    ],
    resize_keyboard=True,
)
