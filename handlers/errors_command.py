from aiogram import types
from loader import dp
from utils.misc import rate_limit
from keyboards import start_menu


# Ловим любые команды, которые не указаны у нас в коде и отправляем заглушку
@rate_limit(limit=2)
@dp.message_handler()
async def error_command(message: types.Message):
    await message.answer('Я не понял тебя 😒\nИспользуй команду /start 👈🏻', reply_markup=start_menu)
