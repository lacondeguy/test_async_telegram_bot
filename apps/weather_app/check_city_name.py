letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
           "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "a", "b", "c", "d", "e", "f", "g",
           "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "-", " "]

random_names = ["Лос-Анджелес или Los Angeles", "Санкт-Петербург или Saint Petersburg",
                "Ростов-на-Дону или Rostov na Donu"]


# Проверяем сообщение от пользователя и если оно содержит сиволы из словаря letters, то возвращаем True
def check_city_name(city_name):
    city_name = city_name.lower()
    return all([i in letters for i in city_name])
