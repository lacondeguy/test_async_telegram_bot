import httpx
from data import config
import logging
import json

headers = {"apikey": config.FIXER_TOKEN}


# Используем асинхронную библиотеку httpx, чтобы узнать результат обмена валюты используя API FIXER
async def exchange_request(from_currency, to_currency, amount):
    try:
        async with httpx.AsyncClient() as client:
            to_currency = str(to_currency[-3:])
            from_currency = str(from_currency[-3:])
            url = f'https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount={amount}'
            response = await client.get(url, headers=headers)
            status_code = response.status_code
            if status_code == 200:
                result = json.loads(response.text)
                return (
                    f"{result['query']['amount']} {result['query']['from']} ➡️ "
                    f"{result['query']['to']} {round(result['result'], 2)}\n\n"
                    f"Курс {result['query']['from']} к {result['query']['to']} = {round(result['info']['rate'], 2)}"
                )
            else:
                return 'Error'
    except Exception as e:
        logging.info('Error: ', e)
        return 'Error'
