from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from basic_calculator import Calculator
first = 'gs'
second = 'bu'
url = 'https://testsheepnz.github.io/BasicCalculator.html'
def test_dif():
    browser = webdriver.Chrome()

    conc = Calculator(browser, url)
    conc.scroll()
    conc.select_prototype()
    conc.first_nun(first)
    conc.second_nun(second)
    conc.select_concatenate()
    conc.calculate_click()
    result = conc.result()

    assert result == 'gsbu'

    browser.quit()