import allure

from generators import generate_user_body
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем')
    def test_success_create_order_authorized(self):
        create_body = generate_user_body()
        login_body = create_body.copy()
        del login_body['name']
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        token = None

        with allure.step('Регистрация пользователя'):
            UserMethods.create_user(create_body)
        with allure.step('Авторизация пользователя и получение токена'):
            token = UserMethods.get_token(login_body['email'], login_body['password'])
        with allure.step('Создание заказа'):
            response = OrderMethods.create_order_with_token(ingredients, token)
        print(response.json())
        assert response.status_code == 200

    @allure.title('Создание заказа без авторизации')
    def test_create_order_no_authorized_fail(self):
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        with allure.step('Создание заказа'):
            response = OrderMethods.create_order(ingredients)
        print(response.json())

    @allure.title('Создание заказа с неверным хешем')
    def test_create_order_invalid_hash(self):
        invalid_hash = {"ingredients": ["invalid_hash"]}
        with allure.step('Создание заказа'):
            response = OrderMethods.create_order(invalid_hash)
        assert response.status_code == 400
        assert response.json()['message'] == 'One or more ids provided are incorrect'
