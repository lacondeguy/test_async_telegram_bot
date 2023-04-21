from aiogram.dispatcher.filters.state import StatesGroup, State

# Создаем класс Currency и наследуемся от StatesGroup, создаем состояния
class Currency(StatesGroup):
    from_currency_state = State()
    to_currency_state = State()
    amount_state = State()