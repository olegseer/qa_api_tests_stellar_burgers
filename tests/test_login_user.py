import allure

from generators import generate_user_body
from methods.user_methods import UserMethods


class TestLoginUser:

    def test_success_login_user(self, user_data):
        create_body, login_body = user_data
        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        with allure.step('Авторизация пользователя'):
            response = UserMethods.login_user(login_body['email'], login_body['password'])
        print(response.json()['accessToken'])
        assert response.status_code == 200
        assert response.json()['success'] is True
        assert response.json()['accessToken'] is not None
