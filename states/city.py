from aiogram.dispatcher.filters.state import StatesGroup, State

# Создаем класс City и наследуемся от StatesGroup, создаем состояние
class City(StatesGroup):
    city_state = State()