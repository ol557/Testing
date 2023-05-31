import requests
import json
# создаем переменную с URL и id=12345
url = 'https://petstore.swagger.io/v2/pet/12345'


#отправляем delete-запрос удаление питомца с id=12345
#response = requests.delete(url)

#print(response.status_code)
#print(response.json())

def test_delete_status_code_200():
    #отправляем delete-запрос и получаем ответ
    response = requests.delete(url)
    #проверям статус кода в ответе
    assert response.status_code == 200
