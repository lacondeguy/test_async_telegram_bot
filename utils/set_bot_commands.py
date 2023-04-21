from aiogram import types


# Создаем описание команд для бота
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Подсказки'),
    ])
