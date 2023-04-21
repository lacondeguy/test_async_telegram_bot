from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp
from states import City, Currency
from utils.misc import rate_limit
from apps import *
from keyboards import start_menu, from_currency_menu
from aiogram.types import InputFile
from data import config
from random import choice


# Устанавливаем значение в декораторе @rate_limit(limit=2).
# В данном случае 5 - это значит, что бот будет игнорировать команды 5 сек, если пользователь спамит сообщениями.
# Слушаем команду 'прогноз погоды' и записывам ответ в city_state
@rate_limit(limit=5)
@dp.message_handler(Text(equals=["Прогноз погоды 🌤", "Ввести город еще раз!"]))
async def button_weather(message: types.Message):
    await message.reply("Введите город на русском или английском языке")
    await City.city_state.set()


# Проверка ответа на валидность, если верно то используя функцию check_city_name узнаем прогноз погоды
@rate_limit(limit=5)
@dp.message_handler(state=City.city_state)
async def wait_city(message: types.Message, state: FSMContext):
    city_answer = message.text
    await state.update_data(city_state=city_answer)
    data = await state.get_data()
    city = data.get('city_state')
    if check_city_name(city):
        result = await check_weather(city)
        if result == 'Error':
            await message.reply(f'Кажется такого города не существует. '
                                f'Попробуйте, например:\n{choice(random_names)}',
                                reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.reply(result, reply_markup=start_menu)
            await state.finish()
    else:
        await message.reply(f'Город введен не верно. Попробуйте, например:\n'
                            f'{choice(random_names)}', reply_markup=types.ReplyKeyboardRemove())


# Слушаем команду 'конвертор валют' и начинаем слушать ответ пользователя
@rate_limit(limit=5)
@dp.message_handler(text="Конвертор валют 💵")
async def button_exchange(message: types.Message):
    await message.reply("Выберете валютную пару", reply_markup=from_currency_menu)
    await Currency.from_currency_state.set()


# Проверям валидность и записывам первый тикер из пары в from_currency_state, далее слушаем следующий ответ
@rate_limit(limit=5)
@dp.message_handler(state=Currency.from_currency_state)
async def from_currency_wait(message: types.Message, state: FSMContext):
    from_currency = message.text
    if check_valid_currency(from_currency):
        await state.update_data(from_currency_state=from_currency)
        await message.answer("Выберете валютную пару, в которую вы хотите конвертировать",
                             reply_markup=from_currency_menu)
        await Currency.to_currency_state.set()
    else:
        await message.reply(f'Вы ввели не верную валюту, используйте кнопки для ввода', reply_markup=from_currency_menu)


# Проверям валидность и записывам второй тикер из пары в to_currency_state, слушаем следующий ответ
@rate_limit(limit=5)
@dp.message_handler(state=Currency.to_currency_state)
async def to_currency_wait(message: types.Message, state: FSMContext):
    to_currency = message.text
    if check_valid_currency(to_currency):
        await state.update_data(to_currency_state=to_currency)
        await message.answer('Напишите кол-во цифрами, например, 100.5', reply_markup=types.ReplyKeyboardRemove())
        await Currency.amount_state.set()
    else:
        await message.reply(f'Вы ввели не верную валюту, используйте кнопки для ввода', reply_markup=from_currency_menu)


# Проверям валидность и записывам кол-во amount_state.
# Если валидно, то ипсользуем exchange_request, чтобы узнать результат
@rate_limit(limit=5)
@dp.message_handler(state=Currency.amount_state)
async def amount_wait(message: types.Message, state: FSMContext):
    amount = message.text
    if check_numeric(amount):
        await state.update_data(amount_state=amount)
        await message.reply(f'Сейчас попробую посчитать', reply_markup=types.ReplyKeyboardRemove())
        data = await state.get_data()
        from_currency = data.get('from_currency_state')
        to_currency = data.get('to_currency_state')
        amount = data.get('amount_state')
        result = await exchange_request(from_currency, to_currency, amount)
        if result == 'Error':
            await message.reply(f'Не смог получить данные :( Попробуйте позднее..', reply_markup=start_menu)
        else:
            await message.reply(result, reply_markup=start_menu)

        await state.finish()
    else:
        await message.reply(f'Вы ввели не верное кол-во. Введите, например, 100.5',
                            reply_markup=types.ReplyKeyboardRemove())


# Слушаем команду 'Получить случайное фото' и используя get_random_image выбираем рандомную фото и отправляем
@rate_limit(limit=5)
@dp.message_handler(text="Получить случайное фото 🐳")
async def button_random_foto(message: types.Message):
    path_bytes = InputFile(path_or_bytesio=get_random_image())
    chat_id = message.from_user.id
    await dp.bot.send_photo(chat_id=chat_id, photo=path_bytes)


# Используя get_random_poll берем случайный опрос и отправляем его в чат заданный в CHAT_ID
@rate_limit(limit=5)
@dp.message_handler(commands=['poll'])
async def create_poll(message: types.Message):
    poll = get_random_poll()
    await dp.bot.send_poll(chat_id=config.CHAT_ID, question=poll.question,
                           options=poll.options, is_anonymous=poll.is_anonymous)
