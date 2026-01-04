# Лухверчик Алла, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order_by_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track_id))