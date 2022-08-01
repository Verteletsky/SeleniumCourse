import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestClass:
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()

    def test_registration1(self):
        self.browser.get(self.link1)
        # Ваш код, который заполняет обязательные поля
        in1 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        in1.send_keys("Roman")

        in2 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        in2.send_keys("Verteletsky")

        in3 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        in3.send_keys("verteletsky@bitrix24.ru")

        time.sleep(1)

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.browser.quit()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert 'Congratulations! You have successfully registered!' == welcome_text

    def test_registration2(self):
        self.browser.get(self.link2)
        # Ваш код, который заполняет обязательные поля
        in1 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        in1.send_keys("Roman")

        in2 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        in2.send_keys("Verteletsky")

        in3 = self.browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        in3.send_keys("verteletsky@bitrix24.ru")

        time.sleep(1)

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.browser.quit()

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert 'Congratulations! You have successfully registered!' == welcome_text
