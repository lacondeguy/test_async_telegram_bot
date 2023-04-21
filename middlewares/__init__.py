from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware


# Создаем функцию setup и подключаем класс антифлуда
def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
