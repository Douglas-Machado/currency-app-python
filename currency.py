"""CurrencyApi class to make requests"""
import requests

class CurrencyAPI():
    """Api class"""

    def get_currency(self, coins):
        """get api currency"""
        response = requests.get(
            f"https://economia.awesomeapi.com.br/last/{coins}",
            timeout=10000
        )
        name_value = {
            'price': response.json()['USDBRL']['high'],
            'name': response.json()['USDBRL']['name']
        }
        return name_value
