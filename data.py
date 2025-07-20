import generators


class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'   # Базовый URL сервиса
    CREATE_COURIER = 'api/v1/courier'  # Эндпоинт для создания учетной записи курьера
    COURIER_LOGIN = 'api/v1/courier/login'  # Эндпоинт для входа курьера в систему
    COURIER_DELETE = 'api/v1/courier/'  # Эндпоинт для удаления курьера
    CREATE_ORDER = 'api/v1/orders'  # Эндпоинт для создания заказа
    GET_ORDER_LIST = 'api/v1/orders'  # Эндпоинт для получения списка заказов
    GET_CANCEL = 'api/v1/orders/cancel?track='  # Эндпоинт для отмены заказа
    TRACK_ORDER = '/api/v1/orders/track?t='  # Эндпоинт для отслеживания заказа


class DataForOrder:
    order_data = {      # Словарь с данными для создания заказа
        "firstName": "Alena",
        "lastName": "Kit",
        "address": "Plekhanova 17",
        "metroStation": 3,
        "phone": "+79854321234",
        "rentTime": 3,
        "deliveryDate": "2025-07-30",
        "comment": "Go to the diploma as soon as possible"
    }
    scooter_color = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]


class DataForRegistration:
    reg_data = [      # Список словарей с разными комбинациями данных для регистрации
        {'login': generators.login_generator(), 'firstName': generators.name_generator()},
        {'login': generators.login_generator(), 'password': generators.password_generator()},
        {'firstName': generators.name_generator(), 'password': generators.password_generator()}
    ]


class ResponseBody:     # Ожидаемые ответы от API
    COURIER_CREATION_SUCCESS = {'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    COURIER_ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'code': 400, 'message': 'Недостаточно данных для входа'}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'   # Флаг успешного создания заказа
    SUCCESSFUL_GET_ORDER_LIST = 'orders'  # Флаг успешного получения списка заказов



