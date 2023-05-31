from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


url = 'https://testsheepnz.github.io/BasicCalculator.html'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

class Calculator():


    def __init__(self, browser):
        self._driver = browser
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.get(url)
        self._driver.implicitly_wait(15)

    #проскролить страницу вниз
    def scroll(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #выбрать сборку prototype
    def select_prototype(self):
        self._driver.find_element(By.XPATH, '//select[@id="selectBuild"]').click()
        self._driver.find_element(By.XPATH, '//select[@id="selectBuild"]/option[text()="Prototype"]').click()

    #выбрать поле first и ввести число
    def first_nun(self, first):
        self._driver.find_element(By.XPATH, '//input[@id="number1Field"]').send_keys(first)

    #выбрать поле second и ввести число
    def second_nun(self, second):
        self._driver.find_element(By.XPATH, '//input[@id="number2Field"]').send_keys(second)

    #выбрать операцию subtract
    def select_subtract(self):
        self._driver.find_element(By.XPATH, '//select[@id="selectOperationDropdown"]').click()
        self._driver.find_element(By.XPATH, '//select[@id="selectOperationDropdown"]/option[text()="Subtract"]').click()

    #выбрать операцию concatenate
    def select_concatenate(self):
        self._driver.find_element(By.XPATH, '//div[@id').click()

    #нажать кнопку calculate
    def calculate_click(self):
        self._driver.find_element(By.XPATH, '//input[@id="calculateButton"]').click()

    def result(self):
        result = self._driver.find_element(By.XPATH, '//input[@id="numberAnswerField"]').text
        result = int(result)
        return result