import allure
import requests
from data import Flags
from data import Url


class TestOrderList:

    @allure.title('Тест получения списка заказов. Эндпоинт: /api/v1/orders')
    def test_successful_get_order_list(self):
        # Формируем URL для запроса
        response = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}')
        # Проверяем статус-код и наличие флага в ответе
        assert response.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response.json()
