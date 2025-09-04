import allure
import pytest
import requests

from data import Urls
from generators import generate_user_body
from methods.user_methods import UserMethods


class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    def test_success_create_user(self, user_data):
        create_body = user_data
        with allure.step('Регистрация пользователя'):
            response = UserMethods.create_user(create_body)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Нельзя создать пользователя с существующим логином')
    def test_create_user_exist_login_fail(self, user_data):
        create_body = user_data
        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        with allure.step('Попытка повторной регистрации с тем же логином'):
            response = UserMethods.create_user(create_body)
        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title('Нельзя создать пользователя с пустым обязательным полем')
    @pytest.mark.parametrize('empty_field', ['email', 'password', 'name'])
    def test_create_user_required_field_is_empty_fail(self, user_data, empty_field):
        create_body = generate_user_body()
        create_body[empty_field] = ''
        with allure.step(f'Попытка регистрации без поля {empty_field}'):
            response = UserMethods.create_user(create_body)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'



