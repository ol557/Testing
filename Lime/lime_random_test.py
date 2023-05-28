from time import sleep
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
# s = Service('C:/Users/Qasquad/Downloads/chromedriver_win32/chromedriver.exe')
# driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://lime-shop.ru")

menu = '//*[@id="AppNavbar"]/div[1]/div[1]/div'
driver.find_element(By.XPATH, menu).click()
sleep(3)

clothes = '//span[text()="Одежда"]'
driver.find_element(By.XPATH, clothes).click()
sleep(3)

# one_element = '//ul[@class="mainmenu-children mainmenu__children"]'
# elements = driver.find_elements(By.XPATH, one_element)
# random_element = elements[random.randint(0, len(elements)-1)].click()
# print(elements)

shirtes = '//span[text()="РУБАШКИ"]'
driver.find_element(By.XPATH, shirtes).click()
sleep(3)

shirts = '//*[@id="app"]/div[1]/div/div/div/nav/ul/li[2]/ul/li[14]/ul/li[2]/a/span'
driver.find_element(By.XPATH, shirts).click()
sleep(25)

img = '//*[@id="app"]/div[5]/div/div/div[1]/div[1]/div/div[1]/a/div/picture/img'
driver.find_element(By.XPATH, img).click()
sleep(3)

size = '//div[@class="SizeSelector__arrow"]'
driver.find_element(By.XPATH, size).click()
sleep(3)

size_m = '//span[text()="S"]'
driver.find_element(By.XPATH, size_m).click()
sleep(3)

# получение информации о выбранном товаре
description = '//*[@id="app"]/div[5]/div[2]/div/div/div[1]/div[2]/div/h1'
text_description = driver.find_element(By.XPATH, description).text
print(text_description, '!!!')

price = '//div[@class="product__price"]'
text_price = driver.find_element(By.XPATH, price).text.partition('руб')[0]
text_price = int(text_price)
print(text_price + 1)

article = '//div[@class="product__article"]'
text_article = driver.find_element(By.XPATH, article).text
print(text_article)

color = '//div[@class="ColorSelector__title"]'
text_color = driver.find_element(By.XPATH, color).text.partition(': ')[2]
text_color = text_color.upper()
print(text_color)

size_go = '//div[@class="SizeSelector__header"]'
text_size_go = driver.find_element(By.XPATH, size_go).text
print(text_size_go)

# добавление в корзину
cart = '//button[@class="btn btn-cart"]'
driver.find_element(By.XPATH, cart).click()
sleep(3)
# переход в корзину
go_cart = '//*[@id="AppNavbar"]/div[2]/a[3]/div'
sleep(5)
# driver.refresh()
driver.find_element(By.XPATH, go_cart).click()
sleep(3)

x = '//button[@class="IButton IButtonClose"]'
driver.find_element(By.XPATH, x).click()
sleep(3)

# получение данных из корзины
cart_description = '//div[@class="CartTable__name"]'
text_cart_description = driver.find_element(By.XPATH, cart_description).text
print(text_cart_description)

cart_price = '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div[3]/div[1]/span'
text_cart_price = driver.find_element(By.XPATH, cart_price).text.partition('РУБ')[0]
text_cart_price = int(text_cart_price)
print(text_cart_price)

cart_color = '//div[@class="CartTable__color"]/p[1]'
text_cart_color = driver.find_element(By.XPATH, cart_color).text
print(text_cart_color)

cart_size = '//div[@class="SizeSelector__selected"]'
text_cart_size = driver.find_element(By.XPATH, cart_size).text
print(text_cart_size)

cart_article = '//div[@class="CartTable__color"]/p[2]'
text_cart_article = driver.find_element(By.XPATH, cart_article).text
print(text_cart_article)

cart_value = '//div[@class="DropdownList__selected"]'
text_cart_value = driver.find_element(By.XPATH, cart_value).text
text_cart_value = int(text_cart_value)
print(text_cart_value)

cart_all = '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[4]/div[2]/span'
text_cart_all = driver.find_element(By.XPATH, cart_all).text.partition('руб')[0]
text_cart_all = int(text_cart_all)
print(text_cart_all)

# проверка текста с картинки и корзины
def test_text():
    assert text_description == text_cart_description

def test_price():
    assert text_price == text_cart_price

def test_color():
    assert text_color == text_cart_color

def test_size():
    assert text_size_go == text_cart_size

def test_article():
    assert text_cart_article in text_article

def test_all():
    assert text_cart_value*text_cart_price == text_cart_all
