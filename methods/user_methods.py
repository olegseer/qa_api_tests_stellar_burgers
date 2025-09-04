import allure
import requests

from data import Urls


class UserMethods:

    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(body):
        return requests.post(Urls.SIGN_UP, json=body)

    @staticmethod
    @allure.step('Авторизация пользователя')
    def login_user(email, password):
        return requests.post(Urls.LOG_IN, json={'email': email, 'password': password})

    @staticmethod
    @allure.step
    def delete_user(token):
        return requests.delete(Urls.DELETE, headers={'Authorization': f'{token}'})
