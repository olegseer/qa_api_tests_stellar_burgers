class Urls:

    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    SIGN_UP = f'{BASE_URL}/api/auth/register'  # создание пользователя
    LOG_IN = f'{BASE_URL}/api/auth/login'  # авторизация пользователя
    DELETE = f'{BASE_URL}/api/auth/user'  # удаление пользователя
    MAKE_ORDER = f'{BASE_URL}/api/orders'  # создание заказа


class Messages:
    ALREADY_EXIST = 'User already exists'
    REQUIRED_FIELD = 'Email, password and name are required fields'
    INCORRECT_DATA = 'email or password are incorrect'
    NO_INGREDIENTS = 'Ingredient ids must be provided'
    SHOULD_AUTH = 'You should be authorised'


class Ingredients:

    VALID_INGREDIENTS = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    INVALID_INGREDIENTS = ['invalidhash']
