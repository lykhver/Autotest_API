import requests
import pytest

# НОВЫЙ URL сервера
BASE_URL = "https://955c2879-8b7f-46d1-af6f-efb118a26076.serverhub.praktikum-services.ru"

def test_create_and_get_order():
    """
    Автоматизация теста к API:
    1. Клиент создает заказ.
    2. Проверяется, что по треку заказа можно получить данные о заказе.
    """
    print("=" * 60)
    print("Начинаем тест создания заказа и получения по треку")
    print("=" * 60)
    
    # 1. Выполнить запрос на создание заказа
    print("\n1. Создание заказа...")
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
    
    print(f"URL: {create_order_url}")
    print(f"Данные заказа: {order_data}")
    
    response = requests.post(create_order_url, json=order_data)
    print(f"Код ответа: {response.status_code}")
    
    if response.status_code != 201:
        print(f"Текст ответа: {response.text}")
    
    # Проверяем, что заказ создан успешно
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}"
    print("✅ Заказ успешно создан")
    
    # 2. Сохранить номер трека заказа
    print("\n2. Сохранение номера трека...")
    track_number = response.json()["track"]
    print(f"Трек номер: {track_number}")
    assert track_number is not None, "Трек номер не получен"
    
    # 3. Выполнить запрос на получение заказа по треку заказа
    print("\n3. Получение заказа по треку...")
    get_order_url = f"{BASE_URL}/api/v1/orders/track?t={track_number}"
    print(f"URL: {get_order_url}")
    
    get_response = requests.get(get_order_url)
    print(f"Код ответа: {get_response.status_code}")
    
    if get_response.status_code != 200:
        print(f"Текст ответа: {get_response.text}")
    
    # 4. Проверить, что код ответа равен 200
    assert get_response.status_code == 200, f"Ошибка получения заказа: {get_response.status_code}"
    print("✅ Заказ успешно получен по треку")
    
    # Дополнительные проверки
    print("\n4. Проверка данных заказа...")
    order_data_response = get_response.json()["order"]
    
    # Проверяем основные поля
    assert order_data_response["firstName"] == "Иван", "Неверное имя"
    assert order_data_response["lastName"] == "Иванов", "Неверная фамилия"
    assert order_data_response["address"] == "Москва, ул. Пушкина, д. 10", "Неверный адрес"
    assert str(order_data_response["phone"]) == "+79991234567", "Неверный телефон"
    
    print("✅ Данные заказа корректны")
    print("=" * 60)
    print("✅ Тест пройден успешно!")
    print(f"📦 Трек номер заказа: {track_number}")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    try:
        test_create_and_get_order()
    except AssertionError as e:
        print(f"\n❌ Ошибка в тесте: {e}")
        print("\nВозможные причины:")
        print("1. Неверный URL API")
        print("2. Сервер не доступен")
        print("3. Изменилась структура API")
        print("4. Неверные данные запроса")
        raise
    except Exception as e:
        print(f"\n❌ Неожиданная ошибка: {e}")
        raise
