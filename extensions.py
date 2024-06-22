import json
import requests
from config import keys

class APIExeption(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote : str, base : str, amount : str):
        if quote == base:
            raise APIExeption(f'НЕ возможно перевести в {base}')

            # quote_ticker, base_ticker = keys[quote], keys[base]
        try:
            quote_ticker = keys[quote]
        except KeyError:
            APIExeption(f'НЕ удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            APIExeption(f'НЕ удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            APIExeption(f"НЕ удалось обработать  количество {amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base