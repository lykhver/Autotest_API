import requests

BASE_URL = "https://7b5a425a-22c1-49b3-8794-31d967111295.serverhub.praktikum-services.ru"

def check_endpoints():
    print("Проверяем доступность эндпоинтов...")
    
    # Проверяем базовый URL
    try:
        response = requests.get(BASE_URL)
        print(f"GET {BASE_URL} - статус: {response.status_code}")
        print(f"Ответ: {response.text[:200]}...")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    
    # Попробуем разные варианты endpoints
    endpoints = [
        "/api/v1/orders",
        "/api/orders",
        "/orders",
        "/api/v1/order",
        "/v1/orders"
    ]
    
    for endpoint in endpoints:
        url = BASE_URL + endpoint
        try:
            response = requests.get(url)
            print(f"GET {url} - статус: {response.status_code}")
            if response.status_code == 200:
                print(f"  Успешно! Ответ: {response.text[:100]}...")
        except Exception as e:
            print(f"  Ошибка: {e}")

if __name__ == "__main__":
    check_endpoints()
