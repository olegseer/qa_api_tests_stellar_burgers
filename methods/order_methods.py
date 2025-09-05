import allure
import requests

from data import Urls


class OrderMethods:

    @staticmethod
    @allure.step('Создание заказа без авторизации')
    def create_order(ingredients):
        return requests.post(Urls.MAKE_ORDER, json={"ingredients": ingredients})

    @staticmethod
    @allure.step('Создание заказа с авторизацией')
    def create_order_with_token(ingredients, token):
        return requests.post(Urls.MAKE_ORDER, headers={'Authorization': f'{token}'}, json={"ingredients": ingredients})
