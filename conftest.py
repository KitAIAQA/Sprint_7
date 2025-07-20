import pytest
import requests
import generators
from data import Url


@pytest.fixture
def create_courier():
    # Генерируем данные для курьера
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    # Формируем тела запросов
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    # Создаем курьера
    requests.post(url = f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json = create_courier_body)
    # Выполняем вход курьера
    login_courier = requests.post(url = f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json = login_courier_body)
    # Возвращаем сгенерированные данные
    yield [create_courier_body, login_courier_body, login, password]
    # Очищаем данные после теста
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')


@pytest.fixture
def generate_courier_data():
    # Генерируем данные для курьера
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    # Формируем тела запросов
    creation_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    # Возвращаем сгенерированные данные
    yield [creation_courier_body, login_courier_body]
    # Выполняем вход и удаляем курьера после теста
    login_courier = requests.post(url = f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json = login_courier_body)
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')
