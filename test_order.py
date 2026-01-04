# Лухверчик Алла, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_get_order_info_by_track_success_response():
    # 1. Выполняем запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)
    
    # 2. Сохраняем номер трека заказа
    track_id = response.json()["track"]
    
    # 3. Выполняем запрос на получение заказа по треку заказа
    get_order_response = sender_stand_request.get_order_by_track(track_id)
    
    # 4. Проверяем, что код ответа равен 200
    assert get_order_response.status_code == 200