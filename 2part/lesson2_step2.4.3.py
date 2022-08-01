import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")

    btn = browser.find_element(By.ID, "verify")
    btn.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
