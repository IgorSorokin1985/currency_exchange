import requests
import json

API_KEY = 'DChmySAUP2uZCRDY9Yu9hoHAtLQAhDKo'

class Model:

    def currency_usd(self):
        url = f"https://api.apilayer.com/exchangerates_data/latest?base=USD"
        response = requests.get(url, headers={'apikey': API_KEY})
        response_data = json.loads(response.text)
        rate = response_data["rates"]["RUB"]
        return rate

class View:
    def print_view(self, data):
        print(data)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_currency_usd(self):
        result = self.model.currency_usd()
        self.view.print_view(result)

class Router:
    pass


