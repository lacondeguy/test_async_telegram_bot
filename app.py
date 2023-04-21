from utils.set_bot_commands import set_default_commands
from aiogram import executor
from handlers import dp
import logging
import middlewares


# Создаем функцию, которая вызывается при старте бота
async def on_startup(dp):
    # Устанавливаем параметры логгирования
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
    # Устанавливаем описание стандартных комманд
    await set_default_commands(dp)
    # Запускаем антифлуд
    middlewares.setup(dp)
    print('Бот запустился :)')

if __name__ == '__main__':
    try:
        # Запускаем бота с указанными параметрами: функция при старте, пропускаем все старые сообщения от пользователей
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
        # Ловим исключения и логгируем в py-log.log
    except Exception as e:
        logging.info('Error: ', e)