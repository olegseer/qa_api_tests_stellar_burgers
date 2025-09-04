import pytest
import requests

from data import Urls
from generators import generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture
def user_data():
    create_body = generate_user_body()  # генерация тела для регистрации
    login_body = create_body.copy()  # тело для авторизации
    del login_body['name']  # удаление лишнего элемента словаря
    yield [create_body, login_body]
    auth = UserMethods.login_user(login_body['email'], login_body['password'])
    token = auth.json()['accessToken']
    UserMethods.delete_user(token)
