import requests

from data import Urls


class OrderMethods:

    @staticmethod
    def create_order(ingredients):
        return requests.post(Urls.MAKE_ORDER, json=ingredients)

    @staticmethod
    def create_order_with_token(ingredients, token):
        return requests.post(Urls.MAKE_ORDER, headers={'Authorization': f'{token}'}, json=ingredients)
