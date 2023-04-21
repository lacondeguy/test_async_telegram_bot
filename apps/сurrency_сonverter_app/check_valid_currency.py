availible_currency = ["Рубль - RUB", "Доллар - USD", "Евро - EUR", "Тур. лира - TRY"]


# Проверяем есть ли введеная валюта в списке
def check_valid_currency(currency_name):
    if currency_name in availible_currency:
        return True


# Проверяем прислал ли пользователь число
def check_numeric(amount):
    try:
        amount = float(amount)
        return True
    except:
        return False
