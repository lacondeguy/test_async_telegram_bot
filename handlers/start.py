from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards import start_menu
from utils.misc import rate_limit
from aiogram.dispatcher.filters import Text


# Командой start пользователь отменяет все текущие состояния и бот отправляет начальное привестствие
@rate_limit(limit=2)
@dp.message_handler(state='*', commands=['/start', '/help'])
@dp.message_handler(Text(equals=['/start', '/help'], ignore_case=True), state='*')
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        f"Привет, я уже умею:\n"
        f"• показывать прогноз погоды\n"
        f"• конвертировать валюту\n"
        f"• показывать фото милых животных\n"
        f"Что попробуем? 😉", reply_markup=start_menu
    )
