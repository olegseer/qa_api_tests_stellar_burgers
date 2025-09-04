from faker import Faker


fake = Faker()


def generate_user_body():  # генерация данных для регистрации
    return {
        "email": f'{fake.last_name()}@yandex.ru',
        "password": fake.password(),
        "name": fake.first_name()
    }
