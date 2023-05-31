import requests
import json
# создаем переменную с URL и id=12345
url = 'https://petstore.swagger.io/v2/pet/12345'


# отправляем get-запрос питомца с id=12345
response = requests.get(url)

print(response.status_code)
print(response.json())

def test_get_status_code_200():
    #отправляем get-запрос и получаем ответ
    response = requests.get(url)
    #проверям статус кода в ответе
    assert response.status_code == 200


def test_id():
    response = requests.get(url)
    #переводим ответ в json
    response_body = response.json()
    #проверяем в ответе ключ-значение "id"
    assert response_body["id"] == 12345

def test_name():
    response = requests.get(url)
    #переводим ответ в json
    response_body = response.json()
    #проверяем в ответе ключ-значение "name"
    assert response_body["name"] == "Qwert"