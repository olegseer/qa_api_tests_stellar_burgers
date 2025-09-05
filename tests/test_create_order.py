import allure
import pytest

from data import Ingredients, Messages
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем с ингредиентами')
    def test_success_create_order_with_ingredients_authorized(self, user_data):
        create_body, login_body = user_data
        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        with allure.step('Авторизация пользователя и получение токена'):
            token = UserMethods.get_token(login_body['email'], login_body['password'])
        with allure.step('Создание заказа с ингредиентами'):
            response = OrderMethods.create_order_with_token(Ingredients.VALID_INGREDIENTS, token)
        assert response.status_code == 200
        assert response.json()['order']['owner'] is not None

    @allure.title('Нельзя создать заказ авторизованным пользователем без ингредиентов')
    def test_success_create_order_no_ingredients_authorized(self, user_data):
        create_body, login_body = user_data
        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        with allure.step('Авторизация пользователя и получение токена'):
            token = UserMethods.get_token(login_body['email'], login_body['password'])
        with allure.step('Создание заказа без ингредиентов'):
            response = OrderMethods.create_order_with_token([], token)
        assert response.status_code == 400
        assert response.json()['message'] == Messages.NO_INGREDIENTS

    @allure.title('Нельзя создать заказ без авторизации')
    @allure.description('Создание заказ с ингредиентами и без')
    @pytest.mark.parametrize('ingredients', [Ingredients.VALID_INGREDIENTS, []])
    def test_create_order_no_authorised_fail(self, ingredients):
        with allure.step('Попытка создания заказа без авторизации'):
            response = OrderMethods.create_order(ingredients)
        assert response.status_code == 401
        assert response.json()['message'] == Messages.SHOULD_AUTH

    @allure.title('Нельзя создать заказ с неверным хешем')
    def test_create_order_invalid_hash_server_error(self):
        with allure.step('Попытка создания заказа с неверным хешем'):
            response = OrderMethods.create_order(Ingredients.INVALID_INGREDIENTS)
        assert response.status_code == 500
