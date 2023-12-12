import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException('Введенные валюты должны быть разными\nПосмотрите ещё раз,'
                                      'какие валюты доступны\n'
                                      '/values')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{quote}"\nПосмотрите ещё раз,'
                                      'какие валюты доступны\n'
                                      '/values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{base}"\nПосмотрите ещё раз,'
                                      'какие валюты доступны\n'
                                      '/values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество "{amount}"\nПосмотрите ещё раз,'
                                      'как нужно вводить данные\n'
                                      '/help')

        r = requests.get(f'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_iZwIIXTwBwHQjb9MDsyziqjoxsxG7rSJtzDpiQfY&currencies={base_ticker}&base_currency={quote_ticker}')
        temp = json.loads(r.content)
        total_base = temp['data'][keys[base]]

        return total_base
