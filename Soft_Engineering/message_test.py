from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from basic_calculator import Calculator
nnn = 'string'
url = 'https://testsheepnz.github.io/random-number.html'

def test_message():
    browser = webdriver.Chrome()

    mess = Calculator(browser, url)
    mess.scroll()
    mess.select_demo()
    mess.roll_click()
    mess.data_nnn(nnn)
    mess.submit_click()
    result = mess.message()

    assert result == 'string: Not a number!'

    browser.quit()