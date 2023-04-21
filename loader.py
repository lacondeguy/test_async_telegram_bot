from aiogram import Bot, types, Dispatcher
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Указываем место для хранения состояний FSM
storage = MemoryStorage()
# Указываем токен и метод обработки сообщений
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Создаем диспетчер и указываем место хранения машины состояний
dp = Dispatcher(bot, storage=storage)