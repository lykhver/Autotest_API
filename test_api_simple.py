import requests

# Базовый URL API - используй свой тестовый сервер
BASE_URL = "https://7b5a425a-22c1-49b3-8794-31d967111295.serverhub.praktikum-services.ru"

def test_create_and_get_order():
    print("Начинаем тест создания заказа и получения по треку...")
    
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
    
    print(f"Отправляем запрос на создание заказа: {create_order_url}")
    response = requests.post(create_order_url, json=order_data)
    
    # Проверяем, что заказ создан успешно
    print(f"Код ответа при создании: {response.status_code}")
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}"
    print("✓ Заказ успешно создан")
    
    # 2. Сохраняем номер трека
    track_number = response.json()["track"]
    print(f"Получен трек номер: {track_number}")
    assert track_number is not None, "Трек номер не получен"
    
    # 3. Получение заказа по треку
    get_order_url = f"{BASE_URL}/api/v1/orders/track?t={track_number}"
    print(f"Запрашиваем заказ по треку: {get_order_url}")
    get_response = requests.get(get_order_url)
    
    # 4. Проверяем, что код ответа равен 200
    print(f"Код ответа при получении: {get_response.status_code}")
    assert get_response.status_code == 200, f"Ошибка получения заказа: {get_response.status_code}"
    print("✓ Заказ успешно получен по треку")
    
    # Дополнительные проверки данных заказа
    order_data_response = get_response.json()["order"]
    assert order_data_response["firstName"] == "Иван"
    assert order_data_response["lastName"] == "Иванов"
    assert order_data_response["address"] == "Москва, ул. Пушкина, д. 10"
    
    print("✓ Все проверки пройдены успешно!")
    print(f"Трек номер: {track_number}")
    return True

if __name__ == "__main__":
    try:
        test_create_and_get_order()
        print("\n✅ Тест пройден успешно!")
    except Exception as e:
        print(f"\n❌ Ошибка в тесте: {e}")
        raise
