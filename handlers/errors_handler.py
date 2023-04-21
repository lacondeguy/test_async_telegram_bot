import logging
from loader import dp
from aiogram.utils.exceptions import (BotBlocked, BadRequest, TelegramAPIError, CantParseEntities)


# Обрабатываем исключения
@dp.errors_handler()
async def errors_handler(update, exception):
    if isinstance(exception, BotBlocked):
        logging.info('Bot blocked by User')
        return True
    if isinstance(exception, BadRequest):
        logging.exception(f'BadRequest: {exception} \nUpdate: {update}')
        return True
    if isinstance(exception, TelegramAPIError):
        logging.exception(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True
    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    # Обработка других ошибок
    logging.exception(f'Update: {update} \nException: {exception}')
