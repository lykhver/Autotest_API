import requests
import pytest
import allure

# Базовый URL API - используй свой тестовый сервер
BASE_URL = "https://7b5a425a-22c1-49b3-8794-31d967111295.serverhub.praktikum-services.ru"

@allure.title("Тест создания заказа и получения по треку")
@allure.description("Создание заказа и проверка получения данных по треку")
def test_create_and_get_order():
    # 1. Создание заказа
    create_order_url = f"{BASE_URL}/api/v1/orders"
    order_data = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, ул. Пушкина, д. 10",
        "metroStation": 4,
        "phone": "+79991234567",
        "rentTime": 5,
        "deliveryDate": "2024-01-10",
        "comment": "Позвонить за час",
        "color": ["BLACK"]
    }
    
    response = requests.post(create_order_url, json=order_data)
    
    # Проверяем, что заказ создан успешно
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}"
    
    # 2. Сохраняем номер трека
    track_number = response.json()["track"]
    assert track_number is not None, "Трек номер не получен"
    
    # 3. Получение заказа по треку
    get_order_url = f"{BASE_URL}/api/v1/orders/track?t={track_number}"
    get_response = requests.get(get_order_url)
    
    # 4. Проверяем, что код ответа равен 200
    assert get_response.status_code == 200, f"Ошибка получения заказа: {get_response.status_code}"
    
    # Дополнительные проверки данных заказа
    order_data_response = get_response.json()["order"]
    assert order_data_response["firstName"] == "Иван"
    assert order_data_response["lastName"] == "Иванов"
    assert order_data_response["address"] == "Москва, ул. Пушкина, д. 10"
    
    print(f"Тест пройден успешно! Трек номер: {track_number}")

if __name__ == "__main__":
    test_create_and_get_order()
