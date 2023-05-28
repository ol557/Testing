from element1 import Element
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://lime-shop.ru")

lime = Element(browser)
lime.menu_click()
lime.clothes_click()
lime.random_click()
lime.img_click()
lime.size_click()
x = lime.data_product()
print(lime.data_product())
lime.add_in_card()
lime.go_card()
y = lime.data_product_card()
print(lime.data_product_card())
assert x == y
