"""
Дипломный проект: Тест API.
PEP8 compliant.
"""

import requests

print("Тест API для дипломного проекта")
print("=" * 50)

url = "https://955c2879-8b7f-46d1-af6f-efb118a26076.serverhub.praktikum-services.ru"

try:
    response = requests.get(url, timeout=10)
    print(f"Проверка сервера: {url}")
    print(f"Статус: {response.status_code}")

    if response.status_code == 200:
        print("✅ Сервер доступен")
    else:
        print(f"⚠️  Ответ: {response.status_code}")

except Exception as e:
    print(f"❌ Ошибка: {e}")

print("\nТест завершен")
