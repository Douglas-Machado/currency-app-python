"""main file from app"""

from kivy.app import App
from kivy.lang import Builder
from currency import CurrencyAPI

cApi = CurrencyAPI()

GUI = Builder.load_file("home.kv")

class MyApp(App):
    """simple class to use kivy interface"""
    def build(self):
        return GUI

    def on_start(self):
        response = cApi.get_currency('USD-BRL')
        self.root.ids['currency_name'].text = response['name']
        self.root.ids['usd_currency'].text = response['price']


my_app = MyApp()
my_app.run()
