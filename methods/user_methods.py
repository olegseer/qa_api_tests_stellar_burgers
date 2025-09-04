import allure
import requests

from data import Urls


class UserMethods:

    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(body):
        return requests.post(Urls.SIGN_UP, json=body)
