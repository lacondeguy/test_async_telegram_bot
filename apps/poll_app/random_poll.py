from aiogram import types
import random

polls = [
    types.Poll(
        question='Какой ваш любимый цвет?',
        options=['Красный', 'Зеленый', 'Синий', 'Желтый'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какое ваше любимое животное?',
        options=['Кошка', 'Собака', 'Кролик', 'Попугай'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какой ваш любимый цвет?',
        options=['Красный', 'Зеленый', 'Синий', 'Желтый'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какое ваше любимое животное?',
        options=['Кошка', 'Собака', 'Кролик', 'Попугай'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какой ваш любимый вид спорта?',
        options=['Футбол', 'Баскетбол', 'Теннис', 'Хоккей'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какой ваш любимый музыкальный жанр?',
        options=['Рок', 'Поп', 'Хип-хоп', 'Электронная музыка'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какой ваш любимый вид кулинарии?',
        options=['Итальянская', 'Французская', 'Японская', 'Китайская'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какой ваш любимый город для путешествия?',
        options=['Париж', 'Нью-Йорк', 'Лондон', 'Токио'],
        is_anonymous=False
    ),
    types.Poll(
        question='Какой ваш любимый вид транспорта?',
        options=['Автомобиль', 'Велосипед', 'Самолет', 'Поезд'],
        is_anonymous=False
    ),
]


# Выбираем рандомный текст опроса и возвращаем его
def get_random_poll():
    return random.choice(polls)
