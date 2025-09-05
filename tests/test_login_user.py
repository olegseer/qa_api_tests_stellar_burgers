import allure
import pytest

from data import Messages
from methods.user_methods import UserMethods


class TestLoginUser:

    @allure.title('Успешная авторизация  существующего пользователя')
    def test_success_login_user(self, user_data):
        create_body, login_body = user_data
        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        with allure.step('Авторизация пользователя'):
            response = UserMethods.login_user(login_body['email'], login_body['password'])
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['accessToken'] is not None

    @allure.title('Нельзя авторизоваться с неверными почтой или паролем')
    @pytest.mark.parametrize('invalid_data', ['email', 'password'])
    def test_login_user_invalid_data_fail(self, user_data, invalid_data):
        create_body, login_body = user_data
        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        invalid_user = login_body.copy()
        with allure.step(f'Изменение значения поля {invalid_data} на несуществующее'):
            invalid_user[invalid_data] = 'invalid'
        with allure.step('Попытка авторизации пользователя'):
            response = UserMethods.login_user(invalid_user['email'], invalid_user['password'])
        assert response.status_code == 401
        assert response.json()['message'] == Messages.INCORRECT_DATA
