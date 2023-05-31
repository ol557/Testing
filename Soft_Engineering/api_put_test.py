import requests
import json
# создаем переменную с URL и id=12345
url = 'https://petstore.swagger.io/v2/pet/'
# создаем переменную с данными нового питомца
new_name_pet = {
    'id': 12345,
    'name': 'Чебурашка'
}
# отправляем put-запрос изменение питомца с id=12345 с name=Qwert на name=Чебурашка
response = requests.put(url, json=new_name_pet)

print(response.status_code)
print(response.json())

def test_put_status_code_200():
    #отправляем get-запрос и получаем ответ
    response = requests.put(url, json=new_name_pet)
    #проверям статус кода в ответе
    assert response.status_code == 200


def test_id():
    response = requests.put(url, json=new_name_pet)
    #переводим ответ в json
    response_body = response.json()
    #проверяем в ответе ключ-значение "id"
    assert response_body["id"] == 12345

def test_name():
    response = requests.put(url, json=new_name_pet)
    #переводим ответ в json
    response_body = response.json()
    #проверяем в ответе ключ-значение "name"
    assert response_body["name"] == "Чебурашка"