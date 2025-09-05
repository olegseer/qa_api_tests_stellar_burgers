## Дипломный проект. Задание 2: Автотесты для API
<hr>

## Студент: Олег Шипулев

## <h>Когорта: #26</h>
<hr>

## <h>Проект: Stellar Burger API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Структура проекта и описание:</h3>

| Название файла       | Содержание файла                     |
|----------------------|--------------------------------------|
| tests.dir            | Директория с тестами                 |
| test_create_order.py | Тесты на создание заказа             |
| test_create_user.py  | Тесты на создание пользователя       |
| test_login_user.py   | Тесты на авторизацию пользователя    |
| methods.dir          | Директория с методами                |
| order_methods.py     | Методы заказа                        |
| user_methods.py      | Методы пользователя                  |
| conftest.py          | Фикстура генерации и удаления данных |
| data.py              | Файл с URL и ожидаемыми ответами     |
| generators.py        | Генератор данных                     |
| requirements.txt     | Файл с зависимостями                 |
| allure_results.dir   | Папка с отчетами Allure              |

<hr>

<h3 align="left" style="color:green">Список тестов:</h3>

**Создание заказа**

1. test_success_create_order_with_ingredients_authorized - Успешное создание заказа авторизованным пользователем с ингредиентами
2. test_success_create_order_no_ingredients_authorized - Нельзя создать заказа авторизованным пользователем без ингредиентов
3. test_create_order_no_authorised_fail - Нельзя создать заказ без авторизации с ингредиентами
4. test_create_order_no_authorised_fail - Нельзя создать заказ без авторизации без ингредиентов
5. test_create_order_invalid_hash_server_error - Нельзя создать заказ с неверным хешем

**Создание пользователя**

6. test_success_create_user - Успешное создание пользователя
7. test_create_user_exist_login_fail - Нельзя создать пользователя с существующим логином
8. test_create_user_required_field_is_empty_fail - Нельзя создать пользователя с пустым обязательным полем email
9. test_create_user_required_field_is_empty_fail - Нельзя создать пользователя с пустым обязательным полем password
10. test_create_user_required_field_is_empty_fail - Нельзя создать пользователя с пустым обязательным полем name

**Авторизация пользователя**

11. test_success_login_user - Успешная авторизация  существующего пользователя
12. test_login_user_invalid_data_fail - Нельзя авторизоваться с неверной почтой
13. test_login_user_invalid_data_fail - Нельзя авторизоваться с неверным паролем
