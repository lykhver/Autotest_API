import requests

print("Тест API заказов")

BASE_URL = "https://955c2879-8b7f-46d1-af6f-efb118a26076.serverhub.praktikum-services.ru"

# 1. Создание заказа
order_data = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Москва, ул. Пушкина, д. 10",
    "metroStation": 4,
    "phone": "+79991234567",
    "rentTime": 5,
    "deliveryDate": "2024-01-10",
    "comment": "Тест",
    "color": ["BLACK"]
}

print("1. Создаем заказ...")
try:
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data, timeout=10)
    print(f"   Статус: {response.status_code}")
    
    if response.status_code in [200, 201]:
        track = response.json().get("track")
        print(f"   Трек номер: {track}")
        
        # 2. Получение заказа по треку
        print("\n2. Получаем заказ по треку...")
        get_response = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}", timeout=10)
        print(f"   Статус: {get_response.status_code}")
        
        if get_response.status_code == 200:
            print("✅ Тест пройден успешно!")
        else:
            print(f"❌ Ошибка: {get_response.text}")
    else:
        print(f"❌ Ошибка создания: {response.text}")
        
except Exception as e:
    print(f"❌ Ошибка: {e}")
