from aioowm import OWM
from data import config

weather = OWM(token=config.OWM_TOKEN, language="ru")


# Используем внешнюю библиотеку для асинхронного запроса к OWM, возвращаем рузельтат или ошибку
async def check_weather(city_name):
    try:
        result = await weather.get(city_name)
        return (
            f"Город: {result.city.name} ({result.city.country})\n"
            f"Температура: {result.weather.temperature.now}°C\n"
            f"Описание: {result.weather.description}\n"
            f"Скорость ветра: {result.weather.wind.speed} м/с"
        )
    except AttributeError as e:
        # logging.info('Error: ', e)
        return 'Error'
