# Сначала ипортируем диспетчера из start.py
from .start import dp
from .buttons import dp
# Импорт диспетчера, из errors_command.py, который будет ловить неверные команды
from .errors_command import dp
# Потом мпорт диспетчера, из errors_handler.py, который будет ловить исключения
from .errors_handler import dp

__all__ = ['dp']
