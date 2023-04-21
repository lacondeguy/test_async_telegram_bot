from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Формат стартового меню клавиатуры
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прогноз погоды 🌤"),
            KeyboardButton(text="Конвертор валют 💵"),
        ],
        [
            KeyboardButton(text="Получить случайное фото 🐳")

        ]
    ],
    resize_keyboard=True,
)
