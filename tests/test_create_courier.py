import requests
import pytest
import allure
from data import ResponseBody, Url, DataForRegistration


class TestsCreateNewCourier:

    @allure.title('Тест успешного создания нового курьера. Эндпоинт: /api/v1/courier')
    def test_creation_courier_success(self, generate_courier_data):
        registration = requests.post(url=f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=generate_courier_data[0])
        assert registration.status_code == 201 and (registration.json() == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Тест ошибки при повторной регистрации одного и того же курьера. Эндпоинт: /api/v1/courier')
    def test_creation_courier_clone_error(self, create_courier):
        response = requests.post(url=f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier[0])
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Тест ошибки регистрации курьера, если данных для регистрации не достаточно. Эндпоинт: /api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        response = requests.post(url=f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)