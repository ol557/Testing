from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from basic_calculator import Calculator
first = 2
second = 3

def test_dif():
    browser = webdriver.Chrome()

    diff = Calculator(browser)
    diff.scroll()
    diff.select_prototype()
    diff.first_nun(first)
    diff.second_nun(second)
    diff.select_subtract()
    diff.calculate_click()
    result = diff.result()

    assert result == -1