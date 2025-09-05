import pytest

from generators import generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture
def user_data():
    create_body = generate_user_body()  # генерация тела для регистрации
    login_body = create_body.copy()  # тело для авторизации
    del login_body['name']  # удаление лишнего элемента словаря
    yield [create_body, login_body]
    token = UserMethods.get_token(login_body['email'], login_body['password'])  # получение токена
    UserMethods.delete_user(token)  # удаление пользователя
