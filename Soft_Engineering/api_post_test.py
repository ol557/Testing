import requests
import json
# создаем переменную с URL
url = 'https://petstore.swagger.io/v2/pet'
# создаем переменную с данными нового питомца
new_pet = {
    'id': 12345,
    'name': 'Qwert'
}
# отправляем post-запрос создание питомца с id=12345 и name=Qwert
response = requests.post(url, json=new_pet)

print(response.status_code)
print(response.json())

def test_post_status_code_200():
    #отправляем post-запрос и получаем ответ
    response = requests.post(url, json=new_pet)
    #проверям статус кода в ответе
    assert response.status_code == 200


def test_id():
    response = requests.post(url, json=new_pet)
    #переводим ответ в json
    response_body = response.json()
    #проверяем в ответе ключ-значение "id"
    assert response_body["id"] == 12345

def test_name():
    response = requests.post(url, json=new_pet)
    #переводим ответ в json
    response_body = response.json()
    #проверяем в ответе ключ-значение "name"
    assert response_body["name"] == "Qwert"