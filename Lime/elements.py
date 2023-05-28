from selenium.webdriver.common.by import By
from time import sleep
import random
class Element:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(15)

    def menu_click(self):
        self._driver.find_element(By.XPATH, '//div[@class="columns"]/div[@class="hamburger-menu burger"]').click()
        sleep(3)

    def clothes_click(self):
        self._driver.find_element(By.XPATH, '//span[text()="Одежда"]').click()
        sleep(3)

    def random_click(self):
        list1_elements = self._driver.find_elements(By.XPATH, '//a[@class="mainmenu-children__item has-children"]')
        list1_elements[random.randint(0, len(list1_elements)-1)].click()
        list2_elements = self._driver.find_elements(By.XPATH, '(//ul[@class="mainmenu-children mainmenu__children"])[2]//a')
        list2_elements[random.randint(0, len(list2_elements)-1)].click()
        sleep(3)

    def img_click(self):
        self._driver.find_element(By.XPATH, "(//img[contains(@class, 'CatalogProduct__image')])[1]").click()
        sleep(3)

    def size_click(self):
        self._driver.find_element(By.XPATH, '//div[@class="SizeSelector__arrow"]').click()
        self._driver.find_element(By.XPATH, '//span[text()="S"]').click()
        sleep(3)

    def data_product(self):
        description = self._driver.find_element(By.XPATH, '//h1[@class="product__title"]').text
        price = self._driver.find_element(By.XPATH, '//div[@class="product__price"]').text.partition('руб')[0]
        price = int(price)
        article = self._driver.find_element(By.XPATH, '//div[@class="product__article"]').text.partition(' ')[2]
        color = self._driver.find_element(By.XPATH, '//div[@class="ColorSelector__title"]').text.partition(': ')[2]
        color = color.upper()
        size = self._driver.find_element(By.XPATH, '//div[@class="SizeSelector__header"]').text
        return description, price, article, color, size

    def add_in_card(self):
        self._driver.find_element(By.XPATH, '//button[@class="btn btn-cart"]').click()

    def go_card(self):
        self._driver.find_element(By.XPATH, '//a[@href="/cart"]/div').click()
        self._driver.find_element(By.XPATH, '//button[@class="IButton IButtonClose"]').click()

    def data_product_card(self):
        description_card = self._driver.find_element(By.XPATH, '//div[@class="CartTable__name"]').text
        price_card = self._driver.find_element(By.XPATH, '//div[@class="CartTable__cost"]//span').text.partition('РУБ')[0]
        price_card = int(price_card)
        article_card = self._driver.find_element(By.XPATH, '//div[@class="CartTable__color"]/p[2]').text
        color_card = self._driver.find_element(By.XPATH, '//div[@class="CartTable__color"]/p[1]').text
        size_card = self._driver.find_element(By.XPATH, '//div[@class="SizeSelector__selected"]').text
        return description_card, price_card, article_card, color_card, size_card
